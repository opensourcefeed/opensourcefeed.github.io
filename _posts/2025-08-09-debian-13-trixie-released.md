---
layout: post
title: "Debian 13 'Trixie' Released with Major Updates and New Architecture Support"
categories: [Linux, debian, Releases]
tags: [Debian, Linux, Trixie, Release, Open Source, Operating System]
description: "Debian 13 'Trixie' is here with updated packages, new RISC-V support, and major improvements across desktop, server, and cloud environments."
image: /assets/images/post-images/debian/debian-13.webp
---

The Debian Project has officially announced the release of **Debian 13 "Trixie"**, the new stable version of the universal operating system. Arriving after more than two years of development, Trixie will receive security and long-term support for the next five years.

![Debian 13 featured image](/assets/images/post-images/debian/debian-13.webp)

## Highlights of Debian 13 "Trixie"

- **Supported desktop environments:** GNOME 48, KDE Plasma 6.3, LXDE 13, LXQt 2.1.0, and Xfce 4.20.  
- **Over 14,100 new packages**, total package count now 69,830.  
- **44,326 updated packages** and **8,840 removed obsolete packages**.  
- **64-bit time_t support** across all architectures except i386, ensuring compatibility beyond the year 2038.  
- **Improved manual page translations**, especially for Romanian and Polish.  
- **Byte-for-byte reproducible builds** tracking via the new `debian-repro-status` package.

## Updated Software Packages
Trixie ships with major updates, including:
- **Linux Kernel:** 6.12 LTS series  
- **GCC 14.2**, **Python 3.13**, **PHP 8.4**, **Rustc 1.85**  
- **Apache 2.4.64**, **Nginx 1.26**, **PostgreSQL 17**, **MariaDB 11.8**  
- **LibreOffice 25.2**, **GIMP 3.0.4**, **Inkscape 1.4**  
- **Systemd 257**, **OpenSSH 10.0p1**, **OpenSSL 3.5**  

## New Architecture Support
For the first time, Debian officially supports the **riscv64** architecture, enabling Debian to run on 64-bit RISC-V hardware.  
**Supported architectures now include:** amd64, arm64, armel, armhf, ppc64el, riscv64, and s390x.

⚠️ **i386 is no longer a regular architecture** — no kernel or installer is provided. It’s now intended only for use on amd64 CPUs.

## Cloud and Live Images
Debian 13 is available on:
- **Cloud platforms:** Amazon EC2, Microsoft Azure, OpenStack, PlainVM, and NoCloud images.
- **Live images** for amd64 and arm64, with multiple desktop choices or a base system.

Live images can be run without installation and come with the Calamares installer for easy setup.

## Installation and Upgrade
- Installable from Blu-ray, DVD, CD, USB, or over the network.
- Available in **78 languages**, with both text-based and graphical installers.
- Upgrading from Debian 12 “Bookworm” is supported via APT, but backups are strongly recommended.

## Why This Release Matters
Debian 13 "Trixie" continues Debian’s tradition of being **“The Universal Operating System”** — from desktops to servers, clusters, and embedded devices. With modern software, new architectures, and long-term stability, it remains a top choice for both individuals and enterprises.

📥 **Download now:** [Debian 13 "Trixie" Official Download Page](https://www.debian.org/distrib/)  
📄 **Read the release notes:** [Debian 13 Release Notes](https://www.debian.org/releases/trixie/releasenotes)
