---
layout: post
title: "CachyOS April 2026 Release Adds Shelly, DNS-over-HTTPS, and Fingerprint sudo"
categories: [cachyos, linux, release]
tags: [cachyos, arch-linux, linux, shelly, dns-over-https, fingerprint, release]
description: "CachyOS April 2026 release introduces Shelly, DNS-over-HTTPS, fingerprint sudo, improved installer, and better hardware support."
image: /assets/images/post-images/cachyos/cachyos-april-2026-release.webp
---

**The** CachyOS team has announced its April 2026 release, the third release of the year. As detailed in the [official release announcement](https://cachyos.org/blog/2604-april-release/), this update introduces a new default package manager, DNS-over-HTTPS support, fingerprint-based sudo, and multiple improvements to the installer and hardware detection.

One of the most notable changes is the introduction of **Shelly** as the default graphical package manager, replacing Octopi. The installer now also creates a clean system snapshot immediately after installation and keeps it as a permanent restore point.

![CachyOS April 2026 Release Image](/assets/images/post-images/cachyos/cachyos-april-2026-release.webp)

GRUB `os-prober` is now enabled by default, allowing the installer to detect other operating systems automatically—useful for dual-boot setups.

The installer has also been updated with a new MangoWM desktop option (including dotfiles), and an option to install MangoWM with the DMS shell. The UKUI desktop has been removed, while the GNOME package selection has been streamlined and modernised.

For AMD GPU users, CachyOS now uses a different Plymouth theme, as the previous one had rendering issues with the `amdgpu` driver on some multi-monitor laptop setups.

## DNS-over-HTTPS and Welcome App Improvements

CachyOS-Welcome now includes **DNS-over-HTTPS (DoH)** support using `blocky`. The updated DNS configuration page allows users to test latency, automatically select the fastest server, or configure custom DNS providers.

Additional improvements include:
- Displaying DNS server metadata such as region and filtering
- A VRAM management toggle (`dmemcg-booster`)
- KDE-specific foreground booster support
- Full keyboard navigation for accessibility
- Updated SVG icons for better HiDPI support
- Integration of `wezterm` in the terminal helper

## Fingerprint sudo and Hardware Enhancements

The `chwd` hardware detection tool now supports fingerprint authentication for sudo prompts via `fprint`, enabling automatic setup on supported devices.

Other improvements include:
- Native USB device detection via `libusb` and `sysfs`
- CPU detection enhancements for better Intel power management
- Improved handheld device detection (including ROG Ally)
- New Wi-Fi profile support for Marvell AVASTAR hardware (Surface Pro 4)

## Storage and Performance Tweaks

CachyOS has switched the default NVMe I/O scheduler from `none` to **kyber**, aiming to improve system responsiveness under mixed workloads.

## Bug Fixes and Stability Improvements

This release includes several fixes across core components:
- Installer now logs selected partition methods
- Old microcode packages are removed when reusing boot partitions
- Improved NVIDIA profile handling in `chwd`
- Removal of forced Xorg sessions in legacy NVIDIA profiles
- Fixes for incorrect handheld detection cases

Some features were also removed or adjusted due to compatibility issues, including:
- Dropping `S01x` power management (NVIDIA 595 issues)
- Disabling `AggressiveVblank` due to VR-related problems

## Updating Existing Systems

No manual intervention is required for existing users. You can update your system with:

```bash
sudo pacman -Syu
```

## Download

The latest CachyOS April 2026 release is available in both Desktop and Handheld editions via official mirrors and SourceForge links provided in the [official release announcement](https://cachyos.org/blog/2604-april-release/).