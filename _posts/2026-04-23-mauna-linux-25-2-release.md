---
layout: post
title: "Mauna Linux 25.2 Released with APT 3.2, GIMP 3.2.2, and Calamares 3.4.2"
categories: [amarok, debian, release]
tags: [mauna-linux, debian-trixie, release, apt, gimp, calamares]
description: "Mauna Linux 25.2 is out as a minor update to the 25 series. It brings APT 3.2 with rollback support, GIMP 3.2.2, Calamares 3.4.2, and a Debian 13.4 Trixie base."
image: /assets/images/post-images/mauna/mauna-linux-25.2.webp
---

**The** Mauna Linux team has announced the release of Mauna Linux 25.2. This is a minor update to the Mauna 25 series, which means existing users do not need a fresh install — running Mauna Update is enough to get all the changes.

![Mauna Linux 25.2 released](/assets/images/post-images/mauna/mauna-linux-25.2.webp)

Mauna Linux is a Debian-based distribution from Brazil that ships multiple desktop environments and a curated set of applications for everyday use. The [Mauna 25 "Polaris" series](/mauna-linux-25-polaris-release/) moved to Debian 13 Trixie and introduced GNOME 48. This latest point release builds on that foundation with fresh package updates and several noteworthy component upgrades.

## What's New in Mauna Linux 25.2

### APT 3.2 with Native Rollback (Xfce AHE Edition)

The Xfce Advanced Hardware Enablement edition now ships with APT 3.2, which adds a long-requested transaction history and rollback system. Users can now run `apt history-list` to view past transactions, inspect a specific one with `apt history-info <ID>`, and undo or redo changes using `apt history-undo` and `apt history-redo`. The `apt history-rollback` command reverts a full series of changes. This behaviour is similar to what DNF offers on Red Hat-based systems.

APT 3.2 also brings an improved dependency resolver that handles source-package upgrades, avoids removing essential software when binaries are missing for some architectures, and logs performance counters in JSONL format. It also prevents the system from entering sleep mode while `dpkg` is running.

### GIMP 3.2.2

GIMP 3.2.2 is the first maintenance release of the 3.2 series. It improves SVG path import scaling in the Paths panel, fixes several image import plug-ins (FITS, TIM, PAA, ICNS, PVR, SFW, and JIF), and resolves a PaintShop Pro plug-in issue that caused the active selection shape to load incorrectly. The PSD plug-in now imports all channels from multi-channel PSD files and better handles PSD resources embedded in TIFF and JPEG files, including layers, paths, and vector layers.

### Calamares 3.4.2

The installer is updated to Calamares 3.4.2. Key additions include support for the KDE Plasma Login Manager as a display manager option, alternative greeter paths for LightDM, and correct identification of NVMe and MMC drives as SSDs. The partition module now enforces 4 KB alignment on all partitions, which improves performance on modern solid-state storage. Mauna [first added the Calamares installer back in the 24.1 release](/mauna-243-release/) when it also introduced Advanced Hardware Enablement.

### Updated Core Applications

OnlyOffice Desktop Editors is updated to version 9.3.1. The suite handles `.docx`, `.xlsx`, and `.pptx` files and works entirely offline. Firefox 150.0 remains the default browser, while Librewolf 149.0.2 is also available.

The "About Mauna" application (1.1.3) gains the ability to change the system hostname, more kernel configuration output, additional command logs, and security fixes. The Application Manager is updated to 8.4.1.

### Firmware and Kernel

The firmware bundle is updated to the April 10, 2026 snapshot (20260410). The standard kernel is Linux 6.12.73, while the Xfce AHE edition uses the newer 6.17.8 kernel.

## Package Highlights

| Component | Version |
|---|---|
| Firefox | 150.0 |
| Librewolf | 149.0.2 |
| Calamares | 3.4.2 |
| APT (AHE) | 3.2 |
| Firmware | 20260410 |
| Kernel (standard) | 6.12.73 |
| Kernel (AHE) | 6.17.8 |
| Debian base | 13.4 Trixie |
| OnlyOffice | 9.3.1 |
| Application Manager | 8.4.1 |
| GIMP | 3.2.2 |
| Telegram Desktop | 5.7.2 |
| Cinnamon | 6.4.10 |
| LXQt | 2.1.0 |
| MATE | 1.26.1 |
| Xfce | 4.20 |

## Upgrading or Fresh Install

Existing [Mauna Linux 25.1](/mauna-linux-25-1-release/) users will receive upgrade notifications through the Mauna Update application — no reinstall is needed. Fresh ISO images for Mauna Linux 25.2 are available from the [official download page](https://maunalinux.top/download/).

For the full release announcement (in Portuguese), see the [official Mauna Magazine post](https://magazine.maunalinux.top/2026/04/mauna-linux-252-lancado.html).