---
layout: post
title: "CachyOS August 2026: Shelly Rewritten in Zig, Server Edition Preview"
categories: [cachyos, arch, release]
tags: [cachyos, arch-linux, shelly, zig, rust, package-manager, release]
description: "CachyOS August 2026 brings a Zig rewrite of the Shelly package manager, Rust-powered Cachy-Update and chwd-kernel, plus experimental Server Edition profiles."
image: /assets/images/post-images/cachyos/cachyos-august-2026-release.webp
---

**The** CachyOS team has published its August 2026 release, the fifth ISO of the year. This update is headlined by a full rewrite of Shelly, the default GUI package manager, and a wave of Rust-powered components across the system.

![CachyOS August 2026 release - Shelly package manager rewritten in Zig](/assets/images/post-images/cachyos/cachyos-august-2026-release.webp)

The [CachyOS April 2026 release](/cachyos-april-2026-release/) first introduced Shelly as the default package manager. This month's release takes it further: the entire application was rewritten from C# to Zig, dropping the managed runtime in favor of native binaries. The result is lower memory usage and faster startup times.

## Shelly Gets a Major Overhaul

The desktop app gained a first-run welcome screen, list and grid package browsing, and AUR PKGBUILD previews with live build output. A new Utilities section provides quick access to database sync, cache cleanup, and orphan removal — tasks that previously required a terminal.

The CLI was rebuilt with integrated repository and AUR search, combined update checks covering repositories, AUR, AppImages, and Flatpaks, plus TOML-based backup import and export. Flatpak support is no longer bundled by default and is now available as an optional `shelly-flatpak-backend` package.

## Rust Moves Into More Components

Cachy-Update, the system tray updater, was rebased onto Arch-Update v4.x and its applet rewritten in Rust. A new `--check --enable` option enables automated update checks and starts the tray in one command. The default check interval is now 6 hours, and tray pagination is configurable via `TrayUpdatesPerPage`.

The kernel-manager backend inside chwd was also rewritten from C++ to Rust and merged directly into `chwd-kernel`. On the hardware detection side, chwd now uses board name pattern matching for better handheld device identification, and Bulgarian localization was added.

## Experimental Server Edition Profiles

The CLI installer received fixes and refactoring, and now includes experimental installation profiles for a forthcoming Server Edition. This is the first sign that CachyOS is looking beyond desktops and gaming handhelds into server workloads — a notable shift for the project.

## Desktop and Installer Changes

The [CachyOS March 2026 release](/cachyos-march-2026-release/) introduced animated installer previews; this release continues that momentum. Hyprland installations now use `noctalia-greeter` instead of SDDM. Cinnamon switched from `lightdm-gtk-greeter` to `lightdm-slick-greeter`. GNOME gained `gvfs-dnssd` and COSMIC received `cosmic-monitor`.

New Noctalia variants for `mango` and `niri` window managers were added, alongside Noctalia v5 support for Hyprland dotfiles. The Nord KDE theme was updated for Plasma 6.7.

CachyOS-Welcome received a DNS rework so the speed-test based server ranking now correctly selects the fastest DNS server. The `cachyos-rate-mirrors` backend now queries the CachyOS mirrorlist API for mirror ranking, improving accuracy for regional and outdated mirrors. A new Tier 2 mirror in Hungary was also added.

## Updating

Existing users need no manual steps. A standard system update is all that is required:

```bash
sudo pacman -Syu
```

For more details and download links for the Desktop and Handheld editions, see the [official CachyOS August 2026 release announcement](https://cachyos.org/blog/2608-august-release/).