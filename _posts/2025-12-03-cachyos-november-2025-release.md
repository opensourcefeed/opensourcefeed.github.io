---
layout: post
title: "CachyOS November 2025 Release Brings Accessibility Upgrades and Hardware Improvements"
categories: [Linux, cachyos, Release]
tags: [CachyOS, Linux, Accessibility, Plasma Login Manager, COSMIC, Bcachefs, NVIDIA]
description: "CachyOS November 2025 release adds accessibility tools, hardware improvements, login manager changes, and key fixes."
image: /assets/images/post-images/cache-nov2025.webp
---

**CachyOS** has published its **November 2025 release**, the seventh update this year. This update improves accessibility, hardware support, installer behavior, and gaming features.

![CachyOS November 2025 release](/assets/images/post-images/cache-nov2025.webp)

## Accessibility Improvements

The ISO and installer now include **Orca** and **espeak-ng**. These tools offer screen-reading support and help users with visual impairments install CachyOS without barriers.

## mkinitcpio and Filesystem Updates

CachyOS now enables the **systemd mkinitcpio hook** for supported setups. The hook disables itself when users choose **ZFS** or **Bcachefs**.  
For Bcachefs users, the release adds **bcachefs-dkms**, which replaces the default module and offers better integration.

## Login Manager and Desktop Enhancements

The installer now supports:

- **Plasma Login Manager**  
- **Cosmic Greeter**

Cosmic installations now use **Cosmic Greeter** instead of SDDM. Plasma Login Manager remains available but is not yet the default due to missing KDE Settings integration.

## Hardware Detection Improvements

The system now installs the following on supported hardware:

- **intel-media-sdk**
- **vpl-gpu-rt**

Support for the legacy **NVIDIA 390xx** driver is removed. Fermi GPUs now use **Nouveau NvBoost**.

This release also adds support for the **Xbox ROG Ally** and **ROG Ally X** handheld devices.

## Installer and System Tools

**CachyOS-Hello** now opens the main PackageInstaller instead of using an internal one. It also supports CLI operations for GUI features.

In **cachyos-settings**, recompression is disabled for pages that ZRAM cannot compress, as it offered no benefit.

## Proton-CachyOS Improvements

The gaming stack receives several updates:

- **dxvk-gplasync** is now available as an alternative DXVK through `PROTON_DXVK_GPLASYNC=1`.
- AMD’s Anti-Lag layer is disabled when enabling `PROTON_FSR4_UPGRADE` due to stability issues.
- Wayland fixes improve fullscreen behavior, dead keys, DPI, and video output.
- A tuned **per-game shader cache** reduces cache overflow and shader recompilation.
- Added upgrades for **FSR3** and **XeSS**.

## Fixes

### Limine Bootloader
- Fixed cases where entries did not register on systems with broken UEFI.
- The system now uses the **systemd btrfs-overlayfs hook** for compatibility.

### Installer (Calamares)
- Removed the **attr2** option for XFS mount settings.

### Hardware Detection (chwd)
- Disabled the T2 chip’s USB Ethernet interface.

For [further informations on CachyOS november 2025 update](https://cachyos.org/blog/2511-november-release/), see the official release announcement.

