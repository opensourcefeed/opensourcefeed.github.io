---
layout: distribution
uid: dragonfly
title: 'DragonFly'
tagline: 'BSD with a unique direction'
Category: Distribution
type : BSD
permalink: /distribution/dragonfly
logo: dragonfly.png
preview: 
home_page: https://www.dragonflybsd.org/
base: freebsd
desktops: [awesome, cinnamon, fluxbox, jwm, plasma, lxde, mate, openbox, xfce]
purchase:
  OSDisc : "https://www.osdisc.com/products/dragonfly"

description: 
  DragonFly BSD an operating system makes use of same Unix ideals and APIs and shares code with other BSD distributions but takes it in a different direction.

releases:
  DragonFly 5.4.0: "/1-dragonfly-5.4.0-released/"
  DragonFly 5.0.0 : "https://www.dragonflybsd.org/release50"
  DragonFly BSD 4.4.3 : "https://open-source-feed.blogspot.com/2016/04/dragonflybsd-443-released.html"
  DragonFly BSD 4.4.1 : "https://open-source-feed.blogspot.com/2015/12/dragonflybsd-441-released.html"
---

**DragonFly BSD** is an operating system belonging to the family of BSD derived operating systems. It makes use of UNIX concepts and APIs used in other BSD derived operating system and is grown from same ancestor code base. However, it takes BSD in a completely different direction.

Following are some of the features that makes DragonFly BSD different from other BSD derived operating systems.
- Hammer, a modern high performance filesystem with built-in mirroring and historic access functionality.
- Virtual kernels provide the ability to run a full-blown kernel as a user process for the purpose of managing resources or for accelerated kernel development and debugging.
- The kernel uses several synchronization and locking mechanisms for SMP. Much of the work done since the project began has been in this area. A combination of intentional simplification of certain classes of locks to make more expansive subsystems less prone to deadlocks, and the rewriting of nearly all the original codebase using algorithms designed specifically with SMP in mind, has resulted in an extremely stable, high-performance kernel that is capable of efficiently using all CPU, memory, and I/O resources thrown at it.
- DragonFlyBSD has virtually no bottlenecks or lock contention in-kernel. Nearly all operations are able to run concurrently on any number of cpus.
- DragonFly is uniquely positioned to take advantage of the wide availability of affordable Solid Storage Devices (SSDs), by making use of swap space to cache filesystem data and meta-data.
- The DragonFly storage stack comprises robust, natively written AHCI and NVME drivers, stable device names via DEVFS and a partial implementation of Device Mapper for reliable volume management and encryption.
