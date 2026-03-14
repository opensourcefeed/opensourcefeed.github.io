---
layout: post
title: "EndeavourOS Titan Released: Linux 6.19, Improved GPU Support, and a New Hardware Tool"
categories: [endeavour, linux, release]
tags: [endeavouros, linux, arch-linux, gpu-drivers, release, rolling-release]
description: "EndeavourOS Titan arrives with Linux 6.19, full GPU driver installation, hardware detection improvements, and a new eos-hwtool for managing GPU drivers."
image: /assets/images/post-images/endeavouros/endeavouros-titan.jpeg
---

**EndeavourOS** is an Arch-based rolling release Linux distribution that aims to keep the Arch experience accessible without heavy customisation. Its latest ISO release, named **Titan** after Saturn's largest moon and the second-largest moon in the solar system, is now available. The release ships with Linux kernel 6.19 and brings meaningful improvements to the installation process, particularly around GPU driver handling.

![EndeavourOS Titan release featuring Linux 6.19 and improved GPU driver support](/assets/images/post-images/endeavouros/endeavouros-titan.jpeg)

The team notes that existing users don't need to reinstall. If you keep your system updated, you already have the latest packages. Titan's changes apply only to new installs, the Calamares installer, and the live environment.

## What Ships with EndeavourOS Titan?

The live environment includes the following core components:

- **Calamares** 26.03.1.3-1
- **Firefox** 148.0-1
- **Linux** 6.19.6.arch1-1
- **Mesa** 1:26.0.1-1
- **Xorg-server** 21.1.21-1
- **Nvidia-utils** 590.48.01-4

## GPU Driver Improvements

The most notable change in Titan is how it handles GPU drivers during installation. The installer now detects hardware for all GPUs and virtual machines and automatically installs the appropriate drivers — including Vulkan drivers and packages needed for hardware-accelerated video decoding where supported. GPU drivers are also loaded early by default, which helps avoid display issues during and after installation.

## New Tool: eos-hwtool

Titan introduces `eos-hwtool`, a new command-line utility used internally by the installer. It is also available to all EndeavourOS users and lets you install or remove GPU drivers at any time after installation. This fills a gap for users who swap hardware or want to manage drivers without reinstalling the system.

## Better Mirror Handling

Mirror ranking has also been improved. When the installer runs offline, it now provides an optimised mirror list rather than falling back on defaults. This should result in faster package downloads after installation on systems without an internet connection during setup.

## Slightly Larger ISO

The ISO size has grown from roughly 3 GB to 3.4 GB, compared to its predecessor [Ganymede Neo](/endeavouros-ganymede-neo-released/). The increase comes from the new GPU driver packages and hardware detection features — not from added desktop software. EndeavourOS maintains its minimal approach, and the base install remains close to a stock Arch Linux experience.

## California Age Verification Law

The team also briefly addressed the recently proposed age verification law in California that would apply to operating systems by 2027. EndeavourOS has no infrastructure to track downloads or user identities, which makes compliance impractical. Like Arch Linux, the project collects no user data. The team is watching how organisations like the OSI, FSF, and Linux Foundation respond, as the law could affect a wide range of FOSS projects.

## Download

Titan is available now from the [EndeavourOS homepage](https://endeavouros.com/). For full details on the release, see the [official announcement](https://endeavouros.com/news/whats-new-in-endeavouros-titan-release/).