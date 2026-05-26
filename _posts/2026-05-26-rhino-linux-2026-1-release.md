---
layout: post
title: "Rhino Linux 2026.1 Brings Lomiri to Desktop and ARM64"
categories: [rhino-linux, ubuntu, release]
tags: [rhino-linux, lomiri, pacstall, rolling-release, ubports, ubuntu]
description: "Rhino Linux 2026.1 brings Lomiri desktop images for x86_64 and ARM64, Pacstall 6.4.x updates, and Linux kernel 7.0.9 for generic systems."
image: /assets/images/post-images/rhino-linux/rhino-linux-2026-1.webp
---

**The** Rhino Linux team has announced the 2026.1 snapshot release, the first of the year for this Ubuntu-based rolling-release distribution. The headline addition is Lomiri — the convergent desktop environment from the UBports project — now available on generic x86_64 and ARM64 ISO images.

Rhino Linux is a community-maintained distribution based on Ubuntu's development branch, built around the [Pacstall](https://pacstall.dev/) package manager and the Xfce-based Unicorn desktop environment. It follows a rolling-release model, so existing users can update in place without reinstalling.

![Rhino Linux 2026.1 with Lomiri on x86_64 and ARM64](/assets/images/post-images/rhino-linux/rhino-linux-2026-1.webp)

## Lomiri Comes to x86_64 and ARM64

The biggest change in 2026.1 is the launch of generic ISO images with Lomiri as a desktop environment option. Previously, Lomiri was only available for mobile hardware such as PINE64 devices. Users installing Rhino Linux on standard x86_64 or ARM64 machines can now select Lomiri from the downloads page alongside the familiar Unicorn desktop.

Lomiri originated as Canonical's Unity 8 shell, designed for Ubuntu Touch. After Canonical ended that project, the UBports community took over development. It is built for convergence — the same interface adapts across phones, tablets, and conventional desktops. Rhino Linux has been collaborating with UBports since late 2025 to upstream patches and extend Lomiri's reach beyond mobile hardware.

The team notes that Lomiri on generic systems is still an evolving experience, and work with UBports continues. This release builds on the same Linux 7.0 kernel generation that [Ubuntu 26.04 LTS adopted](/ubuntu-26-04-resolute-raccoon-release/). Fans of Xfce-based Ubuntu derivatives may also be interested in [Xubuntu 25.10's Xfce 4.20 improvements](/xubuntu-25-10-release/).

## Pacstall 6.4.x Updates

Pacstall, the AUR-inspired package manager at the heart of Rhino Linux, received notable updates in this cycle. The 6.4.x series introduces two new internal variables — `DNUM` and `CDNUM` — alongside `PACSTALL_XTRACEFD` and `PACSTALL_XTRACEFDLOG` environment variables for better debugging. Scripts can now export `KVER` to pre- and post-install hooks. The release also includes bug fixes, internal code cleanups, and translation updates. The full changelog is on the [Pacstall releases page](https://github.com/pacstall/pacstall/releases/tag/6.4.0).

## Kernel Versions by Hardware

Kernel versions vary by target hardware:

| Image | Kernel |
|---|---|
| Generic (x86_64/ARM64) | 7.0.9-generic |
| PinePhone & PineTab | 6.18.32-sunxi |
| PinePhone Pro | 6.18.32-rockchip |
| PineTab2 | 6.9.0-okpine |
| Raspberry Pi | 7.0.0-raspi |

## Download

The 2026.1 ISO images are available from the [official Rhino Linux website](https://rhinolinux.org). Existing users do not need to reinstall — running `sudo apt update && sudo apt full-upgrade` or using the Pacstall package manager is sufficient to stay current. For full release details, see the [official announcement](https://blog.rhinolinux.org/news-26).