---
layout: post
title:  "CachyOS March 2026 Release: Animated Desktop Previews, Winboat for Windows Apps, and Major Handheld Edition Upgrades"
categories: cachyos Release
tags: [cachyos, arch-linux, kde-plasma, handheld-gaming, winboat, installer, steam-deck]
excerpt: "CachyOS has dropped its March 2026 ISO with visual desktop previews during installation, one-click Winboat setup for running Windows software via Docker, a refreshed website, and enhanced support for gaming handhelds like Steam Deck and Lenovo Legion Go."
image: /assets/images/post-images/cachyos/march-2026.jpg
---

**The** CachyOS team has just released new ISOs for March 2026 (build 260308), continuing their focus on performance-tuned [Arch Linux](/distribution/arch) with optimizations for modern CPUs and custom kernels.

![CachyOS March 2026 release is available now](/assets/images/post-images/cachyos/march-2026.jpg)

This update stands out for its user-facing improvements: animated previews in the installer, easier Windows compatibility via Winboat, a modernized website, and substantial enhancements to the Handheld Edition aimed at devices like the Steam Deck and Lenovo Legion Go.

## Installer Gets Visual and Smarter Upgrades

The Calamares-based installer now displays animated GIF or WebP previews for selected desktop environments, currently supported for [Plasma](/desktop/plasma), GNOME, Niri, and COSMIC. This gives new users a clear visual sense of each DE before committing.


Other notable installer changes include:
> - JPEG XL support for smaller preview image files
- Desktop environment list reordered from beginner-friendly to advanced (e.g., window managers last)
- Cachy-Update enabled by default on GNOME and KDE installs
- Improved CPU microcode detection (installs only what's needed)
- Clearer error messaging for undersized EFI partitions

## Winboat Integration and Accessibility

The CachyOS-Welcome app now features a convenient button to install and activate Winboat—a Docker-based solution for running Windows applications seamlessly on Linux. Keyboard navigation has been added for better accessibility, and Ukrainian translation support is included.

## Kernel, Tools, and Website Refresh

- The linux-cachyos kernel now uses proper tagged releases in a dedicated repository (replacing the old single-patch approach).
- chwd significantly shrinks initramfs size for NVIDIA discrete GPU setups.
- Mirror rating improved for users in China and Russia via cachyos-rate-mirrors.
- Wireless regulatory domain now auto-configures based on timezone in cachyos-settings.
- The official CachyOS website has undergone a full redesign for a more contemporary feel.

New community mirrors have been added in Russia (jura12 / cachy-arch.ru), Sweden (Zyner), and Canada (All Things Linux).

## Handheld Edition Sees Big Improvements

The Handheld Edition—tailored for portable gaming—receives some of the most exciting changes:

- gamescope-session-plus replaced by gamescope-session-cachyos (a fork of Valve's version) that enables firmware updates via fwupd on Steam Deck and Lenovo Legion Go.
- Login manager switched from SDDM to plasma-login-manager.
- Limine becomes the default bootloader with automatic snapshots (systemd-boot remains an option).
- Handheld and desktop Calamares codebases merged for consistency.
- ISO now defaults to Wayland over X11.
- Better generic handheld profiles and GPU support in chwd; fwupd enabled for Lenovo devices.

## Key Fixes Across the Board
- bcachefs removed from filesystem options (now requires DKMS module).
- Encryption issues with certain LUKS2 setups resolved.
- “ly” display manager activation fixed.
- Sensitive data (IP, username, hostname, MAC) redacted in bug reports.

## Upgrading for Existing Users
If you're already running CachyOS, a standard system update is all that's required—no manual intervention needed:

```bash
sudo pacman -Syu
```

For [further information on CachyOS March 2026 release](https://cachyos.org/blog/2603-march-release/), see the official release announcement in the projects blog.