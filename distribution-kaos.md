---
layout: distribution
uid: kaos
title: 'KaOS'
Category: Distribution
type : Linux
permalink: /distribution/kaos
logo: kaos-logo.png
preview: krita-op.jpg # TODO: replace with a KaOS screenshot or logo card, this is a Krita image
image: /assets/images/preview/krita-op.jpg # TODO: same as above
blog: https://kaosx.us/news/
home_page: https://kaosx.us
desktops: [plasma]
base : Independent
tagline: "A Lean, Rolling KDE Linux Distribution"

description : KaOS is an independent, rolling-release Linux distro built around KDE Plasma and Qt, with its own repositories and a curated package set.

releases:
  KaOS 2026.11: /kaos-2026-11-release/
  KaOS 2026.02: /kaos-february-iso-release/
  KaOS 2024.09: /kaos-202409-release/
  KaOS 2020.07 : "/kaos-2020.07-release/"
  KaOS 2018.10 : "/00-kaos-2018.10-released-with-plasma-5.14/"
  KaOS 2018.06 : "https://open-source-feed.blogspot.com/2018/06/kaos-201806-released-with-plasma-5131.html"
  KaOS 2017.09 : "https://open-source-feed.blogspot.com/2017/09/kaos-201709-snapshot-released-with.html"
  KaOS 2017.02 : "https://open-source-feed.blogspot.com/2017/02/kaos-201702-snapshot-released-with.html"
  KaOS 2017.01 : "https://open-source-feed.blogspot.com/2017/01/kaos-201701-released-with-fresh-look.html"
  KaOS 2016.11 : "https://open-source-feed.blogspot.com/2016/11/kaos-201611-released-with-plasma-583.html"
  KaOS 2016.09 : "https://open-source-feed.blogspot.com/2016/09/kaos-201609-released-with-latest-kde.html"
  KaOS 2016.01 : "https://open-source-feed.blogspot.com/2016/01/kaos-201601-released.html"
  KaOS 2015.11 : "https://open-source-feed.blogspot.com/2015/11/kaos-201511-is-available-now.html"

screenshots:
  KaOS 2020.07 : "/kaos-2020.07-release/"
  KaOS 2018.04 : "https://distroscreens.blogspot.com/2018/05/kaos-201804-screenshots.html"

---

**KaOS** is an independent, rolling-release Linux distribution that does one thing: deliver a polished [KDE Plasma](/desktop/plasma) desktop on a Qt-based software stack. It is not a spin of another distro. It ships its own repositories and keeps the package list deliberately small.

## What makes KaOS different?

Most distros try to offer every desktop and every package. KaOS does the opposite.

- **Plasma only.** There are no GNOME, Xfce or Cinnamon editions. Because the team supports a single desktop, Plasma and KDE Frameworks get tested as one product rather than as one option among many.
- **Qt first.** Core apps and tooling lean on Qt, so the desktop looks and behaves consistently. You are less likely to see GTK apps clashing with Plasma themes.
- **Independent and rolling.** KaOS is not based on another distribution (see [Based on](#) above), and packages update continuously. You install once and stay current without major version upgrades. <!-- VERIFY: package manager (pacman?) and own-repo wording against kaosx.us/about -->
- **Curated repositories.** The package set is intentionally limited. That means fewer choices than a large distro, but each package is built to work with the Plasma stack. <!-- VERIFY: any specific package/app counts before adding -->
- **x86_64 only.** KaOS targets 64-bit PCs. There are no 32-bit or ARM builds. <!-- VERIFY: still true -->
- **Periodic ISO snapshots.** New ISOs are published from time to time for fresh installs, while existing systems update through the rolling repos. For what shipped in each snapshot, see the [latest KaOS release](/kaos-2026-11-release/) and the release list below.

## Who is KaOS for?

**Good fit if you:**
- want a Plasma-focused system and don't plan to switch desktops
- like rolling releases and are comfortable updating regularly
- prefer a tidy, opinionated setup over a huge package catalog

**Probably not for you if you:**
- need a very large software repository out of the box
- run 32-bit or ARM hardware
- want long-term-support stability with infrequent, tested point releases

Not sure yet? The [Distro Finder](/distro-chooser/) can help you compare options, and the [full distribution list](/distribution/) covers other KDE and rolling-release choices.

## Getting KaOS

Download the current ISO from the [official KaOS website](https://kaosx.us). Project announcements and release notes are on the [KaOS news page](https://kaosx.us/news/). Write the ISO to a USB drive, boot it, and use the live session to try the desktop before installing. <!-- VERIFY: installer name (Calamares?) and whether live session is offered -->

## Frequently asked questions

**Is KaOS based on Arch Linux?**
No. KaOS is independent. <!-- VERIFY: add one sentence on how it relates to Arch (pacman, similar packaging ideas) once confirmed -->

**Can I use GNOME or another desktop on KaOS?**
KaOS officially supports only KDE Plasma. Other desktops are not part of the project's scope.

**Do I need to reinstall for every new release?**
No. KaOS is a rolling release, so an installed system updates in place. New ISO snapshots mainly benefit fresh installs.

**Where can I see how KaOS looks?**
See the screenshots below, or browse the [KDE Plasma](/desktop/plasma) page for the desktop itself. <!-- TODO: add a current KaOS screenshot with alt text "KaOS KDE Plasma desktop" -->