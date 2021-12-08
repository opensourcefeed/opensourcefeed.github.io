---
title: How to convert JPG images to PNG using ImageMagick in Linux?
layout: post
categories:
- tutorial
- linux
tags:
- imagemagick
- tutorial
- imagemagickconvert jpg to png
- imagemagickjpgto png
- imagickconvertpng to jpg
image: "/assets/images/post-images/png-eligible.webp"
redirect_from:
    - /2021/06/how-to-convert-jpg-images-to-png-using-imagemagick-in-linux/
description: An article briefly explaining how to convert jpg images into PNG using imagemagick - a command line tool for image processing in different platforms.
---

**This** is a continuation of our [tutorial for converting png images to jpg using ImageMagick](/00-convert-png-to-jpg-imagemagick/). You may refer to the same article to learn about PNG and JPG image formats, and also about ImageMagick.

![Featured Image](/assets/images/post-images/png-eligible.webp)

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

## Generic format
In general, we can use ImageMagick to convert from any image format to any other image format using the syntax below.

```bash
$ convert <source image name & format> <destination image name & format>

# example
$ convert sample.png sample.webp
```
