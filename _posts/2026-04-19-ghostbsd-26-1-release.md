---
layout: post
title: "GhostBSD 26.1 Released with FreeBSD 15.0, XLibre, and Zsh"
categories: [ghostbsd, bsd, release]
tags: [ghostbsd, freebsd, bsd, release, xlibre, mate]
description: "GhostBSD 26.1-R15.0p2 is out, rebased on FreeBSD 15.0 with XLibre as the default display server, zsh as the default shell, and better networking tools."
image: /assets/images/post-images/ghostbsd/ghostbsd-26.1-release.webp
---

**The** GhostBSD project has announced GhostBSD 26.1-R15.0p2, the latest release of the desktop-focused BSD operating system built on FreeBSD. This release is a major step forward, moving the base system from the FreeBSD 14 series to FreeBSD 15.0-RELEASE.

![GhostBSD 26.1 with FreeBSD 15.0 base and XLibre display server](/assets/images/post-images/ghostbsd/ghostbsd-26.1-release.webp)

## What's New in GhostBSD 26.1

The headline change is the rebase onto [FreeBSD 15.0-RELEASE](https://www.freebsd.org/releases/15.0R/relnotes/), which brings kernel improvements, broader hardware support, and the latest upstream security patches. For users upgrading from GhostBSD 25.02-R14.3p8, the only supported upgrade path is through Update Station.

Alongside the FreeBSD rebase, GhostBSD now ships [XLibre](https://github.com/X11Libre/xserver) as the default display server, replacing X.Org. XLibre is an active fork of the X.Org Server started in June 2025, focused on modernizing the codebase, improving security, and keeping X11 viable for desktop users. Note that upgrading an existing installation does not automatically switch your display server — if you are currently on X.Org, it will remain on X.Org after the upgrade.

The default shell has changed to zsh. NetworkMGR gains Enterprise WPA (802.1X/EAP) and WireGuard support, making it easier to connect to corporate and VPN networks from the GUI. Update Station can now handle major version upgrades using boot environments, providing a safer in-place upgrade path. Software Station benefits from faster bisect-based package search, and the visual identity has been refreshed with a new wallpaper, updated icons, and new theme variants.

## Bug Fixes

This release resolves several reported problems, including UEFI boot failures on certain hardware, the MATE desktop failing to start on R15, a missing installer in the XFCE edition, and the Live ISO not launching the X server in VirtualBox EFI mode. Various fixes have also landed in xconfig, ghostbsd-build, and ghostbsd-ports.

## Known Issue

One known issue after upgrading: the panel may become invisible. Logging out and back in restores it. The [full list of known issues](https://github.com/orgs/ghostbsd/projects/4/views/26) is tracked on GitHub.

## Download

Fresh ISOs and torrents are available at the [GhostBSD download page](https://www.ghostbsd.org/download). For a full list of changes, see the [complete changelog](https://github.com/orgs/ghostbsd/projects/4/views/17?pane=info&statusUpdateId=195119).

This release continues the line that includes [GhostBSD 24.04.1](https://www.opensourcefeed.org/ghostbsd-240401-release/) and [GhostBSD 24.01.1](https://www.opensourcefeed.org/ghostbsd-24-01-1-release/), both of which ran on the FreeBSD 14 base.