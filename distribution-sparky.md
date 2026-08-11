---
layout: distribution
uid: sparky
title: 'Sparky Linux'
tagline: "Debian-based Linux with lightweight desktops and out-of-the-box convenience"
Category: Distribution
permalink: /distribution/sparky
type : Linux
logo: sparky-logo.png
preview: sparky-lxqt-5.jpg
home_page: https://sparkylinux.org/
forum: https://forum.sparkylinux.org/
desktops: [lxqt, mate, lxde, openbox, enlightenment, jwm, plasma, xfce]
base: [debian]

description : "Sparky Linux is a fast Debian-based Linux distro with lightweight desktops, ready-to-use tools, and semi-rolling updates. Editions, releases and details."

releases:
  Sparky 8.4: /sparkylinux-8-4-release/
  Sparky 2026.03: /sparkylinux-2026-03-released/
  Sparky 8.2: /sparky-linux-8-2-release/
  Sparky Linux 8 Seven Sisters: /sparky-linux-8-seven-sisters-released-based-on-debian-13-trixie/
  Sparky 7.8: /sparky-linux-7-8-released/
  Sparky 7.7: /sparky-7.7-release/
  Sparky Semi-Rolling 2024.08: /sparky-semirolling-202408/
  Sparky Linux 2024.05: /sparky-202405-release/
  Sparky Linux 2024.02: /sparky-2024.02-release/
  Sparky 7.2 Orion Belt: /sparky-72-release/
  Sparky 7.0 Orion Belt: /sparky-7-orion/
  Sparky Linux 6.4: "/sparky-6.4-release/"
  Sparky Linux 2021.09: "/sparky-2021.09-release/"
  Sparky Linux 6.0: "/sparky-6.0-relese/"
  Sparky Linux 5.9: "/sparky5.9-release/"
  Sparky Linux 2019.08: "/1-sparky-linux-2019.08-screenshots/"
  Sparky Linux 4.9: "/2-sparkylinux-4.9-release/"
  Sparky Linux 5.5: "/00-sparky-linux-5.5-released-with-gcc8-linux4.18.6-and-more/"
  Sparky Linux 4.8: "https://open-source-feed.blogspot.com/2018/05/sparky-linux-48-released-with-updated.html"
  Sparky Linux 4.8 RC : "https://goo.gl/RU1Fii"
  Sparky Linux 4.7 Tyche : "https://sparkylinux.org/sparky-4-7/"
  Sparky Linux 5.0 : "https://open-source-feed.blogspot.com/2017/07/sparky-linux-50-released-based-on.html"
  Sparky Linux 4.6 STB : "https://open-source-feed.blogspot.com/2017/06/sparky-linux-46-stb-is-available-now.html"
  Sparky Linux 4.4 Tyche : "https://open-source-feed.blogspot.com/2016/08/sparkylinux-44-tyche-released-in-5.html"
  Sparky Linux 4.3 Special editions : "https://open-source-feed.blogspot.com/2016/05/sparkylinux-43-special-editions.html"
  Sparky Linux 4.3 : "https://open-source-feed.blogspot.com/2016/04/sparkylinux-43-tyche-released-with.html"
  Sparky Linux 4.3-dev : "https://open-source-feed.blogspot.com/2016/03/sparky-linux-43-dev3-minimal-iso.html"
  Sparky Linux 4.2 Special editions : "https://open-source-feed.blogspot.com/2015/12/sparkylinux-42-special-editions-released.html"
  Sparky Linux 4.2 : "https://open-source-feed.blogspot.com/2015/12/sparkylinux-42-tyche-released.html"
  Sparky Linux 4.0 RC : "https://open-source-feed.blogspot.com/2015/04/sparkylinux-40-rc-released.html"

screenshots:
  Sparky Linux 2019.08: "/1-sparky-linux-2019.08-screenshots/"
  
review :
  Sparky Linux provides a fully functioaning & lightweight OS with some glitches (Distrowatch) : "https://distrowatch.com/weekly.php?issue=20171113#sparky"
  Hands on Sparky Linux 4.2 Enlightenment (ZDNet) : "https://www.zdnet.com/article/hands-on-sparky-linux-4-2-enlightenment/"

seo:
  type: OperatingSystem
  
---

**Sparky Linux** is a lightweight GNU/Linux distribution built on [Debian](/distribution/debian) that stands out by combining Debian's solid foundation with a ready-to-use desktop experience. Unlike a vanilla Debian install, Sparky ships with multimedia codecs, essential tools, and a choice of lightweight desktop environments already configured — so you get a working system without hours of post-install setup. It runs well on both modern hardware and older machines with limited resources, making it one of the more versatile Debian-based options available today.

The project maintains two parallel lines: a **Stable** line based on Debian stable (currently Debian 13 *Trixie*) with quarterly updates, and a **Semi-Rolling** line (codenamed *Tiamat*) that tracks Debian Testing for users who want newer software without switching to a fully rolling distribution. Both lines support amd64 and ARM64 architectures.

If you're looking for a Debian derivative with more out-of-the-box polish than plain Debian — without the heavier footprint of Ubuntu or Linux Mint — Sparky Linux is worth a close look. [Download Sparky Linux from the official website.](https://sparkylinux.org/download/)

## Editions

### Home Edition

The primary edition for everyday desktop users. It ships with a fully configured [LXQt](/desktop/lxqt), [MATE](/desktop/mate), [KDE Plasma](/desktop/plasma), or [Xfce](/desktop/xfce) desktop alongside a curated set of applications for productivity, multimedia, and web browsing. Codecs and media support are included out of the box, so there's no need to hunt down additional packages after installation.

### Minimal GUI

A stripped-down graphical edition that boots into a basic [Openbox](/desktop/enlightenment) environment with minimal software preinstalled. Aimed at users who want a clean Debian base with a graphical interface and full control over what gets added on top.

### Minimal CLI

A console-only edition with no graphical environment at all. Intended for experienced users, server setups, or anyone who prefers to build their system entirely from scratch. It's also a good starting point for custom builds.

### Semi-Rolling

The Semi-Rolling edition (codenamed *Tiamat*) tracks Debian Testing repositories, which means software is typically several months newer than what the stable line ships. It offers a middle ground between Debian Stable's conservatism and the rapid churn of a fully rolling distribution like [Arch Linux](/distribution/arch). Suitable for desktop users who want up-to-date software without accepting the instability risk of a bleeding-edge system.

### Special Editions

Purpose-built variants released alongside the main ISO lineup. Current special editions include **GameOver** (preloaded with Linux-compatible games and gaming tools), **Multimedia** (configured for audio and video production), and **Rescue** (a live environment for system recovery and diagnostics). These are based on the semi-rolling Debian Testing line.