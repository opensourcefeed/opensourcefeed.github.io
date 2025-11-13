---
layout: post
title: "Nitrux 5.0.0 Released — Now Fully Powered by Hyprland"
description: "Nitrux 5.0.0 marks a major milestone with the switch to Hyprland, new system updates, and a refined design philosophy focused on clarity and intent."
categories: [nitrux, Release, News]
tags: [Nitrux, Linux, Hyprland, Release, KDE, OpenRC, AppHub]
image: /assets/images/post-images/nitrux/nitrux5.webp
---

**The** Nitrux team has announced the release of **Nitrux 5.0.0**, a major update that brings a new desktop experience, system optimizations, and updated core components. This version replaces KDE Plasma with **Hyprland**, marking a new direction for the distribution.

![Nitrux 5.0.0 release poster](/assets/images/post-images/nitrux/nitrux5.webp)

## A New Direction with Hyprland

With version 5.0.0, Nitrux transitions completely from KDE Plasma to **Hyprland**, a modern Wayland compositor. The developers describe this as more than a desktop switch—it reflects a clearer design philosophy. Nitrux aims to be defined by its architecture, not aesthetics. It targets users who value configuration, control, and a streamlined environment.

The team emphasizes that Nitrux is not meant to mimic other systems. Instead, it rewards curiosity and understanding. This release establishes a foundation for a more intentional and consistent user experience.

## Key Changes and Improvements

Nitrux 5.0.0 introduces several updates, new tools, and removals as part of its realignment.

### Major Updates

- **Hyprland** replaces KDE Plasma as the main desktop.
- **OpenRC 0.63** improves system service management.
- **MauiKit and Maui Apps 4.0.2** bring the latest app updates.
- **Liquorix Kernel 6.17.7** powers the standard ISO.
- **NX Overlayroot** strengthens system immutability.
- **NX AppHub and AppBoxes** simplify user-level app management.
- **Flatpak 1.16.1**, **PipeWire 1.4.8**, **NetworkManager 1.52.1**, and **fwupd 2.0.16** deliver improved compatibility and reliability.

Other core tools like **Python 3.13.7**, **OpenSSL 3.5.3**, and **Qt 6.8.2** have also been updated.

### New Additions

Nitrux now includes several new utilities and subsystems:

- **Hyprland utilities**, **Waybar**, and **Crystal Dock** for a refined Wayland experience.  
- **greetd** and **QtGreet** for lightweight login management.  
- **nwg-look** and **nwg-displays** for GTK and display configuration.  
- **NX AppHub CLI** for rootless app management.  
- **Clipvault** clipboard manager and **Sway Notification Center**.  
- **Gamescope** for gaming and **Grimshot** for screenshots.  
- **Ananicy-cpp** for better CPU and I/O scheduling.  

The release also introduces a **CachyOS-patched kernel variant** for advanced users, optimized for high performance systems.

### Removed Components

To align with its new philosophy, Nitrux 5.0.0 removes several legacy components:

- **KDE Plasma**, **KWin**, and **SDDM** have been deprecated.  
- Tools like **Waydroid**, **Tor**, **Fcitx**, **KDEConnect**, and **Touchegg** have been removed.  
- Support for **virtual machine environments** and legacy drivers such as **Hyper-V**, **EVDI**, and **DisplayLink** has also been dropped.  

These removals are part of a move toward a focused, hardware-oriented Linux system.

## Download Nitrux 5.0.0

Two ISO images are available for download:

- **nitrux-contemporary-cachy-nvopen** — for NVIDIA hardware, includes the open-source NVIDIA kernel module and CachyOS kernel.  
- **nitrux-contemporary-liquorix-mesa** — for AMD, Intel, and non-NVIDIA systems.  

Users can verify the authenticity of downloads using the project’s **SHA512 checksums** and **GPG signatures**. Note that the signing key changes bi-monthly.  

The developers recommend a **fresh installation** rather than an upgrade from older versions, due to the major system transitions in this release.

## A Step Toward Intentional Design

The Nitrux 5.0.0 release is more than an update—it’s a reset. It simplifies the system, emphasizes immutability, and focuses on giving users reliable control. By removing legacy elements and embracing Hyprland, the team is shaping a Linux distribution that values intent, precision, and clarity over imitation.

For full release details, changelog, and known issues, visit the [official Nitrux announcement](https://nxos.org/changelog/release-announcement-nitrux-5-0-0/).

