---
layout: post
title: "Zenwalk Current Milestone 2026: Xfce 4.20, Linux 7.1, Flatpak"
categories: [zenwalk, slackware, release]
tags: [zenwalk, slackware, xfce, flatpak, linux-kernel, rolling-release]
description: "Zenwalk Current Milestone 2026 ships Linux 7.1.7 with the BORE scheduler, Xfce 4.20, native Flatpak integration, and a refreshed graphical system toolbox."
image: /assets/images/post-images/zenwalk/zenwalk-current-milestone-2026.webp
---

**The** Zenwalk project has published its Current Milestone 2026, a fresh ISO snapshot of its rolling development branch. Built on top of Slackware Current, this release combines the latest upstream packages with Zenwalk's own desktop integration and performance tuning — keeping the distribution's long-standing goal intact: a clean, lightweight Slackware system that works as a daily desktop without extra configuration.

![Zenwalk Current Milestone 2026 introduces Linux Kernel 7.1, Flatpak and Xfce 4.20](/assets/images/post-images/zenwalk/zenwalk-current-milestone-2026.webp)

Zenwalk has been around since 2004, founded by Jean-Philippe Guillemin as a personal project. It follows the "one application per task" principle — one browser, one media player, one text editor — which keeps the install lean and the system predictable. If you're unfamiliar with the project, the [Zenwalk distribution page](/distribution/zenwalk) has an overview of its philosophy and approach.

## Flatpak Now Integrated Out of the Box

The most user-facing addition in this milestone is full Flatpak integration. Flatpak is installed and configured from the start, with Flathub set as the default application source. Users can install modern desktop applications through the graphical software store without using the terminal or hunting for compatible packages.

The practical split is clean: the Slackware package layer handles the core operating system, while Flatpak covers the application layer. Both are ready from the first boot. This is a meaningful step for a distribution that has historically required some familiarity with Slackware to manage software beyond the base install.

## Linux 7.1.7 with the BORE Scheduler

Zenwalk Current Milestone 2026 moves to Linux kernel 7.1.7, paired with the BORE (Burst-Oriented Response Enhancer) CPU scheduler patch. BORE adjusts how the kernel allocates CPU time, prioritizing short interactive bursts over longer background tasks. On a desktop, this translates to applications and the window manager staying responsive even when something heavier is running in the background.

For a distribution focused entirely on desktop use, this is a sensible kernel choice — one aimed at what a user actually feels rather than throughput benchmarks.

## Xfce 4.20 with Zenwalk's Dock Layout

The desktop ships Xfce 4.20, the current stable release of the lightweight desktop environment. Zenwalk doesn't use a standard Xfce layout, though. Instead, it uses a dock-centric arrangement inspired by NeXT and Window Maker, placing the application launcher and running apps in a dock rather than a traditional taskbar. The result is a clean, uncluttered workspace that works especially well on widescreen displays.

Other Slackware-based distributions take different approaches to the desktop — [Salix](/distribution/salix) pairs Xfce with a more conventional layout, while [PorteuX](/distribution/porteux) offers multiple desktop environments in a modular, portable format. Zenwalk's dock design makes it visually distinct from both.

## Graphical System Tools

Zenwalk continues to ship a complete set of graphical administration tools covering network configuration, user and group management, storage, services, and software management. The aim is to keep routine system maintenance accessible without requiring the terminal — particularly useful on a rolling system where configurations may occasionally need attention after updates.

## Download

The Zenwalk Current Milestone 2026 ISO is available from the [official Zenwalk website](https://www.zenwalk.org/p/download.html). As a rolling release, existing installations update in place through regular package updates; the new ISO is primarily for fresh installs.
