---
layout: distribution
uid: antix
title: 'antiX'
Category: Distribution
permalink: /distribution/antix
type : Linux
logo: antix-logo.png
preview: antix-preview.jpg
image: /assets/images/preview/antix-preview.jpg
home_page: https://antixlinux.com
desktops: [icewm, fluxbox, jwm, herbstluftwm]
base: [debian]
tagline: Lightweight, systemd-free Linux based on Debian
description : "antiX is a fast, lightweight and systemd-free live distribution based on Debian. It provides a special eco-system called *antiX Magic* to work with both old and new computers"
releases:
  antiX 26 Stephen Kapos: /antix-26-release/
  antiX 23.1 Arditi del Popolo: /antix-231-release/
  antiX 19.1 Marielle Franco: "/antix-19.1-screenshot/"
  antiX 19 Marielle Franco: "/2-antiX-19-release/"
  antiX 17.2 Helen Keller: "/01-antix-17.2-released-with-critical-bug-fixes/"
screenshots:
  antiX 19.1 Marielle Franco: "/antix-19.1-screenshot/"
  antiX 17.2 Helen Keller: "https://distroscreens.blogspot.com/2018/10/antix-172-helen-keller-screenshots.html"
seo:
  type: OperatingSystem
  dateModified: 2026-03-22
---

**antiX** is a fast, lightweight, and systemd-free live distribution based on Debian. It provides a special ecosystem called *antiX Magic* to work with both old and new computers.

The objective of antiX is to provide a lightweight and fully functional operating system for beginners and advanced users alike. It runs smoothly on most systems with a minimum of 512 MB of RAM, making it a practical choice for reviving older hardware.

As a live distribution, antiX can be used for system rescue activities. It runs smoothly on live boot and can work with or without persistence.

A key feature of antiX is its multi-init support. Rather than using systemd, antiX ships with five init systems — **runit** (default), **sysVinit**, **dinit**, **s6-rc**, and **s6-66** — all selectable at boot. Since version 22, antiX is also elogind-free, using eudev in place of systemd-udev. It does not support Flatpak or Snap packages.

## Flavours

antiX 26 comes in two flavours, available for both 64-bit and 32-bit architectures:

- **antiX-full** (~1.7 GB) — includes four window managers (IceWM as default, Fluxbox, JWM, and herbstluftwm), the full LibreOffice suite, Firefox ESR, and a Package Installer for adding more applications.
- **antiX-core** (~520 MB) — a command-line edition with no graphical environment, intended for users who want full control over what to install. Note that antiX-core requires a wired internet connection.