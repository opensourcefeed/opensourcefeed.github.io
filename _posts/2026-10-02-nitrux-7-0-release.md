---
layout: post
title: "Nitrux 7.0 Released with New Workspace Environment"
categories: [nitrux, linux, release]
tags: [nitrux, nitrux-7, hyprland, linux-7-2, mauikit, openrc, systemd-free, immutable, release]
description: "Nitrux 7.0 is out with Linux kernel 7.2.6, Hyprland 0.55.4, and a new first-party Workspace Environment built on MauiKit and OpenRC."
image: /assets/images/post-images/nitrux/nitrux-7-0-release.webp
---

Nitrux 7.0 is out. This Debian-based, systemd-free [Nitrux](/distribution/nitrux) distro ships with Linux kernel 7.2.6 and Hyprland 0.55.4. It also swaps most of its desktop tools for a new set of parts built by the Nitrux team. Nitrux calls the set the Workspace Environment. The release landed on October 1, 2026, more than four months after Nitrux 6.1.

![Nitrux 7.0 featured image](/assets/images/post-images/nitrux/nitrux-7-0-release.webp)

## What is the Workspace Environment?

Older Nitrux releases built the Hyprland session from third-party tools. Version 7.0 replaces them with first-party parts. Each part does one job and runs as its own service.

These services run in a rootless user session. A new tool called `nwsm` manages that session. It is an OpenRC-based session manager from Nitrux. It starts Hyprland, waits for the Wayland socket, and then starts the user services.

The new parts include:

- **Valenz**: the top bar. It has workspace controls, a tray, media controls, a clipboard, and Control Center indicators.
- **Marina**: the dock. It supports several monitors, pinned apps, and window tracking across Hyprland workspaces.
- **Desklock**: a Wayland lock screen written in QML.
- **QMLogout** and **NudgeOSD**: the logout menu and the on-screen display for volume changes.
- **Toma**: a C++ screenshot tool. It replaces the Grimshot script and adds screen recording.
- **Workspace Settings**: the main control center. It covers themes, displays, audio, networking, power, Flatpak permissions, and the greeter.

Nitrux also added a default wallpaper named Blossom. A new MauiKit System framework handles audio, network, power, and notification integration.

## What Nitrux removed

Waybar, Crystal Dock, SwayNC, Hyprlock, Wlogout, and Grimshot are gone from the default setup. You can still get some of them from NX AppHub.

The release also drops Ark, Plasma System Monitor, CoreCtrl, KGpg, Kup Backup, and nwg-look. The Nitrux Power Daemon and Workspace Settings take over from the old `nx-battery-notify`, `nx-dynamic-ppd`, and `nx-envycontrol` scripts.

## AppFinder for software management

AppFinder is a new app built with [MauiKit](/1-nitrux-1.1.0-innovative-znx-mauikit/), the UI framework Nitrux introduced in version 1.1.0. It puts all of Nitrux's software sources in one window:

- NX AppHub recipes (AppBoxes)
- Apps from Flathub
- Personal AppImage recipes, made with a built-in Bundle Builder
- Distrobox development environments

## Kernel, drivers, and core packages

Nitrux 7.0 updates these components:

- Linux kernel 7.2.6 with [CachyOS](/distribution/cachyos) patches
- Hyprland 0.55.4
- KDE Frameworks 6.26.0
- NVIDIA Open Kernel Module 615.71.09
- MauiKit and MauiKit Frameworks 4.0.4
- Nitrux Update Tool System 3.0.3, with a new interface
- Vicinae 0.29.0

The bundled MauiKit apps move to version 4.0.4 as well. Index adds Miller-column browsing and a file-operation dialog. Shelf can save edited PDFs. Clip imports and exports M3U playlists. VVave has a rebuilt music library and a metadata editor. Pix, Nota, Buho, Fiery, and Station get fixes and interface changes.

One change matters if you keep app configs. The MauiKit apps now use `org.maui.*` identifiers instead of `org.kde.*`.

## Security and installer changes

The Calamares installer now builds encrypted installs with LUKS2 instead of LUKS1. It uses Argon2id for key derivation. Nitrux also turned on compression and encryption for F2FS.

The kernel and network settings are tighter too. The release restricts kernel pointers and eBPF. It stops TTY line-discipline autoloading, adds RFC 1337 protection, and disables ICMP redirects.

## Secure Boot warning

The Nitrux GRUB packages contain unsigned UEFI binaries. The default kernel is unsigned too. An installed system may fail to boot if Secure Boot stays on. Nitrux explains the workaround in its [Secure Boot guide](https://nxos.org/documentation/getting-started/installation/installing-nitrux/using-secure-boot-with-nitrux/).

## Download and upgrade

Nitrux 7.0 comes as two ISO images. The `cachy-nvopen` image is for NVIDIA GPUs. The `cachy-mesa` image is for AMD and Intel GPUs. You can get both from the [official release announcement](https://nxos.org/changelog/release-announcement-nitrux-7-0-0/) or from [SourceForge](https://sourceforge.net/projects/nitruxos/files/Release/ISO/).

Users on Nitrux 6.1.0 can upgrade with the Nitrux Update Tool System once the OTA update is ready. Nitrux says its documentation will catch up over the next few days.

For more coverage, see the reports from [Linuxiac](https://linuxiac.com/nitrux-7-0-launches-with-new-workspace-environment-linux-kernel-7-2/) and [9to5Linux](https://9to5linux.com/systemd-free-nitrux-7-0-released-with-linux-kernel-7-2-and-hyprland-0-55-4).
