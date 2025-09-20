---
layout: post
title: "Tails 7.0 Released – Faster Startup, Debian 13 Base, GNOME 48 and Major Updates"
categories: [tails, Privacy, Security]
tags: [Tails, Debian 13, GNOME 48, Tor Browser, Privacy OS]
description: "Tails 7.0 launches with Debian 13 base, GNOME 48, faster startup, updated apps, improved hardware support, and a tribute to Lunar."
image: /assets/images/post-images/tails/tail-7.jpg
---

**The** Tails Project has announced the release of **Tails 7.0**, the first version of the privacy-focused operating system based on **Debian 13 (Trixie)** and **GNOME 48 (Bengaluru)**. This update brings a faster startup experience, major application upgrades, refreshed GNOME features, and improved hardware support.

![Tails 7 featured image](/assets/images/post-images/tails/tail-7.jpg)

## 🕊️ Dedicated to Lunar  
Tails 7.0 is dedicated to the memory of **Lunar (1982–2024)** – a long-time Tor volunteer, Free Software hacker, and community organizer. Lunar’s contributions to Tails, Tor, Debian, and the Reproducible Builds project helped shape the privacy and security landscape we know today.

---

## ⚡ Faster Startup  
Tails 7.0 boots **10–15 seconds faster** on most computers by switching the image compression algorithm from xz to **zstd**.  
* The images are ~10% larger than before.  
* On low-quality USB sticks, startup might still be slower.  
* The Tails team recommends buying USB sticks from reliable sources to avoid counterfeit electronics.

---

## 📦 Updated & Replaced Software  

> - **GNOME Console** replaces GNOME Terminal  
- **GNOME Loupe** replaces GNOME Image Viewer  
- **Tor Browser 14.5.7**  
- **Tor client 0.4.8.17**  
- **Thunderbird 128.14.0esr**  
- **Electrum 4.5.8**  
- **OnionShare 2.6.3**  
- **KeePassXC 2.7.10**  
- **Kleopatra 4:24.12**  
- **Inkscape 1.4**  
- **GIMP 3.0.4**  
- **Audacity 3.7.3**  
- **Text Editor 48.3**  
- **Document Scanner 46.0**

---

## 🎨 GNOME Enhancements  
- Redesigned settings sections (Accessibility, Sound, Mouse & Keyboard in GNOME 44)  
- New accessibility options: Overamplification and Always Show Scrollbars  
- Dynamic workspace indicator replacing the Activities button in GNOME 45  
- Improved Screen Reader with better table navigation and sleep mode (GNOME 46)  
- New battery health preservation option in Power settings (GNOME 48)

---

## 🗑️ Removed Components  
- **Places menu** (use the Files sidebar instead)  
- **Kleopatra** removed from Favorites (still available under Apps ▸ Accessories)  
- **unar** (File Roller still opens most RAR archives)  
- **aircrack-ng** (installable via Additional Software)  
- **Power Statistics utility**  
- **sq package**  
- **Obsolete Network Connection option** from Welcome Screen

---

## 💻 Hardware & System Changes  
- **Linux kernel 6.12.43** improves graphics and Wi-Fi support  
- **RAM requirement increased to 3 GB** (notification shown if unmet; <2% of users affected)  
- **Keyboard selection fixes** for certain languages (#12638)

---

## 🔄 Upgrading to Tails 7.0  
- Automatic upgrades available only from **Tails 7.0~rc1** and **7.0~rc2**  
- All other users must perform a **manual upgrade** to Tails 7.0  

For full details, consult the official [Tails 7.0 release announcement](https://tails.net/news/version_7.0/).