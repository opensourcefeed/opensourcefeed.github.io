---
title: "Endeavour OS Galileo Neo Version 2024-01-25: A Kernel-Powered Refresh"
layout: post
categories: endeavour release
tags:
  - Arch based rolling GNU/Linux distribution
  - User friendly Arch derivative
image: /assets/images/post-images/endeavouros/galileo-20240125.jpg
description: Discover the power of Endeavour OS Galileo Neo 2024-01-25! Updated Linux kernel, streamlined installation, and fixes for an optimized Linux experience. Upgrade now!
---

**The** Endeavour OS team has announced the latest iteration of Endeavour OS Galileo Neo, version 2024-01-25. In this update, the focus remains on delivering essential fixes and core package updates, ensuring a seamless experience for both ISO and the offline KDE Plasma option users.

![Endeavour OS Galileo Neo featured image](/assets/images/post-images/endeavouros/galileo-20240125.jpg)

## What's New in Galileo Neo Version 2024-01-25?

### Kernel Power: Linux 6.7.1.arch1-1

The cornerstone of this release is the updated Linux kernel, version 6.7.1.arch1-1, providing enhanced performance and compatibility. This empowers your system with the latest advancements in the Linux ecosystem.

### Streamlined Installation: Calamares 23.11.1.4-1

Endeavour OS's commitment to user-friendly experiences continues with Calamares 23.11.1.4-1, ensuring a smooth and intuitive installation process. This version brings necessary fixes to enhance the overall stability of the installation procedure.

### Web Browsing Reinvented: Firefox 122.0-1

Stay connected with the latest web technologies using Firefox 122.0-1. This update ensures that your browsing experience is not only secure but also optimized for peak performance.

### Graphics Powerhouse: Mesa 1:23.3.3-1 and Xorg-server 21.1.11-1

Galileo Neo remains at the forefront of graphics technology with Mesa 1:23.3.3-1 and Xorg-server 21.1.11-1. These updates bring essential improvements, ensuring a visually stunning and responsive interface.

### NVIDIA Compatibility: Nvidia-dkms 545.29.1.06-1

For users with NVIDIA graphics cards, Galileo Neo includes Nvidia-dkms 545.29.1.06-1, offering seamless compatibility and optimal performance for your hardware.

## Galileo Neo Fixes

In addition to these updates, Galileo Neo version 2024-01-25 addresses specific issues to elevate the Endeavour OS experience:

- Bash Script Enhancements: Several fixes have been implemented in the Bash script, addressing issues related to running Wayland sessions when the KDE Plasma offline installation option is selected.
- Legacy Graphics Stabilized: Annoying effects and composition issues on the Plasma Live Environment with machines running legacy Intel graphics have been successfully resolved.
- Kernel LTS Auto-Installation: The r8168-lts package is now automatically installed when the Linux kernel LTS is selected in Calamares, ensuring a hassle-free experience for users.
- Online Installation Bug Squashed: The installer now fetches the old named packages seamlessly when the KDE Plasma online installation option is selected.
- Efficient Installation Error Handling: In the event of an installation error, Calamares now properly unmounts the target device, allowing for immediate reuse of the device for another installation session without the need to reboot the ISO.

For further information, read the [Endeavour OS Galileo Neo release announcement](https://endeavouros.com/news/galileo-neo-with-kernel-6-7-1-plasma-offline-and-calamares-fixes/) in the projects official blog.