---
layout: post
title: "Kali Linux 2025.4 Released: GNOME 49, Wayland VM Support, New Tools"
categories: [kali, Linux, Security]
tags: [kali-linux, linux, cybersecurity, wayland]
description: "Kali Linux 2025.4 is released with GNOME 49, KDE Plasma 6.5, Wayland VM support, new security tools, and NetHunter updates."
image: /assets/images/post-images/kali/2025.4.webp
---

Kali Linux 2025.4 is now available. This release focuses on desktop updates, full Wayland support in virtual machines, new tools, and changes to image distribution. The aim remains the same: provide a stable and consistent Kali Linux experience across all platforms.

![Kali Linux 2025.4 released](/assets/images/post-images/kali/2025.4.webp)

## What’s New in Kali Linux 2025.4

Since the 2025.3 release, Kali has introduced updates across all desktop environments, improved Wayland support, and added new security tools.

## Desktop Environment Updates

### GNOME 49

Kali now ships with GNOME 49. The desktop themes have been refreshed, and daily use is more consistent.

Key changes include:

- The **Showtime** app replaces the Totem video player  
- Kali tools are grouped into folders in the app grid  
- A terminal shortcut is available using `Ctrl + Alt + T` or `Win + T`  

GNOME no longer supports X11 sessions. Wayland is now the only display server, and it works smoothly across supported systems.

### KDE Plasma 6.5

KDE Plasma has been updated to version 6.5.

Notable improvements include:

- More flexible window tiling  
- A new screenshot tool with editing options  
- Pinned clipboard items in the panel  
- Fuzzy search support in KRunner  

These changes improve usability without altering familiar workflows.

### Xfce Color Themes

Xfce now supports full color theming. Users can customize colors for icons, GTK applications, Qt applications, and window decorations. Most settings are available in the Appearance application, with Qt settings managed through qt5ct or qt6ct.

## Wayland VM Guest Support

Wayland now fully supports virtual machine guest features. Clipboard sharing, display scaling, and window resizing work correctly when Kali runs as a guest in VirtualBox, VMware, and QEMU. This completes the transition away from X11 in Kali’s desktop environments.

## Kali Live Image Distribution Change

The Kali Live ISO is now distributed only via BitTorrent. The image has grown beyond the 5 GB limit used for CDN-based HTTP downloads. No tools were removed to reduce size. This follows the same approach already used for the larger “Everything” image.

## New Tools Added

Three new tools have been added to the Kali repositories:

- **bpf-linker** – BPF static linker  
- **evil-winrm-py** – Python-based WinRM command execution tool  
- **hexstrike-ai** – MCP server for AI-driven tool automation  

The Linux kernel has also been updated to version **6.16**, along with many package upgrades.

## Kali NetHunter Highlights

Key NetHunter updates in this release include:

- Android 16 support for the Samsung Galaxy S10 series and OnePlus Nord  
- Android 15 support for Xiaomi Mi 9  
- NetHunter Terminal restored with support for modern Magisk versions  
- Wifipumpkin3 previews and updated templates available in the app  

## Documentation and Infrastructure Updates

Kali documentation has been refreshed with new and updated guides. New official mirrors are now available in India, South Korea, and the United States, improving download reliability.

## Availability

Kali Linux 2025.4 is available through fresh installation images and rolling upgrades. Existing users can update using the standard package manager without reinstalling.

For further information and download links, see the [Kali Linux 2025.4 official release announcement](https://www.kali.org/blog/kali-linux-2025-4-release/).
