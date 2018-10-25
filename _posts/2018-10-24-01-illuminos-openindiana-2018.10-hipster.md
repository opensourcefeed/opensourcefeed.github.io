---
title: "Illumos based OpenIndiana Hipster 2018.10 released."
layout: post
categories: openindiana release
tags: openindiana hipster
image: "/assets/images/post-images/openindiana-banner.png"
---

**Mr**. *Alexander Pyhalov* of OpenIndiana project has announced the release of OpenIndiana Hipster 2018.10. It is a stable snapshot of the rolling operating system using *Illumos* kernel. This release includes numerous package updates and bug fixes.

![OpenIndiana Hipster Banner](/assets/images/post-images/openindiana-banner.png)

### What is OpenIndiana Hipster?
OpenIndiana Hipster is a rapid development branch of OpenIdiana, an operating system using the Illumos Kernel. The *Hipster* follows a rolling release model.

Illumos is a consolidated software which provides the essential operating system components like the file system, device drivers, core system libraries and other essential tools.

### What is new in Hipster 2018.10?
OpenIndiana Hipster comes with a set of updated applications. It also includes some security fixes for recently found vulnerabilities. The main changes in OpenIndiana Hipster 2018.10 are as follows.
- Mate desktop has been updated to version 1.20.
- Python 3.5 was added. It includes a lot of modules in additions to the modules provided for 2.7 and 3.4
- The Image Packaging System has received a lot of updates from OmniOS CE IPS and Solaris IPS.
- KVM zone brand now allows you to manage your KVM VMs as illumos zones.
- Several new compilers were added, including GCC 8 (with patches necessary to build illumos) and Rust 1.29. GCC 6 and GCC 7 is still available.
- A lot of components were migrated to 64-bit-only, most newly added software defaults to 64-bit.
- Due to recent security fixes, compatibility with some Solaris applications was broken. This also includes compatibility for VirtualBox.
- GTK+2 was updated to 2.24.32. GTK+3 was updated to 3.24.1, Nimbus theme was rebased on to the top of the B00merang Project theme and updated to work with new GTK+.
- LightDM Gtk Greeter is updated to 2.0.5 and it uses Nimbus theme.
- VLC 2.2.8 and multimedia libraries were migrated to 64-bit; VLC 3.0.4 is still in testing.

For a [complete list of changes in OpenIndiana Hipster 2018.10](https://www.openindiana.org/2018/10/24/openindiana-hipster-2018-10-is-here/), read the release announcement and [release notes](https://wiki.openindiana.org/oi/2018.10+Release+notes) published on projects website.