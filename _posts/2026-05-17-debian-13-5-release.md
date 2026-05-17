---
layout: post
title: "Debian 13.5 Released: 103 Security Fixes and 144 Bug Corrections"
categories: [debian, release]
tags: [debian, debian-13, trixie, release, security, linux]
description: "Debian 13.5, the fifth point release of Debian 13 Trixie, is out with 103 security updates and 144 bug fixes covering glibc, systemd, OpenSSH, Apache, and more."
image: /assets/images/post-images/debian/debian-13-5-release.webp
---

**The** Debian Project has released Debian 13.5, the fifth point release of Debian 13 "Trixie". Released on May 16, 2026, this update consolidates security patches and bug corrections accumulated since the previous point release.

![Debian 13.5 Trixie point release with the Debian swirl logo](/assets/images/post-images/debian/debian-13-5-release.webp)

Debian 13.5 is a point release, not a new version. It brings no new features. Instead, it rolls up fixes released individually over the past months, giving users clean installation media without needing a long post-install update run.

As the Debian Project notes in its [official release announcement](https://www.debian.org/News/2026/20260516), users who already update regularly from `security.debian.org` will find most of these fixes already applied.

## What's Fixed in Debian 13.5

In total, Debian 13.5 includes **103 security advisories** and **144 miscellaneous bug corrections**.

Some of the more significant fixes include:

- **glibc** — Addresses incorrect DNS response handling, invalid hostname returns, and an assertion failure.
- **systemd** — Updated to a new upstream stable release (257.13), with fixes for code execution flaws and an nspawn escape-to-host vulnerability.
- **OpenSSH** — Multiple fixes including a case where `scp` could unexpectedly mark transferred files as setuid/setgid, and a command execution flaw.
- **Apache** — Covers use-after-free, privilege escalation, NULL pointer dereference, and HTTP response splitting vulnerabilities.
- **bubblewrap** — Patches a privilege escalation issue (CVE-2026-41163).
- **nano** — Fixes an overly broad permissions issue (CVE-2026-6842).
- **sudo** — Patches a privilege escalation flaw (CVE-2026-35535).
- **X.Org Server** — Buffer re-use, out-of-bounds read, and use-after-free issues addressed.
- **Python 3.13** — Multiple header injection, denial of service, and validation bypass fixes.

The update also improves compatibility with Python 3.13 across several packages, and corrects an illegal instruction issue on RISC-V 64-bit in GRUB EFI code.

## Desktop Environments in Live Images

Fresh installation images for Debian 13.5 are available for the amd64, arm64, armhf, ppc64el, riscv64, and s390x architectures. Live images ship with several desktop options: GNOME 48, KDE Plasma 6.3.6, Xfce 4.20, Cinnamon 6.4.10, LXQt 2.1, MATE 1.26.1, and LXDE.

If you want a full picture of what changed when Trixie first arrived, the [Debian 13 Trixie release post on OpenSourceFeed](https://www.opensourcefeed.org/debian-13-trixie-released/) is a good starting point.

## How to Upgrade

Existing Trixie users do not need to reinstall. Simply run:

```bash
sudo apt update && sudo apt full-upgrade
```

Point the package manager at any Debian HTTP mirror. A full list of mirrors is at [debian.org/mirror/list](https://www.debian.org/mirror/list).

Alongside Debian 13.5, the project also released Debian 12.14 as an updated point release for the older "Bookworm" series, carrying 145 security fixes and 99 bug corrections.

For the complete list of changed packages, see the [Trixie ChangeLog](https://deb.debian.org/debian/dists/trixie/ChangeLog).