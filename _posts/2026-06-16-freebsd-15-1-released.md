---
layout: post
title: "FreeBSD 15.1 Released: Linux v7.0 Wi-Fi, C23 Progress, and Unicode 17"
categories: [freebsd, bsd, release]
tags: [freebsd, freebsd-15, release, unix, bsd]
description: "FreeBSD 15.1-RELEASE is out with Linux v7.0-based wireless drivers, Unicode 17.0 support, C23 language progress, and improved cloud image packaging."
image: /assets/images/post-images/freebsd/freebsd-15.1.webp
---

**The** FreeBSD Release Engineering Team has announced FreeBSD 15.1-RELEASE, the second release on the stable/15 branch. Released on June 16, 2026, it brings updated wireless drivers, cloud infrastructure improvements, a flexible kernel scheduler, and progress on modern C language support.

![FreeBSD 15.1 release banner showing the FreeBSD logo and version number](/assets/images/post-images/freebsd/freebsd-15.1.webp)

If you follow the FreeBSD 15 series, you may recall that [FreeBSD 15.0 arrived in late 2025](/freebsd-15-0-released/) as a milestone for 64-bit platform consolidation. FreeBSD 15.1 builds on that base with targeted improvements rather than sweeping changes.

## What's New in FreeBSD 15.1

**Wireless networking update.** The `iwlwifi(4)` driver and other LinuxKPI-based wireless networking drivers have been rebased to Linux v7.0. This means better support for modern Intel Wi-Fi adapters on both desktop and laptop hardware.

**Cloud image improvements.** FreeBSD cloud images that use packaged base systems now include `pkg(8)` by default. They also support automatic base system package updates on first boot, making it easier to get a fresh, current system on cloud providers without manual intervention.

**Flexible kernel scheduler.** A new `kern.sched.name` tunable lets you pick the kernel scheduler at boot time. This is useful for users who want to experiment with different scheduling strategies without rebuilding the kernel.

**C23 language support progress.** The FreeBSD project has made significant strides toward full support for C23, the latest revision of the C programming language standard. While not yet complete, this lays the groundwork for compiler and toolchain improvements ahead.

**Unicode 17.0 and CLDR 48.** Unicode support has been updated to Unicode 17.0.0 and CLDR 48, adding 4,803 new characters. This matters for applications that handle multilingual text, emoji, or script rendering.

## Availability and Supported Architectures

FreeBSD 15.1-RELEASE is available for amd64, aarch64, armv7, powerpc64, powerpc64le, and riscv64. Install images include DVD, disc1, memstick, and mini-memstick formats. VM images are available in QCOW2, VHD, and VMDK formats.

Cloud users can find FreeBSD 15.1 on Amazon EC2, Google Compute Engine, and Microsoft Azure. OCI container images are also available via Docker Hub and the GitHub Container Registry.

You can download FreeBSD 15.1 from the [official FreeBSD mirrors](https://download.freebsd.org/releases/ISO-IMAGES/15.1/).

## Dedication

The FreeBSD Project dedicates this release to the memory of Peter G. Neumann, a long-time collaborator on capability-based security and one of the foundational thinkers behind OS security concepts in systems like Multics.

## Support Timeline

FreeBSD 15.1-RELEASE is supported until **March 31, 2027**. FreeBSD 15.0-RELEASE reaches end of life on September 30, 2026. The FreeBSD 15 series as a whole is supported until December 31, 2029.

If you are still on FreeBSD 14.x, you can also check our coverage of [FreeBSD 14.4](/freebsd-14-4-released/), which landed with OpenSSH 10 and OpenZFS 2.2.9 earlier this year.

For more details on this release, see the [official FreeBSD 15.1 announcement](https://www.freebsd.org/releases/15.1R/announce/) and the full [release notes](https://www.FreeBSD.org/releases/15.1R/relnotes/).