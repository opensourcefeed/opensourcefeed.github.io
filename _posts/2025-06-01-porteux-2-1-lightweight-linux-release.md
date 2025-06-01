---
title: "PorteuX 2.1 Released: A modular Linux Distro with Linux Kernel 6.15"
layout: post
categories: [Linux, PorteuX, Release]
tags: [PorteuX, Linux, Slackware, lightweight, portable, Linux 6.15]
description: PorteuX 2.1 brings Linux kernel 6.15, system improvements, and enhanced performance to this portable and modular Linux distro.
image: /assets/images/post-images/PorteuX-2.1-featured.jpg
---

**PorteuX**, the modular and portable Linux distribution inspired by Slax and Porteus, has announced the release of version 2.1. This update brings significant enhancements, including the integration of the latest Linux 6.15 kernel, improved hardware support, and various system optimizations.

![PorteuX 2.1 featured image](/assets/images/post-images/PorteuX-2.1-featured.jpg)

## 🔧 Key Enhancements in PorteuX 2.1

- **Adoption of Linux Kernel 6.15**: PorteuX 2.1 is among the first distributions to incorporate the Linux 6.15 kernel, offering improved hardware compatibility and performance enhancements.

- **Transition to Native NTFS Driver**: The default NTFS driver has been switched from `ntfs-3g` to the kernel-native `ntfs3`. This change aims to provide better performance and integration. Users should note that symlinks stored on NTFS partitions will need to be regenerated.

- **VirtualBox Compatibility Update**: Due to compatibility issues between VirtualBox 7.1.8 and kernel 6.15, PorteuX 2.1 includes a module for VirtualBox 7.2.0 Beta 1. Users are advised to enable 3D acceleration in VirtualBox settings to ensure optimal performance.

- **Bug Fixes and System Improvements**:
  - Resolved an issue where modules could be incorrectly detected as corrupted.
  - Made the Linux installer language-agnostic.
  - Fixed missing `.Xresources` and `.Xmodmap` in the LightDM Xsession file.
  - Addressed the `login=` cheatcode functionality.
  - Corrected issues with `sudo.py` and `pipewire` in the Openbox session.
  - Fixed missing hardware information in the Xfce "About" section.

---

## 🖥️ Desktop Environment Options

PorteuX 2.1 continues to offer a selection of seven desktop environments, catering to various user preferences:

- Cinnamon
- GNOME
- KDE Plasma
- LXDE
- LXQt
- MATE
- Xfce

Each environment is pre-configured with lightweight applications, ensuring a smooth out-of-the-box experience.

---

## 📥 Download and Installation

PorteuX 2.1 is available for download on its [GitHub Releases page](https://github.com/porteux/porteux/releases/tag/v2.1). The distribution is designed for portability and can be run from USB drives or other bootable media.

Installation involves copying the ISO contents to the desired media and executing the appropriate installer script (`porteux-installer-for-linux.run` or `porteux-installer-for-windows.exe`). Users are advised against using ISO installer applications like Rufus or Etcher, as they may render the bootable unit read-only.