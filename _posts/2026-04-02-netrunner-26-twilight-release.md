---
layout: post
title: "Netrunner 26 Twilight Released with Plasma 6.3 and Linux 6.16"
categories: [netrunner, debian, release]
tags: [netrunner, kde-plasma, debian-trixie, linux-6.16, release]
description: "Netrunner 26 Twilight is out, based on Debian 13 Trixie, shipping Plasma 6.3.6, Linux 6.16, XLibre Xserver, and a refreshed app lineup."
image: /assets/images/post-images/netrunner/netrunner-26-twilight.jpg
---

**The** Netrunner team has announced the release of Netrunner 26 Twilight, a 64-bit desktop distribution built on Debian Stable 13 (Trixie). The release includes all current security updates and stable software packages from the Debian base.

![Netrunner 26 Twilight desktop with KDE Plasma 6.3 running on Debian 13 Trixie](/assets/images/post-images/netrunner/netrunner-26-twilight.jpg)

## What's new in Netrunner 26 Twilight?

Netrunner 26 ships with the **Linux 6.16** kernel, going beyond Debian Trixie's default 6.12 kernel for improved hardware support. The release also moves to the **XLibre Xserver** for Plasma X11 sessions.

On the desktop, **KDE Plasma 6.3.6** and **KDE Frameworks 6.13.0** deliver the latest upstream improvements. Audio is handled by Pipewire and Wireplumber. Several Netrunner-specific components have been rewritten for Qt 6 compatibility — including Samba-mounter (now using PolicyKit), a new SDDM theme, and updated Global and Plasma themes for Plasma 6.

**Stacher7**, a graphical frontend for yt-dlp, is included by default, making video downloads straightforward without needing a terminal.

Power-profiles-daemon enables dynamic switching between power-saving and performance modes. Hardware support improvements cover recent AMD and Intel GPUs, sound cards, and wireless chips.

### Updated applications

Netrunner 26 ships with a solid application stack:

- Qt 6.8.2 and KDE Apps 25.04.3
- Firefox 140.7 ESR and Thunderbird 140.6.0 ESR
- LibreOffice 25.2.3
- GIMP 3.0.4 and Inkscape 1.4
- VLC 3.0.23
- VirtualBox 7.2.6
- Kdenlive 24.12.3

Firefox and LibreOffice include translations for ten languages: English, Spanish, French, Italian, German, Polish, Russian, Turkish, and Simplified and Traditional Chinese.

### Debian 13 Trixie base

By building on [Debian 13 Trixie](/debian-13-trixie-released/), Netrunner 26 gains several system-level changes. These include hardening against ROP and COP/JOP attacks on amd64 and arm64, spell-checking support in Qt WebEngine browsers, and APT's shift to the modern `.sources` format (`.deb822`). The `apt modernize-sources` command handles migration from the old `.list` format. The `/tmp` directory now lives in tmpfs (RAM), leading to more frequent cleanup between reboots.

If you enjoy Debian-based KDE distributions, [NeptuneOS 9.0 "Maja"](/neptuneos-9-0-maja-release/) is another recent release worth checking out — also based on Debian 13 Trixie with Plasma 6.3.

## Download

ISO images are available on the [official Netrunner download page](http://netrunner.com/download). For support and feedback, visit the [Netrunner forums](http://support.blue-systems.com/).