---
title: "Debian 11 <em>Bullseye</em> released"
layout: post
categories: debian release
tags: [debian release]
image: /assets/images/post-images/debian/debian-11.jpg
---

**On** 14th August 2021, the Debian team has announced the release of Debian 11 STABLE with the code name *Bullseye*. The Debian 11 release is a result of more than two years of development and testing efforts by the Debian project and the community contributors.

![Debian 11 banner](/assets/images/post-images/debian/debian-11.jpg)

With the help from the Debian Security Team and Debian Long Term Support team, Debian 11 users can enjoy support for five years.

Debian 11 is coming a with a wide range of applications, desktop environments, and window managers. Following are the popular desktop environments available in Debian repositories.
- Gnome 3.38,
- KDE Plasma 5.20,
- LXDE 11,
- LXQt 0.16,
- MATE 1.24,
- Xfce 4.16.

Citing from the official release announcement,
> This release contains over 11,294 new packages for a total count of 59,551 packages, along with a significant reduction of over 9,519 packages that were marked as obsolete and removed. 42,821 packages were updated and 5,434 packages remained unchanged.
bullseye becomes our first release to provide a Linux kernel with support for the exFAT filesystem and defaults to using it for mount exFAT filesystems. Consequently, it is no longer required to use the filesystem-in-userspace implementation provided via the exfat-fuse package. Tools for creating and checking an exFAT filesystem are provided in the exfatprogs package.
Most modern printers are able to use driverless printing and scanning without the need for vendor-specific (often non-free) drivers. bullseye brings forward a new package, ipp-usb, which uses the vendor-neutral IPP-over-USB protocol supported by many modern printers. This allows a USB device to be treated as a network device. The official SANE driverless backend is provided by sane-escl in libsane1, which uses the eSCL protocol.
Systemd in bullseye activates its persistent journal functionality, by default, with an implicit fallback to volatile storage. This allows users that are not relying on special features to uninstall traditional logging daemons and switch over to using only the systemd journal.

For further details, on Debian 11 *Bullseye*, read the [official release announcement](https://www.debian.org/News/2021/20210814) on the project's website, and see the [release notes](https://www.debian.org/releases/bullseye/releasenotes).
