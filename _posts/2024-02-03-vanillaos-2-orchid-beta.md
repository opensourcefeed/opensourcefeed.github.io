---
title: "Vanilla OS 2 Orchid Beta: A complete revamp of the project"
layout: post
categories: vanillaos release
image: /assets/images/post-images/vanilla/vanilla-orchid-beta.jpg
description: "Explore the revolutionary Vanilla OS 2 Orchid Beta – a complete rewrite for stability, security, and speed. Download now for a seamless computing experience! 🚀 #VanillaOS #OrchidBeta #TechUpdate"
---

**The** highly anticipated release of Vanilla OS 2 Orchid Beta has been officially announced! Following a year of meticulous development and a successful five-month Developer Preview, the team is delighted to introduce the first feature-freeze version of Vanilla OS 2 Orchid.

![Vanilla OS 2 Orchid Beta](/assets/images/post-images/vanilla/vanilla-orchid-beta.jpg)

In this substantial update, Orchid signifies more than just a typical upgrade; it marks a complete overhaul of Vanilla OS with a primary focus on stability, security, speed, and user-friendliness. Every aspect of the project underwent thorough reevaluation, incorporating extensive community feedback to deliver a more mature and reliable operating system.

## Key Features of Vanilla OS 2 Orchid Beta

- New Wallpaper: Users will now enjoy a fresh look with a stunning new wallpaper skillfully designed by a community member, hasten.
- Hybrid Debian Base: Orchid utilizes a hybrid base of Debian packages and Vib modules, providing users with increased flexibility and control over the system and update distribution. Previously, Vanilla OS was using Ubuntu as the foundation.
- ABRoot v2: The A/B Partitioning system, ABRoot, has undergone a complete rewrite in Orchid. This ensures faster and more reliable updates, with additional features such as system state dumping for support and seamless switching between flavors without data loss.
- LVM Thin Provisioning: Addressing feedback received from Vanilla OS 22.10, Orchid introduces support for LVM Thin Provisioning. This optimization in disk space usage provides users with more room for their data.
- Sudon't: The traditional use of sudo is now a thing of the past; Vanilla OS 2 Orchid replaces it with PolKit policies. PolKit, unlike sudo, is integrated into the system as a centralized authentication authority, and privileged operations are managed through specific policies defined for each action. This change offers a more controlled and secure approach to performing privileged operations.
- Vanilla System Operator and Apx: VSO and Apx have undergone significant rewriting. VSO now serves as a system shell and package manager and provides Android app support. Apx v2 introduces the creation of custom environments with a new graphical interface, Apx GUI.
- FsGuard and FsWarn: Enhancing system security, Orchid introduces FsGuard and FsWarn. These tools check system integrity during boot and halt in case of discrepancies, ensuring a secure system environment.
- Vanilla Installer and First Setup: The Vanilla Installer has been improved, now using Albius as the backend. First Setup now offers OEM compatibility, allowing manufacturers to pre-install Vanilla OS on devices.
- PRIME Profiles: Orchid introduces a new tool, prime-switch, for easy switching between graphics cards without relying on the command line.
- Vanilla Tools: Vanilla OS 2 Orchid introduces Vanilla Tools, a set of utilities for managing system features quickly and efficiently. 
  - cur-gpu displays details of the currently used graphics card
  - nrun enables running applications using Nvidia graphics card

For [further information on Vanilla OS 2 Orchid Beta release](https://vanillaos.org/blog/article/2024-01-30/vanilla-os-2-orchid-beta-is-here), see the official release announcement on the project website.

## Download Vanilla OS 2 Orchid Beta

Vanilla OS 2 Orchid Beta is available for free download from the projects download page.

<a href="https://vanillaos.org/download/orchid/beta" class="download">Download Vanilla OS 2 Orchid Beta</a>