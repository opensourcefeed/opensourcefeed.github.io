---
layout: post
title: "Ubuntu 26.10 Released: Linux 7.3, GNOME 51 and 10 Flavors"
categories: [ubuntu, linux, release]
tags: [ubuntu, ubuntu-26-10, stonking-stingray, gnome-51, linux-7-3, ubuntu-flavors]
description: "Ubuntu 26.10 Stonking Stingray is out with Linux 7.3, GNOME 51, 100% Rust coreutils, a Myna speech-to-text preview, and releases of all ten official flavors."
image: /assets/images/post-images/ubuntu/ubuntu-26-10-stonking-stingray-release.webp
---

**Canonical** released Ubuntu 26.10, code-named "Stonking Stingray", on October 15, 2026. It is an interim release with nine months of support, and it follows the [Ubuntu 26.04 LTS release](/ubuntu-26-04-resolute-raccoon-release/) from April. This version brings Linux 7.3, GNOME 51, a coreutils package that runs entirely on Rust, and a preview of local speech-to-text. The ten official community flavors shipped on the same day.

![Ubuntu 26.10 Stonking Stingray release](/assets/images/post-images/ubuntu/ubuntu-26-10-stonking-stingray-release.webp)

## What is new in Ubuntu 26.10

### Linux 7.3 and hardware support

Ubuntu 26.10 ships Linux 7.3. The kernel in the release images is 7.3.0-9.9, which Canonical built from 7.3-rc6, because the final upstream 7.3 release arrives after launch.

The kernel adds early support for Snapdragon X2 Elite laptops, including the Asus Zenbook A14 and the Lenovo Yoga Slim 7x Gen 11. It also enables upcoming AMD Zen 6 client platforms, ships SPDX software bills of materials for amd64 and arm64 kernels, and updates ZFS to 2.4.4. The NVIDIA 615 driver series replaces 595 and 610, and it ships only open kernel modules for Turing and newer GPUs.

Ubuntu 26.10 also adds official support for two RVA23 RISC-V platforms, the SpacemiT K3 boards and the SiFive BigSky. It comes with RISC-V desktop images and, according to [Phoronix](https://www.phoronix.com/news/Ubuntu-26.10-Released), install images tuned for amd64v3 CPUs.

### GNOME 51 and desktop changes

The desktop moves to GNOME 51. Many parts of the shell feel smoother, and the update makes several practical changes:

- Settings can rotate the screen automatically on devices with an accelerometer.
- Displays remember monitor brightness across reboots.
- Papers can add visual signatures to documents. These are annotations, not cryptographic proof.
- The Reduced Motion setting now covers more of the desktop.

For more on the upstream release, read our [GNOME 51 coverage](/gnome-51-a-coruna-release/).

App Center shows Snap and Debian package details in one view. It has a new Drivers page for graphics drivers, including NVIDIA branches, and it can install a codec for one-time playback when a media file needs it. Settings can also show whether your computer is a certified Ubuntu device.

Ubuntu 26.10 introduces Myna, a speech-to-text preview. You hold a key to dictate into the focused app, and the processing runs on your computer. Myna is opt-in and does not come preinstalled.

GNOME 51 removes WEP Wi-Fi support from Settings. WEP is an obsolete standard, so use a network with modern security.

### Security changes

The Rust coreutils migration is complete. The last GNU tools, `cp`, `mv` and `rm`, now come from the uutils project, so the default core utilities run on Rust. You can switch back to the GNU versions if you need to.

Other security changes include:

- Sequoia PGP enters the main archive, with `sq` and `sqv` as the planned counterparts to `gpg` and `gpgv`. The GnuPG tools stay available.
- OpenSSL 4 adds Encrypted Client Hello and wider QUIC support.
- Computers without a hardware root of trust can use TPM-backed full-disk encryption if you also set a PIN or passphrase.
- OpenSSH 10.5 comes in two source packages. The default build drops GSSAPI and Kerberos support, and a separate `openssh-gssapi` package keeps it.

### Developer toolchain

| Tool | Version |
|------|---------|
| GCC | 15.2.0 |
| LLVM | 22.1.8 |
| Rust | 1.97.1 |
| Go | 1.27 |
| Python | 3.14.7 |
| OpenJDK | 25.0.4 |
| .NET | 10.0.112 |
| Zig | 0.16 |

The release also uses systemd 261.3 and Mesa 26.2. OpenJDK 27 is available in the `openjdk-27` package.

### Server and enterprise updates

Ubuntu Server 26.10 updates MySQL to the 9.7 LTS line, HAProxy to 3.4.2, Valkey to 9.1 and Samba to 4.24.7. The authd service now supports Microsoft Entra ID password sign-in with multi-factor authentication on the desktop, in the terminal and over SSH.

## Official Ubuntu 26.10 flavors

All ten official flavors released with 26.10, and each gets nine months of maintenance.

| Flavor | Desktop environment |
|--------|---------------------|
| Kubuntu | KDE Plasma 6.7.5 |
| Xubuntu | Xfce 4.20 |
| Lubuntu | LXQt 2.4 |
| Edubuntu | GNOME 51 |
| Ubuntu Studio | KDE Plasma 6.7.5 |
| Ubuntu Budgie | Budgie 10.10.3 |
| Ubuntu Cinnamon | Cinnamon 6.6.9 |
| Ubuntu MATE | MATE |
| Ubuntu Unity | Unity 7.7 |
| Ubuntu Kylin | UKUI 4.20 |

### Kubuntu

Kubuntu 26.10 ships Plasma 6.7.5 with KDE Gear 26.08.1 and KDE Frameworks 6.29. The Wayland session is the default. Reports on the Kubuntu 26.10 beta say this is the last release that offers the Plasma X11 session as a separate install.

### Xubuntu

Xubuntu stays on Xfce 4.20 and adds stability and Wayland fixes. Xfce Terminal 1.2.0 and Ristretto 0.14.0 bring new features, and Xfce Screenshooter can now capture regions and full screens on Wayland. The graphical SSH agent is a known issue in this release.

### Lubuntu

Lubuntu 26.10 uses LXQt 2.4. Read our [LXQt 2.4 release post](/lxqt-2-4-0-release/) for the upstream changes.

### Edubuntu

Edubuntu 26.10 runs on GNOME 51, the same desktop version as Ubuntu.

### Ubuntu Studio

Ubuntu Studio 26.10 shares the Plasma 6.7.5 desktop with Kubuntu.

### Ubuntu Budgie

Ubuntu Budgie 26.10 focuses on Budgie Desktop 10.10.3. The team wrote a bridge that lets Budgie run on the Wayfire compositor, which you can test from its backports PPA. New features include a radio widget for internet radio stations, wind speed units in Budgie Weather, and wallpaper-of-the-day options.

### Ubuntu Cinnamon

Ubuntu Cinnamon 26.10 ships Cinnamon 6.6.9. The menu applet shows your avatar and app descriptions, hot corners work in fullscreen apps, and a new module manages Thunderbolt and USB 4 devices. Nemo can search by regular expression and pause file operations. Zoitechat replaces HexChat.

### Ubuntu MATE

Ubuntu MATE returns after it skipped the 26.04 LTS release. A new maintainer team produced this release. The team could not update every MATE package to the latest version, but the packages in the release are stable. Ubuntu MATE moves from `initramfs-tools` to `dracut`, drops `ifupdown` for `netplan`, and removes `gdebi` from the ISO because the current version is broken.

### Ubuntu Unity

Ubuntu Unity 26.10 stays on Unity 7.7 and focuses on maintenance. It includes the Lomiri Calculator, Files and Terminal apps by default, and it adds new wallpapers. The team plans to install Lomiri by default in a later release and to switch to Ayatana indicators in April 2027.

### Ubuntu Kylin

Ubuntu Kylin 26.10 keeps the UKUI 4.20 desktop and the Linux 7.3 kernel. The release focuses on bug fixes and maintenance for desktop components.

## Download and upgrade

Ubuntu 26.10 gets updates until July 2027. You can download it from the [Ubuntu website](https://ubuntu.com/download), and you can find each flavor's images on its own project site. Read the full [Ubuntu 26.10 release notes](https://documentation.ubuntu.com/release-notes/26.10/) and the [official announcement](https://discourse.ubuntu.com/t/ubuntu-26-10-stonking-stingray-released/89539) before you upgrade.

Users of Ubuntu 26.04 LTS see the upgrade only if they chose to be told about every new release. The upgrade may appear a few days after launch. Systems that use TPM-backed full-disk encryption cannot upgrade from 26.04 LTS at release, but Canonical expects to enable that during the 26.10 lifecycle.
