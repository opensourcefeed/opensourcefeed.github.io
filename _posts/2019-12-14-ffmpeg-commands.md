---
title: "FFmpeg quick reference"
layout: post
categories: tutorial
tags: tutorial ffmpeg
image: "/assets/images/post-images/ffmpg-man.png"
---


**FFmpeg** is a cross-platform compatible, multimedia framework to the record, convert, and stream audio and video. With a powerful command line-tool, FFmpeg makes it possible to process video and audio in batches. You can find [more about FFmpeg](https://www.ffmpeg.org/about.html) on the official website.

![FFmpeg preview in Linux Mint](/assets/images/post-images/ffmpg-man.png)

In this post, we try to demonstrate some quick use cases of FFmpeg. This is an incomplete list and will be updated on the go.

## Converting video from one format to another.
The following command illustrates how we can convert a video file one format to another. During the conversion, we may keep the audio and video codecs the same or change.
```sh
ffmpeg -i <input file> -codec <output-codec> <output-file>
# or if want to change both audio and video codec
ffmpeg -i <input-file> -acodec <output audio> -vcodec <output video> <output-file>

# for example for converting from mkv to mp4
ffmpeg -i input.mkv -codec copy output.mp4
```

Here, if we want to retain the input file codecs, then can provide the value as `copy`. Otherwise can specify the codec name. A complete list of supported codecs can be retrieved by running following command.
```sh
ffmpeg -codecs
```

## Clipping video with start time and end time
It is a common use case to cut/clip video by specifying start time and end time. The following command can be used for the same.
```sh
ffmpeg -i <input-file> -ss <start-time> -to <end-time> -c:v copy -c:a copy <output-file>
```
This command will retain the input audio and video codecs and clip the video from start time to end time. Both times will be specifified in seconds.milliseconds format. More [ffmpeg clipping options](https://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video) are listed in a StackExchange answer.

---
This is a in complete post. It will be updated as we come up with more scenarios that we use in day to day life. 

If you have any other common use case, please comment below. We'll update our aritcle accordingly.