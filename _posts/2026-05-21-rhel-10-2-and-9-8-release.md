---
layout: post
title: "RHEL 10.2 and 9.8 Released with AI Tools and Post-Quantum Security"
categories: [redhat, release, enterprise-linux]
tags: [rhel, rhel-10, rhel-9, release, enterprise-linux, post-quantum, ai, bootc]
description: "Red Hat Enterprise Linux 10.2 and 9.8 are now available with AI-powered CLI tools, updated developer runtimes, image mode enhancements, and post-quantum cryptography."
image: /assets/images/post-images/rhel/rhel-10-2-release.webp
---

**Red Hat** has released RHEL 10.2 and 9.8, the latest minor updates to its enterprise Linux platform. Both releases arrived on May 20, 2026, and deliver improvements across four areas: developer tools, operational management, security, and upgrade reliability.

![Featured illustration for RHEL 10.2 and 9.8 release showing AI-powered CLI tools, enterprise Linux infrastructure, image mode improvements, and post-quantum security themes.](/assets/images/post-images/rhel/rhel-10-2-release.webp)

[Red Hat Enterprise Linux](https://www.opensourcefeed.org/distribution/redhat) is the commercial Linux platform widely used in enterprise data centers and hybrid cloud environments. Both the 10.x and 9.x release tracks remain in active support, receiving ongoing feature updates through minor releases like these.

## AI-Enhanced Command Line

RHEL 10.2 and 9.8 introduce `goose`, an optional command-line AI assistant available in the extensions repository. It connects to the same backend as the existing RHEL command-line assistant but adds streaming responses and a path toward integration with a new Model Context Protocol (MCP) server for RHEL, currently in developer preview. The built-in command-line assistant also gains color output, making it easier to visually separate commands, scripts, and explanations in terminal output.

## Updated Developer Toolsets

Both releases refresh a wide range of language runtimes and developer tools:

- **Go 1.26** brings the Green Tea garbage collector, reducing tail latency and adding HPKE support.
- **Python 3.14** adds live syntax highlighting, smarter autocompletion, and an extended type system.
- **Ruby 4.0** ships the new ZJIT compiler, delivering performance gains for Ruby applications.
- **PostgreSQL 18** adds asynchronous I/O and UUIDv7 support.
- **MariaDB 11.8** introduces a VECTOR datatype aimed at AI/ML workloads.
- **OpenJDK 25**, **PHP 8.4**, **Rust 1.92**, **LLVM 21**, and **Git 2.51** round out the update, each with performance or developer experience improvements.

## Image Mode Improvements

RHEL's image mode, based on bootc, gets several operational improvements. A new `bootc` option lets administrators pre-download OS updates to a fleet without triggering immediate reboots, supporting planned maintenance windows. The new Bootable Containers and Virtualization Kit (BCVK) simplifies testing by automating the path from a local Podman container build to an ephemeral VM test environment. Logically bound images allow organizations to manage diverse system configurations from a single base image, cutting down the number of distinct images to maintain. The RHEL image builder CLI is redesigned to work without a continuously running service, making it better suited to CI/CD pipelines.

## Post-Quantum Security

Red Hat Certificate System 11.0, released alongside RHEL, integrates NIST-standardized ML-DSA signatures to support post-quantum cryptography (PQC). This addresses the risk of "harvest now, decrypt later" attacks — where encrypted data collected today could be decrypted once quantum computers become capable enough. Certificate System 11.0 also introduces zero-touch provisioning for certificate issuance using one-time passwords, automating a process that would otherwise require significant manual effort at scale. Certificate lifespans are projected to shrink to as low as 47 days by 2029, making automation important for organizations managing large fleets.

RHEL 10.2 also introduces sealed images (technology preview), enabling customer-controlled cryptographic integrity for the OS. Organizations can use their own secure boot keys to sign images and configure systems to trust only internally certified builds.

## Simplified Upgrades

Leapp, the RHEL in-place upgrade tool, now supports conversion and major-version upgrades in a single command, removing a previous two-step requirement. Red Hat also released Ansible Certified Content that automates common pre-upgrade issues identified by Leapp, packaging Red Hat's accumulated upgrade knowledge for repeatable automated use. [Fedora Linux](https://www.opensourcefeed.org/distribution/fedora), which serves as the upstream source for RHEL, typically previews features that eventually flow into RHEL minor releases.

For the full details, see the [official RHEL 10.2 and 9.8 announcement](https://www.redhat.com/en/blog/rhel-102-and-98-intelligent-evolution-enterprise-linux). Downloads and release notes are available on the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/479).