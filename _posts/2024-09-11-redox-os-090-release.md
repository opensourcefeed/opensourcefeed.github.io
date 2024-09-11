---
title: "Redox OS 0.9.0 Released: New Features and Major Improvements"
layout: post
categories: redox release
image: /assets/images/post-images/redix-0.9.0.jpg
description: "Redox OS 0.9.0 brings performance boosts, better compatibility, new features, and expanded hardware support, including ARM64 and VirtIO drivers."
---

**Redox OS** has released version 0.9.0, introducing new features, performance enhancements, and bug fixes. Redox OS is a micro-kernel-based operating system written in Rust and follows the core principles of Linux and BSD.

![Redox 0.9.0 featured image](/assets/images/post-images/redix-0.9.0.jpg)

## Key Improvements in Redox OS 0.9.0

### Performance and Stability Enhancements

> - Process and Thread Lifecycle Improvements: Enhanced lifecycle management and signaling, funded by NLnet, boost overall performance and stability.
- System Call and Context Switching: Faster system calls and context switching optimizes system performance.
- Memory Management: Upgrades include a new, faster p2buddy memory allocator and better virtual/physical memory handling.
- Filesystem and ABI Enhancements: Improved filesystem performance and progress towards a stable ABI for better system reliability.

### Expanded Compatibility and Portability

> - COSMIC Desktop Integration: Redox now includes COSMIC Files, Editor, and Terminal, enhancing the user experience.
- Portability of Linux/BSD Programs: Major improvements make it easier to run Linux and BSD software on Redox.
- Unix Path Format: Replaced the URI format with the Unix path format, increasing compatibility with POSIX/Linux libraries.

### Hardware and Software Support

> - Enhanced Bootloader and Driver Support: Improved bootloader compatibility and better PCI/PCIe driver stability.
- ARM64 Support: Progress on ARM64 support, including initial compatibility with Raspberry Pi 3B+.
- VirtIO Drivers: New VirtIO drivers enhance performance in virtual environments.

### Notable Software Ports

> - Simple HTTP Server: The first HTTP web server ported to Redox, along with support for Apache HTTP Server, RustPython, GNU Nano, and Helix editors.
- Rust Program Porting: Focused efforts on porting Rust applications, with many now running on Redox with minimal modification.

### Build System and Documentation Updates

> - Build System Improvements: Enhancements simplify developer workflows and improve the build process for greater efficiency.
- Expanded Documentation: New developer resources, including FAQs and guides, have been added to support porting efforts and community contributions.

For a [complete list of changes and improvements in Redox OS 0.9.0 release](https://www.redox-os.org/news/release-0.9.0/), see the official release announcement in the projects blog.

## Getting Redox OS 0.9.0

Redox OS 0.9.0 is available for free download from the Redox file server.

<a href="https://static.redox-os.org/img/x86_64/" class="download">Download Redox 0.9.0</a>