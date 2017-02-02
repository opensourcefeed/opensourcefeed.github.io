---
layout: post
title: 'Ubuntu 16.04.2 LTS will be postponed till February 9, due to boot issues'
categories: ubuntu news
image: "/assets/images/post-images/ubuntu16042-banner.png"
---
**Mr** *Leann Ogasawara* of Ubuntu engineering team has requested the release team to postpone Ubuntu 16.04.2 LTS release till February 9. This was owing to some serious booting issues found in arm64 systems.

It is expected that, the resolution for currently detected issue will require pulling kernel leve changes and flash kernel. Eventhough this can be completed within the scheduled time, there won't be enough time available for testing which will raise a concern over stability of the release. Considering the seriousness of issue, *Mr Adam Cornard* from Ubuntu release engineering team has agreed to postpone the release till February 9th.

![Ubuntu 16.04.2 banner](/assets/images/post-images/ubuntu16042-banner.png)

You find these mail threads in Ubuntu [release mailing list](https://lists.ubuntu.com/archives/ubuntu-release/2017-January/004015.html).

<blockquote>
Hi Adam (and the Release Team),
<br/>
We would like to formally request an extension for 16.04.2's release.  We
have just identified a serious boot regression on arm64.  The resolution
looks to require landing changes to the kernel, flash-kernel, and possibly
d-i.  While we can likely physically get those changes into the archive in
time for the release, there would be next to no time to test this nor
provide appropriate regression testing on other platforms. We would be much
more comfortable giving that some proper testing before releasing and
therefore would like to request an additional extension for the point
release date.  Thoughts?  We will honor whatever guidance we receive from
you.
<br/>
Thanks,
Leann
<br/>
----
<br/>
I'm a big fan of caution when it comes to the bits that make people's
computers either boot or completely fail to, as it's pretty hard to fix
boot errors after shipping them.  So, yes, a delay for a week while all
this is landed and tested seems entirely reasonable to me.  Will push
the release to Feb 9 instead.
<br/>
... Adam
</blockquote>