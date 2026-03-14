#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"
require "pathname"
require "time"

ROOT = Pathname.new(File.expand_path("..", __dir__))
SCREENSHOTS_DIR = ROOT.join("screenshots")
OUT_FILE = ROOT.join("_data", "galleries.json")

IMAGE_EXTS = %w[.jpg .jpeg .png .webp .gif].freeze

unless SCREENSHOTS_DIR.directory?
  warn "screenshots directory not found at #{SCREENSHOTS_DIR}"
  exit 1
end

galleries = Hash.new { |h, k| h[k] = [] }

Dir.glob(SCREENSHOTS_DIR.join("**", "*")).each do |absolute_path|
  path = Pathname.new(absolute_path)
  next unless path.file?

  ext = path.extname.downcase
  next unless IMAGE_EXTS.include?(ext)

  rel_from_root = path.relative_path_from(ROOT).to_s
  rel_from_screenshots = path.relative_path_from(SCREENSHOTS_DIR).to_s
  folder_rel = File.dirname(rel_from_screenshots)

  # Normalize to the same folder format used by the include: "/screenshots/<folder>"
  folder_key = if folder_rel == "." || folder_rel.empty?
    "/screenshots"
  else
    "/screenshots/#{folder_rel}"
  end

  filename = path.basename(path.extname).to_s
  galleries[folder_key] << { "path" => "/#{rel_from_root}", "filename" => filename }
end

# Stable output: sort folders and files.
sorted = galleries.keys.sort.each_with_object({}) do |folder, acc|
  acc[folder] = galleries[folder].sort_by { |f| f["path"] }
end

payload = {
  "meta" => {
    "generated_at" => Time.now.utc.iso8601,
    "source_dir" => "screenshots",
    "image_exts" => IMAGE_EXTS
  },
  "galleries" => sorted
}

OUT_FILE.write(JSON.pretty_generate(payload) + "\n")
puts "Wrote #{OUT_FILE} (#{sorted.size} galleries)"

