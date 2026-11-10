#!/usr/bin/env ruby
# frozen_string_literal: true

# Writes intrinsic width/height of logo and preview images to
# _data/image_dimensions.json so layouts can emit width/height attributes
# and the browser can reserve space before the image loads (prevents CLS).
#
# Re-run after adding or replacing images:
#   ruby scripts/generate_image_dimensions.rb

require "json"
require "pathname"

ROOT = Pathname.new(File.expand_path("..", __dir__))
OUT_FILE = ROOT.join("_data", "image_dimensions.json")
DIRS = {
  "logo" => ROOT.join("assets", "images", "logo"),
  "preview" => ROOT.join("assets", "images", "preview")
}.freeze

def png_size(data)
  return unless data.byteslice(0, 8) == "\x89PNG\r\n\x1A\n".b

  data.byteslice(16, 8).unpack("NN")
end

def gif_size(data)
  return unless data.start_with?("GIF8")

  data.byteslice(6, 4).unpack("vv")
end

def jpeg_size(data)
  return unless data.byteslice(0, 2) == "\xFF\xD8".b

  pos = 2
  while pos < data.bytesize - 9
    pos += 1 while data.getbyte(pos) != 0xFF && pos < data.bytesize
    pos += 1 while data.getbyte(pos) == 0xFF && pos < data.bytesize
    marker = data.getbyte(pos)
    pos += 1
    length = data.byteslice(pos, 2).unpack1("n")
    if (0xC0..0xCF).cover?(marker) && ![0xC4, 0xC8, 0xCC].include?(marker)
      h, w = data.byteslice(pos + 3, 4).unpack("nn")
      return [w, h]
    end
    pos += length
  end
  nil
end

def webp_size(data)
  return unless data.byteslice(0, 4) == "RIFF" && data.byteslice(8, 4) == "WEBP"

  case data.byteslice(12, 4)
  when "VP8 "
    w, h = data.byteslice(26, 4).unpack("vv")
    [w & 0x3FFF, h & 0x3FFF]
  when "VP8L"
    b = data.byteslice(21, 4).unpack1("V")
    [(b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1]
  when "VP8X"
    w = data.byteslice(24, 3).unpack("C3")
    h = data.byteslice(27, 3).unpack("C3")
    [1 + w[0] + (w[1] << 8) + (w[2] << 16), 1 + h[0] + (h[1] << 8) + (h[2] << 16)]
  end
end

def svg_size(data)
  head = data.byteslice(0, 4096).to_s.force_encoding("UTF-8").scrub
  tag = head[/<svg\b[^>]*>/m]
  return unless tag

  if (vb = tag[/viewBox\s*=\s*["']([^"']+)["']/, 1])
    nums = vb.split(/[\s,]+/).map(&:to_f)
    return [nums[2].round, nums[3].round] if nums.size == 4 && nums[2].positive? && nums[3].positive?
  end
  w = tag[/\swidth\s*=\s*["']([\d.]+)(px)?["']/, 1]
  h = tag[/\sheight\s*=\s*["']([\d.]+)(px)?["']/, 1]
  [w.to_f.round, h.to_f.round] if w && h
end

def image_size(path)
  data = File.binread(path)
  png_size(data) || gif_size(data) || jpeg_size(data) || webp_size(data) || svg_size(data)
rescue StandardError
  nil
end

result = {}
DIRS.each do |key, dir|
  result[key] = {}
  Dir.children(dir).sort.each do |name|
    path = dir.join(name)
    next unless path.file?

    size = image_size(path)
    if size && size.all? { |v| v.is_a?(Integer) && v.positive? }
      result[key][name] = { "w" => size[0], "h" => size[1] }
    else
      warn "Skipping #{path.relative_path_from(ROOT)}: size unknown"
    end
  end
end

File.write(OUT_FILE, JSON.pretty_generate(result) + "\n")
puts "Wrote #{OUT_FILE.relative_path_from(ROOT)} (#{result.values.sum(&:size)} images)"
