---
layout: distribution
uid: q4os
title: 'Q4OS'
Category: Distribution
permalink: /distribution/q4os
type : Linux
logo: q4os.png
preview: q4os.jpg
home_page: https://q4os.org/
desktops: [trinity, plasma]
base: [debian]
tagline: Desktop OS with classic experience
image: /assets/images/preview/q4os.jpg
last_modified_at: 2026-10-10

description : "Q4OS is a lightweight Debian-based Linux distribution featuring Trinity and KDE Plasma desktops, designed for speed, stability, and older computers."

releases:
  Q4OS 6.10 Andromeda: /q4os-6-10-andromeda-release/
  Q4OS 6.7 Andromeda: /q4os-6-7-andromeda-release/
  Q4OS 6.1 Andromeda: /q4os-6-1-andromeda-released/
  Q4OS 5.8 Aquarius: /q4os-58-release/
  Q4OS 5.6 Aquarius: /q4os-56-aquarius/
  Q4OS 5.2 Aquarius: /q4os-52-aquarius-release/
  Q4OS 4.6 Gemini: /q4os-4.6-release/
  Q4OS 3.12: "/q4os-3.12/"
  Q4OS 3.10: "/q4os-3.10-release/"
  Q4OS 3.1 testing : "https://open-source-feed.blogspot.com/2018/01/q4os-31-testing-image-released-based-on.html"
  Q4OS 1.4.11 : "https://open-source-feed.blogspot.com/2016/06/q4os-1411-released-with-improved-nvidia.html"
  Q4OS 1.4.10 : "https://open-source-feed.blogspot.com/2016/05/q4os-1410-orion-released-with-improved.html"
  Q4OS 2.1 Scorpion testing : "https://open-source-feed.blogspot.com/2016/04/q4os-21-scorpion-testing-image-is.html"
  Q4OS 1.4.9 Orion : "https://open-source-feed.blogspot.com/2016/04/q4os-149-orion-released.html"

screenshots:
  Q4OS 5.2 Aquarius: /q4os-52-aquarius-release/
  Q4OS 3.10: "/q4os-3.10-release/"
  Q4OS 3.8: "/windows-xp-days-q4os-3.8/"

stories:
  Converting Q4OS into a Windows XP clone using XPQ4 : "https://open-source-feed.blogspot.com/2016/04/converting-q4os-into-windows-xp-clone.html"

faq:
  "Is Q4OS good for old computers?": "Yes. The Trinity edition is designed for old, low-memory hardware and lists a 256 MB RAM minimum. The Plasma edition needs more, at least 1 GB of RAM."
  "Is Q4OS beginner friendly?": "Yes. A familiar desktop layout plus the graphical Welcome Screen, Desktop Profiler and Setup Utility make it easy to get started without the terminal."
  "Can Q4OS replace Windows?": "For everyday tasks such as browsing, email, office work and media, yes, and it runs well on hardware that struggles with current Windows versions. If you depend on Windows-only software, check that a Linux alternative exists before switching."
  "How long is Q4OS supported?": "Each stable series is supported for about five years. Andromeda (6.x) runs to around 2030 and Aquarius (5.x) to June 2028. Gemini (4.x) was due to reach end of life in September 2026, so upgrade if you still use it."

seo:
  type: SoftwareApplication
---

**Q4OS** is a lightweight, Debian-based Linux distribution built for speed, stability and older computers. It ships with two desktops: the modern **KDE Plasma**, the default in the current Andromeda series, and the classic **Trinity Desktop (TDE)**, a fork of KDE 3 with very low memory use.

The latest release, [Q4OS 6.10 Andromeda](/q4os-6-10-andromeda-release/), is based on Debian 13 "Trixie" (13.7). Get the ISO from the [official download page](https://q4os.org/downloads1.html).

## System Requirements

| Edition | CPU | RAM | Disk |
|---|---|---|---|
| **Trinity** | 350 MHz Pentium II or better | 256 MB minimum | 5 GB |
| **KDE Plasma** | Any x86 or x64 processor | 1 GB minimum, 2 GB recommended | 5 GB minimum, 10 GB recommended |
{: .table .table-bordered}

Trinity has long been available for 32-bit hardware, which is rare among current distributions. Check the download page for the architecture you need.

## Key Features

- **Two desktops.** Choose Plasma for a modern, customizable desktop, or Trinity for a traditional layout that runs on very old machines.
- **Desktop Profiler.** Configure the system for different usage scenarios with predefined applications and settings.
- **Setup Utility.** Install additional software and third-party applications from a graphical tool.
- **Welcome Screen.** Shortcuts for common configuration tasks, software installation and documentation.
- **Familiar look.** Windows-like layouts and themes help people switching from Windows. The XPQ4 tool goes further and gives Q4OS a Windows XP look (see the story below).
- **Debian stable base.** You get APT, Debian's repositories and about five years of support per stable series, and Debian guides generally apply to Q4OS as well.

## Who Should Use Q4OS?

Q4OS is a good fit if you are:

- Switching from Windows and want a familiar layout
- Reviving an older laptop or desktop
- Running a school, office or lab with mixed or aging hardware
- A fan of traditional desktops who still wants current security updates

It is probably not the best choice if you want the very latest desktop software, since Debian stable favors reliability over novelty.

## Q4OS vs Other Lightweight Distributions

| | Q4OS | [Lubuntu](/distribution/lubuntu) | [Linux Lite](/distribution/lite) | [antiX](/distribution/antix) |
|---|---|---|---|---|
| **Base** | Debian | Ubuntu | Ubuntu | Debian |
| **Default desktop** | KDE Plasma (Trinity optional) | LXQt | Xfce | IceWM and other light window managers |
{: .table .table-bordered}

Q4OS stands out for pairing Debian's stability with Trinity, a desktop few other distributions still offer. Not sure which distro suits you? Try our [Distro Finder](/distro-chooser/).