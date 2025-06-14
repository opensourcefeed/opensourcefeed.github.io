---
layout: post
title: "Kali Linux 2025.2 Released – MITRE Menu, NetHunter Smartwatch & More"
categories: [Linux, kali, Release]
tags: [Kali Linux, Linux Distribution, Penetration Testing, Hacking Tools, Open Source]
description: "Discover what's new in Kali Linux 2025.2: a MITRE-aligned tool menu, GNOME 48 & KDE 6.3 upgrades, BloodHound CE, 13 new tools, and breakthrough NetHunter features."
image: /assets/images/post-images/kali/2025.2.webp
---

Kali Linux 2025.2 has officially launched on 13 June 2025—the second major update of the year. It introduces a smarter tool menu, fresh desktop enhancements, stronger pentesting utilities, and impressive NetHunter innovations.

![Kali Linux 2025.2 featured image](/assets/images/post-images/kali/2025.2.webp)

## What's new in Kali Linux 2025.2?

### 🧭 MITRE-Aligned Kali Menu

The Kali menu has been thoroughly revamped to follow the **MITRE ATT&CK** framework. This improves organization and tool discovery for both attackers and defenders, and the menu is now fully managed via YAML—making future updates more streamlined.

### 🖥️ Desktop Enhancements: GNOME 48 & KDE Plasma 6.3

- **GNOME 48** brings notification stacking, HDR support, dynamic triple buffering, a new “papers” document viewer, and a handy VPN‑IP panel indicator that lets you copy your VPN address with one click.  
- **KDE Plasma 6.3** delivers refined fractional scaling, accurate Night Light color, detailed GPU/battery monitoring, and enhanced customization across both tiling and classic desktop setups.  
- Plus, all-new community wallpapers now ship via the `kali-community-wallpapers` package.

### 🛡️ BloodHound Community Edition

Kali Linux now ships with **BloodHound CE**, along with a full suite of ingestors such as `azurehound`, `bloodhound-ce-python`, and `sharphound`. This upgrade enhances Active Directory reconnaissance through a cleaner interface and faster performance.

### 📱 NetHunter Innovations

- **Smartwatch Wi‑Fi Injection**: The TicWatch Pro 3 (with bcm43436b0 chipset) can now perform wireless de-authentication and WPA2 handshake capture—directly from the wrist—thanks to NexMon-powered support.  
- **CARsenal Toolkit**: Formerly known as CAN Arsenal, this toolkit is now rebranded and includes tools like `hlcand`, `VIN Info`, and `CaringCaribou`—all under a new, user-friendly interface.  
- **Android Radio Teaser**: A sneak peek of NetHunter KeX on car head units hints at upcoming Android Auto compatibility.

### 🧰 New Tools & ARM Improvements

- **13 new tools** have been added, including `azurehound`, `binwalk3`, `bopscrk`, `crlfuzz`, `gitxray`, `rubeus`, `tinja`, and more. Additionally, utilities like `xclip` are now pre-installed by default.  
- **ARM updates** include a unified Raspberry Pi 5 64-bit image running on the 6.12 kernel, updated driver support across other SBCs, and enhancements from NexMon firmware.

### 📥 How to Install or Upgrade

**Brand-new install**: download the appropriate ISO or image from the official Kali download page.

**Upgrade existing Kali**:
```bash
sudo apt update && sudo apt -y full-upgrade
grep VERSION /etc/os-release  # should show VERSION_ID="2025.2"
uname -r                       # kernel 6.12.x-amd64
```

For [further information on Kali Linux 2025.2](https://www.kali.org/blog/kali-linux-2025-2-release/) - read the official release announcement.