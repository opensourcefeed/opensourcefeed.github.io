---
title: How to convert JPG images to PNG using ImageMagick in Linux?
layout: post
categories:
- tutorial
- linux
tags:
- imagemagick
- jpg-to-png
- image-conversion
- linux
image: "/assets/images/post-images/kde-neon-5.10.jpg"
redirect_from:
    - /2021/06/how-to-convert-jpg-images-to-png-using-imagemagick-in-linux/
description: An article briefly explaining how to convert jpg images into PNG using imagemagick - a command line tool for image processing in different platforms.
last_modified_at: 2026-07-27
---

**This** is a continuation of our [tutorial for converting png images to jpg using ImageMagick](/00-convert-png-to-jpg-imagemagick/). You may refer to the same article to learn about PNG and JPG image formats, and also about ImageMagick.

![A JPG photograph being converted to PNG format](/assets/images/post-images/kde-neon-5.10.jpg)

**TL;DR:** `convert image.jpg image.png` (ImageMagick 6) or `magick image.jpg image.png` (ImageMagick 7). Note that converting a JPG to PNG does **not** recover any quality lost during the original JPG compression — PNG just stops further loss from that point on.

## Why convert JPG to PNG?

The most common reasons to go from JPG to PNG are needing a lossless format for further editing (avoiding repeated generation loss from re-saving as JPG), needing to add transparency to an image that a JPG can't support, or preparing a photo for use as an icon, logo, or overlay where PNG's lossless edges matter.

## How to perform JPG to PNG conversion using ImageMagick?
ImageMagick provides a set of command-line tools for performing image manipulation operations. **convert** is one such tool in the ImageMagick tool suite, that facilitates the conversion of images between various formats. It also provides options to resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more.

You can read the complete `convert` tool documentation using the man pages. The man page for `convert` can be read using the following commands:
```bash
$ convert --help
   OR
$ man convert
```
The image format conversion can be done using the following command:
```bash
$ convert [original image] [converted image name]
```
This command can be used to convert between any valid image formats.

> **Note (ImageMagick 7+):** Most current Linux distributions ship ImageMagick 7, where the standalone `convert` binary is deprecated in favor of the `magick` command. The syntax is otherwise identical — just replace `convert` with `magick`:
> ```bash
> $ magick [original image] [converted image name]
> ```

If we want to convert multiple jobs at once, we may use a simple batch job like the below:
```bash
for image in *.jpg ; 
do 
    convert "$image" "${image%.*}.png" ;
done
```
In one line, it can be written like,
```bash
$ for image in *.jpg ;  do convert "$image" "${image%.*}.png" ; done
```

Alternatively, `mogrify` can batch-convert an entire directory in place without a loop:
```bash
$ mogrify -format png *.jpg
```
This creates a `.png` copy of every JPG in the current directory, leaving the original JPG files untouched.

## Generic format
The `convert`/`magick` syntax works between any two image formats, not just JPG and PNG — see our [PNG to JPG tutorial](/00-convert-png-to-jpg-imagemagick/#how-to-convert-from-any-image-format-to-any-other-image-format) for the general form and more examples.

## Frequently Asked Questions

**Does converting JPG to PNG improve image quality?**
No. PNG is lossless going forward, but it can't restore detail already lost when the source image was saved as JPG. Converting a low-quality JPG to PNG just locks in that same quality at a larger file size.

**Will converting to PNG increase the file size?**
Usually, yes. PNG's lossless compression typically produces larger files than JPG for photographs, though it compresses simple graphics well.

**Can I add transparency to a JPG by converting it to PNG?**
Converting alone won't add transparency — PNG supports an alpha channel, but you need a separate step (like background removal) to actually make part of the image transparent after conversion.
