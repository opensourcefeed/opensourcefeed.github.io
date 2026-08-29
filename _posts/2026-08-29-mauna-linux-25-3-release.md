---
layout: post
title: "Mauna Linux 25.3 Released with Debian 13.6, APT 3.3, and Mesa 26.0.1"
categories: [amarok, debian, release]
tags: [mauna-linux, debian-trixie, linux-release, xfce, cinnamon, lxqt, mate]
description: "Mauna Linux 25.3 is out with Debian 13.6 Trixie base, APT 3.3 in Xfce AHE, Mesa 26.0.1, Firefox 154.0.1, Kernel 6.12.94, and a new Nvidia driver tool."
image: /assets/images/post-images/mauna/mauna-linux-25-3-release.webp
---

**The** Mauna Linux team has announced the release of Mauna Linux 25.3. This is a minor point release in the Mauna 25 "Polaris" series. Existing Mauna 25 users do not need a fresh install — updates arrive as notifications through the Mauna Update application.

![Mauna Linux 25.3 Release](/assets/images/post-images/mauna/mauna-linux-25-3-release.webp)

## What's New in Mauna Linux 25.3

**Updated Debian base**

Mauna Linux 25.3 moves to [Debian 13.6 Trixie](https://www.debian.org/News/2026/20260711), released on July 11, 2026. The update brings 124 bug fixes and 120 security patches to the base, including corrections for an expired Secure Boot certificate authority and several cryptographic library hardening fixes.

**Firefox 154.0.1**

The default browser ships as Firefox 154.0.1, released on August 25, 2026. This version fixes slower access to saved passwords, address autofill failures on some sites, and a bug that added an extra Start Menu shortcut on Windows on every launch.

**Xfce AHE: APT 3.3 and Mesa 26.0.1**

The Xfce Advanced Hardware Enablement (AHE) edition receives two notable updates. APT 3.3 is introduced as the package manager, building on the APT 3.2 rollback and history system that arrived in [Mauna Linux 25.2](https://www.opensourcefeed.org/mauna-linux-25-2-release/). Mesa graphics drivers are updated to 26.0.1, which implements the OpenGL 4.6 and Vulkan 1.4 APIs, subject to driver support on specific hardware.

**Mauna Nvidia Drivers (new)**

A new application, Mauna Nvidia Drivers, simplifies installing proprietary drivers for Nvidia graphics cards. It is not installed by default. Users with Nvidia hardware can install it from the App Store or via the terminal:

```bash
sudo apt update
sudo apt install mauna-nvidia-drivers -y
```

**Updated system applications**

Several core Mauna tools receive fixes and new features in this release:

- *Mauna Image Writer* — rewritten with security breach prevention, a remaining-time indicator, and a full code overhaul.
- *About Mauna* — now prompts for a password correctly, displays exact filenames in dialog boxes, and uses `/proc/meminfo` as a fallback when DMI does not report memory modules.
- *Mauna Update* — adds validation for dpkg configuration in offline update mode, checks source list contents, and validates residual package names.
- *Mauna USB Formatter* — reformatted code, adds btrfs support via argparse, and fixes a missing symbol on the password visibility icon.
- *Application Manager (Mainainstall)* — fixes regression issues in description searches and a multiprocessing error under Python 3.14.

**Updated and new third-party apps**

Discord 1.0.155 joins as a new addition. Other updated packages include Android Studio 2026.1.3, Anydesk 8.0.4, Brave Browser 1.93.138, Element Desktop 1.12.26, Heroic Launcher 2.22.1, Opera Browser 135.0.5973.55, Signal Desktop 8.24.0, and TeamViewer 15.81.5.

**Firmware update**

The firmware collection is updated to the August 10, 2026 snapshot (20260810), improving hardware compatibility for newer devices.

## Highlights

- Firefox 154.0.1
- APT 3.3 (AHE)
- Mesa 26.0.1 (AHE) — OpenGL 4.6 and Vulkan 1.4
- Firmware 20260810
- Kernel 6.12.94
- Debian 13.6 Trixie base
- Mauna Nvidia Drivers (new)
- Cinnamon 6.4.10 / LXQt 2.1.0 / MATE 1.26.1 / Xfce 4.20

For the full release announcement (in Portuguese), see the [official Mauna Magazine post](https://magazine.maunalinux.top/2026/08/mauna-linux-253-lancado.html). Fresh ISO images for Mauna Linux 25.3 are available for download from the [official website](https://maunalinux.top).

*For context on the Polaris series, see [Mauna Linux 25.2](https://www.opensourcefeed.org/mauna-linux-25-2-release/) and [Mauna Linux 25.1](https://www.opensourcefeed.org/mauna-linux-25-1-release/).*
