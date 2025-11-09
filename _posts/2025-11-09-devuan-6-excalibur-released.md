---
layout: post
title: "Devuan 6.0 “Excalibur” Released — Debian 13 without systemd"
categories: devuan linux distributions
tags: devuan, debian-13, linux, systemd-free
description: "Devuan 6.0 “Excalibur” is now available — based on Debian 13 and continues the systemd-free approach."
image: /assets/images/post-images/devuan-6.0.jpg
---

**The** team behind Devuan GNU+Linux has announced the stable release of **version 6.0**, codenamed **“Excalibur”**, on 2 November 2025.  

![Devuan 6.0 Excalibr release](/assets/images/post-images/devuan-6.0.jpg)

This version is based on Debian GNU/Linux 13 (codename “Trixie”) but preserves Devuan’s commitment to avoid using the systemd init system.  

## Key changes  

> - Kernel: Updated to the Linux kernel 6.12 LTS series, providing improved hardware support and real-time features.  
- Init system alternatives: Users can choose among SysVinit, OpenRC or Runit instead of systemd.  
- Filesystem layout: The merged `/usr` hierarchy is now mandatory; if you are upgrading from the previous Devuan release, you must install the `usrmerge` package in advance.  
- Desktop environments: The live-desktop default image uses Xfce; additional options include KDE, MATE, Cinnamon, LXQt and LXDE.  
- Architecture support: Fully supported architectures include AMD64, ARM64, ARMEL, ARMHF and PPC64EL. The project no longer provides an official 32-bit x86 (i386) installer ISO.  

## Upgrade & installation notes  

If you are upgrading from the previous stable version (Devuan 5 “Daedalus”), the mandatory `/usr` merge requires attention: install the `usrmerge` package before you initiate the upgrade.  
All installation media—live, net-install and full desktop ISOs—are available from the official Devuan download page.  

## Why this matters  

Devuan occupies a unique place within the Linux ecosystem. By forking Debian and removing systemd, it provides a platform for users who prefer init-system freedom while staying within Debian’s package ecosystem. With Excalibur, the project aligns itself with Debian 13’s base, ensuring up-to-date packages and hardware support, while maintaining its philosophical stance.  

## Considerations  

- If you rely on 32-bit x86 hardware and were using i386 installer ISOs, note that Devuan 6 no longer provides a dedicated installer for that architecture—though i386 packages may still be available.  
- The `/usr` merge can affect custom partition layouts and scripts that assume a split `/usr` hierarchy.  
- While full desktop environments are supported, you may need to review init-specific service files and configurations, especially if migrating from a system using systemd.

## Final thoughts  

Devuan 6.0 “Excalibur” is a mature, careful update for users who value control over their system’s init and service-management. It may not offer flashy novelty, but it delivers stable infrastructure with clarity of purpose. If you seek a Debian-based system without systemd, Excalibur is a solid option.

