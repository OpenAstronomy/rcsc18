---
interact_link: 01-bash/02-files-and-directories.ipynb
title: 'Files And Directories'
permalink: 'chapters/01-bash/02-files-and-directories'
previouschapter:
  url: chapters/01-bash/01-Introduction
  title: 'Introduction'
nextchapter:
  url: chapters/01-bash/03-working-with-files-and-directories
  title: 'Working With Files And Directories'
redirect_from:
  - 'chapters/01-bash/02-files-and-directories'
---

# Navigating Files and Directories


<section class="objectives panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-certificate"></span> </h2>
</div>


<div class="panel-body">

<p>Questions:</p>
<ul>
<li>"How can I move around on my computer?"</li>
<li>"How can I see what files and directories I have?"</li>
<li>"How can I specify the location of a file or directory on my computer?"</li>
</ul>
<p>Objectives:</p>
<ul>
<li>"Explain the similarities and differences between a file and a directory."</li>
<li>"Translate an absolute path into a relative path and vice versa."</li>
<li>"Construct absolute and relative paths that identify specific files and directories."</li>
<li>"Demonstrate the use of tab completion, and explain its advantages."</li>
</ul>

</div>

</section>


The part of the operating system responsible for managing files and directories 
is called the **file system**.
It organizes our data into files, which hold information, and directories (also called "folders"), which hold files or other directories.

Several commands are frequently used to create, inspect, rename, and delete files and directories.
To start exploring them, we'll go to our open shell window.

First let's find out where we are by running a command called `pwd`
(which stands for "print working directory"). Directories are like *places* - at any time
while we are using the shell we are in exactly one place, called
our **current working directory**. Commands mostly read and write files in the 
current working directory, i.e. "here", so knowing where you are before running
a command is important. `pwd` shows you where you are:


{:.input_area}
```bash
pwd
```

{:.output_stream}
```
/home/stuart/Git/shell-novice/_episodes

```

Here, the computer's response is `/Users/nelle`, which is Nelle's **home directory**.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Home Directory Variation</h2>
</div>


<div class="panel-body">

<p>The home directory path will look different on different operating systems.
On Linux it may look like <code>/home/nelle</code>, and on Windows it will be similar to <code>C:\Documents and Settings\nelle</code> or <code>C:\Users\nelle</code>.<br />
(Note that it may look slightly different for different versions of Windows.) In future examples, we've used Mac output as the default - Linux and Windows output may differ slightly, but should be generally similar.  </p>

</div>

</section>


To understand what a "home directory" is,
let's have a look at how the file system as a whole is organized.  For the
sake of this example, we'll be
illustrating the filesystem on our scientist Nelle's computer.  After this
illustration, you'll be learning commands to explore your own filesystem,
which will be constructed in a similar way, but not be exactly identical.  

On Nelle's computer, the filesystem looks like this:

![The File System](../fig/filesystem.svg)

At the top is the **root directory**
that holds everything else.
We refer to it using a slash character, `/`, on its own;
this is the leading slash in `/Users/nelle`.

Inside that directory are several other directories:
`bin` (which is where some built-in programs are stored),
`data` (for miscellaneous data files),
`Users` (where users' personal directories are located),
`tmp` (for temporary files that don't need to be stored long-term),
and so on.  

We know that our current working directory `/Users/nelle` is stored inside `/Users`
because `/Users` is the first part of its name.
Similarly,
we know that `/Users` is stored inside the root directory `/`
because its name begins with `/`.

## Slashes

Notice that there are two meanings for the `/` character.
When it appears at the front of a file or directory name,
it refers to the root directory. When it appears *inside* a name,
it's just a separator.


Underneath `/Users`,
we find one directory for each user with an account on Nelle's machine,
her colleagues the Mummy and Wolfman.  

![Home Directories](../fig/home-directories.svg)

The Mummy's files are stored in `/Users/imhotep`,
Wolfman's in `/Users/larry`,
and Nelle's in `/Users/nelle`.  Because Nelle is the user in our
examples here, this is why we get `/Users/nelle` as our home directory.  
Typically, when you open a new command prompt you will be in
your home directory to start.  

Now let's learn the command that will let us see the contents of our
own filesystem.  We can see what's in our home directory by running `ls`,
which stands for "listing":


{:.input_area}
```bash
ls
```

{:.output_stream}
```
01-intro.ipynb	  02-filedir.md     05-loop.md	  Untitled.ipynb
01-intro.md	  03-create.md	    06-script.md
02-filedir.ipynb  04-pipefilter.md  07-find.md

```

(Again, your results may be slightly different depending on your operating
system and how you have customized your filesystem.)

`ls` prints the names of the files and directories in the current directory. 
We can make its output more comprehensible by using the **flag** `-F`
(also known as a **switch** or an **option**) ,
which tells `ls` to add a marker to file and directory names to indicate what
they are. A trailing `/` indicates that this is a directory. Depending on your
settings, it might also use colors to indicate whether each entry is a file or 
directory.
You might recall that we used `ls -F` in an earlier example.


{:.input_area}
```bash
ls -F
```

{:.output_stream}
```
01-intro.ipynb	  02-filedir.md     05-loop.md	  Untitled.ipynb
01-intro.md	  03-create.md	    06-script.md
02-filedir.ipynb  04-pipefilter.md  07-find.md

```

### Getting help

`ls` has lots of other **flags**. There are two common ways to find out how 
to use a command and what flags it accepts:

1. We can pass a `--help` flag to the command, such as:


{:.input_area}
```bash
ls --help
```

{:.output_stream}
```
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                               e.g., '--block-size=M'; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                               modification of file status information);
                               with -l: show ctime and sort by name;
                               otherwise: sort by ctime, newest first
  -C                         list entries by columns
      --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                               if omitted), 'auto', or 'never'; more info below
  -d, --directory            list directories themselves, not their contents
  -D, --dired                generate output designed for Emacs' dired mode
  -f                         do not sort, enable -aU, disable -ls --color
  -F, --classify             append indicator (one of */=>@|) to entries
      --file-type            likewise, except do not append '*'
      --format=WORD          across -x, commas -m, horizontal -x, long -l,
                               single-column -1, verbose -l, vertical -C
      --full-time            like -l --time-style=full-iso
  -g                         like -l, but do not list owner
      --group-directories-first
                             group directories before files;
                               can be augmented with a --sort option, but any
                               use of --sort=none (-U) disables grouping
  -G, --no-group             in a long listing, don't print group names
  -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
      --si                   likewise, but use powers of 1000 not 1024
  -H, --dereference-command-line
                             follow symbolic links listed on the command line
      --dereference-command-line-symlink-to-dir
                             follow each command line symbolic link
                               that points to a directory
      --hide=PATTERN         do not list implied entries matching shell PATTERN
                               (overridden by -a or -A)
      --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                               (default if omitted), 'auto', or 'never'
      --indicator-style=WORD  append indicator with style WORD to entry names:
                               none (default), slash (-p),
                               file-type (--file-type), classify (-F)
  -i, --inode                print the index number of each file
  -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  -k, --kibibytes            default to 1024-byte blocks for disk usage;
                               used only with -s and per directory totals
  -l                         use a long listing format
  -L, --dereference          when showing file information for a symbolic
                               link, show information for the file the link
                               references rather than for the link itself
  -m                         fill width with a comma separated list of entries
  -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  -N, --literal              print entry names without quoting
  -o                         like -l, but do not list group information
  -p, --indicator-style=slash
                             append / indicator to directories
  -q, --hide-control-chars   print ? instead of nongraphic characters
      --show-control-chars   show nongraphic characters as-is (the default,
                               unless program is 'ls' and output is a terminal)
  -Q, --quote-name           enclose entry names in double quotes
      --quoting-style=WORD   use quoting style WORD for entry names:
                               literal, locale, shell, shell-always,
                               shell-escape, shell-escape-always, c, escape
                               (overrides QUOTING_STYLE environment variable)
  -r, --reverse              reverse order while sorting
  -R, --recursive            list subdirectories recursively
  -s, --size                 print the allocated size of each file, in blocks
  -S                         sort by file size, largest first
      --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                               time (-t), version (-v), extension (-X)
      --time=WORD            with -l, show time as WORD instead of default
                               modification time: atime or access or use (-u);
                               ctime or status (-c); also use specified time
                               as sort key if --sort=time (newest first)
      --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
  -t                         sort by modification time, newest first
  -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  -u                         with -lt: sort by, and show, access time;
                               with -l: show access time and sort by name;
                               otherwise: sort by access time, newest first
  -U                         do not sort; list entries in directory order
  -v                         natural sort of (version) numbers within text
  -w, --width=COLS           set output width to COLS.  0 means no limit
  -x                         list entries by lines instead of by columns
  -X                         sort alphabetically by entry extension
  -Z, --context              print any security context of each file
  -1                         list one file per line.  Avoid '\n' with -q or -b
      --help     display this help and exit
      --version  output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
Also the TIME_STYLE environment variable sets the default style to use.

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors command to set it.

Exit status:
 0  if OK,
 1  if minor problems (e.g., cannot access subdirectory),
 2  if serious trouble (e.g., cannot access command-line argument).

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/ls>
or available locally via: info '(coreutils) ls invocation'

```

2. We can read its manual with `man`, such as:


{:.input_area}
```bash
man ls
```

{:.output_stream}
```
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
              with -l, print the author of each file

       -b, --escape
              print C-style escapes for nongraphic characters

       --block-size=SIZE
              with  -l,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
              '--block-size=M'; see SIZE format below

       -B, --ignore-backups
              do not list implied entries ending with ~

       -c     with -lt: sort by, and show, ctime (time of last modification of
              file status information); with -l: show ctime and sort by  name;
              otherwise: sort by ctime, newest first

       -C     list entries by columns

       --color[=WHEN]
              colorize  the output; WHEN can be 'always' (default if omitted),
              'auto', or 'never'; more info below

       -d, --directory
              list directories themselves, not their contents

       -D, --dired
              generate output designed for Emacs' dired mode

       -f     do not sort, enable -aU, disable -ls --color

       -F, --classify
              append indicator (one of */=>@|) to entries

       --file-type
              likewise, except do not append '*'

       --format=WORD
              across -x, commas -m, horizontal -x, long -l, single-column  -1,
              verbose -l, vertical -C

       --full-time
              like -l --time-style=full-iso

       -g     like -l, but do not list owner

       --group-directories-first
              group directories before files;

              can   be  augmented  with  a  --sort  option,  but  any  use  of
              --sort=none (-U) disables grouping

       -G, --no-group
              in a long listing, don't print group names

       -h, --human-readable
              with -l and -s, print sizes like 1K 234M 2G etc.

       --si   likewise, but use powers of 1000 not 1024

       -H, --dereference-command-line
              follow symbolic links listed on the command line

       --dereference-command-line-symlink-to-dir
              follow each command line symbolic link

              that points to a directory

       --hide=PATTERN
              do not list implied entries matching shell  PATTERN  (overridden
              by -a or -A)

       --hyperlink[=WHEN]
              hyperlink file names; WHEN can be 'always' (default if omitted),
              'auto', or 'never'

       --indicator-style=WORD
              append indicator with style WORD to entry names: none (default),
              slash (-p), file-type (--file-type), classify (-F)

       -i, --inode
              print the index number of each file

       -I, --ignore=PATTERN
              do not list implied entries matching shell PATTERN

       -k, --kibibytes
              default  to  1024-byte  blocks for disk usage; used only with -s
              and per directory totals

       -l     use a long listing format

       -L, --dereference
              when showing file information for a symbolic link, show informa‐
              tion  for  the file the link references rather than for the link
              itself

       -m     fill width with a comma separated list of entries

       -n, --numeric-uid-gid
              like -l, but list numeric user and group IDs

       -N, --literal
              print entry names without quoting

       -o     like -l, but do not list group information

       -p, --indicator-style=slash
              append / indicator to directories

       -q, --hide-control-chars
              print ? instead of nongraphic characters

       --show-control-chars
              show nongraphic characters as-is (the default, unless program is
              'ls' and output is a terminal)

       -Q, --quote-name
              enclose entry names in double quotes

       --quoting-style=WORD
              use  quoting style WORD for entry names: literal, locale, shell,
              shell-always,  shell-escape,  shell-escape-always,   c,   escape
              (overrides QUOTING_STYLE environment variable)

       -r, --reverse
              reverse order while sorting

       -R, --recursive
              list subdirectories recursively

       -s, --size
              print the allocated size of each file, in blocks

       -S     sort by file size, largest first

       --sort=WORD
              sort  by  WORD instead of name: none (-U), size (-S), time (-t),
              version (-v), extension (-X)

       --time=WORD
              with -l, show time as WORD instead of default modification time:
              atime  or  access  or  use  (-u); ctime or status (-c); also use
              specified time as sort key if --sort=time (newest first)

       --time-style=TIME_STYLE
              time/date format with -l; see TIME_STYLE below

       -t     sort by modification time, newest first

       -T, --tabsize=COLS
              assume tab stops at each COLS instead of 8

       -u     with -lt: sort by, and show, access time; with -l:  show  access
              time  and  sort  by name; otherwise: sort by access time, newest
              first

       -U     do not sort; list entries in directory order

       -v     natural sort of (version) numbers within text

       -w, --width=COLS
              set output width to COLS.  0 means no limit

       -x     list entries by lines instead of by columns

       -X     sort alphabetically by entry extension

       -Z, --context
              print any security context of each file

       -1     list one file per line.  Avoid '\n' with -q or -b

       --help display this help and exit

       --version
              output version information and exit

       The SIZE argument is an integer and  optional  unit  (example:  10K  is
       10*1024).   Units  are  K,M,G,T,P,E,Z,Y  (powers  of 1024) or KB,MB,...
       (powers of 1000).

       The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
       +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
       MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
       MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
       only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
       able sets the default style to use.

       Using  color  to distinguish file types is disabled both by default and
       with --color=never.  With --color=auto, ls emits color codes only  when
       standard  output is connected to a terminal.  The LS_COLORS environment
       variable can change the settings.  Use the dircolors command to set it.

   Exit status:
       0      if OK,

       1      if minor problems (e.g., cannot access subdirectory),

       2      if serious trouble (e.g., cannot access command-line argument).

AUTHOR
       Written by Richard M. Stallman and David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report ls translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2017 Free Software Foundation, Inc.   License  GPLv3+:  GNU
       GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This  is  free  software:  you  are free to change and redistribute it.
       There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation at: <https://www.gnu.org/software/coreutils/ls>
       or available locally via: info '(coreutils) ls invocation'

GNU coreutils 8.29               December 2017                           LS(1)

```

**Depending on your environment you might find that only one of these works (either `man` or `--help`).**
We'll describe both ways below.

#### The `--help` flag

Many bash commands, and programs that people have written that can be
run from within bash, support a `--help` flag to display more
information on how to use the command or program.


{:.input_area}
```bash
ls --help
```

{:.output_stream}
```
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                               e.g., '--block-size=M'; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                               modification of file status information);
                               with -l: show ctime and sort by name;
                               otherwise: sort by ctime, newest first
  -C                         list entries by columns
      --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                               if omitted), 'auto', or 'never'; more info below
  -d, --directory            list directories themselves, not their contents
  -D, --dired                generate output designed for Emacs' dired mode
  -f                         do not sort, enable -aU, disable -ls --color
  -F, --classify             append indicator (one of */=>@|) to entries
      --file-type            likewise, except do not append '*'
      --format=WORD          across -x, commas -m, horizontal -x, long -l,
                               single-column -1, verbose -l, vertical -C
      --full-time            like -l --time-style=full-iso
  -g                         like -l, but do not list owner
      --group-directories-first
                             group directories before files;
                               can be augmented with a --sort option, but any
                               use of --sort=none (-U) disables grouping
  -G, --no-group             in a long listing, don't print group names
  -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
      --si                   likewise, but use powers of 1000 not 1024
  -H, --dereference-command-line
                             follow symbolic links listed on the command line
      --dereference-command-line-symlink-to-dir
                             follow each command line symbolic link
                               that points to a directory
      --hide=PATTERN         do not list implied entries matching shell PATTERN
                               (overridden by -a or -A)
      --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                               (default if omitted), 'auto', or 'never'
      --indicator-style=WORD  append indicator with style WORD to entry names:
                               none (default), slash (-p),
                               file-type (--file-type), classify (-F)
  -i, --inode                print the index number of each file
  -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  -k, --kibibytes            default to 1024-byte blocks for disk usage;
                               used only with -s and per directory totals
  -l                         use a long listing format
  -L, --dereference          when showing file information for a symbolic
                               link, show information for the file the link
                               references rather than for the link itself
  -m                         fill width with a comma separated list of entries
  -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  -N, --literal              print entry names without quoting
  -o                         like -l, but do not list group information
  -p, --indicator-style=slash
                             append / indicator to directories
  -q, --hide-control-chars   print ? instead of nongraphic characters
      --show-control-chars   show nongraphic characters as-is (the default,
                               unless program is 'ls' and output is a terminal)
  -Q, --quote-name           enclose entry names in double quotes
      --quoting-style=WORD   use quoting style WORD for entry names:
                               literal, locale, shell, shell-always,
                               shell-escape, shell-escape-always, c, escape
                               (overrides QUOTING_STYLE environment variable)
  -r, --reverse              reverse order while sorting
  -R, --recursive            list subdirectories recursively
  -s, --size                 print the allocated size of each file, in blocks
  -S                         sort by file size, largest first
      --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                               time (-t), version (-v), extension (-X)
      --time=WORD            with -l, show time as WORD instead of default
                               modification time: atime or access or use (-u);
                               ctime or status (-c); also use specified time
                               as sort key if --sort=time (newest first)
      --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
  -t                         sort by modification time, newest first
  -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  -u                         with -lt: sort by, and show, access time;
                               with -l: show access time and sort by name;
                               otherwise: sort by access time, newest first
  -U                         do not sort; list entries in directory order
  -v                         natural sort of (version) numbers within text
  -w, --width=COLS           set output width to COLS.  0 means no limit
  -x                         list entries by lines instead of by columns
  -X                         sort alphabetically by entry extension
  -Z, --context              print any security context of each file
  -1                         list one file per line.  Avoid '\n' with -q or -b
      --help     display this help and exit
      --version  output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
Also the TIME_STYLE environment variable sets the default style to use.

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors command to set it.

Exit status:
 0  if OK,
 1  if minor problems (e.g., cannot access subdirectory),
 2  if serious trouble (e.g., cannot access command-line argument).

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/ls>
or available locally via: info '(coreutils) ls invocation'

```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Unsupported command-line options</h2>
</div>


<div class="panel-body">

<p>If you try to use an option (flag) that is not supported, <code>ls</code> and other programs
will usually print an error message similar to:</p>
<div class="codehilite"><pre><span></span>$ ls -j
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">ls</span><span class="o">:</span> <span class="n">invalid</span> <span class="n">option</span> <span class="o">--</span> <span class="s1">&#39;j&#39;</span>
<span class="n">Try</span> <span class="s1">&#39;ls --help&#39;</span> <span class="k">for</span> <span class="n">more</span> <span class="n">information</span><span class="o">.</span>
</pre></div>

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> The `man` command</h2>
</div>


<div class="panel-body">

<p>The other way to learn about <code>ls</code> is to type</p>

</div>

</section>



{:.input_area}
```bash
man ls
```


{:.input_area}
```bash
ls -F Desktop
```

{:.output_stream}
```
ls: cannot access 'Desktop': No such file or directory

```



Your output should be a list of all the files and sub-directories on your
Desktop, including the `data-shell` directory you downloaded at
the [setup for this lesson]().  Take a look at your Desktop to confirm that
your output is accurate.  

As you may now see, using a bash shell is strongly dependent on the idea that
your files are organized in a hierarchical file system.
Organizing things hierarchically in this way helps us keep track of our work:
it's possible to put hundreds of files in our home directory,
just as it's possible to pile hundreds of printed papers on our desk,
but it's a self-defeating strategy.

Now that we know the `data-shell` directory is located on our Desktop, we
can do two things.  

First, we can look at its contents, using the same strategy as before, passing
a directory name to `ls`:


{:.input_area}
```bash
ls -F Desktop/data-shell
```

{:.output_stream}
```
ls: cannot access 'Desktop/data-shell': No such file or directory

```



Second, we can actually change our location to a different directory, so
we are no longer located in
our home directory.  

The command to change locations is `cd` followed by a
directory name to change our working directory.
`cd` stands for "change directory",
which is a bit misleading:
the command doesn't change the directory,
it changes the shell's idea of what directory we are in.

Let's say we want to move to the `data` directory we saw above.  We can
use the following series of commands to get there:


{:.input_area}
```bash
cd Desktop
cd data-shell
cd data
```

{:.output_stream}
```
cd: no such file or directory: Desktop
cd: no such file or directory: data-shell
cd: no such file or directory: data

```

These commands will move us from our home directory onto our Desktop, then into
the `data-shell` directory, then into the `data` directory.  `cd` doesn't print anything,
but if we run `pwd` after it, we can see that we are now
in `/Users/nelle/Desktop/data-shell/data`.
If we run `ls` without arguments now,
it lists the contents of `/Users/nelle/Desktop/data-shell/data`,
because that's where we now are:


{:.input_area}
```bash
pwd
```

{:.output_stream}
```
/home/stuart/Git/shell-novice/_episodes

```


{:.input_area}
```bash
ls -F
```

{:.output_stream}
```
01-intro.ipynb  02-filedir.ipynb  03-create.md      05-loop.md    07-find.md
01-intro.md     02-filedir.md     04-pipefilter.md  06-script.md

```

We now know how to go down the directory tree, but
how do we go up?  We might try the following:


{:.input_area}
```bash
cd data-shell
```

{:.output_stream}
```
cd: no such file or directory: data-shell

```

But we get an error!  Why is this?  

With our methods so far,
`cd` can only see sub-directories inside your current directory.  There are
different ways to see directories above your current location; we'll start
with the simplest.  

There is a shortcut in the shell to move up one directory level
that looks like this:


{:.input_area}
```bash
cd ..
```

`..` is a special directory name meaning
"the directory containing this one",
or more succinctly,
the **parent** of the current directory.
Sure enough,
if we run `pwd` after running `cd ..`, we're back in `/Users/nelle/Desktop/data-shell`:


{:.input_area}
```bash
pwd
```

{:.output_stream}
```
/home/stuart/Git/shell-novice

```

The special directory `..` doesn't usually show up when we run `ls`.  If we want
to display it, we can give `ls` the `-a` flag:


{:.input_area}
```bash
ls -F -a
```

{:.output_stream}
```
./                      CONDUCT.md       data/             _config.yml
../                     CONTRIBUTING.md  data-shell/       _episodes/
.git/                   LICENSE.md       fig/              _episodes_rmd/
.github/                Makefile         files/            _extras/
.gitignore              README.md        filesystem/       _includes/
.mailmap                aio.md           index.md          _layouts/
.update-copyright.conf  assets/          reference.md
AUTHORS                 bin/             requirements.txt
CITATION                code/            setup.md

```

`-a` stands for "show all";
it forces `ls` to show us file and directory names that begin with `.`,
such as `..` (which, if we're in `/Users/nelle`, refers to the `/Users` directory)
As you can see,
it also displays another special directory that's just called `.`,
which means "the current working directory".
It may seem redundant to have a name for it,
but we'll see some uses for it soon.

Note that in most command line tools, multiple flags can be combined 
with a single `-` and no spaces between the flags: `ls -F -a` is 
equivalent to `ls -Fa`.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Other Hidden Files</h2>
</div>


<div class="panel-body">

<p>In addition to the hidden directories <code>..</code> and <code>.</code>, you may also see a file
called <code>.bash_profile</code>. This file usually contains shell configuration
settings. You may also see other files and directories beginning
with <code>.</code>. These are usually files and directories that are used to configure
different programs on your computer. The prefix <code>.</code> is used to prevent these
configuration files from cluttering the terminal when a standard <code>ls</code> command
is used.</p>

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Orthogonality</h2>
</div>


<div class="panel-body">

<p>The special names <code>.</code> and <code>..</code> don't belong to <code>cd</code>;
they are interpreted the same way by every program.
For example,
if we are in <code>/Users/nelle/data</code>,
the command <code>ls ..</code> will give us a listing of <code>/Users/nelle</code>.
When the meanings of the parts are the same no matter how they're combined,
programmers say they are <strong>orthogonal</strong>:
Orthogonal systems tend to be easier for people to learn
because there are fewer special cases and exceptions to keep track of.</p>

</div>

</section>


These then, are the basic commands for navigating the filesystem on your computer:
`pwd`, `ls` and `cd`.  Let's explore some variations on those commands.  What happens
if you type `cd` on its own, without giving
a directory?


{:.input_area}
```bash
cd
```

How can you check what happened?  `pwd` gives us the answer!


{:.input_area}
```bash
pwd
```

{:.output_stream}
```
/home/stuart

```

It turns out that `cd` without an argument will return you to your home directory,
which is great if you've gotten lost in your own filesystem.  

Let's try returning to the `data` directory from before.  Last time, we used
three commands, but we can actually string together the list of directories
to move to `data` in one step:


{:.input_area}
```bash
cd Desktop/data-shell/data
```

{:.output_stream}
```
cd: no such file or directory: Desktop/data-shell/data

```

Check that we've moved to the right place by running `pwd` and `ls -F`  

If we want to move up one level from the data directory, we could use `cd ..`.  But
there is another way to move to any directory, regardless of your
current location.  

So far, when specifying directory names, or even a directory path (as above),
we have been using **relative paths**.  When you use a relative path with a command
like `ls` or `cd`, it tries to find that location  from where we are,
rather than from the root of the file system.  

However, it is possible to specify the **absolute path** to a directory by
including its entire path from the root directory, which is indicated by a
leading slash.  The leading `/` tells the computer to follow the path from
the root of the file system, so it always refers to exactly one directory,
no matter where we are when we run the command.

This allows us to move to our `data-shell` directory from anywhere on
the filesystem (including from inside `data`).  To find the absolute path
we're looking for, we can use `pwd` and then extract the piece we need
to move to `data-shell`.


{:.input_area}
```bash
pwd
```

{:.output_stream}
```
/home/stuart

```


{:.input_area}
```bash
cd /Users/nelle/Desktop/data-shell
```

{:.output_stream}
```
cd: no such file or directory: /Users/nelle/Desktop/data-shell

```

Run `pwd` and `ls -F` to ensure that we're in the directory we expect.  


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Two More Shortcuts</h2>
</div>


<div class="panel-body">

<p>The shell interprets the character <code>~</code> (tilde) at the start of a path to
mean "the current user's home directory". For example, if Nelle's home
directory is <code>/Users/nelle</code>, then <code>~/data</code> is equivalent to
<code>/Users/nelle/data</code>. This only works if it is the first character in the
path: <code>here/there/~/elsewhere</code> is <em>not</em> <code>here/there/Users/nelle/elsewhere</code>.</p>
<p>Another shortcut is the <code>-</code> (dash) character.  <code>cd</code> will translate <code>-</code> into
<em>the previous directory I was in</em>, which is faster than having to remember,
then type, the full path.  This is a <em>very</em> efficient way of moving back
and forth between directories. The difference between <code>cd ..</code> and <code>cd -</code> is
that the former brings you <em>up</em>, while the latter brings you <em>back</em>. You can
think of it as the <em>Last Channel</em> button on a TV remote.</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Absolute vs Relative Paths</h2>
</div>


<div class="panel-body">

<p>Starting from <code>/Users/amanda/data/</code>,
which of the following commands could Amanda use to navigate to her home directory,
which is <code>/Users/amanda</code>?</p>
<ol>
<li><code>cd .</code></li>
<li><code>cd /</code></li>
<li><code>cd /home/amanda</code></li>
<li><code>cd ../..</code></li>
<li><code>cd ~</code></li>
<li><code>cd home</code></li>
<li><code>cd ~/data/..</code></li>
<li><code>cd</code></li>
<li><code>cd ..</code></li>
</ol>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<ol>
<li>No: <code>.</code> stands for the current directory.</li>
<li>No: <code>/</code> stands for the root directory.</li>
<li>No: Amanda's home directory is <code>/Users/amanda</code>.</li>
<li>No: this goes up two levels, i.e. ends in <code>/Users</code>.</li>
<li>Yes: <code>~</code> stands for the user's home directory, in this case <code>/Users/amanda</code>.</li>
<li>No: this would navigate into a directory <code>home</code> in the current directory if it exists.</li>
<li>Yes: unnecessarily complicated, but correct.</li>
<li>Yes: shortcut to go back to the user's home directory.</li>
<li>Yes: goes up one level.</li>
</ol>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Relative Path Resolution</h2>
</div>


<div class="panel-body">

<p>Using the filesystem diagram below, if <code>pwd</code> displays <code>/Users/thing</code>,
what will <code>ls -F ../backup</code> display?</p>
<ol>
<li><code>../backup: No such file or directory</code></li>
<li><code>2012-12-01 2013-01-08 2013-01-27</code></li>
<li><code>2012-12-01/ 2013-01-08/ 2013-01-27/</code></li>
<li><code>original/ pnas_final/ pnas_sub/</code></li>
</ol>
<p><img alt="File System for Challenge Questions" src="../fig/filesystem-challenge.svg" /></p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<ol>
<li>No: there <em>is</em> a directory <code>backup</code> in <code>/Users</code>.</li>
<li>No: this is the content of <code>Users/thing/backup</code>,
   but with <code>..</code> we asked for one level further up.</li>
<li>No: see previous explanation.</li>
<li>Yes: <code>../backup/</code> refers to <code>/Users/backup/</code>.</li>
</ol>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> `ls` Reading Comprehension</h2>
</div>


<div class="panel-body">

<p>Assuming a directory structure as in the above Figure
(File System for Challenge Questions), if <code>pwd</code> displays <code>/Users/backup</code>,
and <code>-r</code> tells <code>ls</code> to display things in reverse order,
what command will display:</p>
<div class="codehilite"><pre><span></span>pnas_sub/ pnas_final/ original/
</pre></div>


<ol>
<li><code>ls pwd</code></li>
<li><code>ls -r -F</code></li>
<li><code>ls -r -F /Users/backup</code></li>
<li>Either #2 or #3 above, but not #1.</li>
</ol>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<ol>
<li>No: <code>pwd</code> is not the name of a directory.</li>
<li>Yes: <code>ls</code> without directory argument lists files and directories
   in the current directory.</li>
<li>Yes: uses the absolute path explicitly.</li>
<li>Correct: see explanations above.</li>
</ol>

</div>

</section>


### Nelle's Pipeline: Organizing Files

Knowing just this much about files and directories,
Nelle is ready to organize the files that the protein assay machine will create.
First,
she creates a directory called `north-pacific-gyre`
(to remind herself where the data came from).
Inside that,
she creates a directory called `2012-07-03`,
which is the date she started processing the samples.
She used to use names like `conference-paper` and `revised-results`,
but she found them hard to understand after a couple of years.
(The final straw was when she found herself creating
a directory called `revised-revised-results-3`.)


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Sorting Output</h2>
</div>


<div class="panel-body">

<p>Nelle names her directories "year-month-day",
with leading zeroes for months and days,
because the shell displays file and directory names in alphabetical order.
If she used month names,
December would come before July;
if she didn't use leading zeroes,
November ('11') would come before July ('7'). Similarly, putting the year first
means that June 2012 will come before June 2013.</p>

</div>

</section>


Each of her physical samples is labelled according to her lab's convention
with a unique ten-character ID,
such as "NENE01729A".
This is what she used in her collection log
to record the location, time, depth, and other characteristics of the sample,
so she decides to use it as part of each data file's name.
Since the assay machine's output is plain text,
she will call her files `NENE01729A.txt`, `NENE01812A.txt`, and so on.
All 1520 files will go into the same directory.

Now in her current directory `data-shell`,
Nelle can see what files she has using the command:


{:.input_area}
```bash
ls north-pacific-gyre/2012-07-03/
```

{:.output_stream}
```
ls: cannot access 'north-pacific-gyre/2012-07-03/': No such file or directory

```

This is a lot to type,
but she can let the shell do most of the work through what is called **tab completion**.
If she types:


{:.input_area}
```bash
ls nor
```

and then presses tab (the tab key on her keyboard),
the shell automatically completes the directory name for her:


{:.input_area}
```bash
ls north-pacific-gyre/
```

{:.output_stream}
```
ls: cannot access 'north-pacific-gyre/': No such file or directory

```

If she presses tab again,
Bash will add `2012-07-03/` to the command,
since it's the only possible completion.
Pressing tab again does nothing,
since there are 19 possibilities;
pressing tab twice brings up a list of all the files,
and so on.
This is called **tab completion**,
and we will see it in many other tools as we go on.


<section class="keypoints panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-exclamation-circle"></span> </h2>
</div>


<div class="panel-body">

<p>Keypoints:</p>
<ul>
<li>"The file system is responsible for managing information on the disk."</li>
<li>"Information is stored in files, which are stored in directories (folders)."</li>
<li>"Directories can also store other directories, which forms a directory tree."</li>
<li>"<code>cd path</code> changes the current working directory."</li>
<li>"<code>ls path</code> prints a listing of a specific file or directory; <code>ls</code> on its own lists the current working directory."</li>
<li>"<code>pwd</code> prints the user's current working directory."</li>
<li>"<code>/</code> on its own is the root directory of the whole file system."</li>
<li>"A relative path specifies a location starting from the current location."</li>
<li>"An absolute path specifies a location from the root of the file system."</li>
<li>"Directory names in a path are separated with <code>/</code> on Unix, but <code>\\</code> on Windows."</li>
<li>"<code>..</code> means 'the directory above the current one'; <code>.</code> on its own means 'the current directory'."</li>
<li>"Most files' names are <code>something.extension</code>. The extension isn't required, and doesn't guarantee anything, but is normally used to indicate the type of data in the file."</li>
</ul>

</div>

</section>

