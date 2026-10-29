---
layout: distribution
uid: kali
title: 'Kali Linux'
Category: Distribution
permalink: /distribution/kali
logo: kali-logo.png
preview: Kali_Linux.jpg
image: /assets/images/preview/Kali_Linux.jpg
type: Linux
home_page: https://www.kali.org/
blog: https://kali.org/blog/
desktops: [xfce, gnome, plasma]   # TODO: add /desktop/xfce page if it does not exist yet
base: [debian]
tagline: Penetration testing and digital forensics distribution
last_modified_at: 2026-10-29

description: "Kali Linux is a Debian-based Linux distribution for penetration testing and digital forensics. Release news, new tools, and updates."

releases:
  Kali Linux 2026.3: /kali-linux-2026-3-release/
  Kali Linux 2026.2: /kali-linux-2026-2-released/
  Kali Linux 2026.1: /kali-linux-2026-1-release/
  Kali Linux 2025.4: /kali-linux-2025-4-released/
  Kali Linux 2025.3: /kali-linux-2025-3-release/
  Kali Linux 2025.2: /kali-linux-2025-2-release/
  Kali Linux 2024.4: /kali-2024.4-release/
  Kali Linux 2024.3: /kali-linux-20243-release/
  Kali Linux 2024.2: /kali-linux-20242/
  Kali Linux 2024.1: /kali-linux-20241-release/
  Kali Linux 2023.3: /kali-202303-release/
  Kali Linux 2022.4: /kali-2022.4-release/
  Kali Linux 2021.4: "/kali-linux-20214-has-been-released/"
  Kali Linux 2021.3: "/kali-2021.3-release/"
  Kali Linux 2021.2: "https://www.kali.org/blog/kali-linux-2021-2-release/"
  Kali Linux 2021.1: "/kali-2021.1-release/"
  Kali Linux 2020.4: "/kalilinux-2020.4-release/"
  Kali Linux 2020.3: "/kali-2020.3-release/"
  Kali Linux 2020.2: "/kali-2020.2-release/"
  Kali Linux 2019.4: "/1-kali-2019.4-screens/"
  Kali Linux 2019.03: "/1-kali-linux-2019.03-release/"
  Kali Linux 2018.3: "/00-kali-linux-2018.03-released-with-linux-4.17/"
  Kali Linux 2018.1: "https://open-source-feed.blogspot.com/2018/02/kali-linux-20181-released-with-amd.html"
  Kali Linux 2017.03: "/kali-linux-201703-released/"
  Kali Linux 2017.02: "https://www.kali.org/news/kali-linux-2017-2-release/"
  Kali Linux 2017.01: "https://open-source-feed.blogspot.com/2017/04/kali-linux-20171-released-with-cool.html"

screenshots:
  # TODO: add a screenshot post for a newer release (2024 or later)
  Kali Linux 2021.4: "/kali-linux-20214-has-been-released/"
  Kali Linux 2021.3: "/kali-2021.3-release/"
  Kali Linux 2020.2: "/kali-2020.2-release/"
  Kali Linux 2019.4: "/1-kali-2019.4-screens/"

related:
  Parrot Security OS: https://www.parrotsec.org/
  BlackArch Linux: https://blackarch.org/

faq:
  "What is Kali Linux used for?": "Kali Linux is used for penetration testing, security research, digital forensics, and security training. It ships with a large set of tools for testing networks, web applications, wireless links, and passwords."
  "Is Kali Linux based on Debian?": "Yes. Kali Linux is built on Debian and follows its testing branch as a rolling distribution, with its own repositories and security tools on top."
  "Which desktop does Kali Linux use?": "Xfce is the default desktop. The installer also offers GNOME and KDE Plasma."
  "Is Kali Linux good for beginners?": "It is not a good first Linux distribution. Kali is built for security work, not daily desktop use. Learn Linux basics on Debian or Ubuntu first, then try Kali in a virtual machine."
  "Is it legal to use Kali Linux?": "Yes, the operating system is legal to download and use. Using its tools against systems you do not own or have written permission to test is illegal in most countries."
  "Is Kali Linux free?": "Yes. Kali Linux is free and open source, and you can download it from the official site."
---

**Kali Linux** is a free, Debian-based operating system built for penetration testing, security research, and digital forensics. It is the successor to BackTrack and is maintained by OffSec (formerly Offensive Security). Security teams use it to find weaknesses in networks and applications before attackers do.

This page collects every Kali Linux release story on OpenSourceFeed, plus a short guide to what Kali includes and who should use it.

## What comes with Kali Linux

Kali includes hundreds of security tools, grouped in the application menu by task. Typical examples:

- **Network scanning and analysis:** Nmap, Wireshark
- **Exploitation:** Metasploit Framework
- **Web application testing:** Burp Suite, sqlmap
- **Password attacks:** John the Ripper, Hashcat, Hydra
- **Wireless testing:** Aircrack-ng
- **Digital forensics:** Autopsy, Volatility

<!-- VERIFY: confirm each tool is still in the default or kali-linux-large metapackage -->

Each release adds new tools and updates existing ones, so check the release stories below for what changed.

## Ways to run Kali Linux

You can install Kali on a PC, run it as a live USB system, or use a ready-made virtual machine image. Kali also runs on ARM devices, in WSL on Windows, and in the cloud. Kali NetHunter brings the toolset to Android phones. Xfce is the default desktop, and the installer also offers [GNOME](/desktop/gnome) and [KDE Plasma](/desktop/plasma).

<!-- VERIFY: current list of images and platforms on kali.org/get-kali -->

For daily desktop use, a general-purpose system such as [Debian](/distribution/debian) is a better fit. Use the [Distro Finder](/distro-chooser/) to compare options.

## Who should use Kali Linux

Kali suits penetration testers, security students, and system administrators who test their own networks. It assumes you are comfortable with the Linux command line. If you are new to Linux, start with a beginner-friendly distribution and try Kali later in a virtual machine.

Many Kali tools can disrupt or damage systems. Use them only on systems you own or have written permission to test.

## Kali Linux release history

Kali follows a rolling model with a new snapshot roughly every quarter. The release table below links to our coverage of each version, from the 2017 releases to the current one.

<!-- VERIFY: confirm the quarterly snapshot cadence is still accurate -->

-----