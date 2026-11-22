---
layout: distribution
uid: backbox
title: 'BackBox Linux'
Category: Distribution
type : Linux
permalink: /distribution/backbox
logo: backbox.png
preview: backbox-preview.jpg
home_page: https://backbox.org/
desktops: [xfce]
base : [ubuntu]
description : Discover BackBox Linux, a lightweight, Ubuntu-based OS built for penetration testing and ethical hacking. Explore its curated security tools and key features.
tagline: Penetration testing distribution
last_modified_at: 2026-11-22

releases:
  BackBox Linux 10: /backbox-linux-10-release/
  BackBox Linux 7: "/backbox-7-release/"
  BackBox Linux 6: "/1-backbox-6.0-released-screenshots/"
  BackBox Linux 5.3: "https://blog.backbox.org/2019/02/18/backbox-linux-5-3-released/"

screenshots:
  BackBox Linux 7: "/backbox-7-release/"
  BackBox Linux 6: "/1-backbox-6.0-released-screenshots/"

related:
  Kali Linux: /distribution/kali
  Parrot Security OS: https://www.parrotsec.org/

faq:
  "What is BackBox Linux used for?": "BackBox Linux is used for penetration testing, vulnerability assessment, digital forensics, and security training. It ships with a curated set of tools for network, web application, and wireless testing."
  "Is BackBox Linux based on Ubuntu?": "Yes. BackBox is built on Ubuntu LTS. BackBox Linux 10 moved to an Ubuntu 26.04 LTS base with the Linux 7.0 kernel and Xfce 4.20."
  "Which desktop does BackBox Linux use?": "Xfce is the only desktop offered, chosen for its low memory and CPU overhead on modest hardware and virtual machines."
  "Is BackBox Linux free?": "Yes. BackBox is free, open-source software and can be downloaded from the official site."
  "Is it legal to use BackBox Linux?": "The operating system itself is legal to download and run. Using its tools against networks or systems you do not own or have written permission to test is illegal in most countries."
  "Is BackBox Linux good for beginners?": "It is better suited to users with some Linux and networking experience. Newcomers to security testing are better served starting with a general-purpose distribution and trying BackBox later in a virtual machine."
---

**BackBox Linux** is a free, open-source, Ubuntu-based Linux distribution built specifically for penetration testing, ethical hacking, and security assessments. First introduced in 2010 and maintained by the BackBox Team, it pairs a lean, fast **Xfce** desktop environment with a curated set of offensive and defensive security tools—prioritizing practical workflow organization, system speed, and Ubuntu compatibility over bloat. The current release, **BackBox Linux 10** (November 2026), runs on an **Ubuntu 26.04 LTS** base with the **Linux 7.0** kernel and **Xfce 4.20**; see the [BackBox Linux 10 release story](/backbox-linux-10-release/) for the full changelog.

## Why Security Professionals Use BackBox Linux

* **Lightweight Performance & Stability:** Built on Ubuntu LTS foundations, it keeps memory and CPU overhead low enough to run smoothly on modest hardware or virtual machines.
* **Curated, Non-Redundant Tooling:** Rather than dumping every tool imaginable into the menu, BackBox organizes essential utilities cleanly by task—covering reconnaissance, vulnerability analysis, web application testing, exploitation, binary inspection, and network forensics (including staples like Nmap, Metasploit Framework, Wireshark, sqlmap, hashcat, and ZAP, alongside newer additions such as ffuf, gobuster, and AFL++).
* **Familiar Ubuntu Ecosystem:** Because it follows standard Ubuntu/Debian packaging and repository conventions, analysts can easily install standard software, manage packages, or add custom tools without fighting an unfamiliar base OS.
* **Practical Security & Deployment Options:** The installer supports normal or minimal setups, full-disk encryption (LVM on LUKS) and ZFS, UEFI/Secure Boot hybrid ISOs, and live/VM workflows tailored for security testing.

## Common Use Cases and Who Should Use BackBox Linux

Security researchers, red/blue teamers, and IT administrators use BackBox Linux for authorized **network and infrastructure audits**, **web app and API security testing**, **vulnerability assessment**, **digital forensics**, and **hands-on cybersecurity training**. It suits penetration testers, security students, and sysadmins auditing their own infrastructure; its Ubuntu base makes it a gentler on-ramp than some other pentest distributions for anyone already comfortable with Debian/Ubuntu package management.

BackBox is not intended as a general-purpose daily desktop, and its tools can disrupt or damage systems if misused—use them only on networks and systems you own or have explicit written authorization to test.

## Getting BackBox Linux

BackBox is free to download as a live/installable ISO from the [official BackBox site](https://backbox.org/). It can run from a USB drive, inside a virtual machine, or installed to disk with full-disk encryption. BackBox is open source, with its project listings citing GPLv2/v3. <!-- VERIFY: confirm exact license wording directly on backbox.org rather than third-party project listings --> Compare it against other security-focused distributions like [Kali Linux](/distribution/kali) using the [Distro Finder](/distro-chooser/) if you're not sure which fits your workflow.