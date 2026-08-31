---
layout: post
title: "ReactOS 0.4.16 Released with Graphical Installer and Better Hardware Support"
categories: [reactos, windows, release]
tags: [reactos, open-source, windows-compatible, release, operating-system]
description: "ReactOS 0.4.16 arrives after 18 months of development with a new graphical installer, unified boot image, HD audio support, a new ATA driver, and Wine 10 sync."
image: /assets/images/post-images/reactos/reactos-0416-release.webp
---

**The** ReactOS Team has announced the release of ReactOS 0.4.16, arriving after about 18 months of active development. This release closes 381 open issues, includes 2,808 commits, and resolves a bug that was first reported back in 2009. The update touches nearly every layer of the system — from the installer to the storage stack — and brings ReactOS closer to running modern Windows applications and hardware drivers.

![ReactOS 0.4.16 graphical installer running on the unified boot image](/assets/images/post-images/reactos/reactos-0416-release.webp)

## Graphical Installer and a Unified Boot Image

The most visible change in this release is the new graphical installer. Previously, ReactOS shipped two separate images — a LiveCD for testing in read-only mode and a BootCD for text-based installation. ReactOS 0.4.16 combines both into a single image with a proper graphical setup wizard.

Hermès Bélusca-Maïto led this effort, which included work on partition management UI, syncing `setupapi` from Wine, and stabilizing the full graphical setup flow. Users can now boot ReactOS, try it live, and install it — all from the same media, similar to how most Linux distributions have worked for years.

## Video and Graphics Fixes

ReactOS has long struggled with GPU compatibility, particularly with Nvidia cards. Justin Miller tracked down a kernel-level issue where the system was running out of system page table entries (PTEs) when loading third-party drivers. This caused a noticeable performance slowdown on Nvidia hardware. Adjusting the memory layout in the memory manager resolved the issue.

For AMD users, an OpenGL rendering bug caused blank windows in some cases. This was fixed by rewriting the `ExtEscape` function, drawing on earlier work by the late core developer James Tabor. The release also builds on the multi-monitor foundation laid during the 0.4.15 cycle.

## HD Audio Support

Prior to this release, ReactOS lacked full HD audio support. The old `hdaudbus.sys` implementation was unfinished and caused frequent system crashes when installing HD audio drivers.

Core developer Oleg Dubinskiy replaced it by importing `sklhdaudbus`, an open-source HD audio bus driver. HD audio controllers compatible with Windows XP and Server 2003 should now work out of the box, including hardware from AMD, IDT, Nvidia, Realtek, and SigmaTel. Volume and balance settings now persist across reboots as well.

## New ATA Storage Driver

Since 2009, ReactOS used the UniATA storage driver. While it enabled SATA and AHCI support at the time, UniATA became a source of slow boot times and the dreaded `INACCESSIBLE_BOOT_DEVICE (0x7B)` bugcheck on many modern systems.

ReactOS 0.4.16 replaces it with a new ATA driver written by Dmitry Borisov. This driver enables ReactOS to boot in more environments, including inside Hyper-V Generation 1. Doug Lyons also fixed the FAT `chkdsk` routines that had broken after the Microsoft FastFAT driver was adopted in 2021, and Mark Jansen added a disk cleanup utility compatible with Windows disk cleanup extensions.

## Networking Improvements

The release adds asynchronous connection support, which improves both performance and compatibility. Many Windows applications assume these async networking APIs are always available. ReactOS 0.4.16 also gains Internet access under Microsoft Virtual PC 2007 and Hyper-V Generation 1, thanks to the DC21X4 network adapter driver introduced during the 0.4.15 cycle.

## Server Core Installation Type

ReactOS now supports a Server Core installation type, contributed by Carl Bialorucki. Like Windows Server Core (introduced with Windows Server 2008), this mode disables the graphical Explorer shell while keeping the full Win32 subsystem running. It is aimed at server and embedded use cases where a full desktop is not needed.

## Wine 10 Sync and 16-bit App Support

ReactOS uses a fork of Wine to implement Windows APIs. For years, the project stayed close to Wine 2.x and 3.x due to compatibility concerns. That restriction has since been dropped, and this release includes significant progress toward syncing the Wine fork with Wine 10.0. Full parity with Wine 11.0 is expected to be much easier now.

For the first time, ReactOS release images include WineVDM, which improves compatibility with 16-bit Windows applications.

If you want to experiment with Windows Vista and newer application support, the project provides build instructions using the `-DDLL_EXPORT_VERSION` flag, though the default release image still targets Windows Server 2003 exports.

## Download ReactOS 0.4.16

This release follows [ReactOS 0.4.15](/reactos-0415-release/), which was dedicated to Eric Kohl on his 26th anniversary with the project and brought major Plug and Play improvements and better audio support. If you are new to the project, the [ReactOS distribution page](/distribution/reactos) has an overview of what ReactOS is and what it aims to do.

You can download ReactOS 0.4.16 from the [official ReactOS website](https://reactos.org/project-news/reactos-0416-released/). The project also accepts donations to fund testing infrastructure and development contracts.

ReactOS remains alpha-quality software and is recommended for testing and evaluation rather than production use.
