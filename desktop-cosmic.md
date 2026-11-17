---
layout: desktop
uid: cosmic
title: 'COSMIC Desktop'
Category: Desktop
permalink: /desktop/cosmic
logo: cosmic-logo.png
preview: cosmic-preview.jpg
home_page: https://system76.com/cosmic/
tagline: 'A Rust-native, Wayland desktop built in-house by System76'
description: 'COSMIC is a Wayland desktop environment written in Rust by System76, the maker of Pop!_OS. It ships with built-in tiling, customizable panels and theming, and is the default desktop of Pop!_OS 24.04 LTS.'
---

**COSMIC** is a Wayland desktop environment designed and built in-house by [System76](https://system76.com/), the computer manufacturer behind [Pop!_OS](/distribution/pop). Unlike most desktops in this list, which are written in C or C++, COSMIC's shell, compositor (`cosmic-comp`) and first-party apps are all written in Rust and share a common application toolkit, `libcosmic`. It replaced the GNOME-based "Pop Shell" that Pop!_OS previously shipped, and became the distribution's default desktop with the release of Pop!_OS 24.04 LTS in December 2025.

## Why Rust and a new toolkit

System76 built COSMIC from scratch rather than extending GNOME or KDE Plasma. The project's stated reasons are memory safety and tighter integration:

- **Memory safety**: Rust's compile-time guarantees rule out the use-after-free and buffer-overflow bugs that are a recurring source of crashes and security advisories in desktops written in C.
- **One toolkit, one codebase**: the shell, compositor and bundled apps (files, settings, terminal, text editor and more) are all built on `libcosmic`, instead of mixing GTK and Qt components with varying look, feel and update cadence.
- **Wayland-native**: COSMIC was designed for Wayland from the start rather than retrofitted from an X11 codebase.

## Built-in tiling and workspace management

COSMIC ships window tiling as a core feature rather than a plugin or extension:

- **Automatic and manual tiling** can be toggled per-workspace, so you can mix a tiled layout for one project with floating windows on another.
- **Dynamic and pinned workspaces**: workspaces can be created on demand as you open more windows, or fixed in number and position if you prefer a predictable layout.
- **Customizable panels and applets**: panel position, size and contents (the app launcher, app library, workspace switcher, system tray applets) can all be rearranged without editing config files by hand.

## Theming and customization

COSMIC exposes most of its look and feel through its own Settings app rather than third-party extensions:

- Light, dark and custom accent-color theming, including matching a brand or organization's color palette.
- Configurable keyboard shortcuts for window management, launching apps and workspace navigation.
- A built-in app library and launcher separate from the taskbar/dock.

## Where to get it

COSMIC isn't exclusive to Pop!_OS. As of late 2026 it's packaged for:

- [**Pop!_OS**](/distribution/pop) 24.04 LTS, where it is the default desktop.
- **Fedora** 41 and later, via the `@cosmic-desktop-environment` group in the standard repositories.
- **Arch Linux**, via the `cosmic-session` package or `cosmic` package group.
- **NixOS**, with dedicated modules since NixOS 25.05.
- **openSUSE Tumbleweed**, via the `X11:COSMIC:Factory` repository.
- **Gentoo**, through a community overlay, currently marked as testing.

Development moves fast: System76 ships point releases of "COSMIC Epoch" roughly every two to four weeks, each adding fixes and incremental features rather than following a slower, traditional desktop release cadence.

## Who it's for

- **Pop!_OS users** upgrading to 24.04 LTS, who get COSMIC automatically as the new default.
- **Tiling window manager fans** who want tiling built into a full desktop environment, instead of configuring i3, Sway or Hyprland by hand.
- **Anyone curious about a from-scratch, memory-safe desktop**, as one of the few mainstream desktop environments not built on GTK or Qt.

Visit the [COSMIC project page](https://system76.com/cosmic/) for downloads, documentation and the current release notes.
