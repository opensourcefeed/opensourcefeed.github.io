---
layout: post
title: "FreeBSD 14.4 Released: OpenSSH 10, OpenZFS 2.2.9, and More"
categories: [freebsd, bsd, release]
tags: [freebsd, freebsd-14, release, unix]
description: "FreeBSD 14.4-RELEASE is out with OpenSSH 10.0p2, OpenZFS 2.2.9, a new sndctl utility, improved jail support, and better cloud-init compatibility."
image: /assets/images/post-images/freebsd/freebsd-14.4.jpg
---

**FreeBSD 14.4-RELEASE** is now available. This is the fifth release on the 14-STABLE branch, sitting between 14.3-RELEASE and the upcoming 14.5-RELEASE. You can grab it from the [official FreeBSD mirrors](https://www.freebsd.org/releases/).

Users looking to move to the latest major version can refer to our [FreeBSD 15.0 release coverage](/freebsd-15-0-released/).

![FreeBSD 14.4 release](/assets/images/post-images/freebsd/freebsd-14.4.jpg)

Existing users can upgrade using `freebsd-update`, and source-based upgrades are supported via the instructions in `/usr/src/UPDATING`.

## What's New in FreeBSD 14.4?

### Security and Core Tools

OpenSSH has been updated to version 10.0p2. This update drops support for the DSA signature algorithm and switches the default key agreement to the post-quantum hybrid algorithm `mlkem768x25519-sha256`. The `sshd(8)` authentication phase now runs in a dedicated `sshd-auth` binary. OpenSSL moves to 3.0.16, and the `unbound(8)` DNS resolver lands at version 1.24.1, which addresses a cache-poisoning issue tracked as CVE-2025-11411.

Several security fixes are included since 14.3, covering vulnerabilities in `xz`, `libarchive`, OpenSSL, `ipfw`, `rtsold`, and jail isolation. Notably, two advisories address jail escape paths — one via `nullfs` and another via file descriptor exchange between jails.

### Userland Changes

A new `sndctl(8)` utility provides control over sound devices, similar to the existing `mixer(8)`.

The `jail(8)` subsystem gains `meta` and `env` parameters, letting administrators attach arbitrary metadata and environment data to jails. This is useful for tooling that manages jail state externally.

`freebsd-update(8)` now installs shared libraries in a fixed order (`libsys`, `libc`, `libthr`, then others) to avoid upgrade failures when moving from 14.x to 15.x.

`bsdinstall(8)` drops support for ZFS-on-MBR installations, which were broken and caused failures. It also now copies `loader.efi` to all ESPs in multi-volume ZFS setups for boot redundancy.

`swapon(8)` gains support for encrypted swap files using `md(4)` devices with an `.eli` suffix in `fstab(5)`.

The `mdo(1)` privilege-escalation utility now accepts more fine-grained control over user and group IDs in launched processes.

`newfs(8)` gets a `-u` flag to disable soft updates and soft updates journaling for UFS2 filesystems.

`sockstat(1)` now shows UDP-Lite endpoints by default.

### OpenZFS

OpenZFS has been updated to version 2.2.9. This release includes fixes to ARC shrinking behaviour, `zpool add` safety checks, zvol blk-mq synchronisation, and BRT range conversion math.

### Cloud and VM Improvements

The `nuageinit(7)` cloud initialisation tool received significant work. It now uses a fully compliant YAML parser, logs execution, and adds support for several cloud-init directives including `runcmd`, `packages`, `write_files`, `tzsetup`, and `doas`. Network configuration now supports `wakeonlan`, `set-name`, and `match.driver`. This is mostly relevant for users running FreeBSD on OpenStack or similar platforms.

### Wireless Networking

The `iwlwifi(4)` driver gains ACPI support, enabling regulatory features for 802.11ax and 802.11be. The net80211 subsystem now correctly handles VHT160 and VHT80P80 channel widths, which were previously broken with modern access points.

### Hardware and Drivers

The `ix(4)` and `ixv(4)` drivers add support for Intel Ethernet E610 hardware, enabling 2.5G, 5G, and 10G link speeds. The `nvme(4)` driver gains BAR5 support, which brings FreeBSD up on Google Compute Engine C4 instances.

A new 9P filesystem (`p9fs(4)`) is available for use with `bhyve(8)` virtio-9p devices, allowing guests to access host file shares. Raspberry Pi Zero 2W device tree support is now included in release SD card images.

### Package Management

The `pkg(7)` bootstrap utility now parses arguments the same way as `pkg(8)`. A side effect: `pkg -f bootstrap` no longer works — use `pkg bootstrap -f` instead.

### Contributed Software Updates

- `bc(1)` / `dc(1)`: 7.1.0
- `bmake(1)`: 20251111
- `less(1)`: 685
- `libarchive(3)`: 3.8.5
- `xz(1)`: 5.8.2
- `SQLite`: 3.50.4
- `expat`: 2.7.3
- `libucl(3)`: 0.9.2
- Time Zone database: 2025c
- PCI vendor database: 2026-02-10

### Fonts

The `gallant` console font now includes over 4,300 glyphs — Greek, Cyrillic, IPA, Zapf Dingbats, box drawing, and Powerline symbols among them. The `spleen` font is updated to 2.2.0 with missing characters added and better alignment for high-dpi displays.

### Deprecations to Note

The in-kernel MIDI sequencer is deprecated. The RIP routing daemon (`routed(8)`) is also marked for removal in a future release. Users relying on RIP should migrate to `bird` or `quagga` from ports. IPFW compatibility code for releases before FreeBSD 8 has been removed.

## Upgrading

Binary upgrades from earlier RELEASE versions are supported:

```sh
freebsd-update fetch
freebsd-update install
```

Back up all data and configuration files before upgrading. Check the [release errata](https://www.freebsd.org/releases/14.4R/errata/) for any issues discovered after release.

If you are considering a major version jump, see our [FreeBSD 15.0 release notes](/freebsd-15-0-released/).

Full release notes are available on the [FreeBSD website](https://www.freebsd.org/releases/14.4R/relnotes/).