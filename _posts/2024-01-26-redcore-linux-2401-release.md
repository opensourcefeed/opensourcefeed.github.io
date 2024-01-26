---
title: "Redcore Linux Hardened 2401 <em>Tarazed</em> has been released"
layout: post
categories: redcore release
tags:
  - Gentoo for common people
  - Gentoo with Hardened security
  - Power of gentoo to the masses.
image: /assets/images/post-images/redcore/redcore-2401.jpg
description: "Discover the power of RedCore Linux 2401 (Tarazed) – a stable, performance-boosted release with upgraded core components, modern graphics, and an overhauled sound stack. Explore the latest features now!"
---

**RedCore Linux**, a dynamic operating system rooted in Gentoo Linux, proudly presents its latest stable ISO, version 2401, codenamed Tarazed. After 11 months of meticulous development, this release focuses on refining the core components and improving user experience.

![RedCore Linux 2401 featured image](/assets/images/post-images/redcore/redcore-2401.jpg)

## What’s New in RedCore Linux 2401?

Following section briefly examines the key highlights in the RedCore Linux 2401 release.

### Up-to-Date Core Components

- Resync with Gentoo Linux' testing tree as of 21.01.2024.
- Linux kernel v6.6.13 LTS as the default, with options for v6.1 LTS and v5.15 LTS in repositories for those preferring older kernels.

### Toolchain Upgrade
- Glibc v2.37, gcc v13.2.0, binutils v2.40, clang/llvm v17.0.6, rust v1.74.1 form the basis of the latest toolchain.

### Modernized Graphics
- RedCore Linux 2401 includes the latest Mesa, Xorg, Xwayland, and Wayland components, providing an up-to-date graphical stack.

### Revamped Sound Stack
- Pipewire takes the spotlight as the default sound server implementation, replacing both PulseAudio and JACK, ushering in a modern era for the sound stack.


### Library and Tool Updates

- OpenSSL v3 is now the default, departing from the older OpenSSL v1.
- FFmpeg v6 replaces the previous FFmpeg v4, ensuring compatibility and enhanced multimedia capabilities.

### Kernel Features:

- Landlock LSM is now enabled by default in RedCore Linux kernel builds, empowering applications to leverage its capabilities.

### Sisyphus Package Manager Enhancements:

- Sisyphus' backend has been completely rewritten, providing a cleaner API and decoupling it from the frontend.
- Sisyphus now suggests correct package names, improving the user experience.
- Installation of packages without marking them explicitly installed is now possible.
- Improved handling of packages with identical names but different categories.
- Proper exchange of configuration information between Sisyphus and Portage without conflicts.

For [further information on RedCore Linux 2401](https://redcorelinux.org/news/redcore-linux-hardened-2401-tarazed-stable) release, see the official release announcement in the project's website.

## Download RedCore Linux 2401 Tarazed

RedCore Linux 2401 Tarazed is available for free download from the projects official download page. It brings the KDE Plasma Desktop environment. The download mirror is available in different regions.

<a href="https://redcorelinux.org/download" class="download">Download RedCore Linux 2401 Tarazed</a>