---
title: How to convert PNG images to JPG using ImageMagick in Linux?
layout: post
categories:
- tutorial
- linux
tags:
- imagemagick
- imagemagickconvertpng to jpg
- imagemagickpngto jpg
- imagemagickconvertto jpg
image: "/assets/images/post-images/png-eligible.webp"
description: A brief tutorial explaining how to convert PNG images to JPG using the ImageMagick/convert tool. Also, learn the difference between PNG and JPG images.
redirect_from:
    - /2021/06/how-to-convert-png-images-to-jpg-using-imagemagick-in-linux/
---

**When** dealing with images, we may have to do several format conversions. Depending on the situation, it can be a JPG to PNG conversion, PNG to SVG conversion, or anything. ImageMagick is a tool that supports most of these image format conversions along with the other operations like resizing, reducing the size, changing color scheme ..etc. In this tutorial, we will see how to convert a PNG file to a JPG file. Also, we'll check how to perform this image conversion as a batch job.

Before jumping to the details, let's get familiar with the terms used here, ie, JPG, PNG, and ImageMagick. If you are already familiar with these, you can directly skip to the conversion part.

## PNG Image Format
PNG (Portable Network Graphics) a raster image format. Raster images use a lossless image compression algorithm. In PNG format, the image will be represented as a collection of interconnected points. The quality of the image will remain unaffected on resizing.

![PNG format is good for simple images](/assets/images/post-images/png-eligible.webp)
*PNG format is best for simple icons & shapes*

PNG format can be used for any image files. However, it is more suitable for icons, symbols, or small shapes which does not require a lot of points to represent. It will consume more space for complex images like photographs. So, it is better to convert complex images into other formats like JPE when we are using it on the Web.

## JPG Image Format
JPG or JPEG (Joint Photographic Experts Group) is a commonly used lossy compression approach for digital photographs. It allows adjusting the compression ratio with a tradeoff between compression and quality of the image.

![JPG format is suitable for complex images](/assets/images/post-images/kde-neon-5.10.jpg)
*JPG format is good for complex shapes*

With JPG format, the quality of the image reduces with compression ratio. More compression implies, less quality and less storage space requirement. This format is used for embedding photographs or complex images on websites.

## ImageMagick
ImageMagick is an open-source tool that provides advanced image manipulation functionalities to create, edit and convert images. It supports more than 200 types of image formats. ImageMagick facilitates resize, flip, rotate, distort, shear, and transform images. It also helps to apply special effects.

Commonly, ImageMagick is used as a command-line tool, which makes it suitable for batch operations. There are many GUI clients which use ImageMagick underhood for performing image manipulation operations.

## How to perform PNG to JPG conversion using ImageMagick?
Now, we are familiar with PNG, JPG, and ImageMagick. So, it is time to talk about the actual topic. How to perform PNG to JPG conversion.

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

If we want to convert multiple jobs at once, we may use a simple batch job as follows:
```bash
for image in *.png ; 
do 
    convert "$image" "${image%.*}.jpg" ;
done
```
In one line, it can be written like,
```bash
$ for image in *.png ;  do convert "$image" "${image%.*}.jpg" ; done
```

## How to convert PNG to JPG by specifying background color?

In some scenarios, PNG images will be coming with transparent background. If we convert those images directly to JPG, it is likely to cause some unexpected results. In such cases, we can specify the background color, so that, the transparency will be replaced with the specific background color.

For converting a single image with background color,
```bash
convert original-image.png -background white -flatten -alpha off new-image.jpg
```

For converting multiple image files with background color,
```bash
for image in *.png ;  do convert "$image" -background white -flatten -alpha off  "${image%.*}.jpg"; done
```

## How to convert from any image format to any other image format?
The *convert* tool provided by ImageMagick can convert from any image format to any other image format. The above example showcases, how to convert a PNG image to a JPG image.

In general, we can perform the image conversion like,
```bash
$ convert <source image name & format> <destination image name & format>
# example
$ convert sample.png sample.webp
```

That's all for now. This post is inspired by an [answer given in superuser - an affiliate of StackExange](https://superuser.com/questions/71028/batch-converting-png-to-jpg-in-linux).

In case of any issues, or clarification please let me know via the comment box below.

You may also read, [tutorial on converting jpg images to png](/convert-jpg-to-png-imagemagick/)
