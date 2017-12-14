---
title: TrueOS 17.12 released with improved stability
layout: post
categories: trueos release
image: http://localhost:4000/assets/images/post-images/trueos17.12.jpg
---

**The** *TrueOS* team has announced the release of TrueOS 17.12, latest 6 monthly stable release of FreeBSD based desktop BSD operating system. This release comes with improved stability to provide a more reliable experience.

There are dramatic improvements in various components & tasks such as OpenRC, boot speed, removable device management, SysAdm API integrations ..etc. The Lumina Desktop has also got several improvements since the previous release.

![TrueOS 17.12 release banner](http://localhost:4000/assets/images/post-images/trueos17.12.jpg)

In addition to the changes in the desktop release, the team was also working on TrueOS server edition. As a proof of this, the team has introduced a new text-based server image with support for Virtualization systems such as *bhyve*. This server image also takes advantage of various improvements in FreeBSD.

Some of the important highlights in TrueOS 17.12 release can be summarized as:
> * Over 1100 OpenRC services have been created for 3rd-party packages. This should ensure the functionality of nearly all available 3rd-party packages that install/use their own services.
> * The OpenRC services for FreeBSD itself have been overhauled, resulting in significantly shorter boot times.
> * Separate install images for desktops and servers (server image uses a text/console installer). The server image provides support for Bhyve.
> * FreeBSD base is synced with 12.0-CURRENT as of December 4th, 2017 (Github commit: 209d01f)
> * FreeBSD ports tree is synced as of November 30th (pre-FLAVOR changes)
> * Lumina Desktop has been updated/developed from 1.3.0 to 1.4.1
> * PCDM now supports multiple simultaneous graphical sessions
> * Removable devices are now managed through the “automounter” service.
> * Devices are “announced” as available to the system via .desktop shortcuts in /media. These shortcuts also contain a variety of optional “Actions” that may be performed on the device.
> * Devices are only mounted while they are being used (such as when browsing via the command line or a file manager).
> * Devices are automatically unmounted as soon as they stop being accessed.
> * Integrated support for all major filesystems (UFS, EXT, FAT, NTFS, ExFAT, etc..)
> * The TrueOS update system has moved to an “active” update backend. This means that the user will need to actually start the update process by clicking the “Update Now” button in SysAdm, Lumina, or PCDM (as well as the command-line option). The staging of the update files is still performed automatically by default but this (and many other options) can be easily changed in the “Update Manager” settings as desired.

For more information, proceed to [TrueOS 17.12 release announcement](https://www.trueos.org/blog/trueos-17-12-release/) published in projects website.