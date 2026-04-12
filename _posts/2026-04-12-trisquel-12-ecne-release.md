---
layout: post
title: "Trisquel 12.0 Ecne Released: APT 3.0, New Browsers, RISC-V Plans"
categories: [trisquel, gnu-linux, release]
tags: [trisquel, trisquel-12, ecne, mate, free-software, fsf, release]
description: "Trisquel 12.0 Ecne is out — a fully free GNU/Linux distro based on Ubuntu 24.04 LTS, with APT 3.0, ungoogled-chromium, IceCat, and support until 2029."
image: /assets/images/post-images/trisquel/trisquel-12-featured.webp
---

**The** Trisquel project has announced the release of Trisquel 12.0, codenamed *Ecne*. This is a Long Term Support release built on Ubuntu 24.04 LTS (Noble Numbat) and will receive security updates until May 2029.

![Trisquel 12.0 Ecne release featuring MATE desktop on a fully free GNU/Linux system](/assets/images/post-images/trisquel/trisquel-12-featured.webp)

Trisquel is one of the few GNU/Linux distributions fully endorsed by the Free Software Foundation. It strips out all proprietary software, drivers, and firmware from its Ubuntu base and ships the Linux-libre kernel in their place. For users who place software freedom above convenience, Trisquel remains one of the most dependable options available.

## What's New in Trisquel 12.0 Ecne

> - **APT 3.0 and deb822 repository format.** Ecne ships with APT 3.0, which enables full adoption of the modern deb822 repository format. This applies across all installation paths — the graphical Ubiquity installer, the text-based netinstall, Synaptic, and other package management tools.
- **More modular kernel.** The team focused on making kernel changes more modular for this release, reducing breakage in udeb components used during installation. Work on updating kernel-wedge continues and is expected to be completed in a future update.
- **AppArmor and LXDE improvements.** AppArmor rules for graphical environments have been revised, improving security coverage for everyday desktop use. Trisquel Mini's LXDE desktop also received upstream improvements — notably, Ubuntu has dropped LXDE from all its official releases, making Trisquel one of its primary maintained homes.
- **New browser options.** Both **ungoogled-chromium** and **IceCat** are now available alongside the continuously maintained **Abrowser**, giving users three fully free web browsing options available in the repositories.
- **Backports repository.** Popular applications including LibreOffice, yt-dlp, Inkscape, Nextcloud Desktop, Kdenlive, Tuba, 0 A.D., and fastfetch are available in their latest versions through the backports repository.

## Available Editions

Trisquel 12.0 ships in five editions:

- **Trisquel** — MATE 1.26 desktop, the default edition for home and office use
- **Triskel** — KDE Plasma 5.27, for users who prefer deep customization
- **Trisquel Mini** — LXDE 0.99.2, lightweight desktop for older hardware and netbooks
- **Trisquel Sugar (TOAST)** — Sugar 0.121 learning platform with educational activities for children
- **Netinstall** — Command-line installer for servers and advanced users

Supported architectures include amd64, ppc64el, arm64, and armhf. The default kernel is Linux-libre 6.8.x, with 6.14.x available as the Hardware Enablement Stack.

## The future of Trisquel

The team has begun initial groundwork for **RISC-V architecture support** — a promising direction as the free hardware ecosystem expands. This follows the addition of 64-bit ARM and POWER support in [Trisquel 11 Aramo](/trisquel-11-release/).

For those interested in a broader look at FSF-endorsed systems, the [Trisquel distribution page on OpenSourceFeed](/distribution/trisquel) offers background on the project's history and editions.

Trisquel is a non-profit project. You can support it by becoming a member, donating, or buying from the Trisquel store.

For downloads and further details, see the [official Trisquel 12.0 Ecne release announcement](https://trisquel.info/en/trisquel-120-ecne-release-announcement).