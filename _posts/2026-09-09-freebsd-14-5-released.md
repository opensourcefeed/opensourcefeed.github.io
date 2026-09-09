---
layout: post
title: "FreeBSD 14.5 Released: Security Fixes, inotify Support, and Updated Toolchain"
categories: [freebsd, bsd, release]
tags: [freebsd, freebsd-14, release, unix, bsd]
description: "FreeBSD 14.5-RELEASE is out with dozens of security fixes, Linux-compatible inotify APIs, LLVM 21.1.8, OpenSSL 3.0.21, and UEFI boot fixes."
image: /assets/images/post-images/freebsd/freebsd-14.5.webp
---

**The** FreeBSD Release Engineering Team has announced FreeBSD 14.5-RELEASE, the sixth and likely final release on the stable/14 branch. It arrived on September 8, 2026, and focuses on maintenance rather than new features — delivering security fixes, driver improvements, and updated third-party software.

![FreeBSD 14.5-RELEASE banner with the FreeBSD demon mascot and version number](/assets/images/post-images/freebsd/freebsd-14.5.webp)

If you are still running FreeBSD 14 in production and are not yet ready to move to [FreeBSD 15.1](/freebsd-15-1-released/), this release is your recommended update path. For a broader overview of the project, see the [FreeBSD distribution page](/distribution/freebsd).

## Security Fixes

Security is the headline story in this release. FreeBSD 14.5 addresses dozens of security advisories, covering a wide range of issues including remote code execution, denial-of-service vectors, kernel stack bugs, and use-after-free vulnerabilities. Many of these were found with the help of AI and LLM-assisted code analysis tools — a growing trend across open source projects.

## inotify Support Added

FreeBSD 14.5 adds Linux-compatible inotify system calls along with matching libc APIs. This allows applications that use inotify for filesystem event monitoring to run on FreeBSD without code changes. It is a practical step toward better Linux application compatibility.

## Toolchain and Software Updates

Several bundled software packages have been updated:

- **LLVM** updated to 21.1.8
- **OpenSSL** updated to 3.0.21
- **ncurses** updated to 6.6
- **XZ** updated to 5.8.3

These updates bring security patches and stability improvements that matter for production systems.

## Hardware and Driver Improvements

The ACPI driver now handles power management better on Apple Mac hardware with dual GPUs. The AHCI driver adds support for additional SATA controllers. The ASMC driver drops 32-bit support, reflecting the project's ongoing focus on 64-bit platforms.

## Boot Fixes

A notable fix in this release resolves amd64 UEFI loader failures that affected some systems. UEFI boot-entry creation in `bsdinstall` has also been restored, which had been missing in prior releases.

## Availability

FreeBSD 14.5-RELEASE is available for the following architectures: amd64, i386, aarch64, armv7, powerpc, powerpc64, powerpc64le, and riscv64. You can install it from bootable ISO images, over the network, or via USB on supported platforms. Pre-built virtual machine images are available in QCOW2, VHD, and VMDK formats for amd64, i386, aarch64, and riscv64.

Existing users can upgrade using `freebsd-update(8)`. Source-based upgrades are supported using the instructions in `/usr/src/UPDATING`.

This is also a good moment to consider whether [FreeBSD 14.4](/freebsd-14-4-released/) users should plan their upgrade path — either staying on 14.5 for stability or moving forward to the 15.x series.

## References
1. [FreeBSD 14.5-RELEASE Announcement](https://www.freebsd.org/releases/14.5R/announce/) — FreeBSD.org
2. [FreeBSD 14.5-RELEASE Release Notes](https://www.freebsd.org/releases/14.5R/relnotes/) — FreeBSD.org
