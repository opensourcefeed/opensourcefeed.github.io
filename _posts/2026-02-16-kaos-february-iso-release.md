---
layout: post
title: "KaOS 2026.02 Tests New Desktop Environment"
description: "KaOS 2026.02 tests a new desktop setup, updates core packages, and keeps its Qt-focused Linux distribution approach."
categories: [kaos, Linux]
tags: [KaOS, Linux distribution, Wayland, Qt, Rolling Release]
image: /assets/images/post-images/kaos/kaos-2026.02.jpg
---

**The** KaOS team has released a new 2026.02. This Linux distribution is known for its KDE Plasma focus, but this release tests a different desktop setup while keeping its Qt-based design.

![KaOS 2026.02 experiments with a new desktop](/assets/images/post-images/kaos/kaos-2026.02.jpg)

## What’s New in KaOS 2026.02?

### Test desktop environment

* Plasma and KWin are not included on this ISO.
* The system uses **niri** with the Noctalia shell and Quickshell on Qt 6.10.2.
* A Wayland compositor manages windows and display. It replaces the traditional X11 approach.
* Plasma 6 remains available in the repositories. This ISO supports wider testing.

### Bootloader change

* Limine is now the default bootloader.
* Other UEFI boot choices remain available in the Calamares installer.

### Core system updates

* Linux kernel 6.18.10
* GCC 15.2.1, Glibc 2.42, Binutils 2.45.1
* Mesa 25.3.5, PipeWire 1.4.9, GStreamer 1.28
* OpenSSH 10.2, Bash 5.3, CMake 4.2
* ISO uses systemd 255.22; installed systems move to 257.10.

### Installer and usability changes

* Calamares no longer opens a browser as root on the welcome page.
* Extra details now show through a QML drawer.
* Automatic partitioning supports XFS, EXT4, BTRFS, and ZFS.
* Default XFS uses CRC and finobt features for better file-system reliability.

### Multimedia and display updates

* phonon-mpv replaces VLC as the sound backend for full Qt6 support.
* SDDM can run in Wayland mode.
* Kjournald provides a GUI tool to view system logs.

### Other notes

* Croeso setup helper assists with common post-install settings.
* Early CPU microcode updates are built into the kernel.
* New artwork includes a custom icon theme.
* Mirror and server support now comes from **YourHostingSolutions** after the shutdown of **Fosshost**.

## Download

You can download the latest ISO from the official KaOS website.
GPG signatures are available to verify file authenticity.

<a href="https://kaosx.us/download/#authenticity-check" class="download">Download KaOS 2026.02</a>

For [further information on KaOS 2026.02](https://kaosx.us/news/2026/kaos02/), see the official release announcement on projects website.
