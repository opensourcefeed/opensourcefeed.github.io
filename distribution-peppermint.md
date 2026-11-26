---
layout: distribution
uid: peppermint
title: 'Peppermint OS'
Category: Distribution
type : Linux
permalink: /distribution/peppermint
logo: peppermintos.png
preview: peppermint-void.webp
preview_caption: Peppermint OS Void edition with the Xfce desktop and the Peppermint Software Center
image: /assets/images/preview/peppermint-void.webp
home_page: https://peppermintos.com
desktops: [xfce]
base : [debian, devuan, void]
tagline: Customize with your own ideas
description : Peppermint OS is a lightweight Xfce Linux distro with Debian, systemd-free Devuan and rolling Void Linux editions, plus its own setup tools.
last_modified_at: 2026-11-26

seo:
  type: OperatingSystem

releases:
  Peppermint OS Void (Loaded): /peppermint-os-void-edition-release/
  Peppermint OS Debian Bookworm: /peppermintos-bookworm/
  Peppermint 10 Respin: /peppermint-10-respin/
  Peppermint 10 : "https://peppermintos.com/2019/05/peppermint-10-released/"
  Peppermint 9 : "https://open-source-feed.blogspot.com/2018/06/peppermint-os-9-released-with-ubuntu.html"
  Peppermint 8 Respin : /peppermint-8-respin-released-with-slick-greeter-updated-themes-more/
  Peppermint 8 : "https://open-source-feed.blogspot.com/2017/05/peppermint-os-8-released-with-linux.html"
  Peppermint 7 Respin : "https://open-source-feed.blogspot.com/2016/12/peppermint-7-respin-released.html"

screenshots :
  Peppermint 10: "/1-peppermintos-10-screenshots/"
  Peppermint 9 : "https://distroscreens.blogspot.com/2018/08/peppermint-os-9-screenshots.html"
  Peppermint 8 : "https://distroscreens.blogspot.com/2017/06/peppermint-os-8-screenshots.html"
  Peppermint 7 : "https://distroscreens.blogspot.com/2016/06/peppermint-os-7-screenshots.html"

stories:
  "Peppermint 7 will launch on 30th June (2016)" : "https://open-source-feed.blogspot.com/2016/06/peppermint-os-7-will-launch-on-30th-june.html"

telegram:
  Peppermint OS: https://t.me/peppermint_os

faq:
  "Is Peppermint OS still based on Ubuntu?": "No. Releases up to Peppermint 10 Respin were built on Ubuntu (via Lubuntu). The current project ships Debian, Devuan and Void Linux editions instead, and the Ubuntu-based releases no longer receive updates."
  "Which Peppermint OS edition should I download?": "Choose the Debian edition for the widest package choice with systemd, the Devuan edition if you want to avoid systemd and pick SysVinit, OpenRC or runit, and the Void edition if you prefer a rolling release with the newest packages."
  "What is the difference between Flagship and Loaded editions?": "Flagship ISOs are intentionally minimal and leave application choices to you. Loaded ISOs come with applications pre-installed, so they are larger; the first Void Loaded ISO is about 4 GB."
  "Which desktop environment does Peppermint OS use?": "Peppermint OS uses Xfce with Thunar as the default file manager. Older releases (7 to 10) combined the LXDE session with Xfce components."
  "Does Peppermint OS support 32-bit computers?": "Not currently. The official ISOs are 64-bit (amd64/x86_64) only. The project says community members are working on a 32-bit ISO, but no release date has been announced."
  "Does Peppermint OS have version numbers?": "No. After the move to Debian, Peppermint switched to continuous delivery: installed systems receive tool and package updates without reinstalling, and ISOs are refreshed periodically instead of carrying version numbers."
---

**Peppermint OS** is a lightweight GNU/Linux distribution that pairs a minimal [Xfce](/desktop/xfce) desktop with a set of in-house configuration tools. It is offered on three bases: [Debian](/distribution/debian), the systemd-free [Devuan](/distribution/devuan), and the rolling-release [Void Linux](/distribution/void). Peppermint suits users who want a fast, uncluttered desktop on modest hardware and prefer to choose their own applications instead of removing preinstalled ones.

## Peppermint OS editions: Debian, Devuan and Void

Peppermint no longer ships a single system. Each edition shares the same desktop and tools but differs in its base, init system and update model:

| Edition | Base | Init system | Update model |
|---------|------|-------------|--------------|
| Debian | Debian 13 "Trixie" | systemd | Debian stable packages, refreshed ISOs |
| Devuan | Devuan 6 "Excalibur" | SysVinit, OpenRC or runit (chosen at install) | Devuan stable packages, refreshed ISOs |
| Void (PepVoid) | Void Linux | runit | Rolling release |

The Void edition, announced in November 2026, is an additional base rather than a replacement: the team stated it is not rebasing Peppermint onto Void. See our [Peppermint OS Void release coverage](/peppermint-os-void-edition-release/) for details on that build and its custom ISO builder. For background on the Devuan base, read about [Devuan 6 Excalibur](/devuan-6-excalibur-released/).

### Flagship and Loaded builds

Peppermint publishes two styles of ISO:

- **Flagship**: deliberately minimal. You get the desktop, core utilities and Peppermint's tools, then install the apps you want.
- **Loaded**: ships with applications pre-installed for users who want a ready-to-use system. The first Void Loaded ISO is about 4 GB. A Flagship build of the Void edition is planned, with no date announced.

All current ISOs are 64-bit only (amd64/x86_64).

## Desktop and default software

Peppermint's mainline desktop is **Xfce**, with **Thunar** as the default file manager. The team keeps the default installation lean, so the desktop starts quickly and uses little memory compared with heavier environments such as GNOME or KDE Plasma.

Recent builds use **XLibre**, a fork of the Xorg server, as the display server. The Debian and Devuan editions moved from Xorg to XLibre in 2026, and the Void edition uses it from its first release.

## Peppermint tools and software center

What sets Peppermint apart from a plain Xfce spin of Debian is its collection of in-house tools, written in Python with Tkinter and PyQt. They help you configure the system after installation and add suggested packages without using the terminal. The November 2026 Void release introduced the **Peppermint Software Center** and refreshed the interface of the Peppermint Tools, and **PepFetch**, a system information script, also received an update.

Because these tools are packaged separately, improvements reach existing installations through normal updates, with no reinstall or new ISO needed.

## Release model: continuous delivery

Since moving to Debian, Peppermint has dropped numbered releases. The project uses continuous delivery: the team refreshes ISOs when the base or the tools change and publishes a Build Ledger that lists what each image contains. The Debian and Devuan editions follow their stable bases, while the Void edition is a true rolling release.

## Installing Peppermint OS

ISOs for all editions are available from the [official downloads page](https://peppermintos.com/trixie-base-downloads/), hosted on SourceForge. Each image comes with a SHA512 checksum, a GPG signature and a public key; the Void edition uses its own signing key, separate from the Debian and Devuan editions. Verify the download before writing it to a USB drive.

After booting the live session, open the menu, search for "install" and launch **Install Peppermint** to start the graphical installer. On the Devuan edition, the installer lets you choose the init system.

## History of Peppermint OS

<!-- VERIFY: founding year (2010) and founders (Kendall Weaver, Shane Remington); revival date (early 2022). The official About page names both as remembered members but does not state the founding year. -->
Peppermint was started in 2010 by Kendall Weaver and Shane Remington. Releases up to Peppermint 10 and the [Peppermint 10 Respin](/peppermint-10-respin/) were based on Ubuntu through [Lubuntu](/distribution/lubuntu) and used a hybrid desktop that combined the LXDE session with Xfce components. Early Peppermint versions focused on web integration through **Ice**, a tool that turned websites into desktop applications (site-specific browsers).

After longtime lead developer Mark Greaves died in 2020, his family asked that the project continue. A community team rebuilt Peppermint on Debian in 2022, using a DevOps and CI/CD workflow in place of the previous one-person release process. The Debian Bookworm update followed in 2023 ([our coverage](/peppermintos-bookworm/)), and the Devuan and Void editions were added later.

## Who should use Peppermint OS?

- **Owners of older or low-spec 64-bit PCs** who want a responsive Xfce desktop.
- **Users who prefer a minimal start** and want to choose their own applications.
- **People avoiding systemd**, through the Devuan edition.
- **Users who want newer packages** without leaving the Peppermint experience, through the Void edition.

If you want a lightweight Debian-based system with more preinstalled tooling, compare Peppermint with [MX Linux](/distribution/mx) or [antiX](/distribution/antix). For a more traditional, beginner-focused desktop, [Linux Mint](/distribution/linuxmint) is a common alternative.

## Peppermint OS community and support

The project is maintained by a volunteer team. Support and development happen in public:

- [Community forums on SourceForge](https://sourceforge.net/p/peppermintos/pepos/)
- [Documentation](https://peppermint_os.codeberg.page/html/)
- [Source code on Codeberg](https://codeberg.org/Peppermint_OS)
- [Mastodon](https://fosstodon.org/@peppermintos), Matrix (`#peppermintos:matrix.org`) and Telegram
