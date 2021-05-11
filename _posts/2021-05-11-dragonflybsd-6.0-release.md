---
title: "DragonFly BSD 6.0 released"
layout: post
categories: dragonfly release
tags: dragonfly release
image: "/assets/images/post-images/dragonfly.png"
---

**The** DragonFly BSD team has announced the release of DragonFly 6.0, a successor of DragonFly 5.8 released in 2020. DragonFly BSD 6.0 brings a revamped VFS caching system, various filesystem updates including HAMMER2, and a long list of userland updates.

![DragonFly BSD 6.0 Preview](/assets/images/post-images/dragonfly.png)

Following are the major updates between DragonFly BSD 5.8 and 6.0 releases.
> - A lot of work on dsynth, for building packages.
- Many updates of contrib system software.
- HAMMER2 work continues, with updates from Tomohiro Kusumi.
- Major VM work for extent-based representation.
- Due to major changes to the VM system we had to remove the MAP_VPAGETABLE mmap() feature, and this also means that vkernels will not be supported in this release. Support may be re-added at a later time via HVM (but not in this release).

You may read the [official DragonFly 6.0 release notes](https://www.dragonflybsd.org/release60/) on the project's website.
