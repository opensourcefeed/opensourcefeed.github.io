---
layout: post
title: "SparkyLinux 8.4 Released with Restored 32-Bit Support"
categories: [sparky, debian, release]
tags: [sparkylinux, sparky-8, debian-trixie, release, linux]
description: "SparkyLinux 8.4, the fourth quarterly update to the Debian 13 Trixie-based Seven Sisters series, brings back 32-bit support and refreshed packages."
image: /assets/images/post-images/sparky/sparky-8-4-release.webp
---

**SparkyLinux** 8.4 is out — the fourth quarterly update to the Sparky 8 "Seven Sisters" stable series, based on Debian 13 "Trixie". The headline change is the return of 32-bit installation images, reversing a decision made when Debian dropped 32-bit ISO support roughly a year ago.

![SparkyLinux 8.4 desktop screenshot showing the Xfce desktop environment with the Seven Sisters release branding](/assets/images/post-images/sparky/sparky-8-4-release.webp)

## What's New in SparkyLinux 8.4

The most significant change is the restoration of 32-bit (i686-pae) Live/Install images. After Debian discontinued its own 32-bit ISO builds, Sparky followed suit — but user demand from those still running older hardware prompted a reversal. The 32-bit editions ship as ultra-lightweight Openbox (MinimalGUI) and CLI (MinimalCLI) images for users who want to configure their system from the ground up. Note that 32-bit images do not include the Calamares graphical installer; installation uses the text-mode command `sudo sparky-installer`.

All packages are refreshed from the stable Debian and Sparky repositories as of August 9, 2026. The full component rundown:

- **Linux kernel (64-bit):** 6.12.101-LTS (with 7.1.8, 6.18.43-LTS, and 6.12.102-LTS available in Sparky repos)
- **Linux kernel (ARM64):** 6.18.39-rpi
- **Linux kernel (32-bit):** 6.12.102-LTS
- **KDE Plasma:** 6.3.6
- **Xfce:** 4.20
- **LXQt:** 2.1.0
- **MATE:** 1.26.0
- **Openbox:** 3.6.1
- **[LibreOffice](/software/libreoffice):** 25.2.3 (26.2.4.2 available via Debian Backports)
- **[Firefox](/software/firefox):** 140.13.0esr (153.0.3 available in Sparky repo for amd64 and arm64)
- **Thunderbird:** 140.13.0esr

The 64-bit (BIOS/UEFI + Secure Boot) edition comes in six flavours: Xfce, LXQt, MATE, KDE Plasma, MinimalGUI (Openbox), and MinimalCLI. ARM64 builds offer Openbox and CLI editions. UEFI installation on any architecture is recommended with an active internet connection.

## Why It Matters

[SparkyLinux](/distribution/sparky) has been a go-to choice for reviving older hardware since its debut in 2012. The project's philosophy — give aging machines a second life — makes the return of 32-bit images a meaningful commitment to users who haven't been able to make the jump to 64-bit hardware. For context, this follows the [initial Sparky 8 "Seven Sisters" release](/sparky-linux-8-seven-sisters-released-based-on-debian-13-trixie/) last August and the [Sparky 8.1 quarterly update](/sparky-8-1-released/) in November 2025.

If you already have Sparky 8 installed, no reinstall is needed — a standard system update is all it takes.

## Download SparkyLinux 8.4

Fresh ISO images for all editions are available on the [SparkyLinux stable download page](https://sparkylinux.org/download/stable/). The live session credentials are `live:live` for PC editions and `pi:sparky` for ARM.

For the full release notes, see the [official Sparky 8.4 announcement](https://sparkylinux.org/sparky-8-4/).