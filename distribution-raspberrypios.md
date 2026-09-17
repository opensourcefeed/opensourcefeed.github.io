---
layout: distribution
uid: raspberry-pi-os
title: 'Raspberry Pi OS'
Category: Distribution
permalink: /distribution/raspberry-pi-os
logo: raspberrypi.png
preview: raspberryos.png
preview_caption: Raspberry Pi OS desktop environment screenshot
home_page: https://www.raspberrypi.com/software/
desktops: labwc (Wayland), PIXEL (legacy)
type: Linux
base: debian
tagline: The official operating system for Raspberry Pi devices
image: /assets/images/preview/raspberryos.png

description: Raspberry Pi OS is the official Debian-based OS for Raspberry Pi. Explore features, editions, and latest releases.

releases:
  Raspberry Pi OS 2026.09: /rpi-desktop-update/
  Raspberry Pi OS 6.2: "/raspberry-pi-os-6-2-release/"
  Raspberry Pi OS Trixie (Oct 2025): "/raspberry-pi-os-trixie-release/"
  Raspberry Pi OS Bookworm (Oct 2023): "https://www.raspberrypi.com/news/bookworm-the-new-version-of-raspberry-pi-os/"
  Raspberry Pi OS Bullseye (Nov 2021): "https://www.raspberrypi.com/news/raspberry-pi-os-debian-bullseye/"
  Raspberry Pi OS Buster (Jun 2019): "https://www.raspberrypi.com/news/buster-the-new-version-of-raspbian/"

seo:
  type: SoftwareApplication
  "applicationCategory": "OperatingSystem"
  "operatingSystem": "Linux"

---

**Raspberry Pi OS** is the official operating system for Raspberry Pi single-board computers. It is based on Debian Linux and optimized for performance, low power consumption, and ease of use, making it ideal for education, development, and DIY projects. It is the successor to [Raspbian](/distribution/raspbian/), the original community-built Debian port for Raspberry Pi hardware.

## Desktop Environment

Since the [Trixie release](/raspberry-pi-os-trixie-release/), Raspberry Pi OS uses a Wayland-based desktop built on **labwc**, replacing the older X11/LXDE stack for improved performance and future compatibility. Earlier versions used **PIXEL (Pi Improved Xwindows Environment, Lightweight)**, a customized environment built on LXDE and Openbox that still ships on Bookworm and older releases.

The overall look and workflow — a taskbar, status icons, and a main menu launcher — has stayed close to the classic PIXEL experience. Recent updates have added optional modern touches such as an icon dock and graphical app launcher, while keeping the classic taskbar available for those who prefer it.

## Editions

Raspberry Pi OS is available in three main editions:

- **Raspberry Pi OS with Desktop** - A complete desktop experience including Chromium browser, LibreOffice, and essential applications.
- **Raspberry Pi OS Lite** - A minimal, command-line only version ideal for headless setups, servers, and advanced users.
- **Raspberry Pi OS with Desktop and Recommended Software** - Includes additional educational tools, programming environments, and utilities for learning and development.

## Key Features

- Optimized for Raspberry Pi hardware
- Lightweight and fast performance
- Wayland desktop based on labwc (PIXEL/LXDE on older releases)
- Optional 64-bit support for modern Raspberry Pi devices
- Strong integration with Raspberry Pi tools and GPIO libraries
- Regular updates aligned with Debian releases

## Supported Devices

Raspberry Pi OS supports a wide range of Raspberry Pi devices, including:

- Raspberry Pi 5
- Raspberry Pi 4
- Raspberry Pi 400
- Raspberry Pi 3 series
- Raspberry Pi Zero and Zero 2 W (Lite version recommended)

## Download Raspberry Pi OS

You can download the latest version of Raspberry Pi OS from the official website:

👉 https://www.raspberrypi.com/software/

## Summary

Raspberry Pi OS is a Debian-based distribution tailored for Raspberry Pi hardware. It combines a lightweight desktop environment with hardware optimizations and regular updates, making it suitable for a wide range of use cases.