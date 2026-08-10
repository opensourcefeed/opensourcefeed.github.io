---
layout: distribution
uid: cachyos
title: 'CachyOS'
tagline: 'Optimized Arch Linux for Speed and Flexibility'
Category: Distribution
type: Linux
permalink: /distribution/cachyos
logo: cachyos-logo.png
preview: cachyos-preview.jpg
image: /assets/images/preview/cachyos-preview.jpg
home_page: https://cachyos.org/
desktops: [plasma, xfce, mate, gnome, cinnamon, lxqt, i3, lxde, budgie, sway]
base: [arch]

description: 'CachyOS is a performance-optimized Arch Linux distro with a custom kernel, multiple desktop choices, and an easy Calamares installer.'

seo:
  type: OperatingSystem

releases:
  CachyOS August 2026: /cachyos-august-2026-release/
  CachyOS April 2026: /cachyos-april-2026-release/
  CachyOS March 2026: /cachyos-march-2026-release/
  CachyOS 260124: /cachyos-260124-release/
  CachyOS November 2025 Release: /cachyos-november-2025-release/
  CachyOS May 2025 Release: /cachyos-may-2025-release/
  CachyOS March 2025 Release: /cachyos-march25-release/
---

**CachyOS** is a performance-optimized, rolling release Linux distribution based on [Arch Linux](/distribution/arch). Built for power users, gamers, and developers, it combines Arch's cutting-edge package availability with a custom kernel and advanced compiler optimizations for maximum speed and responsiveness. An easy graphical installer makes it accessible without sacrificing the control that Arch users expect.

## Performance Enhancements in CachyOS

CachyOS is engineered for speed at every layer of the stack:

- **Custom Linux Kernel**: The **linux-cachyos kernel** is tuned for modern hardware, prioritizing throughput and low latency over generic compatibility.
- **Scheduler Choices**: The CPU scheduler controls how tasks share processor time. CachyOS defaults to BORE for improved desktop interactivity, but lets you switch to EEVDF, sched-ext, ECHO, or RT to match your workload.
- **Optimized Package Compilation**: Packages are compiled using x86-64-v3, x86-64-v4, and Zen4 instruction sets, with LTO (Link Time Optimization), PGO (Profile-Guided Optimization), and BOLT (Binary Optimization and Layout Tool) applied for measurable real-world gains.

## Easy Installation Options

CachyOS provides two installation paths to suit different experience levels:

- **Graphical Installer**: A user-friendly GUI installer based on Calamares — pick your desktop, configure your disk, and be running in minutes.
- **CLI Installer**: A command-line installer for users who want granular control over partitioning, package selection, and system configuration.

## Flexible Desktop Environment Choices

CachyOS supports a wide range of desktop environments at installation time. Full-featured options include KDE Plasma, GNOME, Cinnamon, MATE, and Budgie. Lightweight choices include XFCE, LXQt, and LXDE. Tiling window manager users can choose from i3, Hyprland, Sway, Wayfire, Qtile, and OpenBox. This breadth means you can install once and get exactly the environment you want without post-install reconfiguration.

## Optimized Web Browsing with Cachy-Browser

CachyOS ships Cachy-Browser, a performance-optimized build of [Firefox](/software/firefox/) with compiler optimizations and selected patches applied for speed and responsiveness. Unlike privacy-hardened browsers such as LibreWolf, Cachy-Browser prioritizes performance and usability with reasonable default security settings rather than aggressive privacy modifications — a practical default for most users.

## Who Is CachyOS For?

- **Gamers**: The custom kernel and scheduler options reduce latency and can improve frame times compared to a stock Arch install.
- **Developers**: Rolling release means immediate access to the latest toolchains, libraries, and runtimes — no waiting for a point release cycle.
- **Power users**: Full control over kernel variant, CPU scheduler, and compiler flags, without having to build everything from scratch.
- **Arch newcomers**: The Calamares graphical installer removes the biggest barrier to entry while keeping the full Arch ecosystem intact.

Visit the [CachyOS website](https://cachyos.org/) to download the latest ISO and get started.