---
title: "Essential GNU/Linux commands (initial draft)"
layout: post
categories: tutorial linux
tags: tutorial linux
image: "/assets/images/post-images/linux-command-line.png"
---

**This** is a quick reference for some commonly used GNU/Linux commands. This document will be updated over the time to include more commands.

![Linux Terminal Preview](/assets/images/post-images/linux-command-line.png)
*Image is captured on Linux Mint 19.2 Xfce Edition with cmatrix command running*

## 1. Search for a file
There are multiple ways to search for a file. The easiest way is to use find command.
```
$ find [directory] -name "file name pattern"
$ find [directory] -iregex "pattern"
```
There are some additional parameters that can be used with `find` command.
- P - Never follow symoblic links (default behavior)
- L - Follow symbolic links
- H - Never follow symbolic links, except for files/folders mentioned with command.

## 2. Searching for a text in files
The `grep` command can be used find a particular text in a set of files. By default, `grep` prints the matching line.
```
$ grep "text" "file name pattern"
```
Following options can be used with grep command.
- G - basic regular expression
- i - ignore case
- v - invert match, lines not matching with given pattern or text
- c - number of lines matching with given pattern
- H - print output with file name
- n - show line number

## 3. VI editor commands
**VI** is a command line text editor. It is the most commonly used editor in servers. Some important shortcuts in `vi` editor are listed below. All these commands should be provided in non-interactive mode, ie, after pressing escape and there by leaving edit mode.
- a - append text after cursor
- i - insert text before cursor
- cw - delete from current character to end of word and enable editing
- cc - delete current line and enable editing
- dd - delete current line
- :w - save
- :q - exit
- :q! - exit without save
- :wq - save and exit
- /string - search for string
- ?string - search for string backward
- n - next match for search query
- N - previous match for search query
- G - Goto last line
- nG - Goto nth line
- j - cursor move down
- k - cursor move up
- ^ - beginning of line
- $ - end of line
- w - one word forward
- b - one word backward
- x - delete character
- u - undo last change
- yy - copy to buffer
- p - paste buffer after cursor
- :s/old_text/new_text - find and replace


This is an incomplete list of essential GNU/Linux commands and the list will be updated over time. If you use a command regualrly and not listed here, please comment below so that we can update it here.

