---
title: "OpenMandriva Lx 6.0 Released: Rock the Spring with Plasma 6 and More"
layout: post
image: /assets/images/post-images/openmandriva/lx-6.0-release.jpg
categories: [Linux, OpenMandriva]
tags: [OpenMandriva, KDE Plasma 6, Linux Desktop, Server Edition, Open Source]
description: "OpenMandriva Lx 6.0 'Rock' fixed point release introduces KDE Plasma 6, community spins, and a brand-new Server edition. Explore what’s new!"
---

**The** OpenMandriva community has announced the release of **OpenMandriva Lx 6.0**, codenamed **Rock**, a fixed point release (unlike the rolling branch 'Cooker') that brings major improvements and new additions for both desktop and server users.

![OpenMandriva Lx 6.0 featured image](/assets/images/post-images/openmandriva/lx-6.0-release.jpg)

## 🚀 What's New in OpenMandriva Lx 6.0?

### ✨ KDE Plasma 6 Desktop by Default
The star of the show is the **KDE Plasma 6** desktop environment, available with both X11 and Wayland sessions. For VirtualBox users, X11 is recommended due to some known issues with Wayland and the emulated GPU.

### 🖥️ Community Spins Galore
OpenMandriva continues to embrace choice with updated spins featuring:
- **LXQt 2.2.0**
- **GNOME 48.1**
- **XFCE**
- **COSMIC 1.0 Alpha**

### 🧰 OM-Welcome Tool Enhanced
The OM-Welcome startup and configuration utility for KDE Plasma has seen notable improvements to enhance the first-time setup experience.

## 🧠 Under the Hood Upgrades
The distribution comes packed with up-to-date software:

- **KDE Applications:** 25.04.0 (and 23.08.5)
- **KDE Frameworks:** 6.13.0 (and 5.116)
- **Qt:** 6.9.0 (and 5.15.15)
- **Kernel:** 6.14.2 and 6.15.0-rc2 (built with Clang)
- **LibreOffice:** 25.2.3 with Plasma 6 integration
- **Web Browsers:** Chromium 135.0 with Google spyware disabled and JPEG-XL enabled, Firefox 137.0.2, Falkon 25.04.0
- **GIMP 3.0.2**, **VirtualBox 7.1.8**

### ⚙️ Dev Tools & Libraries
- **LLVM/Clang 19.1.7**, **GCC 14.2.1**
- **Systemd 257.5**, **Mesa 25.0.4**
- **Glibc 2.41**, **Java 24**

Also included is **Proton support** via OpenMandriva's own `proton` and `proton-experimental` repositories — bringing Steam-like game compatibility without non-free components.

## 🛡️ Privacy and Security
All recent vulnerabilities have been addressed promptly, reinforcing OpenMandriva’s commitment to user privacy and system security.

## 🔁 Upgrade Notes
**Users of OpenMandriva Lx 5.0 are advised to perform a fresh install** to take full advantage of the new Plasma 6 desktop experience.

---

## 🖧 Introducing the First Official OpenMandriva Server Edition

Unlike many general-purpose Linux distributions, OpenMandriva Lx 6.0 introduces a **radically different** server edition:

- **No GUI** — designed for experienced administrators.
- **Disk image format** — optimized for VM deployment via QEMU, OpenStack, cloud providers, or physical hardware.
- **Pre-configured user**: `omv` / password `omv`
- **Supports cloud-init** for cloud automation.

### 🧰 Minimal and Modular
The server image includes a minimal set of packages, ready for tailored installations. Need a web or database server? Just use `dnf install`.

### 🔁 Hardware Support
- Generic **x86_64**
- **Aarch64** with UEFI (tested on Ampere eMAG/Altra)
- Optimized builds for **AMD Zen** (Ryzen, EPYC, Threadripper)

---

## 📚 Further Reading & Support

- Check the [Release Notes and Errata](https://wiki.openmandriva.org/) for detailed documentation.
- Share feedback or issues on the [OpenMandriva Forum](https://forum.openmandriva.org/).
- Join live discussions on Matrix: `#openmandriva-cooker:matrix.org`

---
