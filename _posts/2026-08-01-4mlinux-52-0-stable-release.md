---
layout: post
title: "4MLinux 52.0 STABLE Released with Kernel 6.18 LTS and Ultra HDR Support"
categories: [4mlinux, linux, release]
tags: [4mlinux, lightweight-linux, linux-release, kernel-6.18, ultra-hdr]
description: "4MLinux 52.0 STABLE is out with Linux kernel 6.18 LTS, Firefox 153, LibreOffice 26.2.5, Ultra HDR image support, and simplified Wi-Fi configuration."
image: /assets/images/post-images/4MLinux/4mlinux-52-0-stable.webp
---

**The** 4MLinux team has changed the status of the 4MLinux 52.0 series to STABLE. This lightweight, independently developed Linux distribution continues its tradition of packing a full software suite into a minimal footprint, and version 52.0 adds a few notable firsts alongside the usual round of package updates.

![4MLinux 52.0 STABLE desktop showing updated applications and the JWM desktop environment](/assets/images/post-images/4MLinux/4mlinux-52-0-stable.webp)

## What's New in 4MLinux 52.0

The headline upgrade is the Linux kernel, now running on **kernel 6.18**, the latest Long-Term Support (LTS) release. Kernel 6.18 was officially designated as an LTS kernel in December 2025 and will receive security and bug-fix maintenance until December 2027 — a solid foundation for a stability-focused distribution like 4MLinux.

Two usability improvements stand out in this release. Wi-Fi configuration has been simplified, making it easier to get connected on both new and older hardware. Legacy graphics card support has also improved, which matters for users running 4MLinux on older machines — exactly the audience this distribution is designed for.

Ultra HDR image support has been added via **libultrahdr** and **ImageMagick**, letting users view and process High Dynamic Range images without installing extra tools.

### New Applications

Several new programs ship out of the box in 52.0:

- **ksh** (KornShell) — a classic Unix shell, now included by default
- **audioconvert** — a command-line utility for audio format conversion

The following tools are available as downloadable extensions:

- **Rocks'n'Diamonds** — a classic platform game
- **Elvis** — a lightweight Vi clone for terminal editing
- **PDF Tricks** — a Ghostscript-based GUI for working with PDF images

## Updated Software Stack

The core application lineup in 4MLinux 52.0 covers the usual four pillars: office work, web browsing, multimedia, and lightweight server hosting.

**Office and productivity:** [LibreOffice](/software/libreoffice) 26.2.5 is the primary office suite, complemented by the GNOME Office tools — AbiWord 3.0.8,0 [GIMP](/software/gimp) 3.2.4, and Gnumeric 1.12.61.

**Web and email:** [Firefox](/software/firefox) 153.0 and [Chrome](/software/chrome) 151.0 handle browsing, with [Thunderbird](/software/thunderbird) 153.0 for email.

**Multimedia:** Music playback runs through Audacious 4.6.1. Video is covered by [mpv](/software/mpv) 0.41.0 and [VLC](/software/vlc) 3.0.23. Gaming is powered by Mesa 26.0.3.

**Server:** The built-in HTTP/FTP server is based on BusyBox 1.37.0.

**Programming:** PHP 8.5.4, Perl 5.42.1, Python 3.14.3, and Ruby 3.4.8 are all available for developers and scripters.

This release follows [4MLinux 51.0](https://www.opensourcefeed.org/4mlinux-51-0-release/), which brought smarter GPU driver handling and a refreshed application stack, and [4MLinux 49.0](https://www.opensourcefeed.org/4mlinux-49-0-stable-release/), which added Bcachefs filesystem support and enhanced mobile connectivity. For the full history of the distribution, see the [4MLinux distribution page](https://www.opensourcefeed.org/distribution/4mlinux).

## Download

The complete package list for 4MLinux 52.0 is available at [4mlinux.com/addons-52.0.txt](http://4mlinux.com/addons-52.0.txt). You can download the release from the [official 4MLinux website](http://4mlinux.com).