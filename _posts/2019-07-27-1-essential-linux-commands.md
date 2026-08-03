---
title: "Essential Linux commands every user should know"
layout: post
categories: tutorial linux
tags: tutorial linux
image: "/assets/images/post-images/linux-command-line.png"
last_modified_at: 2026-08-03
---

The Linux command line looks intimidating at first, but a handful of commands cover most of what you'll do day to day: finding files, searching text, checking what's running, and editing files over SSH. This guide walks through those commands with practical examples you can try right away.

![Linux Terminal Preview](/assets/images/post-images/linux-command-line.png)
*Image is captured on Linux Mint 19.2 Xfce Edition with cmatrix command running*

## 1. Navigating and listing files

- `pwd` - print the current working directory
- `ls -la` - list all files (including hidden ones) with details like permissions, size, and modified date
- `cd <path>` - change directory (`cd ..` goes up one level, `cd ~` goes home)

```sh
$ pwd
/home/user/projects

$ ls -la
drwxr-xr-x  4 user user 4096 Aug  3 10:00 .
-rw-r--r--  1 user user  220 Aug  3 10:00 notes.txt
```

## 2. Finding a file

The easiest way to locate a file by name is the `find` command.

```sh
$ find [directory] -name "file name pattern"
$ find [directory] -iregex "pattern"
```

For example, to find every `.log` file under `/var/log`:

```sh
$ find /var/log -name "*.log"
```

`find` also accepts flags that control whether it follows symbolic links while searching:
- `-P` - never follow symbolic links (default behavior)
- `-L` - follow symbolic links
- `-H` - never follow symbolic links, except for the directories/files given directly on the command line

## 3. Searching for text inside files

The `grep` command finds a piece of text inside one or more files. By default, `grep` prints each matching line.

```sh
$ grep "text" "file name pattern"
```

To search recursively through every file in a directory, add `-r`:

```sh
$ grep -r "text" "directory name"
```

Example: find every file that mentions "TODO" inside the current project, with line numbers.

```sh
$ grep -rn "TODO" .
./src/app.js:42:// TODO: handle empty response
```

Useful flags for `grep`:
- `-G` - use basic regular expressions (the default)
- `-i` - ignore case
- `-v` - invert match, show lines that do **not** match
- `-c` - print a count of matching lines instead of the lines themselves
- `-H` - print the filename alongside each match
- `-n` - show the line number of each match

## 4. Checking running processes

- `ps aux` - list all running processes
- `top` or `htop` - live view of processes sorted by CPU/memory usage
- `kill <pid>` - stop a process by its process ID
- `kill -9 <pid>` - force-kill a process that won't respond to a normal `kill`

```sh
$ ps aux | grep firefox
user      2345  2.3  4.1  ...  firefox
```

## 5. File permissions

Linux permissions are shown as a 10-character string, e.g. `-rwxr-xr--`, representing owner/group/other read, write, and execute access.

- `chmod 755 file` - set owner to read/write/execute, group and others to read/execute
- `chmod +x file` - make a file executable
- `chown user:group file` - change the file's owner and group

## 6. Redirection and pipes

- `command > file` - write command output to a file, overwriting it
- `command >> file` - append command output to a file
- `command1 | command2` - send the output of `command1` as input to `command2`

```sh
$ ls -la | grep ".conf"
```

## 7. VI editor commands

**VI** (or its modern successor `vim`) is the text editor most likely to be preinstalled on any Linux server. If you're looking for a more modern terminal app to run these commands in, [Tabby](/software/tabby/) is worth a look. It has two modes: **insert mode**, for typing text, and **normal mode**, for issuing commands like the ones below. Press `Esc` to leave insert mode and return to normal mode before using these shortcuts.

- `a` - append text after cursor
- `i` - insert text before cursor
- `cw` - delete from the cursor to the end of the word and switch to insert mode
- `cc` - delete the current line and switch to insert mode
- `dd` - delete the current line
- `:w` - save
- `:q` - exit
- `:q!` - exit without saving
- `:wq` - save and exit
- `/string` - search forward for `string`
- `?string` - search backward for `string`
- `n` - jump to the next search match
- `N` - jump to the previous search match
- `G` - go to the last line
- `nG` - go to line `n`
- `j` - move cursor down
- `k` - move cursor up
- `^` - jump to the beginning of the line
- `$` - jump to the end of the line
- `w` - jump one word forward
- `b` - jump one word backward
- `x` - delete the character under the cursor
- `u` - undo the last change
- `yy` - copy (yank) the current line
- `p` - paste the copied text after the cursor
- `:s/old_text/new_text` - find and replace on the current line

---
This list covers the commands you'll reach for most often, but it isn't exhaustive. If there's a command you use regularly that isn't listed here, let us know in the comments and we'll add it.
