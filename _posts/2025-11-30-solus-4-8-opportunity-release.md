---
layout: post
title: "Solus 4.8 Opportunity Released"
categories: [Linux, solus, Release]
tags: [Solus 4.8, Linux Release, Budgie, GNOME, KDE Plasma, Xfce]
description: "Solus 4.8 Opportunity brings an epoch jump, new software centers, updated desktops, and major system improvements."
image: /assets/images/post-images/solus/solus-48.webp
---

**Solus** has released version 4.8, code-named **Opportunity**. This update introduces a new epoch, refreshed desktops, and several system improvements across all editions. Here is a clear breakdown of what has changed.

![Solus 4.8 Opportunity release](/assets/images/post-images/solus/solus-48.webp)

## What's new in Solus 4.8?

### Core system changes  
- Solus moved to a new epoch, completing the long-running Usr-Merge effort.  
- A new package repository named **Polaris** is now in use.  
- Python 2 is fully removed from the distribution.  
- The website has been redesigned and is easier for the team to maintain.  
- **Plymouth** is enabled by default to support offline update workflows.  
- All packages depending on GObject Introspection now use the **girepository 2.0 API**.

### Default applications  
All editions include updated versions of core applications:

- Firefox 145.0.1  
- LibreOffice 25.2.6  
- Thunderbird 140.5.0  

### Kernel, Mesa, and systemd  
- Linux kernel **6.17.8** (with **6.12.58** as the LTS option)  
- Mesa **25.2.6**  
- systemd updated to **257.10**, with modernized packaging and slimmer 32-bit builds  

## What's new in the Budgie Edition?

The Budgie Edition ships with **Budgie 10.9.4**, built for compatibility with GNOME 49.

### Key improvements  
- Budgie and its applets now use `libpeas-2` and `girepository-2.0`.  
- Support for Python-based applets continues.  

### New default  
- **Pocillo Dark** is now the default GTK theme.


## What's new in the GNOME Edition?

Solus GNOME moves to **GNOME 49.1**, a refinement of the GNOME 49 release.

### Changes in session handling  
- The X11 session is no longer included by default.  
- Users who need X11 can install the `gnome-session-shell-x11` package.

### Key improvements in GNOME 49  
- Accent color support  
- Better accessibility in the Calendar app  
- Faster GNOME Software  
- Improved Remote Desktop support  
- Lock-screen media controls  
- HDR brightness options  

### New defaults  
- **MoreWaita** icon theme  
- **Decibel** audio player  
- **Papers** PDF viewer  
- **Ptyxis** terminal

## What's new in the Plasma Edition?

The Plasma Edition includes the latest KDE stack:

- KDE Frameworks **6.19.0**  
- KDE Plasma **6.5.3**  
- KDE Gear **25.08.3**

### Session changes  
- X11 is no longer shipped by default.  
- Users who want it can install the `plasma-x11` package.

### Plasma 6.5 highlights  
- Automatic theme transitions  
- Fuzzy search in KRunner  
- Rounded bottom window corners  
- Performance improvements in Discover

## What's new in the Xfce Edition?

The Xfce Edition is now promoted to a full Solus edition.

### Key change  
- Ships with **Xfce 4.20**, a stable and lightweight desktop that fits users who prefer speed and reliability.


## Download

You can [download the Solus 4.8 edition](https://getsol.us/download/) of your choice from the Solus download page.