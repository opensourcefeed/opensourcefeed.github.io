---
layout: post
title: Kali Linux 2025.3 Released with Vagrant Updates, Nexmon Support, and New Security Tools
categories: kali security
description: Kali Linux 2025.3 introduces updates to Vagrant, Nexmon support for Raspberry Pi, and 10 new security tools. Learn about the latest features and enhancements in this open-source security distribution.
keywords: Kali Linux, 2025.3, open-source, security tools, Vagrant, Nexmon, Raspberry Pi, NetHunter
image: /assets/images/post-images/kali/2025.3.webp
---

**Kali Linux 2025.3**, the third release of 2025, is now available, bringing updates and new features for security researchers and penetration testers. This open-source distribution continues to evolve with enhancements to virtualization, wireless capabilities, and a set of new tools.

![Kali Linux 2025.3 featured image](/assets/images/post-images/kali/2025.3.webp)

## Enhanced Virtualization with Packer and Vagrant

The release includes updates to HashiCorp’s Packer and Vagrant, tools used for creating and managing virtual machines (VMs). Kali has transitioned from using Packer to DebOS for generating Vagrant VMs, streamlining the process and addressing challenges like building Hyper-V images on Linux. This change improves efficiency for users setting up Kali in virtualized environments.

For further details, refer to the Kali blog post, *Kali Vagrant Rebuilt: Out With Packer, In With DebOS*.

## Nexmon Support for Wireless Testing

Kali Linux 2025.3 reintroduces Nexmon support, enabling monitor mode and packet injection on Broadcom and Cypress wireless chips. This feature is particularly useful for devices like the Raspberry Pi, including the Raspberry Pi 5. Monitor mode allows packet sniffing, while injection mode supports sending custom raw packets, both critical for wireless security testing.

More information is available in the Kali blog post, *The Raspberry Pi’s Wi-Fi Glow-Up*.

## Discontinuation of ARMel Support

Following Debian’s lead, Kali Linux 2025.3 drops support for the ARMel architecture, used by legacy devices like the Raspberry Pi 1, Raspberry Pi Zero W, and ODROID-W. This decision aligns with Debian “trixie” 13 being the last release to support ARMel. The Kali team is redirecting resources to modern architectures like RISC-V to better serve the community.

## Improved VPN IP Panel Plugin for Xfce

The Xfce desktop environment in Kali now features an enhanced VPN IP panel plugin. Initially introduced in Kali 2024.1, the plugin now allows users to select specific network interfaces to monitor, improving flexibility for those managing multiple VPN connections. Users can configure this via the plugin’s preferences dialog.

## New Tools for Security Testing

Kali Linux 2025.3 adds 10 new tools to its repositories, enhancing its capabilities for security auditing and penetration testing:

- **Caido** and **Caido-cli**: A web security auditing toolkit (client and server components).
- **Detect It Easy (DiE)**: Identifies file types.
- **Gemini CLI**: Integrates Gemini AI into the terminal.
- **krbrelayx**: Supports Kerberos relaying and delegation abuse.
- **ligolo-mp**: Facilitates multiplayer pivoting for network testing.
- **llm-tools-nmap**: Combines large language models with nmap for network scanning.
- **mcp-kali-server**: Connects AI agents to Kali.
- **patchleaks**: Identifies and describes security fixes for validation or exploitation.
- **vwifi-dkms**: Manages “dummy” Wi-Fi networks.

The release also includes package updates and new libraries, with plans to adjust the default toolset in Kali 2025.4 via the `kali-linux-default` metapackage.

## Kali NetHunter Updates

Kali NetHunter, the mobile version of Kali, introduces support for the Samsung Galaxy S10, a budget-friendly device with internal monitor mode and injection on 2.4GHz and 5GHz bands. The CARsenal car hacking toolset has been updated with new features, including a Metasploit-Framework tab, a rewritten ICSim (now Simulator), and UI improvements. Experimental support for kernel module installation via Magisk is also included, along with various bug fixes and performance enhancements.

## ARM and Infrastructure Improvements

For ARM single-board computers, Kali recommends using 64-bit (`arm64`) images for Raspberry Pi devices, including the Raspberry Pi 5, while maintaining 32-bit (`armhf`) support for older devices like the Raspberry Pi 2. Kernel update issues have been resolved for smoother ARM performance.

The release also upgrades the tier-0 mirror (`archive.kali.org`) with increased bandwidth (from 500 Mb/s to 3 Gb/s) for faster package syncing. Six new mirrors in Asia and two sponsored by IONOS have been added to improve accessibility.

## How to Install or Upgrade to Kali Linux 2025.3

New users can download Kali Linux 2025.3 images from the [official website](https://www.kali.org/). Weekly builds are available for those wanting the latest packages. Existing users can upgrade with the following commands:

```bash
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
sudo apt update && sudo apt -y full-upgrade
cp -vrbi /etc/skel/. ~/
[ -f /var/run/reboot-required ] && sudo reboot -f
```

Verify the update with:

```bash
grep VERSION /etc/os-release
```

This should display `VERSION="2025.3"`.

## Community Contributions and Documentation

Kali Linux 2025.3 benefits from community contributions, including new tools, bug fixes, and documentation updates. The Kali team encourages participation via their [bug tracker](https://www.kali.org/docs/community/submitting-issues-kali-bug-tracker/) and welcomes new mirrors to expand the network.

For a comprehensive list of changes, visit the [official Kali Linux 2025.3 release announcement](https://www.kali.org/blog/kali-linux-2025-3-release/).