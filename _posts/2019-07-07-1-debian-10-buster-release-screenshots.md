---
title: "Debian 10 'buster' released, see screenshots"
layout: post
categories: debian screenshots
tags: debian screenshots
image: "/screenshots/Debian 10 GNOME/02 About Debian Buster.jpg"
---

**The** Debian team has announced the release of Debian 10 *buster*, latest stable release of *Universal Operating System*. Debian 10 will provide security updates and critical bug fixes for the coming 5 years.

Debian 10 is a result of 25 months of development effort, by the dedicated project members and community contributors around the world. It includes a wide range of desktop environments such as GNOME, Plasma, Cinnamon, MATE, XFCE, LXQt, and LXDE.

Following are remarkable features of Debian 10 release, highlighted in [the official release announcement for Debian 10](https://www.debian.org/News/2019/20190706).
> - Debian 10 GNOME Edition will feature Wayland as default display manager. It also provides Xorg as an alternative and on login screen, users can decide whether to proceed with Wayland or switch to Xorg.
- With the reproducible build project, around 91% of source packages included in Debian 10 will be identical to each other. This means, users can easily verify the attempts to tamper the source packages and build systems. This kind of verification will be enabled in upcoming Debian releases.
- For those in security-sensitive environments AppArmor, a mandatory access control framework for restricting programs' capabilities, is installed and enabled by default. Also, all methods provided by APT (except cdrom, gpgv, and rsh) can optionally make use of seccomp-BPF sandboxing. The https method for APT is included in the apt package and does not need to be installed separately.
- Network filtering is based on the nftables framework by default in Debian 10 buster. Starting with iptables v1.8.2 the binary package includes iptables-nft and iptables-legacy, two variants of the iptables command line interface. The nftables-based variant uses the nf_tables Linux kernel subsystem. The alternatives system can be used to choose between the variants.
- The UEFI support was first time introduced in Debian 7. This feature is now much better and Debian 10 can boot into almost any system which has UEFI boot enabled.
- With pre-installed cups and cups-filters Debian 10 provides support for driverless printing. Configuring printer is now easier in Debian 10.

Following section showcases some screenshots captured in Debian 10 GNOME desktop. Please note in mind, GNOME is only one among the Desktops supported by Debian.
{% include image-gallery.html folder="/screenshots/Debian 10 GNOME" %}
