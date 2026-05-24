---
layout: post
title: "PureOS Crimson Released: Purism's Next Privacy-First Linux"
categories: [pureos, release, linux]
tags: [pureos, purism, crimson, librem, gnome, kde, release]
description: "PureOS Crimson is now available for PCs, servers, and the Librem 5. Byzantium users can upgrade via the PureOS Upgrade app. Here's what changed."
image: /assets/images/post-images/pureos/pureos-crimson-release.webp
---

**Purism** has released PureOS Crimson, the next major version of its privacy-focused Linux distribution. The release follows a development cycle that included an alpha in August 2025 and a beta in early 2026.

PureOS is a Debian-based distribution maintained by Purism. It is fully endorsed by the Free Software Foundation and ships exclusively free software. It runs on Purism's Librem laptops, the Librem 5 smartphone, and standard PCs and servers. If you're interested in how PureOS compares to other privacy-oriented options, see our [roundup of privacy-focused Linux distributions](https://www.opensourcefeed.org/insights/privacy-focused-linux-distros/).

![Featured image for PureOS Crimson release highlighting privacy-first Linux features including Librem 5 support, Debian base, stability improvements, and free software focus with a crimson-purple abstract background and Linux penguin mascot.](/assets/images/post-images/pureos/pureos-crimson-release.webp)

## What's new in PureOS Crimson

### Stability and reliability

The team resolved a corner case that could cause systems to suspend without warning when suspend was enabled. A crash triggered by disconnecting an external display on the Librem 5 and Librem 11 is also fixed.

The Librem 5's hardware killswitches can disable internal sensors like the accelerometer. A bug caused the system to use an invalid sensor value after a killswitch was toggled, sometimes producing unexpected screen rotations. This is now fixed — the last valid sensor reading is retained correctly.

### Camera improvements on the Librem 5

The rear camera on the Librem 5 has a known silicon-level bug in its camera interface (ERR050384) that can lock up the interface in certain conditions. The team worked around this by carefully tuning camera clock rates to avoid the affected modes used by Millipixels.

Millipixels itself received several updates: red QR codes are now easier to scan, video recordings have better audio synchronization and consistent white balance, and photos and videos rotate automatically to match the phone's orientation. Photo post-processing now runs on the GPU using OpenGL, which is more efficient and enables better lens correction, tone mapping, and sharpening.

### Metapackage updates

The PureOS Plasma image now includes standard KDE applications by default and no longer installs GNOME Software. All desktop images include minimal development tools. The GNOME metapackage was synced with Debian Bookworm, and the Plymouth boot splash was removed from the server image metapackage, since servers don't need graphical boot components.

## Upgrading from Byzantium

Existing PureOS Byzantium users will receive the PureOS Upgrade application through regular system updates. Fresh installation images are available for [PCs](https://docs.puri.sm/Software/PureOS/Installation/Download.html), [servers](https://docs.puri.sm/Hardware/enterprise/ls/maintenance/os-reinstall.html), and the [Librem 5](https://docs.puri.sm/Hardware/Librem_5/Maintenance/Reflashing.html).

Purism notes that all Librem hardware — including the older Librem 13 and 15 laptops — is supported with this release. Purism does not impose an end-of-life date on its hardware.

## What's next: PureOS Dawn

With Crimson out, development has already started on PureOS Dawn, the next major release. Purism says much of the infrastructure work done for Crimson carries forward, and expects the path to Dawn to be shorter.

Read the full [PureOS Crimson release announcement](https://puri.sm/posts/pureos-crimson-development-report-april-2026-pureos-crimson-released/) on the Purism blog.