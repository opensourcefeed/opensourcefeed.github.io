---
layout: post
title: "Sparky Linux 7.8 Released with Updated Packages and Fixes"
categories: [Linux, sparky]
tags: [SparkyLinux, Debian, Linux Distro, Orion Belt, Release]
description: "Sparky Linux 7.8, the latest point release of Orion Belt series based on Debian 12, is now available with updated packages and fixes."
image: /assets/images/post-images/sparky/sparky-7.8.jpg
---

**Sparky Linux 7.8**, the eighth point release of the *Orion Belt* stable series, is now available for download. This quarterly update brings in the latest security patches, performance improvements, and updated packages from both Sparky and Debian 12 "Bookworm".

![Sparky 7.8 featured image](/assets/images/post-images/sparky/sparky-7.8.jpg)

### 🔧 What’s New in Sparky 7.8?

Here’s a quick overview of the notable changes and updates:

> - System base updated with all packages from Debian and Sparky stable repos as of **July 14, 2025**
- **Linux kernel (PC)**: 6.1.140-LTS  
  (Optional kernels available: 6.15.6, 6.12.38-LTS, 6.6.98-LTS in Sparky repos)
- **LibreOffice**: 7.4.7  
  (You can also access version 25.2.3 from Debian backports)
- Desktop environments:
  - KDE Plasma 5.27.5
  - LXQt 1.2.0
  - MATE 1.26
  - Xfce 4.18
  - Openbox 3.6.1
- **Firefox ESR**: 128.12.0esr  
  (v140.0.4 available in Sparky repos)
- **Thunderbird ESR**: 128.12.0esr
- **GIMP** is now preinstalled in the live media
- **Fixed**: Library conflicts caused by older Debian Multimedia packages have been resolved  
  _(Tip: Uninstall `libavutil57` v10:5.1.3 and its dependencies, then reinstall version 7:5.1.6 if needed.)_

> ⚠️ **ARM images are not updated in this release** — ARM users should continue using version 7.7.

### 💻 Available Editions

Sparky 7.8 “Orion Belt” is available for various platforms:

#### For amd64 (BIOS/UEFI + Secure Boot):
- Xfce
- LXQt
- MATE
- KDE Plasma
- MinimalGUI (Openbox)
- MinimalCLI (text mode)

#### For i686 (non-PAE BIOS/UEFI - Legacy):
- MinimalGUI (Openbox)
- MinimalCLI (text mode)

#### ARM Editions (7.7 only):
- ARMHF & ARM64: Openbox & CLI

### 🔐 Default Login Credentials
- **PC (Live)**: `live:live`  
- **ARM**: `pi:sparky`

### 🔄 Already Using Sparky 7?

No need to reinstall! Just keep your system up to date using your package manager.

### 📥 Download Now

Get the latest Sparky 7.8 ISO images from the official [Sparky Linux Download Page](https://sparkylinux.org/download/stable/)

For [further information on Sparky 7.8](https://sparkylinux.org/sparky-7-8/), see the official release announcement.

