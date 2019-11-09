---
title: "Project Trident announces an alpha quality release based on Void Linux"
layout: post
categories: trident release
tags: trident release
image: "/assets/images/post-images/trident-void.png"
---

**The** Project Trident has announced the release of a new alpha quality distribution based on Void Linux. This is the first public release from the project after announcing the plan to migrate from TrueOS to Void Linux.

Last month, the Project Trident team had published their plan for migrating from existing TrueOS base to Void Linux. Void Linux based alpha release is a footstep to the same objective. The team is planning to deliver the first stable Void Linux based release on January 2020.

Going forward, the Trident team will work on porting existing tools and utilities, preparing the user management subsystem and implementing a boot-to-graphics system for the Void Linux based distribution. The results will be made available to the community as a BETA release.

![Void Linux based Trident banner](/assets/images/post-images/trident-void.png)

## There is no Graphical Desktop Setup
The Project Trident's Void Linux based distribution is at the early stage of development now. So there is no graphical environment configured for the system.

If you really like to explore the system with GUI setup, there is an *immature* [Lumina Desktop](/desktop/lumina) implementation included from Void Linux repositories. After booting the system, GUI can be launched with **start-lumina-desktop** command.

Regarding the Lumina Desktop, it is not *customized* in this release to make it appealing for regular use. Also, the default Trident tools are not available in this system. The user would have to take some effort to create shortcuts, and to customize the system for a better experience.

## What we can expect from this Alpha image?
We can expect the following from the Alpha image provided by Project Trident.
> - A full “ZFS-on-root” installation of Void Linux
- A full walk-through of the installation procedure in an easy-to-use fashion. No experience with disk formatting or partitioning is required.
- Hybrid EFI and BIOS-boot capabilities. Both for the ISO and for the system post-install.
- Encrypted SWAP on ZFS (if swap space is selected)
- Support for both “glibc” and “musl” versions of Void packages in a single installer.
- Support for detecting and connecting to Wireless networks in an easy-to-use series of prompts (DHCP only). These settings get transferred over to the new installation for out-of-box network support.
- Due to the constant flow of updates to the Void Linux package repositories, this image is a complete “net-install” implementation. This means that all installed packages are always the current version from the repository, and result in a system that is fully up to date after the install is completed.

For further information on the [Void Linux based Trident distribution](https://project-trident.org/post/void-alpha-available/), see the release announcement.