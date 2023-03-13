---
title: helloSystem r0.8.1 brings core system improvements, UI enhancements, and bug fixes
layout: post
categories: hello release
tags:
  - helloSystem
  - release
  - MAC inspired BSD Desktop
  - Robust mac like desktop experience.
  - MAC like free operating system
image: /assets/images/post-images/hello/0.8.1.png
videoTitle: helloSystem 0.7 Desktop Tour
video: https://www.youtube.com/embed/yzRmH5f2WS8
attribution: ChatGPT, an AI language model
description: helloSystem's latest release, r0.8.1, brings improvements to the core system, bootloader, and user interface, as well as bug fixes and new features.
---

The helloSystem has recently released a new update, version r0.8.1, that addresses feedback from the DistroWatch 0.8.0 review by Jesse Smith. This open-source desktop operating system is built on top of FreeBSD, and the latest release brings several improvements and bug fixes.

![helloSystem 0.8.1 featured image](/assets/images/post-images/hello/0.8.1.png)

The update includes enhancements to the core system, such as USB tethering of Android phones and 5.1 audio systems working out of the box. Swap is enabled by default on disks larger than 80 GB, and keyboard and language choice are now persisted in UEFI NVRAM. The bootloader now loads the kernel and modules without showing text on the screen and adjusts colors for verbose and single-user boot.

The user interface has also been improved, with USB sound devices now shown with their vendor and model in the Volume menu. The "About This Computer" dialog has been updated to show information about the Xorg GPU driver being used, and the "Install FreeBSD" utility is now called "Install helloSystem." The "Processes" utility now shows the total CPU and memory usage and uses application bundle names and icons.

Other enhancements include improved usability of the Create Live Media utility and work on a Backup utility that uses ZFS send/receive to backup zpool/usr/home.

Bug fixes include hardware probe now succeeding uploading, the list of sound devices updating when right-clicking the volume menu, and the dialog to enter a password now showing the correct text following the SUDO_ASKPASS_TEXT conventions.

The helloSystem continues to focus on being user-friendly, beautiful, and straightforward, making it an excellent choice for those looking for a simple and aesthetically pleasing operating system. The new update demonstrates the project's commitment to addressing feedback and improving the user experience.