---
title: "GhostBSD 23.10.1 released"
layout: post
categories: ghostbsd release
image: /assets/images/post-images/ghostbsd/ghostbsd-23101.jpg
description: "Discover GhostBSD 23.10.1: A FreeBSD-based OS with enhanced features, network improvements, and software updates."
---

**The** GhostBSD team has announced the release of GhostBSD 23.10.1 - a FreeBSD based desktop operating system. In GhostBSD 23.10.1, the FreeBSD base system and kernel 1302508.

![GhostBSD 23.10.1 featured image](/assets/images/post-images/ghostbsd/ghostbsd-23101.jpg)

## What's new in GhostBSD 23.10.1?

In addition to the FreeBSD updates, GhostBSD 23.10.1 contains software updates, some improvements to Update Station, and new features to NetworkMgr. Also, os-generic-userland-devtools has been removed from the default installation to reduce the live system image.

Following section briefly explains the key highlights in GhostBSD 23.10.1.

> - Introduce the ability to set Static IP address.
- Introduce the ability to set DNS Server information.
- Add packages description window to Software Station.
- Add graphics/qgis-ltr and graphics/qgis to GhostBSD binary packages for installation to GhostBSD. It already exists in FreeBSD.
- Add progress for update-station the check-now option.
- Refactor with DRY principles
- Change GhostBSD version to be static like 23.10.1
- FreeBSD stable/13.0 for 23.10.1
- Introduced progress when looking for updates using check-update
- Removed os-generic-userland-devtools from default installation
- Removed code to get version file since it is hard coded in base now

For [further information on FreeBSD 23.10.1](https://www.ghostbsd.org/news/GhostBSD_23.10.1_Now_Available), read the official release announcement in projects website.

<a href="https://download.ghostbsd.org/releases/amd64/23.10.1/GhostBSD-23.10.1.iso" class="download">Download GhostBSD 23.10.1 ISO</a>

<a href="https://www.ghostbsd.org/download" class="download">All GhostBSD download options</a>