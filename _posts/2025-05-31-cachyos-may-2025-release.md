---
title: "CachyOS May 2025 Release: Enhanced Theming, Compatibility, and Handheld Support"
layout: post
categories: [linux, cachyos, release]
tags: [CachyOS, Linux, Arch, NVIDIA, Proton, Handheld]
description: CachyOS May 2025 release brings new theming, NVIDIA fixes, Proton 10, and better support for handhelds. Explore all the latest updates.
image: /assets/images/post-images/cachyos-may-2025.webp
---

**The** CachyOS team announced the release of the CachyOS May 2025 edition. CachyOS is a performance-focused, Arch-based Linux distribution designed to provide a fast, responsive, and customizable experience for desktop and handheld users. The CachyOS May 2025 release includes unified system theming, improved NVIDIA GPU support, Steam Deck enhancements, and updates to Proton-CachyOS for better gaming performance.

![CachyOS May 2025 featured image](/assets/images/post-images/cachyos-may-2025.webp)

## ✨ Highlights of the May 2025 Release

### 🎨 Unified Theming and Visual Enhancements

The May 2025 release introduces a new Plymouth boot animation and a refreshed GRUB theme, aiming to provide a cohesive and modern visual experience across the system. These enhancements will be automatically applied to new installations. Existing users can manually adopt these changes by following the instructions provided in the release notes.

### 🖥️ Improved NVIDIA GPU Support

Addressing previous challenges with older NVIDIA GPUs, particularly the 10xx series and earlier, the May 2025 release introduces an automatic driver detection mechanism in the Live ISO. This system intelligently loads the appropriate proprietary NVIDIA module during boot, eliminating the need for a separate “NVIDIA” boot entry and enhancing compatibility for a broader range of hardware.

### 🌐 Deprecation of Cachy-Browser

Due to limited maintenance resources, the in-house Cachy-Browser has been deprecated. Users will receive a prompt upon launching the browser, guiding them through the process of migrating their profiles to Firefox or compatible alternatives, ensuring continued security and a consistent browsing experience.

### 🌍 Enhanced Mirror Availability

To improve download speeds for users in Asia, a new 10 Gbps mirror has been added in Bangladesh, courtesy of Limda Hosting. This addition aims to provide better connectivity and faster updates for users in the region.

### 🎮 Handheld Edition Enhancements

The handheld edition of CachyOS sees notable improvements, including the integration of SteamOS-Manager and enhancements to the Live ISO's automatic detection capabilities. These updates aim to provide a more seamless and optimized experience for users on devices like the Steam Deck.

### 🕹️ Proton-CachyOS Updates

Gamers will benefit from the updated Proton-CachyOS package, now rebased to Proton 10. This update brings full Wayland support for the Steam Linux Runtime, Wine patches related to Wayland, improved FSR4 (FidelityFX Super Resolution) support tailored for RDNA4 GPUs, and haptics support for the DualSense controller. These enhancements aim to deliver a smoother and more immersive gaming experience.

### 🔧 Additional Fixes and Improvements

- **Russia CDN Fix:** The `cachyos-rate-mirrors` script now includes a fallback mechanism to address CDN blocks in Russia, ensuring smoother installations.
- **KDE Taskbar:** The "Discover" application launcher icon has been removed from the KDE taskbar for a cleaner interface.
- **ddcutil Update:** Updated to the latest RC version to fix issues causing freezes on AMD GPUs during video playback.

---

For a comprehensive overview and detailed instructions on these updates, please refer to the official [CachyOS May 2025 Release Announcement](https://cachyos.org/blog/2505-may-release/).