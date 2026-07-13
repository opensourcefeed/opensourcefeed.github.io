---
layout: post
title: "Debian 13.6 Released: 124 Fixes, 120 Security Updates"
categories: [debian, linux, release]
tags: [debian, debian-13, trixie, release, point-release]
description: "Debian 13.6 arrives as the sixth Trixie point release, fixing Secure Boot CA expiry, reverting geoip-database, and bundling 120 security updates."
image: /assets/images/post-images/debian/debian-13.6.jpg
---

**The** Debian Project has released Debian 13.6, the sixth point update to its stable "Trixie" series. The release lands on July 11, 2026, less than two months after Debian 13.5.

![Debian 13.6 release featuring 124 bug fixes, 120 security updates, and Secure Boot certificate updates.](/assets/images/post-images/debian/debian-13.6.webp)

## What a point release actually changes

A point release like 13.6 is not a new version of Debian 13. It only refreshes the packages on the installation media. If you already run Trixie and update regularly from security.debian.org, you will not need to download much — most of these fixes are already on your system. People who set up new machines benefit the most, since the updated ISOs save a long round of post-install patching.

There is no need to throw away existing Trixie install media. You can bring any Debian 13 system fully up to date by pointing your package manager at a current mirror and running the standard upgrade commands.

## Secure Boot certificate expiry

The most important change in 13.6 involves Secure Boot. The 2013 UEFI Secure Boot certificate authority that ships on most PCs and signs bootloaders has now expired. Debian has updated `fwupd` to upstream version 2.0.20, which can push the newer Certificate Authority, Key Exchange Key, and revocation database updates to your firmware. If a future `shim-signed` update relies on the new keys and your firmware never received them, your system could fail to boot with Secure Boot turned on. Anyone running Trixie with Secure Boot enabled should apply CA, KEK, and DBX updates from their hardware vendor, following the guidance on the [Debian wiki's Secure Boot page](https://wiki.debian.org/SecureBoot/CAChanges#What_should_I_do.3F).

## geoip-database reverted

For licensing reasons, the `geoip-database` package has been rolled back to a version from around December 2019. Newer GeoLite database releases no longer meet the Debian Free Software Guidelines and cannot be redistributed. If your applications depend on `geoip-database` for IP-to-location lookups, expect outdated allocation data, and consider getting a GeoLite license directly from MaxMind instead of relying on the Debian package.

## Notable package fixes

Debian 13.6 packs in 124 bug fixes and 120 security updates across the archive. A few packages stand out:

- **samba**, **postfix**, **qemu**, and **wireshark** all move to new upstream stable releases carrying their own batches of security fixes.
- **apache2** gets patches for use-after-free bugs, a cross-site scripting flaw, several buffer overflows, and denial-of-service issues.
- **curl** closes a long list of CVEs, including bearer-token redirect leaks, stale cookie leaks, and credential exposure across redirects.
- **python3.13** fixes an SSL/TLS crash, reference leaks, and several request-smuggling and path-traversal issues.
- **dolphin** patches a sandbox escape, and **rsync** rejects overly long HTTP proxy response lines tied to a recent CVE.

The full changelog, including every affected package and its Debian Security Advisory, is available on the [official Debian 13.6 announcement](https://www.debian.org/News/2026/20260711).

## Desktop environments and download

Fresh installation and live images ship with KDE Plasma 6.3.6, GNOME 48, Xfce 4.20, Cinnamon 6.4.10, LXQt 2.1, MATE 1.26.1, and LXDE 0.11.1, plus a new IceWM-based "Junior" edition. Alongside 13.6, Debian also released Debian 12.14 for the older "Bookworm" series with its own set of bug and security fixes.

If you're setting up a new system, grab the refreshed ISOs from the [Debian download page](https://www.debian.org/distrib/). If you already run [Debian 13 "Trixie"](https://www.opensourcefeed.org/debian-13-trixie-released/), a routine `apt full-upgrade` is all you need — there's no need to wait if you're coming from [Debian 13.5](https://www.opensourcefeed.org/debian-13-5-release/). For background on the distribution itself, see our [Debian overview page](https://www.opensourcefeed.org/distribution/debian).