---
layout: post
title: "Q4OS 6.10 Andromeda Released with Debian 13.7 Base"
categories: [q4os, debian, release]
tags: [q4os, q4os-6, andromeda, debian-13, trixie, plasma, trinity, release]
description: "Q4OS 6.10 Andromeda arrives on a Debian 13.7 base with a Trinity-free Plasma edition, slimmer live media, and a new WiFi tool for first login."
image: /assets/images/post-images/q4os/q4os-6-10-andromeda-release.webp
---

**The** Q4OS team has released Q4OS 6.10 Andromeda, a fresh set of installation media for its long-term support line. The announcement came on 8 October 2026. The release builds on Debian Trixie 13.7 and brings the newest stable Debian kernel along with security patches and bug fixes.

![Q4OS 6.10 Andromeda release](/assets/images/post-images/q4os/q4os-6-10-andromeda-release.webp)


## What is new in Q4OS 6.10

The release notes are short and focus on four changes:

- The Plasma edition drops all Trinity packages.
- The live media are slimmer, since they now ship with the Basic desktop profile.
- A new WiFi connection tool helps you get online at the first login.
- The release rolls in every cumulative update made since the last Andromeda stable release.

Q4OS uses desktop profiles to decide which software goes onto a system. A lighter default profile on the live media fits the smaller image size.

## Debian 13.7 base

Debian 13.7 is the seventh point release of Debian 13 "Trixie". The Debian project published it on 12 September 2026, and it focuses on security fixes and corrections for serious bugs. Q4OS 6.9 used this same base when it arrived in mid-September, so the changes in 6.10 come from the Q4OS side. For the previous step in the Debian line, see our post on the [Debian 13.6 point release](/debian-13-6-release/).

## Plasma edition drops Trinity packages

Q4OS has offered two desktops since its early days: KDE Plasma and the lighter Trinity desktop. When [Q4OS 6.1 Andromeda launched in September 2025](/q4os-6-1-andromeda-released/), the project promoted the option to install both side by side and switch between them. Version 6.10 removes Trinity packages from the Plasma edition. The announcement does not say whether the side-by-side option stays, so check the Q4OS documentation before you plan a dual-desktop setup.

The team has taken this path before. The Q4OS 3.10 release in 2020 made Plasma independent of Trinity and cut the size of the Plasma media.

## How to get Q4OS 6.10

New users can download the installation media from the [Downloads section](https://q4os.org/downloads1.html) of the Q4OS website. Existing installations do not need a reinstall. The team is rolling the new packages out through the Q4OS repositories, and the standard system update process will pick them up.

Q4OS 6.10 follows a steady rhythm of updates in 2026. Version 6.7 arrived in May on a Debian 13.5 base, as we covered in our [Q4OS 6.7 Andromeda report](/q4os-6-7-andromeda-release/). Versions 6.8 and 6.9 followed in July and September. Andromeda is an LTS release, and the project has promised at least five years of security patches and updates from its September 2025 debut.

Sources: [Q4OS 6.10 Andromeda stable announcement](https://www.q4os.org/blog.html), [Debian 13 "Trixie" release information](https://www.debian.org/releases/trixie/)
