---
layout: distribution
uid: aerynos
title: 'AerynOS (formerly Serpent OS)'
tagline: 'Independent Atomic Linux'
Category: Distribution
type: Linux
permalink: /distribution/aerynos
redirect_from:
  - /distribution/serpentos
logo: aerynos.svg
preview: aeryn-preview.jpeg
home_page: https://aerynos.com
desktops: [plasma, gnome, cosmic, budgie]
base: Independent
description: "AerynOS (formerly Serpent OS) is an independent alpha-stage Linux distribution with atomic, rollback-capable updates via moss, its own Rust tooling, and GNOME, KDE Plasma, COSMIC and Budgie."
seo:
  type: OperatingSystem

stories:
  Serpent OS rebrands as AerynOS : /serpentos-rebrading-aerynos/

faq:
  "Is AerynOS free and open source?": "Yes. AerynOS is free, open-source software developed in the open on GitHub. The project is funded through community sponsorship."
  "Do I need an internet connection to install AerynOS?": "Yes. The installer downloads the latest package sets during installation, so a working network connection is required."
  "How can I get help or contribute to AerynOS?": "The community talks on Zulip, Discourse and Mastodon. The project welcomes contributions of code, artwork, documentation and package recipes."
---

## What is AerynOS?

**AerynOS** (styled **aerynOS** since August 2026, and previously known as **Serpent OS**) is an independent [Linux distribution](/distribution/) built from the ground up with its own tooling. It is not based on any other distribution. The project focuses on reliable atomic updates, easy rollback, and modern system tools written in Rust.

> **Development status:** AerynOS is an **alpha technical preview**. The project says it is not yet recommended for daily use by people who need a stable, production-ready system. Early adopters should be technically minded and willing to report and help fix issues.

## Atomic updates and rollback

All software changes go through **moss**, AerynOS's package and system state manager. Each install, removal or update is applied as a single atomic transaction. If something fails, the running system is left untouched.

moss keeps previous system states, so you can roll back to an earlier state from the command line. The last five states can also be chosen from the boot menu. Unlike image-based immutable distributions, AerynOS does not need a reboot to apply each update. moss supports both imperative commands and declarative system definitions.

## Its own Rust tooling

AerynOS builds and maintains its core tools in-house, mostly in Rust:

* **moss**: package and system state manager with atomic transactions and rollback.
* **boulder**: builds packages from YAML-based recipe files.
* **blsforme**: a boot management tool that follows the Boot Loader Specification and handles the ESP and XBOOTLDR partitions.
* **lichen**: the system installer. The 2026.11 ISO also includes a new terminal-based `lichen-installer` for testing. It sets up Btrfs with a separate `@home` subvolume but does not yet support disk encryption or dual booting.

## Desktops and kernels

The installer offers four desktop environments, listed in the table below. Around a dozen Wayland compositors are also in the repositories, including Hyprland and niri. The live ISO boots into GNOME.

AerynOS provides three kernel flavours: **linux-stable** (the default), **linux-lts**, and **linux-gaming**. The gaming flavour adds handheld-gaming patches and performance tweaks. NVIDIA drivers and firmware updates through fwupd are available in the repositories.

## Release history

AerynOS publishes regular alpha ISO snapshots alongside its project updates:

| Release | Date | Highlights |
|---|---|---|
| 2026.11 | November 2026 | Plasma 6.8, GNOME 51, COSMIC 1.11, Budgie 10.10 added, Linux 7.2, new `lichen-installer` preview, breaking moss CLI changes |
| 2026.08 | August 2026 | Stable and gaming kernels moved to Linux 7.1 |
| 2026.05 | May 2026 | Plasma 6.6, GNOME 50, COSMIC 1.0.11, Linux 7.0, three kernel flavours |
| February 2026 update | February 2026 | Plasma 6.6.1 with Plasma Login Manager, GNOME 49.4, COSMIC 1.0.8, new console-only install option |

## From Serpent OS to AerynOS

The project announced its rename from Serpent OS to AerynOS in February 2025, because the team felt the old name carried negative connotations. Its development team and technical goals stayed the same.

In April 2026 the project introduced a new triquetra logo and colour palette. In August 2026 it adjusted the logo colours and fonts and changed how it styles its name to "aerynOS".
