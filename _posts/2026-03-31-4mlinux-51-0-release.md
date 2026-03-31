---
layout: post
title: "4MLinux 51.0 Released with Updated Apps and Smarter GPU Support"
categories: [4mlinux, release]
tags: [4mlinux, linux, lightweight-linux, release, mesa, vulkan]
description: "4MLinux 51.0 is now stable, bringing LibreOffice 26.2, Firefox 149, Mesa 25.3.1 with Vulkan, AY/YM audio emulation, and intelligent hardware detection."
image: /assets/images/post-images/4MLinux/4mlinux-51-0-release.jpg
---

**The** 4MLinux team has announced the stable release of 4MLinux 51.0. This lightweight distribution keeps its familiar focus on maintenance, multimedia, mini server, and games — while updating its core software stack and adding smarter GPU driver handling.

![4MLinux 51.0 stable release featuring updated apps and Vulkan GPU support](/assets/images/post-images/4MLinux/4mlinux-51-0-release.jpg)

## What's New in 4MLinux 51.0

The release ships with a refreshed set of core applications. For office work, users get LibreOffice 26.2 alongside the GNOME Office suite — AbiWord 3.0.7, GIMP 3.0.8, and Gnumeric 1.12.60. Browsing is covered by Firefox 149.0 and Chrome 146.0, with email handled by Thunderbird 140.9.

On the multimedia side, Audacious 4.5.1 handles music, while VLC 3.0.23 and SMPlayer 25.6.0 take care of video. Gaming runs on Mesa 25.3.1. Developers will find PHP 8.4.14, Perl 5.42.0, Python 3.13.8, and Ruby 3.4.7 available out of the box.

One of the headline additions in this release is improved GPU driver support. The system now ships a comprehensive driver suite: Mesa 25.3.1 with VAAPI and Vulkan for modern GPUs, Mesa 21.3.9 with VAAPI and VDPAU for legacy adapters, Intel VAAPI in both i965 and iHD variants, and up-to-date firmware for AMD, Intel, and NVIDIA cards. On top of that, 4MLinux 51.0 can now detect your hardware and apply the best driver settings automatically.

Another new feature is improved support for ZX Spectrum and Atari music through the AY/YM emulation library — a nice addition for retro audio enthusiasts. Two new downloadable extensions also arrive: Midori (a lightweight web browser) and cmus (a terminal-based music player).

The built-in HTTP/FTP server continues to run on BusyBox 1.37.0 for users who need a minimal server setup.

If you want to dig into the full package list, the project maintains a [complete list of included packages](http://4mlinux.com/addons-51.0.txt) on its website.

This is a solid follow-up to [4MLinux 49.0](https://www.opensourcefeed.org/4mlinux-49-0-stable-release/), which added Bcachefs support and mobile connectivity improvements, and [4MLinux 47.0](https://www.opensourcefeed.org/4m-linux-47-stable/), which brought KVM virtual block device support. You can also visit the [4MLinux distribution page](/distribution/4mlinux) for the full release history.

4MLinux 51.0 is available as a free download from the [official website](http://4mlinux.com/index.php?page=download). For the full release notes, see the [official announcement](https://4mlinux-releases.blogspot.com/2026/03/4mlinux-510-stable-released.html).