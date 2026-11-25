---
layout: distribution
uid: pop
title: "Pop!_OS"
tagline: 'Ubuntu-based Linux from System76 with the COSMIC desktop'
Category: Distribution
permalink: /distribution/pop
type : Linux
logo: popos.png
preview: popos-preview.jpg
# VERIFY: this preview shows an early GNOME-era release. Replace it with an official COSMIC screenshot from System76.
preview_caption: An early Pop!_OS release with its former GNOME-based desktop
home_page: https://system76.com/pop
desktops: [cosmic, gnome]
base : [ubuntu]
description: "Pop!_OS is System76's Ubuntu LTS-based Linux distro with the Rust-built COSMIC desktop, auto-tiling, hybrid GPU handling and NVIDIA ISOs."

releases:
  Pop!_OS 26.04 LTS: /pop-os-26-04-lts-release/
  Pop!_OS 24.04 LTS: /pop-os-24-04-lts-released/
  Pop!_OS 21.04: "/popos-21.04-release/"
  Pop!_OS 20.10: "https://blog.system76.com/post/632781631953027072/whats-new-in-popos-2010"
  'Pop!_OS 20.04': "/popos-20.04-release/"
  'Pop!_OS 18.04': 'https://blog.system76.com/post/179217201328/see-what-changes-have-been-orbiting-popos'

screenshots:
  'Pop!_OS 20.04 screenshots': "/popos-20.04-release/"
  'Pop!_OS 18.10 screenshots': "https://distroscreens.blogspot.com/2018/11/popos-1810-screenshots.html"

stories:
  'elementary OS creates a brand new installer in collaboration with Pop!_OS': "https://open-source-feed.blogspot.com/2018/02/elementary-os-creates-brand-new.html"

faq:
  "Is Pop!_OS still based on Ubuntu?": "Yes. Each Pop!_OS release is built on an Ubuntu LTS release and uses Ubuntu's package archive alongside System76's own repository. Pop!_OS 26.04 LTS is based on Ubuntu 26.04 LTS, and Pop!_OS 24.04 LTS is based on Ubuntu 24.04 LTS."
  "Does Pop!_OS still use GNOME?": "No. Pop!_OS 22.04 LTS was the last release built on a customized GNOME desktop. Since Pop!_OS 24.04 LTS, the default desktop is COSMIC, which System76 wrote from scratch in Rust."
  "How often does Pop!_OS release a new version?": "Pop!_OS now follows Ubuntu's LTS releases rather than shipping every six months. System76 skipped the interim versions after 22.04, and only one Pop!_OS LTS release is supported at a time, until its successor arrives."
  "Which Pop!_OS ISO should I download?": "Choose the NVIDIA ISO if your computer has an NVIDIA graphics card, because it includes the proprietary driver. Choose the standard ISO for AMD or Intel graphics. An ARM ISO is available for supported ARM64 hardware."
  "Can I upgrade from Pop!_OS 24.04 to 26.04?": "Yes, but not immediately. System76 plans to enable the in-place upgrade from 24.04 LTS to 26.04 LTS in December 2026. Until then, a fresh install is the only way to run 26.04, so back up your files first."
  "Do I need System76 hardware to run Pop!_OS?": "No. Pop!_OS is free to download and install on most 64-bit PCs and laptops. System76 computers ship with it preinstalled and receive firmware updates through it."
---

**Pop!_OS** is a free Linux distribution developed by System76, a US company that builds Linux laptops and desktops. It is based on [Ubuntu](/distribution/ubuntu) LTS releases and, since version 24.04 LTS, ships System76's own [COSMIC desktop](/desktop/cosmic) instead of GNOME. The current release is [Pop!_OS 26.04 LTS](/pop-os-26-04-lts-release/), released on 24 November 2026.

Pop!_OS aims to be a practical workstation for developers, creators and gamers. It focuses on keyboard-friendly window management, sensible hardware support out of the box, and a short path from installation to a working system.

## COSMIC: the Pop!_OS desktop

COSMIC is a desktop environment that System76 built from scratch in Rust. It replaced the customized GNOME session that Pop!_OS used up to 22.04 LTS. System76 built its own desktop to get full control over features such as tiling and panels, which had become hard to maintain as GNOME extensions.

Key parts of the COSMIC experience on Pop!_OS:

- **Built-in tiling:** switch any workspace or display between floating and auto-tiled windows from the panel, and move windows with the keyboard or mouse.
- **Flexible workspaces:** horizontal or vertical layouts, per-display or shared workspaces, and pinned workspaces that persist after a reboot.
- **Panel and dock layouts:** use a panel plus a dock or a single panel, and place them on any screen edge.
- **Constellations (26.04):** one-click theme bundles that set the wallpaper, accent colors, icons and fonts together, and can be exported and shared.
- **Native apps:** COSMIC Files, Terminal, Text Editor, Settings, Store, and, from 26.04, COSMIC Viewer and System Monitor.

COSMIC is updated on a rolling basis, so many features arrive on Pop!_OS between major releases. See our [COSMIC desktop page](/desktop/cosmic) for more detail.

## Hardware support

Hardware support is a large part of what separates Pop!_OS from a stock Ubuntu install:

- **NVIDIA ISO:** a separate installer image includes the proprietary NVIDIA driver, so NVIDIA systems work without extra setup after installation.
- **Hybrid graphics:** on laptops with integrated and dedicated GPUs, apps pick the right GPU automatically. You can also launch a specific app on the dedicated GPU from its right-click menu. Pop!_OS 26.04 further improved automatic GPU selection.
- **ARM support:** Pop!_OS 24.04 LTS added an ARM64 build. It is officially supported on the System76 Thelio Astra and community-supported on other ARM devices through Tow-Boot.
- **Input devices (26.04):** drawing tablets with pen tilt support, and an on-screen keyboard that works with touch and gamepad input.

## Installation and upgrades

The Pop!_OS installer handles disk setup, including full disk encryption, in a few steps. It also offers a **Refresh Install** option that reinstalls the operating system while keeping your home folder, settings and Flatpak apps. You can start it from the installer or by holding the Space key at boot to reach the recovery partition.

Software comes from Ubuntu's archive, System76's repository and Flathub, which is enabled by default. Unlike Ubuntu, Pop!_OS does not use Snap packages by default.

New releases are offered to existing users through a notification in the system. The command-line route is the `pop-upgrade release upgrade` command. <!-- VERIFY: confirm pop-upgrade is the documented command for the 24.04 to 26.04 upgrade once System76 enables it. --> System76 plans to open the upgrade from 24.04 LTS to 26.04 LTS in December 2026. Pop!_OS 26.04 also lets you turn on automatic updates, either during first setup or later in Settings.

## Release cycle

Early Pop!_OS versions followed Ubuntu's six-month schedule, from 17.10 through 21.10. After 22.04 LTS, System76 stopped shipping interim releases to focus on building COSMIC. The next release was 24.04 LTS in December 2025.

System76 has said that Pop!_OS releases will follow Ubuntu's LTS schedule from 26.04 onward. Only one LTS version is supported at a time, so when a new LTS arrives, plan to move to it.

## Who is Pop!_OS for?

- **Developers:** an Ubuntu LTS base with wide package availability, plus a tiling desktop designed for keyboard-driven work.
- **Gamers:** a ready-made NVIDIA ISO, hybrid graphics handling, and recent drivers and Mesa in each release.
- **Creators:** drawing tablet support in 26.04 opens the desktop to illustration, photo editing and CAD work.
- **Owners of System76 computers:** the operating system that the hardware is designed and tested with.

Pop!_OS may not suit you if you want a traditional GNOME layout, in which case [Ubuntu](/distribution/ubuntu) or [Fedora Workstation](/distribution/fedora) with [GNOME](/desktop/gnome) is a closer fit. It also does not suit anyone who prefers a rolling-release base.

## Pop!_OS compared with Ubuntu

| | Pop!_OS | Ubuntu |
|---|---|---|
| Default desktop | COSMIC | GNOME |
| Extra app format | Flatpak (Flathub enabled) | Snap |
| NVIDIA driver | Separate ISO with driver included | Optional during installation |
| Tiling | Auto-tiling built into the desktop | Edge and quarter snapping |
| Release cadence | LTS releases only | LTS every two years plus interim releases |

## History

System76 announced Pop!_OS in 2017 as a replacement for stock Ubuntu on its computers. Early releases customized GNOME with System76's own theme, and Pop!_OS 20.04 added Pop Shell, a GNOME extension that brought auto-tiling to the desktop. In 2018, System76 worked with the [elementary OS](/distribution/elementary) team on a new system installer, with System76 maintaining the *distinst* installation backend. COSMIC itself started as a set of GNOME customizations in Pop!_OS 21.04 before System76 began the Rust rewrite that debuted as the default desktop in 24.04 LTS.

## Download Pop!_OS

Pop!_OS is available from the official [System76 Pop!_OS page](https://system76.com/pop). Pick the NVIDIA ISO for NVIDIA graphics, the standard ISO for AMD or Intel graphics, or the ARM ISO for supported ARM64 hardware.
