---
layout: post
title: "antiX 26 Released: Debian Trixie, Five Init Systems"
categories: [antix, debian, release]
tags: [antix, antix-26, debian, trixie, systemd-free, lightweight, linux]
description: "antiX 26 is out, based on Debian 13 Trixie, featuring five init systems, updated kernels, IceWM, and a full application suite for old and new hardware."
image: /assets/images/post-images/antix/antix26.jpg
---

**The** antiX community has announced the release of antiX 26, named after [Stephen Kapos](https://www.counterfire.org/article/a-life-through-dictatorship-holocaust-and-protest-interview-with-stephen-kapos/). This new version builds on Debian 13 (Trixie) and continues the project's commitment to running fast on both old and new hardware — without systemd.

![antiX 26 Linux desktop with IceWM window manager showing the systemd-free Debian Trixie release](/assets/images/post-images/antix/antix26.jpg)

## What's New in antiX 26

The headline addition in antiX 26 is support for five init systems: runit (the new default), sysVinit, dinit, s6-rc, and s6-66. This makes antiX one of the most flexible systemd-free distributions available. Credit for integrating the init systems goes to community contributor ProwlerGR, who also implemented the experimental turnstile support.

antiX 26 ships two flavours: a full edition (around 2 GB) and a core edition (around 660 MB), both available for 64-bit and 32-bit architectures.

## Base System and Kernels

antiX 26 is based on Debian 13 (Trixie) but ships without systemd, libsystemd0, elogind, or libelogind0. It uses eudev in place of udev. Two kernels are included: the customised 5.10.240 kernel for all editions, and a customised 6.6.119 kernel available on the 64-bit full edition only.

## Window Managers and Desktop

The release sticks with its lightweight window manager lineup: IceWM (default), Fluxbox, JWM, and the tiling manager herbstluftwm. Users who prefer tiling on the stacking managers can use the included wingrid-antix tool to achieve that layout.

## Applications

The full edition includes a wide range of applications:

- **Productivity:** LibreOffice, Firefox ESR, Claws Mail, Evince (PDF reader), Geany and Leafpad editors
- **Multimedia:** Pipewire/WirePlumber (default on 64-bit), XMMS, Celluloid, MPV, Xine, and gtk-pipe-viewer for YouTube playback without a browser
- **File management:** zzzFM, Rox Filer, Midnight Commander
- **Networking:** ConnMan, Ceni, gnome-ppp
- **Backup and burning:** LuckyBackup, Xfburn
- **System tools:** antiX Control Centre, Package Installer, Repo Manager, ddm-mx for NVIDIA drivers, bootrepair

Several in-house scripts have also been updated, including antiX TV, antiX Radio, the Finder script, and the antiX SAMBA manager. antiX 26 continues to exclude snaps and Flatpaks, as both depend on systemd or elogind.

This release also continues the tradition of strong 32-bit support — a key reason antiX appeals to users running older machines that many distributions have dropped.

If you're new to antiX, you can learn more about the project in the [antiX distribution overview on OpenSourceFeed](https://www.opensourcefeed.org/distribution/antix). Those looking at previous milestones can check out the [antiX 23.1 release coverage](https://www.opensourcefeed.org/antix-231-release/) for context on how the project has evolved.

## Download

antiX 26 ISOs are available from [SourceForge](https://sourceforge.net/projects/antix-linux/files/Final/antiX-26/). See the [official release announcement](https://antixlinux.com/antix-26-released/) for full details.