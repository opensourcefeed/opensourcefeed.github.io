---
layout: distribution
uid: vanillaos
title: 'Vanilla OS'
Category: Distribution
permalink: /distribution/vanillaos
logo: vanilla-logo.png
preview: vanilla.jpg
image: /assets/images/preview/vanilla.jpg
home_page: https://vanillaos.org/
desktops: [gnome]
base: [debian, ubuntu]
description: Vanilla OS is an immutable, Debian-based Linux distribution focused on stability, security, and a clean GNOME experience. Explore features, releases, and more.
last_modified_at: 2026-08-26
releases:
  Vanilla OS 3 Reunion: /vanilla-os-3-reunion-release/
  Vanilla OS 2 Orchid: /vanillaos-2-orchid-beta/
  Vanilla OS 22.10: "https://vanillaos.org/2022/12/29/vanilla-os-22-10-kinetic.html"
---

**Vanilla OS** is an immutable Linux operating system built on [Debian](/distribution/debian), designed for users who want a stable, secure, and clutter-free desktop. By making the core system read-only and applying changes atomically, Vanilla OS protects against unintended modifications and makes it easy to roll back if something goes wrong.

## Key Features

- **Immutable core** — The root filesystem is read-only by default, powered by ABRoot for atomic updates and safe rollbacks <!-- VERIFY: confirm ABRoot is still the underlying technology in latest release -->
- **Clean GNOME experience** — Ships with a near-stock [GNOME](/desktop/gnome) desktop, free of unnecessary customizations
- **Flexible package management** — Apx allows installing packages from multiple sources (Debian, Ubuntu, AUR, and more) in managed containers, keeping the base system pristine <!-- VERIFY: confirm Apx is still included and feature set is accurate -->
- **Debian foundation** — Built on [Debian](/distribution/debian) for long-term stability; early releases were [Ubuntu](/distribution/ubuntu)-based

## Who Is Vanilla OS For?

Vanilla OS suits users who want a reliable daily-driver Linux desktop without worrying about a bad update breaking their system. It is a good fit for developers and power users who appreciate immutability and container-based workflows, as well as newcomers who want a stable, low-maintenance GNOME environment.

## Get Vanilla OS

Visit the [official Vanilla OS website](https://vanillaos.org/) to download the latest release, read the documentation, and explore installation guides.