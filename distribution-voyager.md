---
layout: distribution
uid: voyager
title: 'Voyager Live'
Category: Distribution
permalink: /distribution/voyager
logo: voyager-logo.png
image: /assets/images/preview/voyager-preview.jpg
preview: voyager-preview.jpg
preview_caption: "Voyager Live desktop screenshot" # TODO: describe what the screenshot actually shows
home_page: https://voyagerlive.org/
desktops: [gnome, xfce]
base: [debian, ubuntu]
tagline: "French Xubuntu and Debian Linux"
description: "Voyager Live is a French Linux distro built on Xubuntu and Debian, offering polished GNOME and Xfce desktops with preconfigured tools."
last_modified_at: 2026-10-17

releases:
  Voyager 26.10: /voyager-26-10-release/
  "Voyager 25.10": "/voyager-25-10-release/"
  "Voyager Live 13 (Debian 13)": "/voyager-13-debian-released/"
  "Voyager 21.10": "/voyager-21.10-ge-release/"
  "Voyager 11 Bullseye": "/voyager-11-release/"
  "Voyager GE 19.10": "/2-voyager-19.10-release/"
  "Voyager 10": "/voyager-10-with-screenshots/"
  "Voyager GE 18.10": "/1-voyager-ge-18.10-brings-gnome-shell/"
  "Voyager Live 16.04 LTS": "https://open-source-feed.blogspot.com/2016/04/voyager-live-1604-lts-released.html"
  # TODO: check for newer releases (e.g. Voyager 26.04, Voyager 13.x point releases) and add posts

screenshots:
  "Voyager 10": "/voyager-10-with-screenshots/"

# NOTE: key renamed from "review" to "reviews" - the layout loops over page.reviews
reviews:
  "Voyager 16.04 offers a smooth Linux adventure": "https://open-source-feed.blogspot.com/2016/06/voyager-live-1604-offers-smooth-linux.html"

faq:
  "Is Voyager Live based on Ubuntu or Debian?": "Both. The Ubuntu-based editions descend from Xubuntu and follow Ubuntu's six-month release cycle, while the Debian edition (Voyager 13) is built on Debian 13 'Trixie'."
  "Is Voyager Live just Xubuntu with a new theme?": "Historically the author described it as a customization layer over Xubuntu rather than a separate base, adding its own themes, tools and configuration on top of the same packages. Newer releases use GNOME as the main desktop."
  "Which desktop does Voyager Live use?": "Early releases used Xfce. Starting with Voyager GE 18.10, GNOME Shell became the main desktop, and Xfce, the original desktop, is still listed among its desktop environments."
  "Where can I download Voyager Live?": "Downloads are listed on the official website at voyagerlive.org. See our release posts below for what changed in each version."
---

**Voyager Live** is a French Linux distribution that started as a customization layer on top of Xubuntu and now ships both Ubuntu-based and Debian-based editions. Releases are announced by Rodolphe Bachelart, and the distro is aimed at people who want a finished-looking desktop with the tools already chosen, instead of assembling one package by package.

## How Voyager Live started

The first Voyager releases used the lightweight Xfce desktop on top of Xubuntu. Rather than forking, the project reused the Xubuntu base and its package sources, then added its own theme, icons, preinstalled applications and settings. <!-- VERIFY: still true for current Ubuntu-based releases (shared repositories and release cycle) -->

Early releases also aimed to cover several usage profiles, such as gaming, multimedia and privacy-focused use, from one installation. <!-- VERIFY: multi-profile claim is from 2018 coverage; confirm it still applies -->

## From Xfce to GNOME

With [Voyager GE 18.10](/1-voyager-ge-18.10-brings-gnome-shell/), GNOME Shell became the main desktop for the first time, giving the distro a more modern look. Xfce stayed part of the project for lighter hardware. <!-- VERIFY: since 24.10, DistroWatch describes GNOME and Xfce as one unified interface; confirm whether Xfce is still a separate edition -->

You can read more about the two environments on our [GNOME](/desktop/gnome) and [Xfce](/desktop/xfce) pages.

## Ubuntu and Debian editions

Voyager now comes in two lines, and the choice mostly comes down to release style:

- **Ubuntu-based:** follows Ubuntu's April and October releases, so newer software arrives sooner. The latest release covered here is [Voyager 25.10](/voyager-25-10-release/), built on Ubuntu 25.10 with GNOME 49. See [Ubuntu](/distribution/ubuntu) for the base system. <!-- TODO: check for Voyager 26.04 -->
- **Debian-based:** [Voyager 13](/voyager-13-debian-released/) is built on Debian 13 "Trixie" with GNOME and the Linux 6.12 LTS kernel, and benefits from Debian's security and LTS support. See [Debian](/distribution/debian) for the base system.

## Things to know before trying it

- The ISO files are large, over 4 GB for the Debian edition, so allow time to download and a big enough USB stick. <!-- VERIFY: current ISO sizes -->
- The Ubuntu-based and Debian-based lines are released on separate schedules, so check the official site to see which edition has the newest version.

## Download and release notes

Download images from the [official Voyager Live website](https://voyagerlive.org/). For what changed in each version, see the release posts listed in the table below, starting with [Voyager 25.10](/voyager-25-10-release/) and [Voyager Live 13](/voyager-13-debian-released/).