---
layout: post
title: "Tiny Core Linux 17.0 Released with Kernel 6.18.2 and Updated Toolchain"
description: "Tiny Core Linux 17.0 released Feb 10, 2026 with kernel 6.18.2, updated GCC, glibc, and lightweight ISO images from ~20MB."
categories: [tinycore, Linux, Open Source, Releases]
tags: [Tiny Core Linux, Linux Release, Lightweight Linux, Open Source, Linux Kernel]
image: /assets/images/post-images/tinycore-v17.jpg
---

Tiny Core Linux 17.0 was released on February 10, 2026. This version updates core system packages, improves scripts, and keeps the distro small and fast.

![Tiny Core v17.0 released](/assets/images/post-images/tinycore-v17.jpg)

Tiny Core Linux is known for its minimal size. The system runs mainly from RAM and users install apps as extensions. This keeps performance high even on older hardware.

## What's new in Tiny Core v17.0?

### Core System Updates

- Linux kernel updated to **6.18.2**
- glibc updated to **2.42**
- GCC updated to **15.2.0**
- binutils updated to **2.45.1**
- e2fsprogs updated to **1.47.3**
- util-linux updated to **2.41.2**

These updates improve hardware support, compatibility, and development tools.

### ISO Image Sizes

This release keeps the lightweight design:

- **Core ISO:** ~20 MB  
- **TinyCore ISO:** ~26 MB  
- **CorePlus ISO:** ~288 MB (includes more drivers and desktop tools)

Users can pick the edition based on their needs.

### System Improvements

Maintenance updates include:

- HTTPS mirror support updates  
- Fixes in `tce-update` fetch handling  
- Improved HTTPS checks in system scripts  
- PATH update to include `/usr/local/bin`  
- Shutdown script fixes for file list handling  
- Expanded udev input device permissions  

These changes improve reliability and usability.

## Download Tiny Core v17.0

- http://www.tinycorelinux.net/17.x/x86/release  
- http://www.tinycorelinux.net/17.x/x86_64/release  

You may also the [Tiny Core v17.0 release announcement](https://forum.tinycorelinux.net/index.php/topic,28008.0.html) in the project forum website.
