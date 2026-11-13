---
layout: distribution
uid: redhat
title: 'Red Hat Enterprise Linux'
Category: Distribution
type: Linux
permalink: /distribution/redhat
logo: redhat.png
preview: redhat.jpg
preview_caption: Red Hat Enterprise Linux (RHEL) with the GNOME desktop
image: /assets/images/preview/redhat.jpg
home_page: https://www.redhat.com/
desktops: [gnome]
base: Independent
tagline: Enterprise Linux platform for hybrid cloud and enterprise infrastructure
seo_title: "Red Hat Enterprise Linux (RHEL): Releases, Lifecycle & Download"
description: "Red Hat Enterprise Linux (RHEL) is Red Hat's enterprise Linux distribution. See latest releases, lifecycle, architectures and how to download it free."

releases:
  RHEL 10.3: /rhel-10-3-and-9-9-release/
  RHEL 9.9: /rhel-10-3-and-9-9-release/
  RHEL 10.2: /rhel-10-2-and-9-8-release/
  RHEL 9.8: /rhel-10-2-and-9-8-release/

stories:
  Fedora Linux 44 Released: /fedora-linux-44-release/
  Red Hat introduces ARM server support for Enterprise Linux: "https://www.redhat.com/en/blog/red-hat-introduces-arm-server-support-red-hat-enterprise-linux"
---

**Red Hat Enterprise Linux** (RHEL) is the commercial Linux distribution from Red Hat, built for servers, cloud infrastructure, virtualization and containers. Its main selling points are a ten-year support lifecycle, a certified hardware and software ecosystem, and a steady release cadence. The current branches are RHEL 10 and RHEL 9, with RHEL 8 still in maintenance.

## What is RHEL?

RHEL is a subscription product, but it is built from open-source software. Fedora is the community upstream where new features appear first. CentOS Stream sits between Fedora and RHEL as the upstream for upcoming RHEL minor releases. Red Hat then hardens, certifies and supports the result.

The distribution uses the RPM package format and the DNF package manager. Workstation installs ship with the [GNOME](/desktop/gnome) desktop, while most deployments run headless on servers or in the cloud. RHEL is also the base for Red Hat's wider stack, including OpenShift, Podman and Ansible.

## What's new in modern RHEL

Recent releases concentrate on:

- **Image mode (bootc):** build and update the OS as a container image.
- **AI tooling:** command-line assistants and an MCP server for RHEL (developer preview).
- **Security and compliance:** hardening profiles, post-quantum cryptography work and sealed images (technology preview).
- **Automation:** tighter integration with Ansible, including content that automates Leapp pre-upgrade fixes.
- **Containers and hybrid cloud:** Podman, OpenShift and certified cloud images.

For release-by-release detail, see our coverage of [RHEL 10.3 and 9.9](/rhel-10-3-and-9-9-release/) and [RHEL 10.2 and 9.8](/rhel-10-2-and-9-8-release/).

## Lifecycle and support

RHEL 8, 9 and 10 each get ten years of Full Support plus Maintenance Support, followed by an Extended Life Phase and optional paid extended support.

| Version | Maintenance support ends |
|---------|--------------------------|
| RHEL 10 | May 31, 2035 |
| RHEL 9  | May 31, 2032 |
| RHEL 8  | May 31, 2029 |

<!-- VERIFY: confirm dates against https://access.redhat.com/support/policy/updates/errata -->

RHEL 7 reached the end of its extended support in 2024 and RHEL 6 before it, so neither should be used for new deployments.

## Supported architectures

- x86_64
- ARM64 (aarch64)
- IBM Power
- IBM Z

## Is there a free version of RHEL?

Yes, with limits. Red Hat offers a no-cost Developer Subscription for individuals, intended for development and self-supported use rather than production. Sign up through the Red Hat Developer program, then download the ISO and register your system. <!-- VERIFY: current system limit per individual subscription and terms -->

If you want a RHEL-compatible system with no subscription at all, look at community rebuilds such as AlmaLinux and Rocky Linux, or [Oracle Linux](/distribution/oracle). Fedora is the community option if you want newer software.

## Download Red Hat Enterprise Linux

Get RHEL 10 or RHEL 9 from the [Red Hat Developer download page](https://developers.redhat.com/products/rhel/download). <!-- VERIFY: current official download URL --> A free Red Hat account is required. The full RHEL documentation is on the [Red Hat Customer Portal](https://docs.redhat.com/).