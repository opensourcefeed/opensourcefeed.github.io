---
layout: post
title: "PorteuX 2.4 Released with COSMIC Desktop and Major Fixes"
description: "PorteuX 2.4 introduces the COSMIC desktop environment, improved performance, and key bug fixes. It is the final release based on Slackware stable."
categories: [porteux, Linux]
tags: [PorteuX, Slackware, Linux, Release]
image: /assets/images/post-images/PorteuX-2.4.webp
---

PorteuX 2.4 is now available, introducing the **COSMIC desktop environment** for the current branch. The COSMIC desktop is still in beta, so users should expect some issues, such as high CPU usage from `cosmic-osd`.  

![PorteuX 2.4 release poster](/assets/images/post-images/PorteuX-2.4.webp)

This update also marks an important milestone — **PorteuX 2.4 is the final release to include a version based on Slackware stable**. The team decided to move fully to the rolling branch, which is tested extensively before each release and offers a more up-to-date experience.

## Key Fixes

This release includes several improvements across different desktop environments and system components:

- Fixed system time synchronization during boot. When the timezone is set, both system and BIOS clocks now update using the NTP server.  
- Fixed cheatcode handling when using UUIDs without trailing slashes.  
- Fixed rendering issues in Cinnamon on Wayland and Xorg session problems in KDE Plasma.  
- Fixed cropped and small title bars in Xfce and Openbox.  
- Fixed notification close button display in LXQt.  
- Improved linker flags for better performance and smaller binaries.  
- Improved PorteuX Language Switcher with search and filter features.  
- Improved touchpad support and reliability of the deactivate script.  

## New Additions

PorteuX 2.4 introduces new tools and expanded functionality:

- **COSMIC desktop environment** (available on current only).  
- **PorteuX Timezone Switcher** – a new tool to manage timezone and clock type (localtime or UTC).  
- **New cheatcodes:** `noupdateclock` to disable automatic time updates, and `kmap` support for Wayland sessions.  
- Added autoload support for **cron** and **docker** daemons.  
- Added HEIC image support in LXQt.  

## Updates and Changes

The release brings refreshed software packages and themes:

- Kernel updated to **6.17.7**.  
- NVIDIA driver updated to **580.105.08**.  
- Desktop environments updated:  
  - Cinnamon 6.4.13  
  - GNOME 49.1  
  - KDE Plasma 6.5.2  
  - LXQt 2.3.0  
- MATE search tool now displays sizes in binary units (KiB, MiB, GiB).  
- LXDE theme updated to match the PorteuX style.  
- PorteuX Modules application rewritten for faster performance.  
- Elementary icon set in Xfce now adapts automatically to dark or light themes.  

## Looking Ahead

With this release, PorteuX shifts its focus to the **rolling branch**, ensuring users have access to the latest packages and desktop environments. Users on the stable version can expect continued reliability, but future innovation will center on the current branch.

For [detailed technical notes on PorteuX 2.4](https://github.com/porteux/porteux/releases/tag/v2.4), visit the official release announcement.