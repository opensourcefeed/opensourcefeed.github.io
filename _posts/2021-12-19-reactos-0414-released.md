---
title: ReactOS 0.4.14 released
description: ReactOS team announced the release of ReactOS 0.4.14 - a relatively stable release of ReactOS with several improvements in bootloader, kernel and the shell.
layout: post
categories: reactos release
tags:
  - reactos
  - release
  - windows like distribution
  - operating system supporting windows executable
  - windows like operating system
image: /assets/images/post-images/reactos/reactos_0414.jpg
video: https://www.youtube.com/embed/JTSednp-RqA 
---

**The** ReactOS team has announced the release of ReactOS 0.4.14. ReactOS 0.4.14 brings several improvements and fixes in different components ranging from Freeloader (the bootloader) to the shell.

![ReactOS 0.4.14 featured image](/assets/images/post-images/reactos/reactos_0414.jpg)
*Image Courtesy: Official release announcement*

ReactOS 0.4.14 is a result of 1 year of development and regression effort. It does not include many of the latest development updates announced in 2021, but it includes several regression fixes and patches to provide a more solid experience. Those who prefer to explore the latest enhancements instead of a robust experience can try the nightly builds.

## What is new in ReactOS 0.4.14?
The key features in the ReactOS 0.4.14 release are as follows.
> - The shell introduces a 'Send To' feature with which files can be sent to a predefined location with the right-click. Also, there are options for opening file location of shortcuts and for opening terminal anywhere with the right-click menu.
- Introduces NEC PC-9800 boot support. NEC PC-9800 (or PC-98 in short) is a series of 16-bit and 32-bit Japanese computers developed and manufactured by NEC. As that type of hardware is based on x86 processors, it is a relatively easy porting target.
- Improvements in ICMP (Internet Control Message Protocol) which range from the implementation of the IOCTL_ICMP_ECHO_REQUEST I/O control code to a full rewrite of the Icmp** routines.
- Improvements and enhancemnets to the kernel to increase the overall robustiness of the system.
- Introduces support for booting Linux 64-bit systems in 64-bit FreeLoader and fixed an issue where FreeLoader couldn’t read from an EXT2 volume, hence preventing booting.
- Reduced memory footprint due to obsolete fonts being removed (116 MB to 92 MB)

For [other changes in ReactOS 0.4.14 release](https://reactos.org/project-news/reactos-0414-released/), read the official release announcement in the ReactOS website.

## Download ReactOS 0.4.14
You can download ReactOS 0.4.14 or the latest release from the offiical download page. The download page, follows a 'Pay What you Want' model. So, we are not providing the direct download link. Instead, you can find the link in the ReactOS download page.

<a class="download" href="https://reactos.org/download/">Download ReactOS 0.4.14</a>

## ReactOS 0.4.14 screenshots
{% include image-gallery.html folder="/screenshots/ReactOS 0.4.14" %}