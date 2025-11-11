---
layout: post
title: "MX Linux 25 “Infinity” Released — Built on Debian 13 Trixie"
categories: [mx, Linux]
tags: [MX Linux, Debian, Release, KDE, Xfce, Fluxbox]
description: MX Linux 25 “Infinity” is now available with Debian 13 base, systemd support, updated desktops, and new MX Tools based on Qt6.
image: /assets/images/post-images/mx/mx-25.webp
---

**MX Linux 25 “Infinity”** is now available for download. This version builds on **Debian 13 Trixie** and introduces major updates to desktops, MX Tools, and the installer.

![MX Linux 25 Infinity Release Poster](/assets/images/post-images/mx/mx-25.webp)

## Overview

MX 25 ships with **systemd** as the default init system for all editions.  
Users who prefer **sysVinit** can choose clearly labeled ISOs available for the Xfce and Fluxbox variants.

Available desktop environments:

- **Xfce 4.20**
- **KDE Plasma 6.3.6**
- **Fluxbox 1.3.7**

Most editions use the **Debian 6.12.48 kernel**, while the **Xfce AHS** variant includes the **6.16 Liquorix kernel** for newer hardware support.

> 📦 You can also explore previous releases like [MX Linux 23 Libretto](/mx-linux-23-libretto-released/) for comparison.

## Key Updates

- **Qt6 Migration:** All MX Tools now use Qt 6 for improved performance and compatibility.  
- **New MX Updater:** The long-standing `apt-notifier` has been replaced by `mx-updater`, which offers optional **nala** backend support.  
- **Installer Improvements:** A new *replace-install* option preserves home folders when reinstalling. Secure Boot is now supported on 64-bit UEFI systems using signed Debian kernels.  
- **ZRAM Swap:** The installer can now create zram swap devices.  
- **MX Cleanup Enhancements:** MX Cleanup can remove unused DKMS drivers and extra language manuals.  

## Desktop Tweaks

- **Xfce:** Updated configuration, with **Engrampa** replacing File-Roller as the archive tool.  
- **KDE Plasma:** Wayland is the default session; X11 is still available. **Qimgv** replaces Gwenview.  
- **Fluxbox:** Updated menus and panel configuration. **Audacious** replaces Deadbeef as the audio player.  

## Other Improvements

- Improved compatibility of the **antiX live system** with systemd.  
- New themes and refreshed artwork.  
- Many bug fixes, optimizations, and translation updates.


## Migration and Availability

Current MX 23 users can visit the [MX Linux migration page](https://mxlinux.org/migration) for upgrade guidance.  

**MX 25 ISOs** are available for **Xfce**, **KDE**, and **Fluxbox** editions — including SysVinit and AHS variants.

Each ISO includes checksums and signature files for verification.

For [more information on MX-25](https://mxlinux.org/blog/mx-25-infinity-isos-now-available/), see the official release announcement in projects blog.