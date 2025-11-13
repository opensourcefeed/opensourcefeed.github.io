---
layout: distribution
uid: nitrux
title: 'Nitrux'
tagline: 'Innovation Our Motivation'
Category: Distribution
type : Linux
permalink: /distribution/nitrux
logo: nitrux.png
preview: nitrux-preview.jpg
home_page: https://nxos.org/
desktops: [plasma]
base : [ubuntu]
telegram: 
  Nitrux: "https://t.me/nitrux"

description : "Nitrux is a Debian-based, immutable Linux OS featuring Hyprland, OpenRC, AppBoxes, and strong sandboxing for a secure and modern desktop experience."

releases:
  Nitrux 5.0.0: /nitrux-5-0-0-released/
  Nitrux 1.7.0: "/nitrux-1.7.0-release/"
  Nitrux 1.6.1: "/nitrux-1.6.1-release/"
  Nitrux 1.3.7: "/nitrux-1.3.7-release/"
  Nitrux 1.2.9: "/nitrux-1.2.9-release/"
  Nitrux 1.1.1: "/1-nitrux-1.1.1-release/"
  Nitrux 1.1.0: "/1-nitrux-1.1.0-innovative-znx-mauikit/"
  Nitrux 1.0.16 : "/00-Nitrux-1.0.16-released-with-package-updates-from-Ubuntu-Cosmic/"
  Nitrux 1.0.15 : "/00-Nitrux-1.0.15-released-with-updated-hardware-and-graphics-stack/"
  Nitrux 1.0.13 : "https://open-source-feed.blogspot.com/2018/06/nitrux-1013-released-with-improved.html"
  Nitrux 1.0.10 : "../Nitrux-1.0.10-released-with-package-updates-from-bionic/"

screenshots:
  Nitrux 1.2.9: "/nitrux-1.2.9-release/" 
  Nitrux 1.0.15 : "https://distroscreens.blogspot.com/2018/09/nitrux-os-1015-screenshots.html"
  Nitrux 1.0.10 : "https://distroscreens.blogspot.com/2018/04/nitrux-1010-screenshots.html"

---

**Nitrux** is a 64-bit Linux distribution built from Debian, designed with an emphasis on simplicity, performance, and system integrity. It uses OpenRC as its init system instead of Systemd and features the Hyprland window manager, Waybar, and greetd for a responsive Wayland-based desktop. Nitrux also integrates its own desktop environment, NX Desktop, built with components from KDE Plasma and Maui Shell, offering a consistent and modern user interface.

At its core, Nitrux is immutable, meaning the root filesystem cannot be modified after installation. This approach improves reliability, protects against tampering and malware, and simplifies maintenance. The distribution uses Overlayroot to manage immutability and supports atomic updates and rollbacks through the Nitrux Update Tool System, which performs safe, backup-based upgrades.

Nitrux includes NX AppHub, a user-level application management system built around AppBoxes—reproducible, sandboxed software bundles derived from Debian and other curated sources. Applications remain rootless and self-contained, preserving the system’s immutable design. The distribution also supports Flatpak and Distrobox for running additional applications or containerized environments without compromising its structure.

Performance tuning is a key focus in Nitrux. It ships with kernel-level optimizations such as asynchronous I/O handling, zswap, Transparent Hugepages, and enhanced TCP buffer management for high-speed networks. The filesystem uses zstd compression and integrity checks to prevent data corruption, while Aesthetic FHS introduces a cleaner, more readable directory structure.

Security is reinforced through a layered approach. Firejail, AppArmor, and Bubblewrap provide application sandboxing. Kernel hardening features mitigate memory exploits and speculative execution attacks, while password policies and root account restrictions strengthen access control. Nitrux supports multiple encryption methods, including block-device and filesystem-level encryption, providing users with a dependable and privacy-focused desktop platform.