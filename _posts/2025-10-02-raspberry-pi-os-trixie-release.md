---
layout: post
title: "Raspberry Pi OS Trixie Released with New Theme, Control Centre, and Modular Packaging"
categories: [Linux, raspberry-pi-os, Release]
tags: [Raspberry Pi OS, Trixie, Debian, Linux, Raspberry Pi]
description: "Raspberry Pi OS Trixie arrives with a refreshed theme, new Control Centre, modular packaging, and Debian’s year 2038 fix."
image: /assets/images/post-images/raspberrypi.webp
---

**The** Raspberry Pi Foundation has announced a major new release of **Raspberry Pi OS**, now based on **Debian 13 “Trixie”**. This update brings a refreshed desktop experience, a brand-new **Control Centre application**, and a more **modular packaging system**, along with all the stability and updates inherited from Debian Trixie.

![Raspberry Pi OS Trixie featured image](/assets/images/post-images/raspberrypi.webp)

## Year 2038 Fix

One of the biggest under-the-hood changes in Debian Trixie is the move from 32-bit to **64-bit time values**. Traditionally, Linux stored time as a 32-bit value counting seconds since January 1, 1970. This would have overflowed on **January 19, 2038**, resetting systems to 1970. With 64-bit values, Raspberry Pi OS Trixie is now safe until the year 292,277,026,596 — well beyond concern.

## Fresh Look: New Theme, Icons, and Fonts

Users will immediately notice a refreshed **desktop theme**. The update introduces:

- **Nunito Sans Light** as the new default font (replacing Piboto used for over a decade).  
- A **new icon set** and overall visual tweaks.  
- **Wallpapers by Greg Annandale**, with the default showing a sunrise over the Drakensberg mountains in Lesotho.  

This is also the first time Raspberry Pi OS visuals have benefited from an external UI designer’s contribution.

## New Control Centre Application

The release consolidates multiple preference tools (such as Raspberry Pi Configuration, Appearance Settings, Screen Configuration, etc.) into a single **Control Centre**.  

Control Centre highlights:  
- Unified access to system settings.  
- Scroll-to-switch navigation between categories.  
- Plugin-based design, allowing future extensions by the Raspberry Pi team or third parties.  

Developers can find plugin-writing instructions on the [Control Centre GitHub](https://github.com/RPi-Distro) page.

## Updated Bookshelf Experience

The **Bookshelf application**, first launched during the COVID-19 lockdown, has been updated to reflect the new **magazine access policy**.  
- Subscribers to *Raspberry Pi Official Magazine* now get early access to titles.  
- Free readers will see upcoming issues with a **padlock icon**, becoming available after a few months.  
- Subscribers can unlock all titles instantly by signing in.

## Modular Packaging System

A major behind-the-scenes improvement is the introduction of **meta-packages**, making Raspberry Pi OS installation and customization more flexible.  

For example:  
- `rpd-wayland-core` or `rpd-x-core` for minimal Wayland/X desktops.  
- `rpd-theme` for icons, fonts, and GTK theme.  
- `rpd-preferences` for Control Centre.  
- `rpd-applications` and `rpd-utilities` for software bundles.  
- `rpd-developer` and `rpd-graphics` for developer tools and graphics utilities.  

This modular approach makes it easy to **convert Lite images into full desktops**, or remove unused components from a full image.

## How to Get Raspberry Pi OS Trixie

The Raspberry Pi team **strongly recommends flashing a fresh image** rather than attempting an in-place upgrade.  

You can get the new release via:  
- **Raspberry Pi Imager**  
- Or direct downloads from the [Raspberry Pi OS downloads page](https://www.raspberrypi.com/software/).  

As always, remember to back up before making major changes.

For [further information on Raspberry Pi OS Trixie](https://www.raspberrypi.com/news/trixie-the-new-version-of-raspberry-pi-os/), see the official release announcement on project's blog.