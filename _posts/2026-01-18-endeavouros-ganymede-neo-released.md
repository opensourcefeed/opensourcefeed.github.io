---
layout: post
title: "EndeavourOS 2026.01.12 Ganymede Neo Released With Updated ISO and Installer Fixes"
categories:
  - endeavour
  - Linux
  - Distribution Release
tags:
  - EndeavourOS
  - Arch Linux
  - Linux Release
  - Open Source
description: "EndeavourOS Ganymede Neo 2026.01.12 is released with updated packages, Calamares installer fixes, and NVIDIA driver changes for new installs."
image: /assets/images/post-images/endeavouros/2026.01.12-banner.jpg
---

**The** EndeavourOS team has released EndeavourOS Ganymede Neo (2026.01.12), a refreshed ISO that includes upstream updates and minor changes compared to the original Ganymede ISO.

![EndeavourOS 2026.01.12 release](/assets/images/post-images/endeavouros/2026.01.12-banner.jpg)

According to the project, Neo releases ship with updated packages and small adjustments.

## What ships with Ganymede Neo (2026.01.12)?

The Ganymede Neo ISO and offline installer ship with the following components:

> - **Calamares** 26.01.1.5-1  
- **Firefox** 146.0.1-1  
- **Linux kernel** 6.18.4.arch1-1  
- **Mesa** 1:25.3.3-2  
- **Xorg Server** 21.1.21-1  
- **NVIDIA utilities** 590.48.01-2  

## Bug fixes and changes

Ganymede Neo includes the following fixes and changes:

- The long startup time issue in the Calamares installer has been resolved.
- The **Nemo Preview** package has been removed from the default Cinnamon and Budgie installation bundles. This follows its removal from the Arch Linux repositories.
- The proprietary NVIDIA driver option now uses **nvidia-open**, following upstream changes to NVIDIA drivers announced by Arch Linux.

With this change:
- The proprietary driver option supports **Turing GPUs (GTX 16xx) and newer**.
- Earlier NVIDIA GPUs remain supported using the default boot option, which loads the **Nouveau** open-source driver.

## Availability and next release

The **Ganymede Neo ISO** is available for free download from the EndeavourOS homepage.

For [further reading on EndeavourOS 2026.01.12](https://endeavouros.com/news/ganymede-neo-is-out-with-core-updates-and-upstream-nvidia-changes/), see the official release announcement.
