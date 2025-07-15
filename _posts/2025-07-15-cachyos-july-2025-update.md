---
layout: post
title: "CachyOS July 2025 Update: Shell Choice, Wayland Default & Gaming Upgrades"
description: "CachyOS July 2025 adds shell choice at install, Wayland by default for Plasma, Anti‑Lag 2/FSR 4 gaming tech, firmware tools, and Legion Go support."
date: 2025-07-15
tags: [CachyOS, Linux, update, Wayland, gaming]
image: /assets/images/post-images/cachyos-july-2025.webp
---

**CachyOS** — an Arch-based Linux distro focused on performance and gaming—has just released its **July 2025 update**, packing user-friendly improvements, gaming boosts, and better device support. 

![CacyOS July 2025 featured image](/assets/images/post-images/cachyos-july-2025.webp)

Following section briefly examines salient features in CachyOS July 2025 update.

## 🔹 Choose Your Shell During Installation  
You can now select between **Fish**, **Zsh**, or stick with **Bash** during the installer. If no choice is made, Fish remains the default, but Bash is available as a safe fallback.

---

## 🖥 Wayland Is Now Default for KDE Plasma  
New Plasma installs will boot into **Wayland** by default (using Plasma 6.4.2). For systems with older NVIDIA cards, an X11 session will install automatically to prevent issues.

---

## ⚙️ Easier Firmware Updates with `fwupd`  
The update includes **fwupd** on both KDE and GNOME editions. Now firmware (for laptops, printers, etc.) can be managed easily using graphical tools like Discover or GNOME Software.

---

## 🚫 Better Stability: systemd‑oomd Disabled  
The controversial **systemd‑oomd** feature—known for closing apps prematurely—has been disabled to improve system stability.

---

## 🎮 Gaming Enhancements: Anti‑Lag 2 and FSR 4  
- **Mesa-git** now supports AMD **Anti‑Lag 2**, reducing input lag in Vulkan games.  
- **Proton‑CachyOS** includes this feature and adds the `PROTON_FSR4_UPGRADE` variable to automatically upgrade games from FSR 3.1 to **FSR 4**.  
- Includes upstream **Wine-Wayland** and anti-cheat patches for smoother gameplay.

---

## 🔄 Firefox Simplified and Cleaned Up  
The older *cachy-browser* has been removed. In its place are:  
- **cachyos‑firefox‑settings** — a set of tweaks on standard Firefox, and  
- **firefox‑pure** — a fully optimized Firefox build included by default.

---

## 🎮 Handheld Edition Now Supports Lenovo Legion Go  
The Handheld Edition now boots seamlessly on the **Lenovo Legion Go** (including the Go S model), with SteamOS-style tweaks included.


For [further information on CachyOS July 2025 update](https://cachyos.org/blog/2507-july-release/) - see the official release announcement.