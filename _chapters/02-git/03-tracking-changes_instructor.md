---
interact_link: 02-git/03-tracking-changes_instructor.ipynb
title: 'Tracking Changes'
permalink: 'chapters/02-git/03-tracking-changes'
previouschapter:
  url: chapters/02-git/02-creating-repositories
  title: 'Creating Repositories'
nextchapter:
  url: chapters/02-git/04-exploring-history
  title: 'Exploring History'
redirect_from:
  - 'chapters/02-git/03-tracking-changes'
---

# Tracking Changes

## Adding files and the staging area

First let’s make sure we’re still in the right directory. You should be in the planets directory.


{:.input_area}
```xonsh
pwd
```

{:.output_stream}
```
/home/stuart/Git/Aperio/stfc_website/notebooks/02-git


```

If you are still in moons, navigate back up to planets


{:.input_area}
```xonsh
pwd
```

{:.output_stream}
```
/home/stuart/Git/Aperio/stfc_website/notebooks/02-git


```


{:.input_area}
```xonsh
cd ..
```

{:.output_stream}
```


```

Let’s create a file called mars.txt that contains some notes about the Red Planet’s suitability as a base. We’ll use nano to edit the file; you can use whatever editor you like. In particular, this does not have to be the core.editor you set globally earlier. But remember, the bash command to create or edit a new file will depend on the editor you choose (it might not be nano). For a refresher on text editors, check out “Which Editor?” in The Unix Shell lesson.

```
$ nano mars.txt
```

Type the text below into the mars.txt file:

> Cold and dry, but everything is my favorite color

mars.txt now contains a single line, which we can see by running:


{:.input_area}
```xonsh
ls
```

{:.output_stream}
```
00-lessons.ipynb             [0m[01;34m01-bash[0m  [01;34m03-fundamentals-of-python[0m  [01;34m05-writing-effective-tests[0m  [01;34m07-collaborating-with-git[0m  [01;34m12-images-and-vis[0m
00-lessons_instructor.ipynb  [01;34m02-git[0m   [01;34m04-further-python[0m          [01;34m06-approximating-pi[0m         [01;34m08-collaborating-with-git[0m  environment.yml


```


{:.input_area}
```xonsh
cat mars.txt
```

{:.output_stream}
```


```

If we check the status of our project again, Git tells us that it’s noticed the new file:


{:.input_area}
```xonsh
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

The “untracked files” message means that there’s a file in the directory that Git isn’t keeping track of. We can tell Git to track a file using git add:


{:.input_area}
```xonsh
git add mars.txt
```

{:.output_stream}
```


```

and then check that the right thing happened:


{:.input_area}
```xonsh
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

Git now knows that it’s supposed to keep track of mars.txt, but it hasn’t recorded these changes as a commit yet. To get it to do that, we need to run one more command:


{:.input_area}
```xonsh
git commit -m "Start notes on Mars as a base"
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit


```

When we run `git commit`, Git takes everything we have told it to save by using `git add` and stores a copy permanently inside the special `.git` directory. This permanent copy is called a commit (or revision) and its short identifier is `f22b25e`. Your commit may have another identifier.

We use the `-m` flag (for “message”) to record a short, descriptive, and specific comment that will help us remember later on what we did and why. If we just run `git commit` without the `-m` option, Git will launch `nano` (or whatever other editor we configured as `core.editor`) so that we can write a longer message.

Good commit messages start with a brief (<50 characters) statement about the changes made in the commit. Generally, the message should complete the sentence “If applied, this commit will” . If you want to go into more detail, add a blank line between the summary line and your additional notes. Use this additional space to explain why you made changes and/or what their impact will be.

If we run `git status` now:


{:.input_area}
```xonsh
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

it tells us everything is up to date. If we want to know what we’ve done recently, we can ask Git to show us the project’s history using `git log`:


{:.input_area}
```xonsh
git log
```

{:.output_stream}
```
[33mcommit f68b2a3223f18d25a1e63380893d73b1cd30abc1[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 12:03:19 2018 +0100

    update notebooks

[33mcommit e11ebdc8bf78e2f52229b57d144967a4f99f88b6[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:59:41 2018 +0100

    update notebooks

[33mcommit 8809182d0e0e353f09367556d01b92de1ec450a4[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:50:41 2018 +0100

    update notebooks

[33mcommit c53a36e0edfeb20a335c2a41b2103fe7f19b6bd0[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:27:13 2018 +0100

    update notebooks

[33mcommit 0492cd39d704c9505f11d273c08cbb7c56024258[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:09:11 2018 +0100

    clean old image

[33mcommit 5077f80a291ee911d249b903a264ee40fb590b65[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:07:55 2018 +0100

    update notebooks

[33mcommit 39dd5be002135b4db35c2a216be5bbeb31a7c256[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 10:58:27 2018 +0100

    update notebooks

[33mcommit cf909a51854d650a70f87811f0c47668ab7eae6d[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 10:46:13 2018 +0100

    update notebooks

[33mcommit ebf6c876ee828a4b1d7e6d0ada2a3228232b71c6[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:37:25 2018 +0100

    update notebooks

[33mcommit 2e2caef43b2c47352ebdefbf55436eeb08f65f24[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:26:13 2018 +0100

    update notebooks

[33mcommit 9b727a7acbd4b7ec231cbaa0a469e4b0cf0ab507[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:17:05 2018 +0100

    remove old part 1 files

[33mcommit 965532dda2db870e8a97615b6d3de0e00815c11f[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:07:49 2018 +0100

    update notebooks

[33mcommit 94821cff313d14dda904524abae6ce792c6a70f0[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 15:58:10 2018 +0100

    update notebooks

[33mcommit 72c8550e9eb6cec7f26fa725b3e5d03f189e86db[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 15:32:21 2018 +0100

    update notebooks

[33mcommit c425f76ebea51c7bc98cc51b31fd863cc06cf02c[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 14:37:22 2018 +0100

    remove old checkpoints

[33mcommit 85d4a6e3502e186960ea3e07efc1634d3b7af4a2[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 14:36:53 2018 +0100

    add an ignore

[33mcommit 012340795d6728194a442430e64d128155e05991[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 14:14:54 2018 +0100

    update notebooks

[33mcommit f1717d7c38bd17655f463507bba9d13d3e7d9985[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 13:25:06 2018 +0100

    update notebooks

[33mcommit 166a8d60458d2ceeda27fb1c5ed079936590e918[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 13:22:54 2018 +0100

    update notebooks

[33mcommit 34268e85dbe4bbfac0117bec784ac506ef180d85[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 13:16:44 2018 +0100

    update notebooks

[33mcommit e1cfe1d6622718d3143023ceb840c05d7871d8af[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 11:59:19 2018 +0100

    update notebooks

[33mcommit 19eef9b9716460f7ef77f26cfc0169d81f891054[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 11:53:37 2018 +0100

    update notebooks

[33mcommit e5b43481e35f616f088e1654d66880617f7ea36c[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 18:13:58 2018 +0100

    update notebooks

[33mcommit f73be5b9f60dd0ee613ad15fbc3231048a03cf3e[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 18:03:01 2018 +0100

    update notebooks

[33mcommit 7bdabf6834f532e4e5de1e1a9e85422407b75888[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 17:54:50 2018 +0100

    update notebooks

[33mcommit c250be1783d071580fda3d2891628c8df853b137[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 15:25:09 2018 +0100

    update notebooks

[33mcommit fc10d58c600d177dc926edc61dc1b301ee74d070[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 15:17:46 2018 +0100

    update notebooks

[33mcommit 28a17be8c094e79639f869b56bc765f149b6f855[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 15:09:46 2018 +0100

    update notebooks

[33mcommit fa3dd411dc0cb59bc8c0216fd9fb8487cdc6b9ad[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Tue Aug 21 14:52:41 2018 +0100

    update notebooks

[33mcommit acb9d1ddad4f4655b6843ad9f5d4dc0fb4c1a8d9[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Tue Aug 21 14:05:23 2018 +0100

    update notebooks

[33mcommit c55fe06c415a14e4ab66e59dfd69f96f33bddb00[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Tue Aug 21 14:01:21 2018 +0100

    update notebooks

[33mcommit 83d22fb72dfe2cb97c889f9eee27d6e59029fd15[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 12:46:10 2018 +0100

    update notebooks

[33mcommit 1352289e11215e0cf06e4e9b198f2571b87f3634[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 10:20:43 2018 +0100

    update notebooks

[33mcommit b148b305b6e687c965eba8a940b6ae7120415f97[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 19:44:41 2018 +0100

    update notebooks

[33mcommit 78a9d78eb0ca9ad231a59832329da4f586639edf[m
Merge: d25859c 8b09b5b
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:44:05 2018 +0100

    Merge branch 'master' of github.com:Cadair/rcsc_notebooks

[33mcommit d25859c54c981f7ad5bfda39cab74ded27ee47ac[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:43:42 2018 +0100

    update notebooks

[33mcommit 6b2f4ce898c4cd01fd95e5845459cbb39c5fbc8f[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:43:12 2018 +0100

    update notebooks

[33mcommit 8b09b5bb88eaca994de7891453c3e51f6506b40f[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:38:23 2018 +0100

    remove old setup instructions notebook

[33mcommit b0f041be189f301d0a30b320d8e3bcec8d9b9999[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:34:41 2018 +0100

    remove old files

[33mcommit 50d31acffc688854e363d30cb7d91bfd8d515e70[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:29:55 2018 +0100

    update notebooks

[33mcommit 12ba0802861674559bb85e7f84c6464c2086663d[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 15 13:19:13 2018 +0100

    Add the environment file for binder

[33mcommit a4f3524945c89174cbabe8ce7f99494feea5f629[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 15 11:41:18 2018 +0100

    update notebooks

[33mcommit 3331567c4ba480f95db6e3a054a6534f412b225b[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 15 11:24:51 2018 +0100

    update notebooks

[33mcommit 3931f8dc17f956ed0679689911ac3bea815e7ea1[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Fri Jul 27 15:08:53 2018 +0100

    update notebooks

[33mcommit e7f170a42d7c39070b626315443539dcec24ddf9[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Fri Jul 27 15:08:33 2018 +0100

    update notebooks

[33mcommit 032584df56650bcd5d902cc91bfc243b9d7a35ce[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 23:06:27 2018 +0100

    update notebooks

[33mcommit e070aca61aada496596cc4a7fce647f076de7189[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 23:06:12 2018 +0100

    what the shit

[33mcommit cc7ffecf0dc9cd00522ba4542b83e300acdbf22c[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 22:54:18 2018 +0100

    update notebooks

[33mcommit ca7243f1f46cbabf40a8206ce8b857c25452e5eb[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 22:50:37 2018 +0100

    Add readme


```

`git log` lists all commits made to a repository in reverse chronological order. The listing for each commit includes the commit’s full identifier (which starts with the same characters as the short identifier printed by the git commit command earlier), the commit’s author, when it was created, and the log message Git was given when the commit was created.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Where Are My Changes?</h2>
</div>


<div class="panel-body">

<p>If we run <code>ls</code> at this point, we will still see just one file called <code>mars.txt</code>. That’s because Git saves information about files’ history in the special <code>.git</code> directory mentioned earlier so that our filesystem doesn’t become cluttered (and so that we can’t accidentally edit or delete an old version).</p>

</div>

</section>


Now suppose Dracula adds more information to the file. (Again, we’ll edit with `nano` and then `cat` the file to show its contents; you may use a different editor, and don’t need to `cat`.)


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
```

{:.output_stream}
```



```

```
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
```

When we run git status now, it tells us that a file it already knows about has been modified:


{:.input_area}
```xonsh
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

The last line is the key phrase: “no changes added to commit”. We have changed this file, but we haven’t told Git we will want to save those changes (which we do with `git add`) nor have we saved them (which we do with `git commit`). So let’s do that now. It is good practice to always review our changes before saving them. We do this using git diff. This shows us the differences between the current state of the file and the most recently saved version:


{:.input_area}
```xonsh
git diff
```

{:.output_stream}
```
nbdiff /tmp/67g4sn_01-introducing-the-shell_instructor.ipynb 01-bash/01-introducing-the-shell_instructor.ipynb
--- /tmp/67g4sn_01-introducing-the-shell_instructor.ipynb  2018-08-30 12:07:31.165576
+++ 01-bash/01-introducing-the-shell_instructor.ipynb  2018-08-30 12:07:15.235755
[34m## replaced (type changed from NoneType to int) /cells/4/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/4/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      1TB-1/	boot/  dev/    home/   misc/  opt/   run/   sys/  var/
[32m+      1TB-2/	cifs/  etc/    lib@    mnt/   proc/  sbin@  tmp/  windows/
[32m+      bin@	data/  games/  lib64@  net/   root/  srv/   usr/

[0mnbdiff /tmp/eqaPWY_02-files-and-directories_instructor.ipynb 01-bash/02-files-and-directories_instructor.ipynb
--- /tmp/eqaPWY_02-files-and-directories_instructor.ipynb  2018-08-30 12:07:31.688903
+++ 01-bash/02-files-and-directories_instructor.ipynb  2018-08-30 12:07:27.595616
[34m## replaced (type changed from NoneType to int) /cells/2/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/2/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/8/execution_count:[0m
[31m-  None
[32m+  2

[0m[34m## inserted before /cells/8/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis

[0m[34m## replaced (type changed from NoneType to int) /cells/10/execution_count:[0m
[31m-  None
[32m+  3

[0m[34m## inserted before /cells/10/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/12/execution_count:[0m
[31m-  None
[32m+  4

[0m[34m## inserted before /cells/12/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      Usage: ls [OPTION]... [FILE]...
[32m+      List information about the FILEs (the current directory by default).
[32m+      Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
[32m+      
[32m+      Mandatory arguments to long options are mandatory for short options too.
[32m+        -a, --all                  do not ignore entries starting with .
[32m+        -A, --almost-all           do not list implied . and ..
[32m+            --author               with -l, print the author of each file
[32m+        -b, --escape               print C-style escapes for nongraphic characters
[32m+            --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
[32m+                                     e.g., '--block-size=M'; see SIZE format below
[32m+        -B, --ignore-backups       do not list implied entries ending with ~
[32m+        -c                         with -lt: sort by, and show, ctime (time of last
[32m+                                     modification of file status information);
[32m+                                     with -l: show ctime and sort by name;
[32m+                                     otherwise: sort by ctime, newest first
[32m+        -C                         list entries by columns
[32m+            --color[=WHEN]         colorize the output; WHEN can be 'always' (default
[32m+                                     if omitted), 'auto', or 'never'; more info below
[32m+        -d, --directory            list directories themselves, not their contents
[32m+        -D, --dired                generate output designed for Emacs' dired mode
[32m+        -f                         do not sort, enable -aU, disable -ls --color
[32m+        -F, --classify             append indicator (one of */=>@|) to entries
[32m+            --file-type            likewise, except do not append '*'
[32m+            --format=WORD          across -x, commas -m, horizontal -x, long -l,
[32m+                                     single-column -1, verbose -l, vertical -C
[32m+            --full-time            like -l --time-style=full-iso
[32m+        -g                         like -l, but do not list owner
[32m+            --group-directories-first
[32m+                                   group directories before files;
[32m+                                     can be augmented with a --sort option, but any
[32m+                                     use of --sort=none (-U) disables grouping
[32m+        -G, --no-group             in a long listing, don't print group names
[32m+        -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
[32m+            --si                   likewise, but use powers of 1000 not 1024
[32m+        -H, --dereference-command-line
[32m+                                   follow symbolic links listed on the command line
[32m+            --dereference-command-line-symlink-to-dir
[32m+                                   follow each command line symbolic link
[32m+                                     that points to a directory
[32m+            --hide=PATTERN         do not list implied entries matching shell PATTERN
[32m+                                     (overridden by -a or -A)
[32m+            --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
[32m+                                     (default if omitted), 'auto', or 'never'
[32m+            --indicator-style=WORD  append indicator with style WORD to entry names:
[32m+                                     none (default), slash (-p),
[32m+                                     file-type (--file-type), classify (-F)
[32m+        -i, --inode                print the index number of each file
[32m+        -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
[32m+        -k, --kibibytes            default to 1024-byte blocks for disk usage;
[32m+                                     used only with -s and per directory totals
[32m+        -l                         use a long listing format
[32m+        -L, --dereference          when showing file information for a symbolic
[32m+                                     link, show information for the file the link
[32m+                                     references rather than for the link itself
[32m+        -m                         fill width with a comma separated list of entries
[32m+        -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
[32m+        -N, --literal              print entry names without quoting
[32m+        -o                         like -l, but do not list group information
[32m+        -p, --indicator-style=slash
[32m+                                   append / indicator to directories
[32m+        -q, --hide-control-chars   print ? instead of nongraphic characters
[32m+            --show-control-chars   show nongraphic characters as-is (the default,
[32m+                                     unless program is 'ls' and output is a terminal)
[32m+        -Q, --quote-name           enclose entry names in double quotes
[32m+            --quoting-style=WORD   use quoting style WORD for entry names:
[32m+                                     literal, locale, shell, shell-always,
[32m+                                     shell-escape, shell-escape-always, c, escape
[32m+                                     (overrides QUOTING_STYLE environment variable)
[32m+        -r, --reverse              reverse order while sorting
[32m+        -R, --recursive            list subdirectories recursively
[32m+        -s, --size                 print the allocated size of each file, in blocks
[32m+        -S                         sort by file size, largest first
[32m+            --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
[32m+                                     time (-t), version (-v), extension (-X)
[32m+            --time=WORD            with -l, show time as WORD instead of default
[32m+                                     modification time: atime or access or use (-u);
[32m+                                     ctime or status (-c); also use specified time
[32m+                                     as sort key if --sort=time (newest first)
[32m+            --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
[32m+        -t                         sort by modification time, newest first
[32m+        -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
[32m+        -u                         with -lt: sort by, and show, access time;
[32m+                                     with -l: show access time and sort by name;
[32m+                                     otherwise: sort by access time, newest first
[32m+        -U                         do not sort; list entries in directory order
[32m+        -v                         natural sort of (version) numbers within text
[32m+        -w, --width=COLS           set output width to COLS.  0 means no limit
[32m+        -x                         list entries by lines instead of by columns
[32m+        -X                         sort alphabetically by entry extension
[32m+        -Z, --context              print any security context of each file
[32m+        -1                         list one file per line.  Avoid '\n' with -q or -b
[32m+            --help     display this help and exit
[32m+            --version  output version information and exit
[32m+      
[32m+      The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
[32m+      Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
[32m+      
[32m+      The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
[32m+      FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
[32m+      then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
[32m+      TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
[32m+      Also the TIME_STYLE environment variable sets the default style to use.
[32m+      
[32m+      Using color to distinguish file types is disabled both by default and
[32m+      with --color=never.  With --color=auto, ls emits color codes only when
[32m+      standard output is connected to a terminal.  The LS_COLORS environment
[32m+      variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+      Exit status:
[32m+       0  if OK,
[32m+       1  if minor problems (e.g., cannot access subdirectory),
[32m+       2  if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+      Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+      or available locally via: info '(coreutils) ls invocation'

[0m[34m## replaced (type changed from NoneType to int) /cells/14/execution_count:[0m
[31m-  None
[32m+  5

[0m[34m## inserted before /cells/14/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      LS(1)                            User Commands                           LS(1)
[32m+      
[32m+      NNAAMMEE
[32m+             ls - list directory contents
[32m+      
[32m+      SSYYNNOOPPSSIISS
[32m+             llss [_O_P_T_I_O_N]... [_F_I_L_E]...
[32m+      
[32m+      DDEESSCCRRIIPPTTIIOONN
[32m+             List  information  about  the FILEs (the current directory by default).
[32m+             Sort entries alphabetically if none of --ccffttuuvvSSUUXX nor ----ssoorrtt  is  speci‐
[32m+             fied.
[32m+      
[32m+             Mandatory  arguments  to  long  options are mandatory for short options
[32m+             too.
[32m+      
[32m+             --aa, ----aallll
[32m+                    do not ignore entries starting with .
[32m+      
[32m+             --AA, ----aallmmoosstt--aallll
[32m+                    do not list implied . and ..
[32m+      
[32m+             ----aauutthhoorr
[32m+                    with --ll, print the author of each file
[32m+      
[32m+             --bb, ----eessccaappee
[32m+                    print C-style escapes for nongraphic characters
[32m+      
[32m+             ----bblloocckk--ssiizzee=_S_I_Z_E
[32m+                    with  --ll,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
[32m+                    '--block-size=M'; see SIZE format below
[32m+      
[32m+             --BB, ----iiggnnoorree--bbaacckkuuppss
[32m+                    do not list implied entries ending with ~
[32m+      
[32m+             --cc     with --lltt: sort by, and show, ctime (time of last modification of
[32m+                    file status information); with --ll: show ctime and sort by  name;
[32m+                    otherwise: sort by ctime, newest first
[32m+      
[32m+             --CC     list entries by columns
[32m+      
[32m+             ----ccoolloorr[=_W_H_E_N]
[32m+                    colorize  the output; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'; more info below
[32m+      
[32m+             --dd, ----ddiirreeccttoorryy
[32m+                    list directories themselves, not their contents
[32m+      
[32m+             --DD, ----ddiirreedd
[32m+                    generate output designed for Emacs' dired mode
[32m+      
[32m+             --ff     do not sort, enable --aaUU, disable --llss ----ccoolloorr
[32m+      
[32m+             --FF, ----ccllaassssiiffyy
[32m+                    append indicator (one of */=>@|) to entries
[32m+      
[32m+             ----ffiillee--ttyyppee
[32m+                    likewise, except do not append '*'
[32m+      
[32m+             ----ffoorrmmaatt=_W_O_R_D
[32m+                    across --xx, commas --mm, horizontal --xx, long --ll, single-column  --11,
[32m+                    verbose --ll, vertical --CC
[32m+      
[32m+             ----ffuullll--ttiimmee
[32m+                    like --ll ----ttiimmee--ssttyyllee=_f_u_l_l_-_i_s_o
[32m+      
[32m+             --gg     like --ll, but do not list owner
[32m+      
[32m+             ----ggrroouupp--ddiirreeccttoorriieess--ffiirrsstt
[32m+                    group directories before files;
[32m+      
[32m+                    can   be  augmented  with  a  ----ssoorrtt  option,  but  any  use  of
[32m+                    ----ssoorrtt=_n_o_n_e (--UU) disables grouping
[32m+      
[32m+             --GG, ----nnoo--ggrroouupp
[32m+                    in a long listing, don't print group names
[32m+      
[32m+             --hh, ----hhuummaann--rreeaaddaabbllee
[32m+                    with --ll and --ss, print sizes like 1K 234M 2G etc.
[32m+      
[32m+             ----ssii   likewise, but use powers of 1000 not 1024
[32m+      
[32m+             --HH, ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee
[32m+                    follow symbolic links listed on the command line
[32m+      
[32m+             ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee--ssyymmlliinnkk--ttoo--ddiirr
[32m+                    follow each command line symbolic link
[32m+      
[32m+                    that points to a directory
[32m+      
[32m+             ----hhiiddee=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell  PATTERN  (overridden
[32m+                    by --aa or --AA)
[32m+      
[32m+             ----hhyyppeerrlliinnkk[=_W_H_E_N]
[32m+                    hyperlink file names; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'
[32m+      
[32m+             ----iinnddiiccaattoorr--ssttyyllee=_W_O_R_D
[32m+                    append indicator with style WORD to entry names: none (default),
[32m+                    slash (--pp), file-type (----ffiillee--ttyyppee), classify (--FF)
[32m+      
[32m+             --ii, ----iinnooddee
[32m+                    print the index number of each file
[32m+      
[32m+             --II, ----iiggnnoorree=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell PATTERN
[32m+      
[32m+             --kk, ----kkiibbiibbyytteess
[32m+                    default  to  1024-byte  blocks for disk usage; used only with --ss
[32m+                    and per directory totals
[32m+      
[32m+             --ll     use a long listing format
[32m+      
[32m+             --LL, ----ddeerreeffeerreennccee
[32m+                    when showing file information for a symbolic link, show informa‐
[32m+                    tion  for  the file the link references rather than for the link
[32m+                    itself
[32m+      
[32m+             --mm     fill width with a comma separated list of entries
[32m+      
[32m+             --nn, ----nnuummeerriicc--uuiidd--ggiidd
[32m+                    like --ll, but list numeric user and group IDs
[32m+      
[32m+             --NN, ----lliitteerraall
[32m+                    print entry names without quoting
[32m+      
[32m+             --oo     like --ll, but do not list group information
[32m+      
[32m+             --pp, ----iinnddiiccaattoorr--ssttyyllee=_s_l_a_s_h
[32m+                    append / indicator to directories
[32m+      
[32m+             --qq, ----hhiiddee--ccoonnttrrooll--cchhaarrss
[32m+                    print ? instead of nongraphic characters
[32m+      
[32m+             ----sshhooww--ccoonnttrrooll--cchhaarrss
[32m+                    show nongraphic characters as-is (the default, unless program is
[32m+                    'ls' and output is a terminal)
[32m+      
[32m+             --QQ, ----qquuoottee--nnaammee
[32m+                    enclose entry names in double quotes
[32m+      
[32m+             ----qquuoottiinngg--ssttyyllee=_W_O_R_D
[32m+                    use  quoting style WORD for entry names: literal, locale, shell,
[32m+                    shell-always,  shell-escape,  shell-escape-always,   c,   escape
[32m+                    (overrides QUOTING_STYLE environment variable)
[32m+      
[32m+             --rr, ----rreevveerrssee
[32m+                    reverse order while sorting
[32m+      
[32m+             --RR, ----rreeccuurrssiivvee
[32m+                    list subdirectories recursively
[32m+      
[32m+             --ss, ----ssiizzee
[32m+                    print the allocated size of each file, in blocks
[32m+      
[32m+             --SS     sort by file size, largest first
[32m+      
[32m+             ----ssoorrtt=_W_O_R_D
[32m+                    sort  by  WORD instead of name: none (--UU), size (--SS), time (--tt),
[32m+                    version (--vv), extension (--XX)
[32m+      
[32m+             ----ttiimmee=_W_O_R_D
[32m+                    with --ll, show time as WORD instead of default modification time:
[32m+                    atime  or  access  or  use  (--uu); ctime or status (--cc); also use
[32m+                    specified time as sort key if ----ssoorrtt=_t_i_m_e (newest first)
[32m+      
[32m+             ----ttiimmee--ssttyyllee=_T_I_M_E___S_T_Y_L_E
[32m+                    time/date format with --ll; see TIME_STYLE below
[32m+      
[32m+             --tt     sort by modification time, newest first
[32m+      
[32m+             --TT, ----ttaabbssiizzee=_C_O_L_S
[32m+                    assume tab stops at each COLS instead of 8
[32m+      
[32m+             --uu     with --lltt: sort by, and show, access time; with --ll:  show  access
[32m+                    time  and  sort  by name; otherwise: sort by access time, newest
[32m+                    first
[32m+      
[32m+             --UU     do not sort; list entries in directory order
[32m+      
[32m+             --vv     natural sort of (version) numbers within text
[32m+      
[32m+             --ww, ----wwiiddtthh=_C_O_L_S
[32m+                    set output width to COLS.  0 means no limit
[32m+      
[32m+             --xx     list entries by lines instead of by columns
[32m+      
[32m+             --XX     sort alphabetically by entry extension
[32m+      
[32m+             --ZZ, ----ccoonntteexxtt
[32m+                    print any security context of each file
[32m+      
[32m+             --11     list one file per line.  Avoid '\n' with --qq or --bb
[32m+      
[32m+             ----hheellpp display this help and exit
[32m+      
[32m+             ----vveerrssiioonn
[32m+                    output version information and exit
[32m+      
[32m+             The SIZE argument is an integer and  optional  unit  (example:  10K  is
[32m+             10*1024).   Units  are  K,M,G,T,P,E,Z,Y  (powers  of 1024) or KB,MB,...
[32m+             (powers of 1000).
[32m+      
[32m+             The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
[32m+             +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
[32m+             MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
[32m+             MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
[32m+             only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
[32m+             able sets the default style to use.
[32m+      
[32m+             Using  color  to distinguish file types is disabled both by default and
[32m+             with ----ccoolloorr=_n_e_v_e_r.  With ----ccoolloorr=_a_u_t_o, ls emits color codes only  when
[32m+             standard  output is connected to a terminal.  The LS_COLORS environment
[32m+             variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+         EExxiitt ssttaattuuss::
[32m+             0      if OK,
[32m+      
[32m+             1      if minor problems (e.g., cannot access subdirectory),
[32m+      
[32m+             2      if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      AAUUTTHHOORR
[32m+             Written by Richard M. Stallman and David MacKenzie.
[32m+      
[32m+      RREEPPOORRTTIINNGG BBUUGGSS
[32m+             GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+             Report ls translation bugs to <https://translationproject.org/team/>
[32m+      
[32m+      CCOOPPYYRRIIGGHHTT
[32m+             Copyright © 2017 Free Software Foundation, Inc.   License  GPLv3+:  GNU
[32m+             GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
[32m+             This  is  free  software:  you  are free to change and redistribute it.
[32m+             There is NO WARRANTY, to the extent permitted by law.
[32m+      
[32m+      SSEEEE AALLSSOO
[32m+             Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+             or available locally via: info '(coreutils) ls invocation'
[32m+      
[32m+      GNU coreutils 8.29               December 2017                           LS(1)

[0m[34m## replaced (type changed from NoneType to int) /cells/17/execution_count:[0m
[31m-  None
[32m+  6

[0m[34m## inserted before /cells/17/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      Usage: ls [OPTION]... [FILE]...
[32m+      List information about the FILEs (the current directory by default).
[32m+      Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
[32m+      
[32m+      Mandatory arguments to long options are mandatory for short options too.
[32m+        -a, --all                  do not ignore entries starting with .
[32m+        -A, --almost-all           do not list implied . and ..
[32m+            --author               with -l, print the author of each file
[32m+        -b, --escape               print C-style escapes for nongraphic characters
[32m+            --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
[32m+                                     e.g., '--block-size=M'; see SIZE format below
[32m+        -B, --ignore-backups       do not list implied entries ending with ~
[32m+        -c                         with -lt: sort by, and show, ctime (time of last
[32m+                                     modification of file status information);
[32m+                                     with -l: show ctime and sort by name;
[32m+                                     otherwise: sort by ctime, newest first
[32m+        -C                         list entries by columns
[32m+            --color[=WHEN]         colorize the output; WHEN can be 'always' (default
[32m+                                     if omitted), 'auto', or 'never'; more info below
[32m+        -d, --directory            list directories themselves, not their contents
[32m+        -D, --dired                generate output designed for Emacs' dired mode
[32m+        -f                         do not sort, enable -aU, disable -ls --color
[32m+        -F, --classify             append indicator (one of */=>@|) to entries
[32m+            --file-type            likewise, except do not append '*'
[32m+            --format=WORD          across -x, commas -m, horizontal -x, long -l,
[32m+                                     single-column -1, verbose -l, vertical -C
[32m+            --full-time            like -l --time-style=full-iso
[32m+        -g                         like -l, but do not list owner
[32m+            --group-directories-first
[32m+                                   group directories before files;
[32m+                                     can be augmented with a --sort option, but any
[32m+                                     use of --sort=none (-U) disables grouping
[32m+        -G, --no-group             in a long listing, don't print group names
[32m+        -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
[32m+            --si                   likewise, but use powers of 1000 not 1024
[32m+        -H, --dereference-command-line
[32m+                                   follow symbolic links listed on the command line
[32m+            --dereference-command-line-symlink-to-dir
[32m+                                   follow each command line symbolic link
[32m+                                     that points to a directory
[32m+            --hide=PATTERN         do not list implied entries matching shell PATTERN
[32m+                                     (overridden by -a or -A)
[32m+            --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
[32m+                                     (default if omitted), 'auto', or 'never'
[32m+            --indicator-style=WORD  append indicator with style WORD to entry names:
[32m+                                     none (default), slash (-p),
[32m+                                     file-type (--file-type), classify (-F)
[32m+        -i, --inode                print the index number of each file
[32m+        -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
[32m+        -k, --kibibytes            default to 1024-byte blocks for disk usage;
[32m+                                     used only with -s and per directory totals
[32m+        -l                         use a long listing format
[32m+        -L, --dereference          when showing file information for a symbolic
[32m+                                     link, show information for the file the link
[32m+                                     references rather than for the link itself
[32m+        -m                         fill width with a comma separated list of entries
[32m+        -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
[32m+        -N, --literal              print entry names without quoting
[32m+        -o                         like -l, but do not list group information
[32m+        -p, --indicator-style=slash
[32m+                                   append / indicator to directories
[32m+        -q, --hide-control-chars   print ? instead of nongraphic characters
[32m+            --show-control-chars   show nongraphic characters as-is (the default,
[32m+                                     unless program is 'ls' and output is a terminal)
[32m+        -Q, --quote-name           enclose entry names in double quotes
[32m+            --quoting-style=WORD   use quoting style WORD for entry names:
[32m+                                     literal, locale, shell, shell-always,
[32m+                                     shell-escape, shell-escape-always, c, escape
[32m+                                     (overrides QUOTING_STYLE environment variable)
[32m+        -r, --reverse              reverse order while sorting
[32m+        -R, --recursive            list subdirectories recursively
[32m+        -s, --size                 print the allocated size of each file, in blocks
[32m+        -S                         sort by file size, largest first
[32m+            --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
[32m+                                     time (-t), version (-v), extension (-X)
[32m+            --time=WORD            with -l, show time as WORD instead of default
[32m+                                     modification time: atime or access or use (-u);
[32m+                                     ctime or status (-c); also use specified time
[32m+                                     as sort key if --sort=time (newest first)
[32m+            --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
[32m+        -t                         sort by modification time, newest first
[32m+        -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
[32m+        -u                         with -lt: sort by, and show, access time;
[32m+                                     with -l: show access time and sort by name;
[32m+                                     otherwise: sort by access time, newest first
[32m+        -U                         do not sort; list entries in directory order
[32m+        -v                         natural sort of (version) numbers within text
[32m+        -w, --width=COLS           set output width to COLS.  0 means no limit
[32m+        -x                         list entries by lines instead of by columns
[32m+        -X                         sort alphabetically by entry extension
[32m+        -Z, --context              print any security context of each file
[32m+        -1                         list one file per line.  Avoid '\n' with -q or -b
[32m+            --help     display this help and exit
[32m+            --version  output version information and exit
[32m+      
[32m+      The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
[32m+      Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
[32m+      
[32m+      The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
[32m+      FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
[32m+      then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
[32m+      TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
[32m+      Also the TIME_STYLE environment variable sets the default style to use.
[32m+      
[32m+      Using color to distinguish file types is disabled both by default and
[32m+      with --color=never.  With --color=auto, ls emits color codes only when
[32m+      standard output is connected to a terminal.  The LS_COLORS environment
[32m+      variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+      Exit status:
[32m+       0  if OK,
[32m+       1  if minor problems (e.g., cannot access subdirectory),
[32m+       2  if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+      Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+      or available locally via: info '(coreutils) ls invocation'

[0m[34m## replaced (type changed from NoneType to int) /cells/20/execution_count:[0m
[31m-  None
[32m+  7

[0m[34m## inserted before /cells/20/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      LS(1)                            User Commands                           LS(1)
[32m+      
[32m+      NNAAMMEE
[32m+             ls - list directory contents
[32m+      
[32m+      SSYYNNOOPPSSIISS
[32m+             llss [_O_P_T_I_O_N]... [_F_I_L_E]...
[32m+      
[32m+      DDEESSCCRRIIPPTTIIOONN
[32m+             List  information  about  the FILEs (the current directory by default).
[32m+             Sort entries alphabetically if none of --ccffttuuvvSSUUXX nor ----ssoorrtt  is  speci‐
[32m+             fied.
[32m+      
[32m+             Mandatory  arguments  to  long  options are mandatory for short options
[32m+             too.
[32m+      
[32m+             --aa, ----aallll
[32m+                    do not ignore entries starting with .
[32m+      
[32m+             --AA, ----aallmmoosstt--aallll
[32m+                    do not list implied . and ..
[32m+      
[32m+             ----aauutthhoorr
[32m+                    with --ll, print the author of each file
[32m+      
[32m+             --bb, ----eessccaappee
[32m+                    print C-style escapes for nongraphic characters
[32m+      
[32m+             ----bblloocckk--ssiizzee=_S_I_Z_E
[32m+                    with  --ll,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
[32m+                    '--block-size=M'; see SIZE format below
[32m+      
[32m+             --BB, ----iiggnnoorree--bbaacckkuuppss
[32m+                    do not list implied entries ending with ~
[32m+      
[32m+             --cc     with --lltt: sort by, and show, ctime (time of last modification of
[32m+                    file status information); with --ll: show ctime and sort by  name;
[32m+                    otherwise: sort by ctime, newest first
[32m+      
[32m+             --CC     list entries by columns
[32m+      
[32m+             ----ccoolloorr[=_W_H_E_N]
[32m+                    colorize  the output; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'; more info below
[32m+      
[32m+             --dd, ----ddiirreeccttoorryy
[32m+                    list directories themselves, not their contents
[32m+      
[32m+             --DD, ----ddiirreedd
[32m+                    generate output designed for Emacs' dired mode
[32m+      
[32m+             --ff     do not sort, enable --aaUU, disable --llss ----ccoolloorr
[32m+      
[32m+             --FF, ----ccllaassssiiffyy
[32m+                    append indicator (one of */=>@|) to entries
[32m+      
[32m+             ----ffiillee--ttyyppee
[32m+                    likewise, except do not append '*'
[32m+      
[32m+             ----ffoorrmmaatt=_W_O_R_D
[32m+                    across --xx, commas --mm, horizontal --xx, long --ll, single-column  --11,
[32m+                    verbose --ll, vertical --CC
[32m+      
[32m+             ----ffuullll--ttiimmee
[32m+                    like --ll ----ttiimmee--ssttyyllee=_f_u_l_l_-_i_s_o
[32m+      
[32m+             --gg     like --ll, but do not list owner
[32m+      
[32m+             ----ggrroouupp--ddiirreeccttoorriieess--ffiirrsstt
[32m+                    group directories before files;
[32m+      
[32m+                    can   be  augmented  with  a  ----ssoorrtt  option,  but  any  use  of
[32m+                    ----ssoorrtt=_n_o_n_e (--UU) disables grouping
[32m+      
[32m+             --GG, ----nnoo--ggrroouupp
[32m+                    in a long listing, don't print group names
[32m+      
[32m+             --hh, ----hhuummaann--rreeaaddaabbllee
[32m+                    with --ll and --ss, print sizes like 1K 234M 2G etc.
[32m+      
[32m+             ----ssii   likewise, but use powers of 1000 not 1024
[32m+      
[32m+             --HH, ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee
[32m+                    follow symbolic links listed on the command line
[32m+      
[32m+             ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee--ssyymmlliinnkk--ttoo--ddiirr
[32m+                    follow each command line symbolic link
[32m+      
[32m+                    that points to a directory
[32m+      
[32m+             ----hhiiddee=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell  PATTERN  (overridden
[32m+                    by --aa or --AA)
[32m+      
[32m+             ----hhyyppeerrlliinnkk[=_W_H_E_N]
[32m+                    hyperlink file names; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'
[32m+      
[32m+             ----iinnddiiccaattoorr--ssttyyllee=_W_O_R_D
[32m+                    append indicator with style WORD to entry names: none (default),
[32m+                    slash (--pp), file-type (----ffiillee--ttyyppee), classify (--FF)
[32m+      
[32m+             --ii, ----iinnooddee
[32m+                    print the index number of each file
[32m+      
[32m+             --II, ----iiggnnoorree=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell PATTERN
[32m+      
[32m+             --kk, ----kkiibbiibbyytteess
[32m+                    default  to  1024-byte  blocks for disk usage; used only with --ss
[32m+                    and per directory totals
[32m+      
[32m+             --ll     use a long listing format
[32m+      
[32m+             --LL, ----ddeerreeffeerreennccee
[32m+                    when showing file information for a symbolic link, show informa‐
[32m+                    tion  for  the file the link references rather than for the link
[32m+                    itself
[32m+      
[32m+             --mm     fill width with a comma separated list of entries
[32m+      
[32m+             --nn, ----nnuummeerriicc--uuiidd--ggiidd
[32m+                    like --ll, but list numeric user and group IDs
[32m+      
[32m+             --NN, ----lliitteerraall
[32m+                    print entry names without quoting
[32m+      
[32m+             --oo     like --ll, but do not list group information
[32m+      
[32m+             --pp, ----iinnddiiccaattoorr--ssttyyllee=_s_l_a_s_h
[32m+                    append / indicator to directories
[32m+      
[32m+             --qq, ----hhiiddee--ccoonnttrrooll--cchhaarrss
[32m+                    print ? instead of nongraphic characters
[32m+      
[32m+             ----sshhooww--ccoonnttrrooll--cchhaarrss
[32m+                    show nongraphic characters as-is (the default, unless program is
[32m+                    'ls' and output is a terminal)
[32m+      
[32m+             --QQ, ----qquuoottee--nnaammee
[32m+                    enclose entry names in double quotes
[32m+      
[32m+             ----qquuoottiinngg--ssttyyllee=_W_O_R_D
[32m+                    use  quoting style WORD for entry names: literal, locale, shell,
[32m+                    shell-always,  shell-escape,  shell-escape-always,   c,   escape
[32m+                    (overrides QUOTING_STYLE environment variable)
[32m+      
[32m+             --rr, ----rreevveerrssee
[32m+                    reverse order while sorting
[32m+      
[32m+             --RR, ----rreeccuurrssiivvee
[32m+                    list subdirectories recursively
[32m+      
[32m+             --ss, ----ssiizzee
[32m+                    print the allocated size of each file, in blocks
[32m+      
[32m+             --SS     sort by file size, largest first
[32m+      
[32m+             ----ssoorrtt=_W_O_R_D
[32m+                    sort  by  WORD instead of name: none (--UU), size (--SS), time (--tt),
[32m+                    version (--vv), extension (--XX)
[32m+      
[32m+             ----ttiimmee=_W_O_R_D
[32m+                    with --ll, show time as WORD instead of default modification time:
[32m+                    atime  or  access  or  use  (--uu); ctime or status (--cc); also use
[32m+                    specified time as sort key if ----ssoorrtt=_t_i_m_e (newest first)
[32m+      
[32m+             ----ttiimmee--ssttyyllee=_T_I_M_E___S_T_Y_L_E
[32m+                    time/date format with --ll; see TIME_STYLE below
[32m+      
[32m+             --tt     sort by modification time, newest first
[32m+      
[32m+             --TT, ----ttaabbssiizzee=_C_O_L_S
[32m+                    assume tab stops at each COLS instead of 8
[32m+      
[32m+             --uu     with --lltt: sort by, and show, access time; with --ll:  show  access
[32m+                    time  and  sort  by name; otherwise: sort by access time, newest
[32m+                    first
[32m+      
[32m+             --UU     do not sort; list entries in directory order
[32m+      
[32m+             --vv     natural sort of (version) numbers within text
[32m+      
[32m+             --ww, ----wwiiddtthh=_C_O_L_S
[32m+                    set output width to COLS.  0 means no limit
[32m+      
[32m+             --xx     list entries by lines instead of by columns
[32m+      
[32m+             --XX     sort alphabetically by entry extension
[32m+      
[32m+             --ZZ, ----ccoonntteexxtt
[32m+                    print any security context of each file
[32m+      
[32m+             --11     list one file per line.  Avoid '\n' with --qq or --bb
[32m+      
[32m+             ----hheellpp display this help and exit
[32m+      
[32m+             ----vveerrssiioonn
[32m+                    output version information and exit
[32m+      
[32m+             The SIZE argument is an integer and  optional  unit  (example:  10K  is
[32m+             10*1024).   Units  are  K,M,G,T,P,E,Z,Y  (powers  of 1024) or KB,MB,...
[32m+             (powers of 1000).
[32m+      
[32m+             The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
[32m+             +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
[32m+             MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
[32m+             MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
[32m+             only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
[32m+             able sets the default style to use.
[32m+      
[32m+             Using  color  to distinguish file types is disabled both by default and
[32m+             with ----ccoolloorr=_n_e_v_e_r.  With ----ccoolloorr=_a_u_t_o, ls emits color codes only  when
[32m+             standard  output is connected to a terminal.  The LS_COLORS environment
[32m+             variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+         EExxiitt ssttaattuuss::
[32m+             0      if OK,
[32m+      
[32m+             1      if minor problems (e.g., cannot access subdirectory),
[32m+      
[32m+             2      if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      AAUUTTHHOORR
[32m+             Written by Richard M. Stallman and David MacKenzie.
[32m+      
[32m+      RREEPPOORRTTIINNGG BBUUGGSS
[32m+             GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+             Report ls translation bugs to <https://translationproject.org/team/>
[32m+      
[32m+      CCOOPPYYRRIIGGHHTT
[32m+             Copyright © 2017 Free Software Foundation, Inc.   License  GPLv3+:  GNU
[32m+             GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
[32m+             This  is  free  software:  you  are free to change and redistribute it.
[32m+             There is NO WARRANTY, to the extent permitted by law.
[32m+      
[32m+      SSEEEE AALLSSOO
[32m+             Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+             or available locally via: info '(coreutils) ls invocation'
[32m+      
[32m+      GNU coreutils 8.29               December 2017                           LS(1)

[0m[34m## replaced (type changed from NoneType to int) /cells/21/execution_count:[0m
[31m-  None
[32m+  8

[0m[34m## inserted before /cells/21/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'Desktop': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/23/execution_count:[0m
[31m-  None
[32m+  9

[0m[34m## inserted before /cells/23/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'Desktop/data-shell': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/25/execution_count:[0m
[31m-  None
[32m+  10

[0m[34m## inserted before /cells/25/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: Desktop: No such file or directory
[32m+      bash: cd: data-shell: No such file or directory
[32m+      bash: cd: data: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/27/execution_count:[0m
[31m-  None
[32m+  11

[0m[34m## inserted before /cells/27/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/28/execution_count:[0m
[31m-  None
[32m+  12

[0m[34m## inserted before /cells/28/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/30/execution_count:[0m
[31m-  None
[32m+  13

[0m[34m## inserted before /cells/30/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: data-shell: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/32/execution_count:[0m
[31m-  None
[32m+  14

[0m[34m## replaced (type changed from NoneType to int) /cells/34/execution_count:[0m
[31m-  None
[32m+  15

[0m[34m## inserted before /cells/34/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks

[0m[34m## replaced (type changed from NoneType to int) /cells/36/execution_count:[0m
[31m-  None
[32m+  16

[0m[34m## inserted before /cells/36/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ./			     03-fundamentals-of-python/   12-images-and-vis/
[32m+      ../			     04-further-python/		  environment.yml
[32m+      00-lessons_instructor.ipynb  05-writing-effective-tests/  .git
[32m+      00-lessons.ipynb	     06-approximating-pi/	  .gitignore
[32m+      01-bash/		     07-collaborating-with-git/
[32m+      02-git/			     08-collaborating-with-git/

[0m[34m## replaced (type changed from NoneType to int) /cells/41/execution_count:[0m
[31m-  None
[32m+  17

[0m[34m## replaced (type changed from NoneType to int) /cells/43/execution_count:[0m
[31m-  None
[32m+  18

[0m[34m## inserted before /cells/43/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart

[0m[34m## replaced (type changed from NoneType to int) /cells/45/execution_count:[0m
[31m-  None
[32m+  19

[0m[34m## inserted before /cells/45/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: Desktop/data-shell/data: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/47/execution_count:[0m
[31m-  None
[32m+  20

[0m[34m## inserted before /cells/47/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart

[0m[34m## replaced (type changed from NoneType to int) /cells/48/execution_count:[0m
[31m-  None
[32m+  21

[0m[34m## inserted before /cells/48/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: /Users/nelle/Desktop/data-shell: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/60/execution_count:[0m
[31m-  None
[32m+  22

[0m[34m## inserted before /cells/60/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'north-pacific-gyre/2012-07-03/': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/62/execution_count:[0m
[31m-  None
[32m+  23

[0m[34m## inserted before /cells/62/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'nor': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/64/execution_count:[0m
[31m-  None
[32m+  24

[0m[34m## inserted before /cells/64/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'north-pacific-gyre/': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0mnbdiff /tmp/xIoQWF_03-working-with-files-and-directories_instructor.ipynb 01-bash/03-working-with-files-and-directories_instructor.ipynb
--- /tmp/xIoQWF_03-working-with-files-and-directories_instructor.ipynb  2018-08-30 12:07:32.428895
+++ 01-bash/03-working-with-files-and-directories_instructor.ipynb  2018-08-30 12:07:21.372353
[34m## replaced (type changed from NoneType to int) /cells/1/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## replaced (type changed from NoneType to int) /cells/3/execution_count:[0m
[31m-  None
[32m+  2

[0m[34m## inserted before /cells/3/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/4/execution_count:[0m
[31m-  None
[32m+  3

[0m[34m## inserted before /cells/4/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png

[0m[34m## replaced (type changed from NoneType to int) /cells/6/execution_count:[0m
[31m-  None
[32m+  4

[0m[34m## replaced (type changed from NoneType to int) /cells/8/execution_count:[0m
[31m-  None
[32m+  5

[0m[34m## inserted before /cells/8/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/12/execution_count:[0m
[31m-  None
[32m+  6

[0m[34m## replaced (type changed from NoneType to int) /cells/14/execution_count:[0m
[31m-  None
[32m+  7

[0m[34m## replaced (type changed from NoneType to int) /cells/15/execution_count:[0m
[31m-  None
[32m+  8

[0m[34m## replaced (type changed from NoneType to int) /cells/20/execution_count:[0m
[31m-  None
[32m+  9

[0m[34m## inserted before /cells/20/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/24/execution_count:[0m
[31m-  None
[32m+  10

[0m[34m## replaced (type changed from NoneType to int) /cells/26/execution_count:[0m
[31m-  None
[32m+  11

[0m[34m## replaced (type changed from NoneType to int) /cells/29/execution_count:[0m
[31m-  None
[32m+  12

[0m[34m## inserted before /cells/29/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash/thesis

[0m[34m## replaced (type changed from NoneType to int) /cells/30/execution_count:[0m
[31m-  None
[32m+  13

[0m[34m## replaced (type changed from NoneType to int) /cells/31/execution_count:[0m
[31m-  None
[32m+  14

[0m[34m## inserted before /cells/31/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/32/execution_count:[0m
[31m-  None
[32m+  15

[0m[34m## replaced (type changed from NoneType to int) /cells/34/execution_count:[0m
[31m-  None
[32m+  16

[0m[34m## inserted before /cells/34/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      rm: cannot remove 'thesis': Is a directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/36/execution_count:[0m
[31m-  None
[32m+  17

[0m[34m## replaced (type changed from NoneType to int) /cells/41/execution_count:[0m
[31m-  None
[32m+  18

[0m[34m## inserted before /cells/41/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/42/execution_count:[0m
[31m-  None
[32m+  19

[0m[34m## replaced (type changed from NoneType to int) /cells/43/execution_count:[0m
[31m-  None
[32m+  20

[0m[34m## replaced (type changed from NoneType to int) /cells/44/execution_count:[0m
[31m-  None
[32m+  21

[0m[34m## replaced (type changed from NoneType to int) /cells/45/execution_count:[0m
[31m-  None
[32m+  22

[0m[34m## inserted before /cells/45/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/47/execution_count:[0m
[31m-  None
[32m+  23

[0m[34m## replaced (type changed from NoneType to int) /cells/49/execution_count:[0m
[31m-  None
[32m+  24

[0m[34m## inserted before /cells/49/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/51/execution_count:[0m
[31m-  None
[32m+  25

[0m[34m## replaced (type changed from NoneType to int) /cells/53/execution_count:[0m
[31m-  None
[32m+  26

[0m[34m## replaced (type changed from NoneType to int) /cells/55/execution_count:[0m
[31m-  None
[32m+  27

[0m[34m## inserted before /cells/55/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/59/execution_count:[0m
[31m-  None
[32m+  28

[0m[34m## replaced (type changed from NoneType to int) /cells/60/execution_count:[0m
[31m-  None
[32m+  29

[0m[34m## inserted before /cells/60/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt  thesis/quotations.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/62/execution_count:[0m
[31m-  None
[32m+  30

[0m[34m## replaced (type changed from NoneType to int) /cells/63/execution_count:[0m
[31m-  None
[32m+  31

[0m[34m## inserted before /cells/63/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'quotes.txt': No such file or directory
[32m+      thesis/quotations.txt
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0mnbdiff /tmp/8fImmq_01-introduction-to-version-control_instructor.ipynb 02-git/01-introduction-to-version-control_instructor.ipynb
--- /tmp/8fImmq_01-introduction-to-version-control_instructor.ipynb  2018-08-30 12:07:33.205553
+++ 02-git/01-introduction-to-version-control_instructor.ipynb  2018-08-30 12:07:29.392262
[34m## replaced (type changed from NoneType to int) /cells/7/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/7/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      user.name=Stuart Mumford
[32m+      user.email=stuart@cadair.com
[32m+      user.signingkey=E6276769
[32m+      commit.gpgsign=true
[32m+      push.default=simple
[32m+      alias.log=log --show-signature
[32m+      difftool.latex.cmd=latexdiff  $LOCAL $REMOTE
[32m+      difftool.latexadd.cmd=latexdiff --graphics-markup=none -t BOLD -f IDENTICAL -s COLOR -X caption $LOCAL $REMOTE
[32m+      difftool.prompt=false
[32m+      alias.ldiff=difftool -t latex
[32m+      alias.ldiffadd=difftool -t latexadd
[32m+      alias.tree=log --decorate --graph --show-signature
[32m+      alias.wdiff=diff
[32m+      credential.helper=/usr/lib/git-core/git-credential-gnome-keyring
[32m+      filter.lfs.clean=git-lfs clean %f
[32m+      filter.lfs.smudge=git-lfs smudge %f
[32m+      filter.lfs.required=true
[32m+      color.ui=auto
[32m+      core.editor=vim
[32m+      github.user=Cadair
[32m+      github.oauth-token=1f70bdc8ea2446bd1f2fd3c30fefa8ce1b31e676
[32m+      url.git@github.com:.insteadof=gh:
[32m+      url.git@gitlab.com:.insteadof=gl:
[32m+      diff.jupyternotebook.command=git-nbdiffdriver diff
[32m+      merge.jupyternotebook.driver=git-nbmergedriver merge %O %A %B %L %P
[32m+      merge.jupyternotebook.name=jupyter notebook merge driver
[32m+      difftool.nbdime.cmd=git-nbdifftool diff "$LOCAL" "$REMOTE"
[32m+      mergetool.nbdime.cmd=git-nbmergetool merge "$BASE" "$LOCAL" "$REMOTE" "$MERGED"
[32m+      mergetool.prompt=false
[32m+      magithub.online=false
[32m+      magithub.status.includestatusheader=false
[32m+      magithub.status.includepullrequestssection=false
[32m+      magithub.status.includeissuessection=false
[32m+      core.repositoryformatversion=0
[32m+      core.filemode=true
[32m+      core.bare=false
[32m+      core.logallrefupdates=true
[32m+      core.worktree=../../../notebooks
[32m+      remote.origin.url=https://github.com/cadair/rcsc_notebooks
[32m+      remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
[32m+      branch.master.remote=origin
[32m+      branch.master.merge=refs/heads/master
[32m+      

[0m

```

The output is cryptic because it is actually a series of commands for tools like editors and patch telling them how to reconstruct one file given the other. If we break it down into pieces:

1. The first line tells us that Git is producing output similar to the Unix diff command comparing the old and new versions of the file.
1. The second line tells exactly which versions of the file Git is comparing; df0654a and 315bf3a are unique computer-generated labels for those versions.
1. The third and fourth lines once again show the name of the file being changed.
1. The remaining lines are the most interesting, they show us the actual differences and the lines on which they occur. In particular, the + marker in the first column shows where we added a line.

After reviewing our change, it’s time to commit it:


{:.input_area}
```xonsh
git commit -m "Add concerns about effects of Mars' moons on Wolfman"
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit

On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

Whoops: Git won’t commit because we didn’t use git add first. Let’s fix that:

git add mars.txt
git commit -m "Add concerns about effects of Mars' moons on Wolfman"

Git insists that we add files to the set we want to commit before actually committing anything. This allows us to commit our changes in stages and capture changes in logical portions rather than only large batches. For example, suppose we’re adding a few citations to relevant research to our thesis. We might want to commit those additions, and the corresponding bibliography entries, but not commit some of our work drafting the conclusion (which we haven’t finished yet).

To allow for this, Git has a special staging area where it keeps track of things that have been added to the current changeset but not yet committed.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Staging Area</h2>
</div>


<div class="panel-body">

<p>If you think of Git as taking snapshots of changes over the life of a project, git add specifies what will go in a snapshot (putting things in the staging area), and git commit then actually takes the snapshot, and makes a permanent record of it (as a commit). If you don’t have anything staged when you type git commit, Git will prompt you to use git commit -a or git commit --all, which is kind of like gathering everyone for the picture! However, it’s almost always better to explicitly add things to the staging area, because you might commit changes you forgot you made. (Going back to snapshots, you might get the extra with incomplete makeup walking on the stage for the snapshot because you used -a!) Try to stage things manually, or you might find yourself searching for “git undo commit” more than you would like!</p>
<p><img alt="" src="http://swcarpentry.github.io/git-novice/fig/git-staging-area.svg" /></p>

</div>

</section>


Let’s watch as our changes to a file move from our editor to the staging area and into long-term storage. First, we’ll add another line to the file:


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
```

{:.output_stream}
```



```


{:.input_area}
```xonsh
git diff
```

{:.output_stream}
```
nbdiff /tmp/2Vp5Wx_01-introducing-the-shell_instructor.ipynb 01-bash/01-introducing-the-shell_instructor.ipynb
--- /tmp/2Vp5Wx_01-introducing-the-shell_instructor.ipynb  2018-08-30 12:07:34.342206
+++ 01-bash/01-introducing-the-shell_instructor.ipynb  2018-08-30 12:07:15.235755
[34m## replaced (type changed from NoneType to int) /cells/4/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/4/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      1TB-1/	boot/  dev/    home/   misc/  opt/   run/   sys/  var/
[32m+      1TB-2/	cifs/  etc/    lib@    mnt/   proc/  sbin@  tmp/  windows/
[32m+      bin@	data/  games/  lib64@  net/   root/  srv/   usr/

[0mnbdiff /tmp/KkZav8_02-files-and-directories_instructor.ipynb 01-bash/02-files-and-directories_instructor.ipynb
--- /tmp/KkZav8_02-files-and-directories_instructor.ipynb  2018-08-30 12:07:34.818868
+++ 01-bash/02-files-and-directories_instructor.ipynb  2018-08-30 12:07:27.595616
[34m## replaced (type changed from NoneType to int) /cells/2/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/2/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/8/execution_count:[0m
[31m-  None
[32m+  2

[0m[34m## inserted before /cells/8/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis

[0m[34m## replaced (type changed from NoneType to int) /cells/10/execution_count:[0m
[31m-  None
[32m+  3

[0m[34m## inserted before /cells/10/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/12/execution_count:[0m
[31m-  None
[32m+  4

[0m[34m## inserted before /cells/12/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      Usage: ls [OPTION]... [FILE]...
[32m+      List information about the FILEs (the current directory by default).
[32m+      Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
[32m+      
[32m+      Mandatory arguments to long options are mandatory for short options too.
[32m+        -a, --all                  do not ignore entries starting with .
[32m+        -A, --almost-all           do not list implied . and ..
[32m+            --author               with -l, print the author of each file
[32m+        -b, --escape               print C-style escapes for nongraphic characters
[32m+            --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
[32m+                                     e.g., '--block-size=M'; see SIZE format below
[32m+        -B, --ignore-backups       do not list implied entries ending with ~
[32m+        -c                         with -lt: sort by, and show, ctime (time of last
[32m+                                     modification of file status information);
[32m+                                     with -l: show ctime and sort by name;
[32m+                                     otherwise: sort by ctime, newest first
[32m+        -C                         list entries by columns
[32m+            --color[=WHEN]         colorize the output; WHEN can be 'always' (default
[32m+                                     if omitted), 'auto', or 'never'; more info below
[32m+        -d, --directory            list directories themselves, not their contents
[32m+        -D, --dired                generate output designed for Emacs' dired mode
[32m+        -f                         do not sort, enable -aU, disable -ls --color
[32m+        -F, --classify             append indicator (one of */=>@|) to entries
[32m+            --file-type            likewise, except do not append '*'
[32m+            --format=WORD          across -x, commas -m, horizontal -x, long -l,
[32m+                                     single-column -1, verbose -l, vertical -C
[32m+            --full-time            like -l --time-style=full-iso
[32m+        -g                         like -l, but do not list owner
[32m+            --group-directories-first
[32m+                                   group directories before files;
[32m+                                     can be augmented with a --sort option, but any
[32m+                                     use of --sort=none (-U) disables grouping
[32m+        -G, --no-group             in a long listing, don't print group names
[32m+        -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
[32m+            --si                   likewise, but use powers of 1000 not 1024
[32m+        -H, --dereference-command-line
[32m+                                   follow symbolic links listed on the command line
[32m+            --dereference-command-line-symlink-to-dir
[32m+                                   follow each command line symbolic link
[32m+                                     that points to a directory
[32m+            --hide=PATTERN         do not list implied entries matching shell PATTERN
[32m+                                     (overridden by -a or -A)
[32m+            --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
[32m+                                     (default if omitted), 'auto', or 'never'
[32m+            --indicator-style=WORD  append indicator with style WORD to entry names:
[32m+                                     none (default), slash (-p),
[32m+                                     file-type (--file-type), classify (-F)
[32m+        -i, --inode                print the index number of each file
[32m+        -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
[32m+        -k, --kibibytes            default to 1024-byte blocks for disk usage;
[32m+                                     used only with -s and per directory totals
[32m+        -l                         use a long listing format
[32m+        -L, --dereference          when showing file information for a symbolic
[32m+                                     link, show information for the file the link
[32m+                                     references rather than for the link itself
[32m+        -m                         fill width with a comma separated list of entries
[32m+        -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
[32m+        -N, --literal              print entry names without quoting
[32m+        -o                         like -l, but do not list group information
[32m+        -p, --indicator-style=slash
[32m+                                   append / indicator to directories
[32m+        -q, --hide-control-chars   print ? instead of nongraphic characters
[32m+            --show-control-chars   show nongraphic characters as-is (the default,
[32m+                                     unless program is 'ls' and output is a terminal)
[32m+        -Q, --quote-name           enclose entry names in double quotes
[32m+            --quoting-style=WORD   use quoting style WORD for entry names:
[32m+                                     literal, locale, shell, shell-always,
[32m+                                     shell-escape, shell-escape-always, c, escape
[32m+                                     (overrides QUOTING_STYLE environment variable)
[32m+        -r, --reverse              reverse order while sorting
[32m+        -R, --recursive            list subdirectories recursively
[32m+        -s, --size                 print the allocated size of each file, in blocks
[32m+        -S                         sort by file size, largest first
[32m+            --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
[32m+                                     time (-t), version (-v), extension (-X)
[32m+            --time=WORD            with -l, show time as WORD instead of default
[32m+                                     modification time: atime or access or use (-u);
[32m+                                     ctime or status (-c); also use specified time
[32m+                                     as sort key if --sort=time (newest first)
[32m+            --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
[32m+        -t                         sort by modification time, newest first
[32m+        -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
[32m+        -u                         with -lt: sort by, and show, access time;
[32m+                                     with -l: show access time and sort by name;
[32m+                                     otherwise: sort by access time, newest first
[32m+        -U                         do not sort; list entries in directory order
[32m+        -v                         natural sort of (version) numbers within text
[32m+        -w, --width=COLS           set output width to COLS.  0 means no limit
[32m+        -x                         list entries by lines instead of by columns
[32m+        -X                         sort alphabetically by entry extension
[32m+        -Z, --context              print any security context of each file
[32m+        -1                         list one file per line.  Avoid '\n' with -q or -b
[32m+            --help     display this help and exit
[32m+            --version  output version information and exit
[32m+      
[32m+      The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
[32m+      Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
[32m+      
[32m+      The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
[32m+      FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
[32m+      then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
[32m+      TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
[32m+      Also the TIME_STYLE environment variable sets the default style to use.
[32m+      
[32m+      Using color to distinguish file types is disabled both by default and
[32m+      with --color=never.  With --color=auto, ls emits color codes only when
[32m+      standard output is connected to a terminal.  The LS_COLORS environment
[32m+      variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+      Exit status:
[32m+       0  if OK,
[32m+       1  if minor problems (e.g., cannot access subdirectory),
[32m+       2  if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+      Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+      or available locally via: info '(coreutils) ls invocation'

[0m[34m## replaced (type changed from NoneType to int) /cells/14/execution_count:[0m
[31m-  None
[32m+  5

[0m[34m## inserted before /cells/14/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      LS(1)                            User Commands                           LS(1)
[32m+      
[32m+      NNAAMMEE
[32m+             ls - list directory contents
[32m+      
[32m+      SSYYNNOOPPSSIISS
[32m+             llss [_O_P_T_I_O_N]... [_F_I_L_E]...
[32m+      
[32m+      DDEESSCCRRIIPPTTIIOONN
[32m+             List  information  about  the FILEs (the current directory by default).
[32m+             Sort entries alphabetically if none of --ccffttuuvvSSUUXX nor ----ssoorrtt  is  speci‐
[32m+             fied.
[32m+      
[32m+             Mandatory  arguments  to  long  options are mandatory for short options
[32m+             too.
[32m+      
[32m+             --aa, ----aallll
[32m+                    do not ignore entries starting with .
[32m+      
[32m+             --AA, ----aallmmoosstt--aallll
[32m+                    do not list implied . and ..
[32m+      
[32m+             ----aauutthhoorr
[32m+                    with --ll, print the author of each file
[32m+      
[32m+             --bb, ----eessccaappee
[32m+                    print C-style escapes for nongraphic characters
[32m+      
[32m+             ----bblloocckk--ssiizzee=_S_I_Z_E
[32m+                    with  --ll,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
[32m+                    '--block-size=M'; see SIZE format below
[32m+      
[32m+             --BB, ----iiggnnoorree--bbaacckkuuppss
[32m+                    do not list implied entries ending with ~
[32m+      
[32m+             --cc     with --lltt: sort by, and show, ctime (time of last modification of
[32m+                    file status information); with --ll: show ctime and sort by  name;
[32m+                    otherwise: sort by ctime, newest first
[32m+      
[32m+             --CC     list entries by columns
[32m+      
[32m+             ----ccoolloorr[=_W_H_E_N]
[32m+                    colorize  the output; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'; more info below
[32m+      
[32m+             --dd, ----ddiirreeccttoorryy
[32m+                    list directories themselves, not their contents
[32m+      
[32m+             --DD, ----ddiirreedd
[32m+                    generate output designed for Emacs' dired mode
[32m+      
[32m+             --ff     do not sort, enable --aaUU, disable --llss ----ccoolloorr
[32m+      
[32m+             --FF, ----ccllaassssiiffyy
[32m+                    append indicator (one of */=>@|) to entries
[32m+      
[32m+             ----ffiillee--ttyyppee
[32m+                    likewise, except do not append '*'
[32m+      
[32m+             ----ffoorrmmaatt=_W_O_R_D
[32m+                    across --xx, commas --mm, horizontal --xx, long --ll, single-column  --11,
[32m+                    verbose --ll, vertical --CC
[32m+      
[32m+             ----ffuullll--ttiimmee
[32m+                    like --ll ----ttiimmee--ssttyyllee=_f_u_l_l_-_i_s_o
[32m+      
[32m+             --gg     like --ll, but do not list owner
[32m+      
[32m+             ----ggrroouupp--ddiirreeccttoorriieess--ffiirrsstt
[32m+                    group directories before files;
[32m+      
[32m+                    can   be  augmented  with  a  ----ssoorrtt  option,  but  any  use  of
[32m+                    ----ssoorrtt=_n_o_n_e (--UU) disables grouping
[32m+      
[32m+             --GG, ----nnoo--ggrroouupp
[32m+                    in a long listing, don't print group names
[32m+      
[32m+             --hh, ----hhuummaann--rreeaaddaabbllee
[32m+                    with --ll and --ss, print sizes like 1K 234M 2G etc.
[32m+      
[32m+             ----ssii   likewise, but use powers of 1000 not 1024
[32m+      
[32m+             --HH, ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee
[32m+                    follow symbolic links listed on the command line
[32m+      
[32m+             ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee--ssyymmlliinnkk--ttoo--ddiirr
[32m+                    follow each command line symbolic link
[32m+      
[32m+                    that points to a directory
[32m+      
[32m+             ----hhiiddee=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell  PATTERN  (overridden
[32m+                    by --aa or --AA)
[32m+      
[32m+             ----hhyyppeerrlliinnkk[=_W_H_E_N]
[32m+                    hyperlink file names; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'
[32m+      
[32m+             ----iinnddiiccaattoorr--ssttyyllee=_W_O_R_D
[32m+                    append indicator with style WORD to entry names: none (default),
[32m+                    slash (--pp), file-type (----ffiillee--ttyyppee), classify (--FF)
[32m+      
[32m+             --ii, ----iinnooddee
[32m+                    print the index number of each file
[32m+      
[32m+             --II, ----iiggnnoorree=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell PATTERN
[32m+      
[32m+             --kk, ----kkiibbiibbyytteess
[32m+                    default  to  1024-byte  blocks for disk usage; used only with --ss
[32m+                    and per directory totals
[32m+      
[32m+             --ll     use a long listing format
[32m+      
[32m+             --LL, ----ddeerreeffeerreennccee
[32m+                    when showing file information for a symbolic link, show informa‐
[32m+                    tion  for  the file the link references rather than for the link
[32m+                    itself
[32m+      
[32m+             --mm     fill width with a comma separated list of entries
[32m+      
[32m+             --nn, ----nnuummeerriicc--uuiidd--ggiidd
[32m+                    like --ll, but list numeric user and group IDs
[32m+      
[32m+             --NN, ----lliitteerraall
[32m+                    print entry names without quoting
[32m+      
[32m+             --oo     like --ll, but do not list group information
[32m+      
[32m+             --pp, ----iinnddiiccaattoorr--ssttyyllee=_s_l_a_s_h
[32m+                    append / indicator to directories
[32m+      
[32m+             --qq, ----hhiiddee--ccoonnttrrooll--cchhaarrss
[32m+                    print ? instead of nongraphic characters
[32m+      
[32m+             ----sshhooww--ccoonnttrrooll--cchhaarrss
[32m+                    show nongraphic characters as-is (the default, unless program is
[32m+                    'ls' and output is a terminal)
[32m+      
[32m+             --QQ, ----qquuoottee--nnaammee
[32m+                    enclose entry names in double quotes
[32m+      
[32m+             ----qquuoottiinngg--ssttyyllee=_W_O_R_D
[32m+                    use  quoting style WORD for entry names: literal, locale, shell,
[32m+                    shell-always,  shell-escape,  shell-escape-always,   c,   escape
[32m+                    (overrides QUOTING_STYLE environment variable)
[32m+      
[32m+             --rr, ----rreevveerrssee
[32m+                    reverse order while sorting
[32m+      
[32m+             --RR, ----rreeccuurrssiivvee
[32m+                    list subdirectories recursively
[32m+      
[32m+             --ss, ----ssiizzee
[32m+                    print the allocated size of each file, in blocks
[32m+      
[32m+             --SS     sort by file size, largest first
[32m+      
[32m+             ----ssoorrtt=_W_O_R_D
[32m+                    sort  by  WORD instead of name: none (--UU), size (--SS), time (--tt),
[32m+                    version (--vv), extension (--XX)
[32m+      
[32m+             ----ttiimmee=_W_O_R_D
[32m+                    with --ll, show time as WORD instead of default modification time:
[32m+                    atime  or  access  or  use  (--uu); ctime or status (--cc); also use
[32m+                    specified time as sort key if ----ssoorrtt=_t_i_m_e (newest first)
[32m+      
[32m+             ----ttiimmee--ssttyyllee=_T_I_M_E___S_T_Y_L_E
[32m+                    time/date format with --ll; see TIME_STYLE below
[32m+      
[32m+             --tt     sort by modification time, newest first
[32m+      
[32m+             --TT, ----ttaabbssiizzee=_C_O_L_S
[32m+                    assume tab stops at each COLS instead of 8
[32m+      
[32m+             --uu     with --lltt: sort by, and show, access time; with --ll:  show  access
[32m+                    time  and  sort  by name; otherwise: sort by access time, newest
[32m+                    first
[32m+      
[32m+             --UU     do not sort; list entries in directory order
[32m+      
[32m+             --vv     natural sort of (version) numbers within text
[32m+      
[32m+             --ww, ----wwiiddtthh=_C_O_L_S
[32m+                    set output width to COLS.  0 means no limit
[32m+      
[32m+             --xx     list entries by lines instead of by columns
[32m+      
[32m+             --XX     sort alphabetically by entry extension
[32m+      
[32m+             --ZZ, ----ccoonntteexxtt
[32m+                    print any security context of each file
[32m+      
[32m+             --11     list one file per line.  Avoid '\n' with --qq or --bb
[32m+      
[32m+             ----hheellpp display this help and exit
[32m+      
[32m+             ----vveerrssiioonn
[32m+                    output version information and exit
[32m+      
[32m+             The SIZE argument is an integer and  optional  unit  (example:  10K  is
[32m+             10*1024).   Units  are  K,M,G,T,P,E,Z,Y  (powers  of 1024) or KB,MB,...
[32m+             (powers of 1000).
[32m+      
[32m+             The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
[32m+             +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
[32m+             MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
[32m+             MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
[32m+             only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
[32m+             able sets the default style to use.
[32m+      
[32m+             Using  color  to distinguish file types is disabled both by default and
[32m+             with ----ccoolloorr=_n_e_v_e_r.  With ----ccoolloorr=_a_u_t_o, ls emits color codes only  when
[32m+             standard  output is connected to a terminal.  The LS_COLORS environment
[32m+             variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+         EExxiitt ssttaattuuss::
[32m+             0      if OK,
[32m+      
[32m+             1      if minor problems (e.g., cannot access subdirectory),
[32m+      
[32m+             2      if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      AAUUTTHHOORR
[32m+             Written by Richard M. Stallman and David MacKenzie.
[32m+      
[32m+      RREEPPOORRTTIINNGG BBUUGGSS
[32m+             GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+             Report ls translation bugs to <https://translationproject.org/team/>
[32m+      
[32m+      CCOOPPYYRRIIGGHHTT
[32m+             Copyright © 2017 Free Software Foundation, Inc.   License  GPLv3+:  GNU
[32m+             GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
[32m+             This  is  free  software:  you  are free to change and redistribute it.
[32m+             There is NO WARRANTY, to the extent permitted by law.
[32m+      
[32m+      SSEEEE AALLSSOO
[32m+             Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+             or available locally via: info '(coreutils) ls invocation'
[32m+      
[32m+      GNU coreutils 8.29               December 2017                           LS(1)

[0m[34m## replaced (type changed from NoneType to int) /cells/17/execution_count:[0m
[31m-  None
[32m+  6

[0m[34m## inserted before /cells/17/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      Usage: ls [OPTION]... [FILE]...
[32m+      List information about the FILEs (the current directory by default).
[32m+      Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
[32m+      
[32m+      Mandatory arguments to long options are mandatory for short options too.
[32m+        -a, --all                  do not ignore entries starting with .
[32m+        -A, --almost-all           do not list implied . and ..
[32m+            --author               with -l, print the author of each file
[32m+        -b, --escape               print C-style escapes for nongraphic characters
[32m+            --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
[32m+                                     e.g., '--block-size=M'; see SIZE format below
[32m+        -B, --ignore-backups       do not list implied entries ending with ~
[32m+        -c                         with -lt: sort by, and show, ctime (time of last
[32m+                                     modification of file status information);
[32m+                                     with -l: show ctime and sort by name;
[32m+                                     otherwise: sort by ctime, newest first
[32m+        -C                         list entries by columns
[32m+            --color[=WHEN]         colorize the output; WHEN can be 'always' (default
[32m+                                     if omitted), 'auto', or 'never'; more info below
[32m+        -d, --directory            list directories themselves, not their contents
[32m+        -D, --dired                generate output designed for Emacs' dired mode
[32m+        -f                         do not sort, enable -aU, disable -ls --color
[32m+        -F, --classify             append indicator (one of */=>@|) to entries
[32m+            --file-type            likewise, except do not append '*'
[32m+            --format=WORD          across -x, commas -m, horizontal -x, long -l,
[32m+                                     single-column -1, verbose -l, vertical -C
[32m+            --full-time            like -l --time-style=full-iso
[32m+        -g                         like -l, but do not list owner
[32m+            --group-directories-first
[32m+                                   group directories before files;
[32m+                                     can be augmented with a --sort option, but any
[32m+                                     use of --sort=none (-U) disables grouping
[32m+        -G, --no-group             in a long listing, don't print group names
[32m+        -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
[32m+            --si                   likewise, but use powers of 1000 not 1024
[32m+        -H, --dereference-command-line
[32m+                                   follow symbolic links listed on the command line
[32m+            --dereference-command-line-symlink-to-dir
[32m+                                   follow each command line symbolic link
[32m+                                     that points to a directory
[32m+            --hide=PATTERN         do not list implied entries matching shell PATTERN
[32m+                                     (overridden by -a or -A)
[32m+            --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
[32m+                                     (default if omitted), 'auto', or 'never'
[32m+            --indicator-style=WORD  append indicator with style WORD to entry names:
[32m+                                     none (default), slash (-p),
[32m+                                     file-type (--file-type), classify (-F)
[32m+        -i, --inode                print the index number of each file
[32m+        -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
[32m+        -k, --kibibytes            default to 1024-byte blocks for disk usage;
[32m+                                     used only with -s and per directory totals
[32m+        -l                         use a long listing format
[32m+        -L, --dereference          when showing file information for a symbolic
[32m+                                     link, show information for the file the link
[32m+                                     references rather than for the link itself
[32m+        -m                         fill width with a comma separated list of entries
[32m+        -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
[32m+        -N, --literal              print entry names without quoting
[32m+        -o                         like -l, but do not list group information
[32m+        -p, --indicator-style=slash
[32m+                                   append / indicator to directories
[32m+        -q, --hide-control-chars   print ? instead of nongraphic characters
[32m+            --show-control-chars   show nongraphic characters as-is (the default,
[32m+                                     unless program is 'ls' and output is a terminal)
[32m+        -Q, --quote-name           enclose entry names in double quotes
[32m+            --quoting-style=WORD   use quoting style WORD for entry names:
[32m+                                     literal, locale, shell, shell-always,
[32m+                                     shell-escape, shell-escape-always, c, escape
[32m+                                     (overrides QUOTING_STYLE environment variable)
[32m+        -r, --reverse              reverse order while sorting
[32m+        -R, --recursive            list subdirectories recursively
[32m+        -s, --size                 print the allocated size of each file, in blocks
[32m+        -S                         sort by file size, largest first
[32m+            --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
[32m+                                     time (-t), version (-v), extension (-X)
[32m+            --time=WORD            with -l, show time as WORD instead of default
[32m+                                     modification time: atime or access or use (-u);
[32m+                                     ctime or status (-c); also use specified time
[32m+                                     as sort key if --sort=time (newest first)
[32m+            --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
[32m+        -t                         sort by modification time, newest first
[32m+        -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
[32m+        -u                         with -lt: sort by, and show, access time;
[32m+                                     with -l: show access time and sort by name;
[32m+                                     otherwise: sort by access time, newest first
[32m+        -U                         do not sort; list entries in directory order
[32m+        -v                         natural sort of (version) numbers within text
[32m+        -w, --width=COLS           set output width to COLS.  0 means no limit
[32m+        -x                         list entries by lines instead of by columns
[32m+        -X                         sort alphabetically by entry extension
[32m+        -Z, --context              print any security context of each file
[32m+        -1                         list one file per line.  Avoid '\n' with -q or -b
[32m+            --help     display this help and exit
[32m+            --version  output version information and exit
[32m+      
[32m+      The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
[32m+      Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
[32m+      
[32m+      The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
[32m+      FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
[32m+      then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
[32m+      TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
[32m+      Also the TIME_STYLE environment variable sets the default style to use.
[32m+      
[32m+      Using color to distinguish file types is disabled both by default and
[32m+      with --color=never.  With --color=auto, ls emits color codes only when
[32m+      standard output is connected to a terminal.  The LS_COLORS environment
[32m+      variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+      Exit status:
[32m+       0  if OK,
[32m+       1  if minor problems (e.g., cannot access subdirectory),
[32m+       2  if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+      Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+      or available locally via: info '(coreutils) ls invocation'

[0m[34m## replaced (type changed from NoneType to int) /cells/20/execution_count:[0m
[31m-  None
[32m+  7

[0m[34m## inserted before /cells/20/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      LS(1)                            User Commands                           LS(1)
[32m+      
[32m+      NNAAMMEE
[32m+             ls - list directory contents
[32m+      
[32m+      SSYYNNOOPPSSIISS
[32m+             llss [_O_P_T_I_O_N]... [_F_I_L_E]...
[32m+      
[32m+      DDEESSCCRRIIPPTTIIOONN
[32m+             List  information  about  the FILEs (the current directory by default).
[32m+             Sort entries alphabetically if none of --ccffttuuvvSSUUXX nor ----ssoorrtt  is  speci‐
[32m+             fied.
[32m+      
[32m+             Mandatory  arguments  to  long  options are mandatory for short options
[32m+             too.
[32m+      
[32m+             --aa, ----aallll
[32m+                    do not ignore entries starting with .
[32m+      
[32m+             --AA, ----aallmmoosstt--aallll
[32m+                    do not list implied . and ..
[32m+      
[32m+             ----aauutthhoorr
[32m+                    with --ll, print the author of each file
[32m+      
[32m+             --bb, ----eessccaappee
[32m+                    print C-style escapes for nongraphic characters
[32m+      
[32m+             ----bblloocckk--ssiizzee=_S_I_Z_E
[32m+                    with  --ll,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
[32m+                    '--block-size=M'; see SIZE format below
[32m+      
[32m+             --BB, ----iiggnnoorree--bbaacckkuuppss
[32m+                    do not list implied entries ending with ~
[32m+      
[32m+             --cc     with --lltt: sort by, and show, ctime (time of last modification of
[32m+                    file status information); with --ll: show ctime and sort by  name;
[32m+                    otherwise: sort by ctime, newest first
[32m+      
[32m+             --CC     list entries by columns
[32m+      
[32m+             ----ccoolloorr[=_W_H_E_N]
[32m+                    colorize  the output; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'; more info below
[32m+      
[32m+             --dd, ----ddiirreeccttoorryy
[32m+                    list directories themselves, not their contents
[32m+      
[32m+             --DD, ----ddiirreedd
[32m+                    generate output designed for Emacs' dired mode
[32m+      
[32m+             --ff     do not sort, enable --aaUU, disable --llss ----ccoolloorr
[32m+      
[32m+             --FF, ----ccllaassssiiffyy
[32m+                    append indicator (one of */=>@|) to entries
[32m+      
[32m+             ----ffiillee--ttyyppee
[32m+                    likewise, except do not append '*'
[32m+      
[32m+             ----ffoorrmmaatt=_W_O_R_D
[32m+                    across --xx, commas --mm, horizontal --xx, long --ll, single-column  --11,
[32m+                    verbose --ll, vertical --CC
[32m+      
[32m+             ----ffuullll--ttiimmee
[32m+                    like --ll ----ttiimmee--ssttyyllee=_f_u_l_l_-_i_s_o
[32m+      
[32m+             --gg     like --ll, but do not list owner
[32m+      
[32m+             ----ggrroouupp--ddiirreeccttoorriieess--ffiirrsstt
[32m+                    group directories before files;
[32m+      
[32m+                    can   be  augmented  with  a  ----ssoorrtt  option,  but  any  use  of
[32m+                    ----ssoorrtt=_n_o_n_e (--UU) disables grouping
[32m+      
[32m+             --GG, ----nnoo--ggrroouupp
[32m+                    in a long listing, don't print group names
[32m+      
[32m+             --hh, ----hhuummaann--rreeaaddaabbllee
[32m+                    with --ll and --ss, print sizes like 1K 234M 2G etc.
[32m+      
[32m+             ----ssii   likewise, but use powers of 1000 not 1024
[32m+      
[32m+             --HH, ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee
[32m+                    follow symbolic links listed on the command line
[32m+      
[32m+             ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee--ssyymmlliinnkk--ttoo--ddiirr
[32m+                    follow each command line symbolic link
[32m+      
[32m+                    that points to a directory
[32m+      
[32m+             ----hhiiddee=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell  PATTERN  (overridden
[32m+                    by --aa or --AA)
[32m+      
[32m+             ----hhyyppeerrlliinnkk[=_W_H_E_N]
[32m+                    hyperlink file names; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'
[32m+      
[32m+             ----iinnddiiccaattoorr--ssttyyllee=_W_O_R_D
[32m+                    append indicator with style WORD to entry names: none (default),
[32m+                    slash (--pp), file-type (----ffiillee--ttyyppee), classify (--FF)
[32m+      
[32m+             --ii, ----iinnooddee
[32m+                    print the index number of each file
[32m+      
[32m+             --II, ----iiggnnoorree=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell PATTERN
[32m+      
[32m+             --kk, ----kkiibbiibbyytteess
[32m+                    default  to  1024-byte  blocks for disk usage; used only with --ss
[32m+                    and per directory totals
[32m+      
[32m+             --ll     use a long listing format
[32m+      
[32m+             --LL, ----ddeerreeffeerreennccee
[32m+                    when showing file information for a symbolic link, show informa‐
[32m+                    tion  for  the file the link references rather than for the link
[32m+                    itself
[32m+      
[32m+             --mm     fill width with a comma separated list of entries
[32m+      
[32m+             --nn, ----nnuummeerriicc--uuiidd--ggiidd
[32m+                    like --ll, but list numeric user and group IDs
[32m+      
[32m+             --NN, ----lliitteerraall
[32m+                    print entry names without quoting
[32m+      
[32m+             --oo     like --ll, but do not list group information
[32m+      
[32m+             --pp, ----iinnddiiccaattoorr--ssttyyllee=_s_l_a_s_h
[32m+                    append / indicator to directories
[32m+      
[32m+             --qq, ----hhiiddee--ccoonnttrrooll--cchhaarrss
[32m+                    print ? instead of nongraphic characters
[32m+      
[32m+             ----sshhooww--ccoonnttrrooll--cchhaarrss
[32m+                    show nongraphic characters as-is (the default, unless program is
[32m+                    'ls' and output is a terminal)
[32m+      
[32m+             --QQ, ----qquuoottee--nnaammee
[32m+                    enclose entry names in double quotes
[32m+      
[32m+             ----qquuoottiinngg--ssttyyllee=_W_O_R_D
[32m+                    use  quoting style WORD for entry names: literal, locale, shell,
[32m+                    shell-always,  shell-escape,  shell-escape-always,   c,   escape
[32m+                    (overrides QUOTING_STYLE environment variable)
[32m+      
[32m+             --rr, ----rreevveerrssee
[32m+                    reverse order while sorting
[32m+      
[32m+             --RR, ----rreeccuurrssiivvee
[32m+                    list subdirectories recursively
[32m+      
[32m+             --ss, ----ssiizzee
[32m+                    print the allocated size of each file, in blocks
[32m+      
[32m+             --SS     sort by file size, largest first
[32m+      
[32m+             ----ssoorrtt=_W_O_R_D
[32m+                    sort  by  WORD instead of name: none (--UU), size (--SS), time (--tt),
[32m+                    version (--vv), extension (--XX)
[32m+      
[32m+             ----ttiimmee=_W_O_R_D
[32m+                    with --ll, show time as WORD instead of default modification time:
[32m+                    atime  or  access  or  use  (--uu); ctime or status (--cc); also use
[32m+                    specified time as sort key if ----ssoorrtt=_t_i_m_e (newest first)
[32m+      
[32m+             ----ttiimmee--ssttyyllee=_T_I_M_E___S_T_Y_L_E
[32m+                    time/date format with --ll; see TIME_STYLE below
[32m+      
[32m+             --tt     sort by modification time, newest first
[32m+      
[32m+             --TT, ----ttaabbssiizzee=_C_O_L_S
[32m+                    assume tab stops at each COLS instead of 8
[32m+      
[32m+             --uu     with --lltt: sort by, and show, access time; with --ll:  show  access
[32m+                    time  and  sort  by name; otherwise: sort by access time, newest
[32m+                    first
[32m+      
[32m+             --UU     do not sort; list entries in directory order
[32m+      
[32m+             --vv     natural sort of (version) numbers within text
[32m+      
[32m+             --ww, ----wwiiddtthh=_C_O_L_S
[32m+                    set output width to COLS.  0 means no limit
[32m+      
[32m+             --xx     list entries by lines instead of by columns
[32m+      
[32m+             --XX     sort alphabetically by entry extension
[32m+      
[32m+             --ZZ, ----ccoonntteexxtt
[32m+                    print any security context of each file
[32m+      
[32m+             --11     list one file per line.  Avoid '\n' with --qq or --bb
[32m+      
[32m+             ----hheellpp display this help and exit
[32m+      
[32m+             ----vveerrssiioonn
[32m+                    output version information and exit
[32m+      
[32m+             The SIZE argument is an integer and  optional  unit  (example:  10K  is
[32m+             10*1024).   Units  are  K,M,G,T,P,E,Z,Y  (powers  of 1024) or KB,MB,...
[32m+             (powers of 1000).
[32m+      
[32m+             The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
[32m+             +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
[32m+             MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
[32m+             MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
[32m+             only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
[32m+             able sets the default style to use.
[32m+      
[32m+             Using  color  to distinguish file types is disabled both by default and
[32m+             with ----ccoolloorr=_n_e_v_e_r.  With ----ccoolloorr=_a_u_t_o, ls emits color codes only  when
[32m+             standard  output is connected to a terminal.  The LS_COLORS environment
[32m+             variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+         EExxiitt ssttaattuuss::
[32m+             0      if OK,
[32m+      
[32m+             1      if minor problems (e.g., cannot access subdirectory),
[32m+      
[32m+             2      if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      AAUUTTHHOORR
[32m+             Written by Richard M. Stallman and David MacKenzie.
[32m+      
[32m+      RREEPPOORRTTIINNGG BBUUGGSS
[32m+             GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+             Report ls translation bugs to <https://translationproject.org/team/>
[32m+      
[32m+      CCOOPPYYRRIIGGHHTT
[32m+             Copyright © 2017 Free Software Foundation, Inc.   License  GPLv3+:  GNU
[32m+             GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
[32m+             This  is  free  software:  you  are free to change and redistribute it.
[32m+             There is NO WARRANTY, to the extent permitted by law.
[32m+      
[32m+      SSEEEE AALLSSOO
[32m+             Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+             or available locally via: info '(coreutils) ls invocation'
[32m+      
[32m+      GNU coreutils 8.29               December 2017                           LS(1)

[0m[34m## replaced (type changed from NoneType to int) /cells/21/execution_count:[0m
[31m-  None
[32m+  8

[0m[34m## inserted before /cells/21/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'Desktop': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/23/execution_count:[0m
[31m-  None
[32m+  9

[0m[34m## inserted before /cells/23/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'Desktop/data-shell': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/25/execution_count:[0m
[31m-  None
[32m+  10

[0m[34m## inserted before /cells/25/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: Desktop: No such file or directory
[32m+      bash: cd: data-shell: No such file or directory
[32m+      bash: cd: data: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/27/execution_count:[0m
[31m-  None
[32m+  11

[0m[34m## inserted before /cells/27/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/28/execution_count:[0m
[31m-  None
[32m+  12

[0m[34m## inserted before /cells/28/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/30/execution_count:[0m
[31m-  None
[32m+  13

[0m[34m## inserted before /cells/30/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: data-shell: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/32/execution_count:[0m
[31m-  None
[32m+  14

[0m[34m## replaced (type changed from NoneType to int) /cells/34/execution_count:[0m
[31m-  None
[32m+  15

[0m[34m## inserted before /cells/34/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks

[0m[34m## replaced (type changed from NoneType to int) /cells/36/execution_count:[0m
[31m-  None
[32m+  16

[0m[34m## inserted before /cells/36/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ./			     03-fundamentals-of-python/   12-images-and-vis/
[32m+      ../			     04-further-python/		  environment.yml
[32m+      00-lessons_instructor.ipynb  05-writing-effective-tests/  .git
[32m+      00-lessons.ipynb	     06-approximating-pi/	  .gitignore
[32m+      01-bash/		     07-collaborating-with-git/
[32m+      02-git/			     08-collaborating-with-git/

[0m[34m## replaced (type changed from NoneType to int) /cells/41/execution_count:[0m
[31m-  None
[32m+  17

[0m[34m## replaced (type changed from NoneType to int) /cells/43/execution_count:[0m
[31m-  None
[32m+  18

[0m[34m## inserted before /cells/43/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart

[0m[34m## replaced (type changed from NoneType to int) /cells/45/execution_count:[0m
[31m-  None
[32m+  19

[0m[34m## inserted before /cells/45/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: Desktop/data-shell/data: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/47/execution_count:[0m
[31m-  None
[32m+  20

[0m[34m## inserted before /cells/47/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart

[0m[34m## replaced (type changed from NoneType to int) /cells/48/execution_count:[0m
[31m-  None
[32m+  21

[0m[34m## inserted before /cells/48/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: /Users/nelle/Desktop/data-shell: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/60/execution_count:[0m
[31m-  None
[32m+  22

[0m[34m## inserted before /cells/60/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'north-pacific-gyre/2012-07-03/': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/62/execution_count:[0m
[31m-  None
[32m+  23

[0m[34m## inserted before /cells/62/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'nor': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/64/execution_count:[0m
[31m-  None
[32m+  24

[0m[34m## inserted before /cells/64/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'north-pacific-gyre/': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0mnbdiff /tmp/ZjH7CL_03-working-with-files-and-directories_instructor.ipynb 01-bash/03-working-with-files-and-directories_instructor.ipynb
--- /tmp/ZjH7CL_03-working-with-files-and-directories_instructor.ipynb  2018-08-30 12:07:35.498860
+++ 01-bash/03-working-with-files-and-directories_instructor.ipynb  2018-08-30 12:07:21.372353
[34m## replaced (type changed from NoneType to int) /cells/1/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## replaced (type changed from NoneType to int) /cells/3/execution_count:[0m
[31m-  None
[32m+  2

[0m[34m## inserted before /cells/3/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/4/execution_count:[0m
[31m-  None
[32m+  3

[0m[34m## inserted before /cells/4/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png

[0m[34m## replaced (type changed from NoneType to int) /cells/6/execution_count:[0m
[31m-  None
[32m+  4

[0m[34m## replaced (type changed from NoneType to int) /cells/8/execution_count:[0m
[31m-  None
[32m+  5

[0m[34m## inserted before /cells/8/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/12/execution_count:[0m
[31m-  None
[32m+  6

[0m[34m## replaced (type changed from NoneType to int) /cells/14/execution_count:[0m
[31m-  None
[32m+  7

[0m[34m## replaced (type changed from NoneType to int) /cells/15/execution_count:[0m
[31m-  None
[32m+  8

[0m[34m## replaced (type changed from NoneType to int) /cells/20/execution_count:[0m
[31m-  None
[32m+  9

[0m[34m## inserted before /cells/20/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/24/execution_count:[0m
[31m-  None
[32m+  10

[0m[34m## replaced (type changed from NoneType to int) /cells/26/execution_count:[0m
[31m-  None
[32m+  11

[0m[34m## replaced (type changed from NoneType to int) /cells/29/execution_count:[0m
[31m-  None
[32m+  12

[0m[34m## inserted before /cells/29/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash/thesis

[0m[34m## replaced (type changed from NoneType to int) /cells/30/execution_count:[0m
[31m-  None
[32m+  13

[0m[34m## replaced (type changed from NoneType to int) /cells/31/execution_count:[0m
[31m-  None
[32m+  14

[0m[34m## inserted before /cells/31/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/32/execution_count:[0m
[31m-  None
[32m+  15

[0m[34m## replaced (type changed from NoneType to int) /cells/34/execution_count:[0m
[31m-  None
[32m+  16

[0m[34m## inserted before /cells/34/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      rm: cannot remove 'thesis': Is a directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/36/execution_count:[0m
[31m-  None
[32m+  17

[0m[34m## replaced (type changed from NoneType to int) /cells/41/execution_count:[0m
[31m-  None
[32m+  18

[0m[34m## inserted before /cells/41/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/42/execution_count:[0m
[31m-  None
[32m+  19

[0m[34m## replaced (type changed from NoneType to int) /cells/43/execution_count:[0m
[31m-  None
[32m+  20

[0m[34m## replaced (type changed from NoneType to int) /cells/44/execution_count:[0m
[31m-  None
[32m+  21

[0m[34m## replaced (type changed from NoneType to int) /cells/45/execution_count:[0m
[31m-  None
[32m+  22

[0m[34m## inserted before /cells/45/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/47/execution_count:[0m
[31m-  None
[32m+  23

[0m[34m## replaced (type changed from NoneType to int) /cells/49/execution_count:[0m
[31m-  None
[32m+  24

[0m[34m## inserted before /cells/49/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/51/execution_count:[0m
[31m-  None
[32m+  25

[0m[34m## replaced (type changed from NoneType to int) /cells/53/execution_count:[0m
[31m-  None
[32m+  26

[0m[34m## replaced (type changed from NoneType to int) /cells/55/execution_count:[0m
[31m-  None
[32m+  27

[0m[34m## inserted before /cells/55/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/59/execution_count:[0m
[31m-  None
[32m+  28

[0m[34m## replaced (type changed from NoneType to int) /cells/60/execution_count:[0m
[31m-  None
[32m+  29

[0m[34m## inserted before /cells/60/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt  thesis/quotations.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/62/execution_count:[0m
[31m-  None
[32m+  30

[0m[34m## replaced (type changed from NoneType to int) /cells/63/execution_count:[0m
[31m-  None
[32m+  31

[0m[34m## inserted before /cells/63/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'quotes.txt': No such file or directory
[32m+      thesis/quotations.txt
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0mnbdiff /tmp/wOHJRo_01-introduction-to-version-control_instructor.ipynb 02-git/01-introduction-to-version-control_instructor.ipynb
--- /tmp/wOHJRo_01-introduction-to-version-control_instructor.ipynb  2018-08-30 12:07:36.225519
+++ 02-git/01-introduction-to-version-control_instructor.ipynb  2018-08-30 12:07:29.392262
[34m## replaced (type changed from NoneType to int) /cells/7/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/7/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      user.name=Stuart Mumford
[32m+      user.email=stuart@cadair.com
[32m+      user.signingkey=E6276769
[32m+      commit.gpgsign=true
[32m+      push.default=simple
[32m+      alias.log=log --show-signature
[32m+      difftool.latex.cmd=latexdiff  $LOCAL $REMOTE
[32m+      difftool.latexadd.cmd=latexdiff --graphics-markup=none -t BOLD -f IDENTICAL -s COLOR -X caption $LOCAL $REMOTE
[32m+      difftool.prompt=false
[32m+      alias.ldiff=difftool -t latex
[32m+      alias.ldiffadd=difftool -t latexadd
[32m+      alias.tree=log --decorate --graph --show-signature
[32m+      alias.wdiff=diff
[32m+      credential.helper=/usr/lib/git-core/git-credential-gnome-keyring
[32m+      filter.lfs.clean=git-lfs clean %f
[32m+      filter.lfs.smudge=git-lfs smudge %f
[32m+      filter.lfs.required=true
[32m+      color.ui=auto
[32m+      core.editor=vim
[32m+      github.user=Cadair
[32m+      github.oauth-token=1f70bdc8ea2446bd1f2fd3c30fefa8ce1b31e676
[32m+      url.git@github.com:.insteadof=gh:
[32m+      url.git@gitlab.com:.insteadof=gl:
[32m+      diff.jupyternotebook.command=git-nbdiffdriver diff
[32m+      merge.jupyternotebook.driver=git-nbmergedriver merge %O %A %B %L %P
[32m+      merge.jupyternotebook.name=jupyter notebook merge driver
[32m+      difftool.nbdime.cmd=git-nbdifftool diff "$LOCAL" "$REMOTE"
[32m+      mergetool.nbdime.cmd=git-nbmergetool merge "$BASE" "$LOCAL" "$REMOTE" "$MERGED"
[32m+      mergetool.prompt=false
[32m+      magithub.online=false
[32m+      magithub.status.includestatusheader=false
[32m+      magithub.status.includepullrequestssection=false
[32m+      magithub.status.includeissuessection=false
[32m+      core.repositoryformatversion=0
[32m+      core.filemode=true
[32m+      core.bare=false
[32m+      core.logallrefupdates=true
[32m+      core.worktree=../../../notebooks
[32m+      remote.origin.url=https://github.com/cadair/rcsc_notebooks
[32m+      remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
[32m+      branch.master.remote=origin
[32m+      branch.master.merge=refs/heads/master
[32m+      

[0m

```

So far, so good: we’ve added one line to the end of the file (shown with a + in the first column). Now let’s put that change in the staging area and see what git diff reports:


{:.input_area}
```xonsh
git add mars.txt
git diff
```

{:.output_stream}
```

nbdiff /tmp/LRpTQq_01-introducing-the-shell_instructor.ipynb 01-bash/01-introducing-the-shell_instructor.ipynb
--- /tmp/LRpTQq_01-introducing-the-shell_instructor.ipynb  2018-08-30 12:07:37.248840
+++ 01-bash/01-introducing-the-shell_instructor.ipynb  2018-08-30 12:07:15.235755
[34m## replaced (type changed from NoneType to int) /cells/4/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/4/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      1TB-1/	boot/  dev/    home/   misc/  opt/   run/   sys/  var/
[32m+      1TB-2/	cifs/  etc/    lib@    mnt/   proc/  sbin@  tmp/  windows/
[32m+      bin@	data/  games/  lib64@  net/   root/  srv/   usr/

[0mnbdiff /tmp/1BfiX1_02-files-and-directories_instructor.ipynb 01-bash/02-files-and-directories_instructor.ipynb
--- /tmp/1BfiX1_02-files-and-directories_instructor.ipynb  2018-08-30 12:07:37.725502
+++ 01-bash/02-files-and-directories_instructor.ipynb  2018-08-30 12:07:27.595616
[34m## replaced (type changed from NoneType to int) /cells/2/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/2/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/8/execution_count:[0m
[31m-  None
[32m+  2

[0m[34m## inserted before /cells/8/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis

[0m[34m## replaced (type changed from NoneType to int) /cells/10/execution_count:[0m
[31m-  None
[32m+  3

[0m[34m## inserted before /cells/10/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/12/execution_count:[0m
[31m-  None
[32m+  4

[0m[34m## inserted before /cells/12/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      Usage: ls [OPTION]... [FILE]...
[32m+      List information about the FILEs (the current directory by default).
[32m+      Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
[32m+      
[32m+      Mandatory arguments to long options are mandatory for short options too.
[32m+        -a, --all                  do not ignore entries starting with .
[32m+        -A, --almost-all           do not list implied . and ..
[32m+            --author               with -l, print the author of each file
[32m+        -b, --escape               print C-style escapes for nongraphic characters
[32m+            --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
[32m+                                     e.g., '--block-size=M'; see SIZE format below
[32m+        -B, --ignore-backups       do not list implied entries ending with ~
[32m+        -c                         with -lt: sort by, and show, ctime (time of last
[32m+                                     modification of file status information);
[32m+                                     with -l: show ctime and sort by name;
[32m+                                     otherwise: sort by ctime, newest first
[32m+        -C                         list entries by columns
[32m+            --color[=WHEN]         colorize the output; WHEN can be 'always' (default
[32m+                                     if omitted), 'auto', or 'never'; more info below
[32m+        -d, --directory            list directories themselves, not their contents
[32m+        -D, --dired                generate output designed for Emacs' dired mode
[32m+        -f                         do not sort, enable -aU, disable -ls --color
[32m+        -F, --classify             append indicator (one of */=>@|) to entries
[32m+            --file-type            likewise, except do not append '*'
[32m+            --format=WORD          across -x, commas -m, horizontal -x, long -l,
[32m+                                     single-column -1, verbose -l, vertical -C
[32m+            --full-time            like -l --time-style=full-iso
[32m+        -g                         like -l, but do not list owner
[32m+            --group-directories-first
[32m+                                   group directories before files;
[32m+                                     can be augmented with a --sort option, but any
[32m+                                     use of --sort=none (-U) disables grouping
[32m+        -G, --no-group             in a long listing, don't print group names
[32m+        -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
[32m+            --si                   likewise, but use powers of 1000 not 1024
[32m+        -H, --dereference-command-line
[32m+                                   follow symbolic links listed on the command line
[32m+            --dereference-command-line-symlink-to-dir
[32m+                                   follow each command line symbolic link
[32m+                                     that points to a directory
[32m+            --hide=PATTERN         do not list implied entries matching shell PATTERN
[32m+                                     (overridden by -a or -A)
[32m+            --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
[32m+                                     (default if omitted), 'auto', or 'never'
[32m+            --indicator-style=WORD  append indicator with style WORD to entry names:
[32m+                                     none (default), slash (-p),
[32m+                                     file-type (--file-type), classify (-F)
[32m+        -i, --inode                print the index number of each file
[32m+        -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
[32m+        -k, --kibibytes            default to 1024-byte blocks for disk usage;
[32m+                                     used only with -s and per directory totals
[32m+        -l                         use a long listing format
[32m+        -L, --dereference          when showing file information for a symbolic
[32m+                                     link, show information for the file the link
[32m+                                     references rather than for the link itself
[32m+        -m                         fill width with a comma separated list of entries
[32m+        -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
[32m+        -N, --literal              print entry names without quoting
[32m+        -o                         like -l, but do not list group information
[32m+        -p, --indicator-style=slash
[32m+                                   append / indicator to directories
[32m+        -q, --hide-control-chars   print ? instead of nongraphic characters
[32m+            --show-control-chars   show nongraphic characters as-is (the default,
[32m+                                     unless program is 'ls' and output is a terminal)
[32m+        -Q, --quote-name           enclose entry names in double quotes
[32m+            --quoting-style=WORD   use quoting style WORD for entry names:
[32m+                                     literal, locale, shell, shell-always,
[32m+                                     shell-escape, shell-escape-always, c, escape
[32m+                                     (overrides QUOTING_STYLE environment variable)
[32m+        -r, --reverse              reverse order while sorting
[32m+        -R, --recursive            list subdirectories recursively
[32m+        -s, --size                 print the allocated size of each file, in blocks
[32m+        -S                         sort by file size, largest first
[32m+            --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
[32m+                                     time (-t), version (-v), extension (-X)
[32m+            --time=WORD            with -l, show time as WORD instead of default
[32m+                                     modification time: atime or access or use (-u);
[32m+                                     ctime or status (-c); also use specified time
[32m+                                     as sort key if --sort=time (newest first)
[32m+            --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
[32m+        -t                         sort by modification time, newest first
[32m+        -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
[32m+        -u                         with -lt: sort by, and show, access time;
[32m+                                     with -l: show access time and sort by name;
[32m+                                     otherwise: sort by access time, newest first
[32m+        -U                         do not sort; list entries in directory order
[32m+        -v                         natural sort of (version) numbers within text
[32m+        -w, --width=COLS           set output width to COLS.  0 means no limit
[32m+        -x                         list entries by lines instead of by columns
[32m+        -X                         sort alphabetically by entry extension
[32m+        -Z, --context              print any security context of each file
[32m+        -1                         list one file per line.  Avoid '\n' with -q or -b
[32m+            --help     display this help and exit
[32m+            --version  output version information and exit
[32m+      
[32m+      The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
[32m+      Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
[32m+      
[32m+      The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
[32m+      FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
[32m+      then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
[32m+      TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
[32m+      Also the TIME_STYLE environment variable sets the default style to use.
[32m+      
[32m+      Using color to distinguish file types is disabled both by default and
[32m+      with --color=never.  With --color=auto, ls emits color codes only when
[32m+      standard output is connected to a terminal.  The LS_COLORS environment
[32m+      variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+      Exit status:
[32m+       0  if OK,
[32m+       1  if minor problems (e.g., cannot access subdirectory),
[32m+       2  if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+      Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+      or available locally via: info '(coreutils) ls invocation'

[0m[34m## replaced (type changed from NoneType to int) /cells/14/execution_count:[0m
[31m-  None
[32m+  5

[0m[34m## inserted before /cells/14/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      LS(1)                            User Commands                           LS(1)
[32m+      
[32m+      NNAAMMEE
[32m+             ls - list directory contents
[32m+      
[32m+      SSYYNNOOPPSSIISS
[32m+             llss [_O_P_T_I_O_N]... [_F_I_L_E]...
[32m+      
[32m+      DDEESSCCRRIIPPTTIIOONN
[32m+             List  information  about  the FILEs (the current directory by default).
[32m+             Sort entries alphabetically if none of --ccffttuuvvSSUUXX nor ----ssoorrtt  is  speci‐
[32m+             fied.
[32m+      
[32m+             Mandatory  arguments  to  long  options are mandatory for short options
[32m+             too.
[32m+      
[32m+             --aa, ----aallll
[32m+                    do not ignore entries starting with .
[32m+      
[32m+             --AA, ----aallmmoosstt--aallll
[32m+                    do not list implied . and ..
[32m+      
[32m+             ----aauutthhoorr
[32m+                    with --ll, print the author of each file
[32m+      
[32m+             --bb, ----eessccaappee
[32m+                    print C-style escapes for nongraphic characters
[32m+      
[32m+             ----bblloocckk--ssiizzee=_S_I_Z_E
[32m+                    with  --ll,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
[32m+                    '--block-size=M'; see SIZE format below
[32m+      
[32m+             --BB, ----iiggnnoorree--bbaacckkuuppss
[32m+                    do not list implied entries ending with ~
[32m+      
[32m+             --cc     with --lltt: sort by, and show, ctime (time of last modification of
[32m+                    file status information); with --ll: show ctime and sort by  name;
[32m+                    otherwise: sort by ctime, newest first
[32m+      
[32m+             --CC     list entries by columns
[32m+      
[32m+             ----ccoolloorr[=_W_H_E_N]
[32m+                    colorize  the output; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'; more info below
[32m+      
[32m+             --dd, ----ddiirreeccttoorryy
[32m+                    list directories themselves, not their contents
[32m+      
[32m+             --DD, ----ddiirreedd
[32m+                    generate output designed for Emacs' dired mode
[32m+      
[32m+             --ff     do not sort, enable --aaUU, disable --llss ----ccoolloorr
[32m+      
[32m+             --FF, ----ccllaassssiiffyy
[32m+                    append indicator (one of */=>@|) to entries
[32m+      
[32m+             ----ffiillee--ttyyppee
[32m+                    likewise, except do not append '*'
[32m+      
[32m+             ----ffoorrmmaatt=_W_O_R_D
[32m+                    across --xx, commas --mm, horizontal --xx, long --ll, single-column  --11,
[32m+                    verbose --ll, vertical --CC
[32m+      
[32m+             ----ffuullll--ttiimmee
[32m+                    like --ll ----ttiimmee--ssttyyllee=_f_u_l_l_-_i_s_o
[32m+      
[32m+             --gg     like --ll, but do not list owner
[32m+      
[32m+             ----ggrroouupp--ddiirreeccttoorriieess--ffiirrsstt
[32m+                    group directories before files;
[32m+      
[32m+                    can   be  augmented  with  a  ----ssoorrtt  option,  but  any  use  of
[32m+                    ----ssoorrtt=_n_o_n_e (--UU) disables grouping
[32m+      
[32m+             --GG, ----nnoo--ggrroouupp
[32m+                    in a long listing, don't print group names
[32m+      
[32m+             --hh, ----hhuummaann--rreeaaddaabbllee
[32m+                    with --ll and --ss, print sizes like 1K 234M 2G etc.
[32m+      
[32m+             ----ssii   likewise, but use powers of 1000 not 1024
[32m+      
[32m+             --HH, ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee
[32m+                    follow symbolic links listed on the command line
[32m+      
[32m+             ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee--ssyymmlliinnkk--ttoo--ddiirr
[32m+                    follow each command line symbolic link
[32m+      
[32m+                    that points to a directory
[32m+      
[32m+             ----hhiiddee=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell  PATTERN  (overridden
[32m+                    by --aa or --AA)
[32m+      
[32m+             ----hhyyppeerrlliinnkk[=_W_H_E_N]
[32m+                    hyperlink file names; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'
[32m+      
[32m+             ----iinnddiiccaattoorr--ssttyyllee=_W_O_R_D
[32m+                    append indicator with style WORD to entry names: none (default),
[32m+                    slash (--pp), file-type (----ffiillee--ttyyppee), classify (--FF)
[32m+      
[32m+             --ii, ----iinnooddee
[32m+                    print the index number of each file
[32m+      
[32m+             --II, ----iiggnnoorree=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell PATTERN
[32m+      
[32m+             --kk, ----kkiibbiibbyytteess
[32m+                    default  to  1024-byte  blocks for disk usage; used only with --ss
[32m+                    and per directory totals
[32m+      
[32m+             --ll     use a long listing format
[32m+      
[32m+             --LL, ----ddeerreeffeerreennccee
[32m+                    when showing file information for a symbolic link, show informa‐
[32m+                    tion  for  the file the link references rather than for the link
[32m+                    itself
[32m+      
[32m+             --mm     fill width with a comma separated list of entries
[32m+      
[32m+             --nn, ----nnuummeerriicc--uuiidd--ggiidd
[32m+                    like --ll, but list numeric user and group IDs
[32m+      
[32m+             --NN, ----lliitteerraall
[32m+                    print entry names without quoting
[32m+      
[32m+             --oo     like --ll, but do not list group information
[32m+      
[32m+             --pp, ----iinnddiiccaattoorr--ssttyyllee=_s_l_a_s_h
[32m+                    append / indicator to directories
[32m+      
[32m+             --qq, ----hhiiddee--ccoonnttrrooll--cchhaarrss
[32m+                    print ? instead of nongraphic characters
[32m+      
[32m+             ----sshhooww--ccoonnttrrooll--cchhaarrss
[32m+                    show nongraphic characters as-is (the default, unless program is
[32m+                    'ls' and output is a terminal)
[32m+      
[32m+             --QQ, ----qquuoottee--nnaammee
[32m+                    enclose entry names in double quotes
[32m+      
[32m+             ----qquuoottiinngg--ssttyyllee=_W_O_R_D
[32m+                    use  quoting style WORD for entry names: literal, locale, shell,
[32m+                    shell-always,  shell-escape,  shell-escape-always,   c,   escape
[32m+                    (overrides QUOTING_STYLE environment variable)
[32m+      
[32m+             --rr, ----rreevveerrssee
[32m+                    reverse order while sorting
[32m+      
[32m+             --RR, ----rreeccuurrssiivvee
[32m+                    list subdirectories recursively
[32m+      
[32m+             --ss, ----ssiizzee
[32m+                    print the allocated size of each file, in blocks
[32m+      
[32m+             --SS     sort by file size, largest first
[32m+      
[32m+             ----ssoorrtt=_W_O_R_D
[32m+                    sort  by  WORD instead of name: none (--UU), size (--SS), time (--tt),
[32m+                    version (--vv), extension (--XX)
[32m+      
[32m+             ----ttiimmee=_W_O_R_D
[32m+                    with --ll, show time as WORD instead of default modification time:
[32m+                    atime  or  access  or  use  (--uu); ctime or status (--cc); also use
[32m+                    specified time as sort key if ----ssoorrtt=_t_i_m_e (newest first)
[32m+      
[32m+             ----ttiimmee--ssttyyllee=_T_I_M_E___S_T_Y_L_E
[32m+                    time/date format with --ll; see TIME_STYLE below
[32m+      
[32m+             --tt     sort by modification time, newest first
[32m+      
[32m+             --TT, ----ttaabbssiizzee=_C_O_L_S
[32m+                    assume tab stops at each COLS instead of 8
[32m+      
[32m+             --uu     with --lltt: sort by, and show, access time; with --ll:  show  access
[32m+                    time  and  sort  by name; otherwise: sort by access time, newest
[32m+                    first
[32m+      
[32m+             --UU     do not sort; list entries in directory order
[32m+      
[32m+             --vv     natural sort of (version) numbers within text
[32m+      
[32m+             --ww, ----wwiiddtthh=_C_O_L_S
[32m+                    set output width to COLS.  0 means no limit
[32m+      
[32m+             --xx     list entries by lines instead of by columns
[32m+      
[32m+             --XX     sort alphabetically by entry extension
[32m+      
[32m+             --ZZ, ----ccoonntteexxtt
[32m+                    print any security context of each file
[32m+      
[32m+             --11     list one file per line.  Avoid '\n' with --qq or --bb
[32m+      
[32m+             ----hheellpp display this help and exit
[32m+      
[32m+             ----vveerrssiioonn
[32m+                    output version information and exit
[32m+      
[32m+             The SIZE argument is an integer and  optional  unit  (example:  10K  is
[32m+             10*1024).   Units  are  K,M,G,T,P,E,Z,Y  (powers  of 1024) or KB,MB,...
[32m+             (powers of 1000).
[32m+      
[32m+             The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
[32m+             +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
[32m+             MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
[32m+             MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
[32m+             only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
[32m+             able sets the default style to use.
[32m+      
[32m+             Using  color  to distinguish file types is disabled both by default and
[32m+             with ----ccoolloorr=_n_e_v_e_r.  With ----ccoolloorr=_a_u_t_o, ls emits color codes only  when
[32m+             standard  output is connected to a terminal.  The LS_COLORS environment
[32m+             variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+         EExxiitt ssttaattuuss::
[32m+             0      if OK,
[32m+      
[32m+             1      if minor problems (e.g., cannot access subdirectory),
[32m+      
[32m+             2      if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      AAUUTTHHOORR
[32m+             Written by Richard M. Stallman and David MacKenzie.
[32m+      
[32m+      RREEPPOORRTTIINNGG BBUUGGSS
[32m+             GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+             Report ls translation bugs to <https://translationproject.org/team/>
[32m+      
[32m+      CCOOPPYYRRIIGGHHTT
[32m+             Copyright © 2017 Free Software Foundation, Inc.   License  GPLv3+:  GNU
[32m+             GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
[32m+             This  is  free  software:  you  are free to change and redistribute it.
[32m+             There is NO WARRANTY, to the extent permitted by law.
[32m+      
[32m+      SSEEEE AALLSSOO
[32m+             Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+             or available locally via: info '(coreutils) ls invocation'
[32m+      
[32m+      GNU coreutils 8.29               December 2017                           LS(1)

[0m[34m## replaced (type changed from NoneType to int) /cells/17/execution_count:[0m
[31m-  None
[32m+  6

[0m[34m## inserted before /cells/17/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      Usage: ls [OPTION]... [FILE]...
[32m+      List information about the FILEs (the current directory by default).
[32m+      Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
[32m+      
[32m+      Mandatory arguments to long options are mandatory for short options too.
[32m+        -a, --all                  do not ignore entries starting with .
[32m+        -A, --almost-all           do not list implied . and ..
[32m+            --author               with -l, print the author of each file
[32m+        -b, --escape               print C-style escapes for nongraphic characters
[32m+            --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
[32m+                                     e.g., '--block-size=M'; see SIZE format below
[32m+        -B, --ignore-backups       do not list implied entries ending with ~
[32m+        -c                         with -lt: sort by, and show, ctime (time of last
[32m+                                     modification of file status information);
[32m+                                     with -l: show ctime and sort by name;
[32m+                                     otherwise: sort by ctime, newest first
[32m+        -C                         list entries by columns
[32m+            --color[=WHEN]         colorize the output; WHEN can be 'always' (default
[32m+                                     if omitted), 'auto', or 'never'; more info below
[32m+        -d, --directory            list directories themselves, not their contents
[32m+        -D, --dired                generate output designed for Emacs' dired mode
[32m+        -f                         do not sort, enable -aU, disable -ls --color
[32m+        -F, --classify             append indicator (one of */=>@|) to entries
[32m+            --file-type            likewise, except do not append '*'
[32m+            --format=WORD          across -x, commas -m, horizontal -x, long -l,
[32m+                                     single-column -1, verbose -l, vertical -C
[32m+            --full-time            like -l --time-style=full-iso
[32m+        -g                         like -l, but do not list owner
[32m+            --group-directories-first
[32m+                                   group directories before files;
[32m+                                     can be augmented with a --sort option, but any
[32m+                                     use of --sort=none (-U) disables grouping
[32m+        -G, --no-group             in a long listing, don't print group names
[32m+        -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
[32m+            --si                   likewise, but use powers of 1000 not 1024
[32m+        -H, --dereference-command-line
[32m+                                   follow symbolic links listed on the command line
[32m+            --dereference-command-line-symlink-to-dir
[32m+                                   follow each command line symbolic link
[32m+                                     that points to a directory
[32m+            --hide=PATTERN         do not list implied entries matching shell PATTERN
[32m+                                     (overridden by -a or -A)
[32m+            --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
[32m+                                     (default if omitted), 'auto', or 'never'
[32m+            --indicator-style=WORD  append indicator with style WORD to entry names:
[32m+                                     none (default), slash (-p),
[32m+                                     file-type (--file-type), classify (-F)
[32m+        -i, --inode                print the index number of each file
[32m+        -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
[32m+        -k, --kibibytes            default to 1024-byte blocks for disk usage;
[32m+                                     used only with -s and per directory totals
[32m+        -l                         use a long listing format
[32m+        -L, --dereference          when showing file information for a symbolic
[32m+                                     link, show information for the file the link
[32m+                                     references rather than for the link itself
[32m+        -m                         fill width with a comma separated list of entries
[32m+        -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
[32m+        -N, --literal              print entry names without quoting
[32m+        -o                         like -l, but do not list group information
[32m+        -p, --indicator-style=slash
[32m+                                   append / indicator to directories
[32m+        -q, --hide-control-chars   print ? instead of nongraphic characters
[32m+            --show-control-chars   show nongraphic characters as-is (the default,
[32m+                                     unless program is 'ls' and output is a terminal)
[32m+        -Q, --quote-name           enclose entry names in double quotes
[32m+            --quoting-style=WORD   use quoting style WORD for entry names:
[32m+                                     literal, locale, shell, shell-always,
[32m+                                     shell-escape, shell-escape-always, c, escape
[32m+                                     (overrides QUOTING_STYLE environment variable)
[32m+        -r, --reverse              reverse order while sorting
[32m+        -R, --recursive            list subdirectories recursively
[32m+        -s, --size                 print the allocated size of each file, in blocks
[32m+        -S                         sort by file size, largest first
[32m+            --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
[32m+                                     time (-t), version (-v), extension (-X)
[32m+            --time=WORD            with -l, show time as WORD instead of default
[32m+                                     modification time: atime or access or use (-u);
[32m+                                     ctime or status (-c); also use specified time
[32m+                                     as sort key if --sort=time (newest first)
[32m+            --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
[32m+        -t                         sort by modification time, newest first
[32m+        -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
[32m+        -u                         with -lt: sort by, and show, access time;
[32m+                                     with -l: show access time and sort by name;
[32m+                                     otherwise: sort by access time, newest first
[32m+        -U                         do not sort; list entries in directory order
[32m+        -v                         natural sort of (version) numbers within text
[32m+        -w, --width=COLS           set output width to COLS.  0 means no limit
[32m+        -x                         list entries by lines instead of by columns
[32m+        -X                         sort alphabetically by entry extension
[32m+        -Z, --context              print any security context of each file
[32m+        -1                         list one file per line.  Avoid '\n' with -q or -b
[32m+            --help     display this help and exit
[32m+            --version  output version information and exit
[32m+      
[32m+      The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
[32m+      Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
[32m+      
[32m+      The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
[32m+      FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
[32m+      then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
[32m+      TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
[32m+      Also the TIME_STYLE environment variable sets the default style to use.
[32m+      
[32m+      Using color to distinguish file types is disabled both by default and
[32m+      with --color=never.  With --color=auto, ls emits color codes only when
[32m+      standard output is connected to a terminal.  The LS_COLORS environment
[32m+      variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+      Exit status:
[32m+       0  if OK,
[32m+       1  if minor problems (e.g., cannot access subdirectory),
[32m+       2  if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+      Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+      or available locally via: info '(coreutils) ls invocation'

[0m[34m## replaced (type changed from NoneType to int) /cells/20/execution_count:[0m
[31m-  None
[32m+  7

[0m[34m## inserted before /cells/20/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      LS(1)                            User Commands                           LS(1)
[32m+      
[32m+      NNAAMMEE
[32m+             ls - list directory contents
[32m+      
[32m+      SSYYNNOOPPSSIISS
[32m+             llss [_O_P_T_I_O_N]... [_F_I_L_E]...
[32m+      
[32m+      DDEESSCCRRIIPPTTIIOONN
[32m+             List  information  about  the FILEs (the current directory by default).
[32m+             Sort entries alphabetically if none of --ccffttuuvvSSUUXX nor ----ssoorrtt  is  speci‐
[32m+             fied.
[32m+      
[32m+             Mandatory  arguments  to  long  options are mandatory for short options
[32m+             too.
[32m+      
[32m+             --aa, ----aallll
[32m+                    do not ignore entries starting with .
[32m+      
[32m+             --AA, ----aallmmoosstt--aallll
[32m+                    do not list implied . and ..
[32m+      
[32m+             ----aauutthhoorr
[32m+                    with --ll, print the author of each file
[32m+      
[32m+             --bb, ----eessccaappee
[32m+                    print C-style escapes for nongraphic characters
[32m+      
[32m+             ----bblloocckk--ssiizzee=_S_I_Z_E
[32m+                    with  --ll,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
[32m+                    '--block-size=M'; see SIZE format below
[32m+      
[32m+             --BB, ----iiggnnoorree--bbaacckkuuppss
[32m+                    do not list implied entries ending with ~
[32m+      
[32m+             --cc     with --lltt: sort by, and show, ctime (time of last modification of
[32m+                    file status information); with --ll: show ctime and sort by  name;
[32m+                    otherwise: sort by ctime, newest first
[32m+      
[32m+             --CC     list entries by columns
[32m+      
[32m+             ----ccoolloorr[=_W_H_E_N]
[32m+                    colorize  the output; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'; more info below
[32m+      
[32m+             --dd, ----ddiirreeccttoorryy
[32m+                    list directories themselves, not their contents
[32m+      
[32m+             --DD, ----ddiirreedd
[32m+                    generate output designed for Emacs' dired mode
[32m+      
[32m+             --ff     do not sort, enable --aaUU, disable --llss ----ccoolloorr
[32m+      
[32m+             --FF, ----ccllaassssiiffyy
[32m+                    append indicator (one of */=>@|) to entries
[32m+      
[32m+             ----ffiillee--ttyyppee
[32m+                    likewise, except do not append '*'
[32m+      
[32m+             ----ffoorrmmaatt=_W_O_R_D
[32m+                    across --xx, commas --mm, horizontal --xx, long --ll, single-column  --11,
[32m+                    verbose --ll, vertical --CC
[32m+      
[32m+             ----ffuullll--ttiimmee
[32m+                    like --ll ----ttiimmee--ssttyyllee=_f_u_l_l_-_i_s_o
[32m+      
[32m+             --gg     like --ll, but do not list owner
[32m+      
[32m+             ----ggrroouupp--ddiirreeccttoorriieess--ffiirrsstt
[32m+                    group directories before files;
[32m+      
[32m+                    can   be  augmented  with  a  ----ssoorrtt  option,  but  any  use  of
[32m+                    ----ssoorrtt=_n_o_n_e (--UU) disables grouping
[32m+      
[32m+             --GG, ----nnoo--ggrroouupp
[32m+                    in a long listing, don't print group names
[32m+      
[32m+             --hh, ----hhuummaann--rreeaaddaabbllee
[32m+                    with --ll and --ss, print sizes like 1K 234M 2G etc.
[32m+      
[32m+             ----ssii   likewise, but use powers of 1000 not 1024
[32m+      
[32m+             --HH, ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee
[32m+                    follow symbolic links listed on the command line
[32m+      
[32m+             ----ddeerreeffeerreennccee--ccoommmmaanndd--lliinnee--ssyymmlliinnkk--ttoo--ddiirr
[32m+                    follow each command line symbolic link
[32m+      
[32m+                    that points to a directory
[32m+      
[32m+             ----hhiiddee=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell  PATTERN  (overridden
[32m+                    by --aa or --AA)
[32m+      
[32m+             ----hhyyppeerrlliinnkk[=_W_H_E_N]
[32m+                    hyperlink file names; WHEN can be 'always' (default if omitted),
[32m+                    'auto', or 'never'
[32m+      
[32m+             ----iinnddiiccaattoorr--ssttyyllee=_W_O_R_D
[32m+                    append indicator with style WORD to entry names: none (default),
[32m+                    slash (--pp), file-type (----ffiillee--ttyyppee), classify (--FF)
[32m+      
[32m+             --ii, ----iinnooddee
[32m+                    print the index number of each file
[32m+      
[32m+             --II, ----iiggnnoorree=_P_A_T_T_E_R_N
[32m+                    do not list implied entries matching shell PATTERN
[32m+      
[32m+             --kk, ----kkiibbiibbyytteess
[32m+                    default  to  1024-byte  blocks for disk usage; used only with --ss
[32m+                    and per directory totals
[32m+      
[32m+             --ll     use a long listing format
[32m+      
[32m+             --LL, ----ddeerreeffeerreennccee
[32m+                    when showing file information for a symbolic link, show informa‐
[32m+                    tion  for  the file the link references rather than for the link
[32m+                    itself
[32m+      
[32m+             --mm     fill width with a comma separated list of entries
[32m+      
[32m+             --nn, ----nnuummeerriicc--uuiidd--ggiidd
[32m+                    like --ll, but list numeric user and group IDs
[32m+      
[32m+             --NN, ----lliitteerraall
[32m+                    print entry names without quoting
[32m+      
[32m+             --oo     like --ll, but do not list group information
[32m+      
[32m+             --pp, ----iinnddiiccaattoorr--ssttyyllee=_s_l_a_s_h
[32m+                    append / indicator to directories
[32m+      
[32m+             --qq, ----hhiiddee--ccoonnttrrooll--cchhaarrss
[32m+                    print ? instead of nongraphic characters
[32m+      
[32m+             ----sshhooww--ccoonnttrrooll--cchhaarrss
[32m+                    show nongraphic characters as-is (the default, unless program is
[32m+                    'ls' and output is a terminal)
[32m+      
[32m+             --QQ, ----qquuoottee--nnaammee
[32m+                    enclose entry names in double quotes
[32m+      
[32m+             ----qquuoottiinngg--ssttyyllee=_W_O_R_D
[32m+                    use  quoting style WORD for entry names: literal, locale, shell,
[32m+                    shell-always,  shell-escape,  shell-escape-always,   c,   escape
[32m+                    (overrides QUOTING_STYLE environment variable)
[32m+      
[32m+             --rr, ----rreevveerrssee
[32m+                    reverse order while sorting
[32m+      
[32m+             --RR, ----rreeccuurrssiivvee
[32m+                    list subdirectories recursively
[32m+      
[32m+             --ss, ----ssiizzee
[32m+                    print the allocated size of each file, in blocks
[32m+      
[32m+             --SS     sort by file size, largest first
[32m+      
[32m+             ----ssoorrtt=_W_O_R_D
[32m+                    sort  by  WORD instead of name: none (--UU), size (--SS), time (--tt),
[32m+                    version (--vv), extension (--XX)
[32m+      
[32m+             ----ttiimmee=_W_O_R_D
[32m+                    with --ll, show time as WORD instead of default modification time:
[32m+                    atime  or  access  or  use  (--uu); ctime or status (--cc); also use
[32m+                    specified time as sort key if ----ssoorrtt=_t_i_m_e (newest first)
[32m+      
[32m+             ----ttiimmee--ssttyyllee=_T_I_M_E___S_T_Y_L_E
[32m+                    time/date format with --ll; see TIME_STYLE below
[32m+      
[32m+             --tt     sort by modification time, newest first
[32m+      
[32m+             --TT, ----ttaabbssiizzee=_C_O_L_S
[32m+                    assume tab stops at each COLS instead of 8
[32m+      
[32m+             --uu     with --lltt: sort by, and show, access time; with --ll:  show  access
[32m+                    time  and  sort  by name; otherwise: sort by access time, newest
[32m+                    first
[32m+      
[32m+             --UU     do not sort; list entries in directory order
[32m+      
[32m+             --vv     natural sort of (version) numbers within text
[32m+      
[32m+             --ww, ----wwiiddtthh=_C_O_L_S
[32m+                    set output width to COLS.  0 means no limit
[32m+      
[32m+             --xx     list entries by lines instead of by columns
[32m+      
[32m+             --XX     sort alphabetically by entry extension
[32m+      
[32m+             --ZZ, ----ccoonntteexxtt
[32m+                    print any security context of each file
[32m+      
[32m+             --11     list one file per line.  Avoid '\n' with --qq or --bb
[32m+      
[32m+             ----hheellpp display this help and exit
[32m+      
[32m+             ----vveerrssiioonn
[32m+                    output version information and exit
[32m+      
[32m+             The SIZE argument is an integer and  optional  unit  (example:  10K  is
[32m+             10*1024).   Units  are  K,M,G,T,P,E,Z,Y  (powers  of 1024) or KB,MB,...
[32m+             (powers of 1000).
[32m+      
[32m+             The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
[32m+             +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
[32m+             MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
[32m+             MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
[32m+             only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
[32m+             able sets the default style to use.
[32m+      
[32m+             Using  color  to distinguish file types is disabled both by default and
[32m+             with ----ccoolloorr=_n_e_v_e_r.  With ----ccoolloorr=_a_u_t_o, ls emits color codes only  when
[32m+             standard  output is connected to a terminal.  The LS_COLORS environment
[32m+             variable can change the settings.  Use the dircolors command to set it.
[32m+      
[32m+         EExxiitt ssttaattuuss::
[32m+             0      if OK,
[32m+      
[32m+             1      if minor problems (e.g., cannot access subdirectory),
[32m+      
[32m+             2      if serious trouble (e.g., cannot access command-line argument).
[32m+      
[32m+      AAUUTTHHOORR
[32m+             Written by Richard M. Stallman and David MacKenzie.
[32m+      
[32m+      RREEPPOORRTTIINNGG BBUUGGSS
[32m+             GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
[32m+             Report ls translation bugs to <https://translationproject.org/team/>
[32m+      
[32m+      CCOOPPYYRRIIGGHHTT
[32m+             Copyright © 2017 Free Software Foundation, Inc.   License  GPLv3+:  GNU
[32m+             GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
[32m+             This  is  free  software:  you  are free to change and redistribute it.
[32m+             There is NO WARRANTY, to the extent permitted by law.
[32m+      
[32m+      SSEEEE AALLSSOO
[32m+             Full documentation at: <https://www.gnu.org/software/coreutils/ls>
[32m+             or available locally via: info '(coreutils) ls invocation'
[32m+      
[32m+      GNU coreutils 8.29               December 2017                           LS(1)

[0m[34m## replaced (type changed from NoneType to int) /cells/21/execution_count:[0m
[31m-  None
[32m+  8

[0m[34m## inserted before /cells/21/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'Desktop': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/23/execution_count:[0m
[31m-  None
[32m+  9

[0m[34m## inserted before /cells/23/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'Desktop/data-shell': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/25/execution_count:[0m
[31m-  None
[32m+  10

[0m[34m## inserted before /cells/25/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: Desktop: No such file or directory
[32m+      bash: cd: data-shell: No such file or directory
[32m+      bash: cd: data: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/27/execution_count:[0m
[31m-  None
[32m+  11

[0m[34m## inserted before /cells/27/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/28/execution_count:[0m
[31m-  None
[32m+  12

[0m[34m## inserted before /cells/28/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/30/execution_count:[0m
[31m-  None
[32m+  13

[0m[34m## inserted before /cells/30/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: data-shell: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/32/execution_count:[0m
[31m-  None
[32m+  14

[0m[34m## replaced (type changed from NoneType to int) /cells/34/execution_count:[0m
[31m-  None
[32m+  15

[0m[34m## inserted before /cells/34/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks

[0m[34m## replaced (type changed from NoneType to int) /cells/36/execution_count:[0m
[31m-  None
[32m+  16

[0m[34m## inserted before /cells/36/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ./			     03-fundamentals-of-python/   12-images-and-vis/
[32m+      ../			     04-further-python/		  environment.yml
[32m+      00-lessons_instructor.ipynb  05-writing-effective-tests/  .git
[32m+      00-lessons.ipynb	     06-approximating-pi/	  .gitignore
[32m+      01-bash/		     07-collaborating-with-git/
[32m+      02-git/			     08-collaborating-with-git/

[0m[34m## replaced (type changed from NoneType to int) /cells/41/execution_count:[0m
[31m-  None
[32m+  17

[0m[34m## replaced (type changed from NoneType to int) /cells/43/execution_count:[0m
[31m-  None
[32m+  18

[0m[34m## inserted before /cells/43/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart

[0m[34m## replaced (type changed from NoneType to int) /cells/45/execution_count:[0m
[31m-  None
[32m+  19

[0m[34m## inserted before /cells/45/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: Desktop/data-shell/data: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/47/execution_count:[0m
[31m-  None
[32m+  20

[0m[34m## inserted before /cells/47/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart

[0m[34m## replaced (type changed from NoneType to int) /cells/48/execution_count:[0m
[31m-  None
[32m+  21

[0m[34m## inserted before /cells/48/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      bash: cd: /Users/nelle/Desktop/data-shell: No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/60/execution_count:[0m
[31m-  None
[32m+  22

[0m[34m## inserted before /cells/60/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'north-pacific-gyre/2012-07-03/': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/62/execution_count:[0m
[31m-  None
[32m+  23

[0m[34m## inserted before /cells/62/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'nor': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0m[34m## replaced (type changed from NoneType to int) /cells/64/execution_count:[0m
[31m-  None
[32m+  24

[0m[34m## inserted before /cells/64/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'north-pacific-gyre/': No such file or directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0mnbdiff /tmp/ExAXhG_03-working-with-files-and-directories_instructor.ipynb 01-bash/03-working-with-files-and-directories_instructor.ipynb
--- /tmp/ExAXhG_03-working-with-files-and-directories_instructor.ipynb  2018-08-30 12:07:38.422161
+++ 01-bash/03-working-with-files-and-directories_instructor.ipynb  2018-08-30 12:07:21.372353
[34m## replaced (type changed from NoneType to int) /cells/1/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## replaced (type changed from NoneType to int) /cells/3/execution_count:[0m
[31m-  None
[32m+  2

[0m[34m## inserted before /cells/3/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/4/execution_count:[0m
[31m-  None
[32m+  3

[0m[34m## inserted before /cells/4/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png

[0m[34m## replaced (type changed from NoneType to int) /cells/6/execution_count:[0m
[31m-  None
[32m+  4

[0m[34m## replaced (type changed from NoneType to int) /cells/8/execution_count:[0m
[31m-  None
[32m+  5

[0m[34m## inserted before /cells/8/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      01-introducing-the-shell_instructor.ipynb
[32m+      01-introducing-the-shell.ipynb
[32m+      02-files-and-directories_instructor.ipynb
[32m+      02-files-and-directories.ipynb
[32m+      03-working-with-files-and-directories_instructor.ipynb
[32m+      03-working-with-files-and-directories.ipynb
[32m+      filesystem-challenge.svg
[32m+      filesystem.svg
[32m+      home-directories.svg
[32m+      nano-screenshot.png
[32m+      thesis/

[0m[34m## replaced (type changed from NoneType to int) /cells/12/execution_count:[0m
[31m-  None
[32m+  6

[0m[34m## replaced (type changed from NoneType to int) /cells/14/execution_count:[0m
[31m-  None
[32m+  7

[0m[34m## replaced (type changed from NoneType to int) /cells/15/execution_count:[0m
[31m-  None
[32m+  8

[0m[34m## replaced (type changed from NoneType to int) /cells/20/execution_count:[0m
[31m-  None
[32m+  9

[0m[34m## inserted before /cells/20/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/24/execution_count:[0m
[31m-  None
[32m+  10

[0m[34m## replaced (type changed from NoneType to int) /cells/26/execution_count:[0m
[31m-  None
[32m+  11

[0m[34m## replaced (type changed from NoneType to int) /cells/29/execution_count:[0m
[31m-  None
[32m+  12

[0m[34m## inserted before /cells/29/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash/thesis

[0m[34m## replaced (type changed from NoneType to int) /cells/30/execution_count:[0m
[31m-  None
[32m+  13

[0m[34m## replaced (type changed from NoneType to int) /cells/31/execution_count:[0m
[31m-  None
[32m+  14

[0m[34m## inserted before /cells/31/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/32/execution_count:[0m
[31m-  None
[32m+  15

[0m[34m## replaced (type changed from NoneType to int) /cells/34/execution_count:[0m
[31m-  None
[32m+  16

[0m[34m## inserted before /cells/34/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      rm: cannot remove 'thesis': Is a directory
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 1

[0m[34m## replaced (type changed from NoneType to int) /cells/36/execution_count:[0m
[31m-  None
[32m+  17

[0m[34m## replaced (type changed from NoneType to int) /cells/41/execution_count:[0m
[31m-  None
[32m+  18

[0m[34m## inserted before /cells/41/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      /home/stuart/Git/Aperio/stfc_website/notebooks/01-bash

[0m[34m## replaced (type changed from NoneType to int) /cells/42/execution_count:[0m
[31m-  None
[32m+  19

[0m[34m## replaced (type changed from NoneType to int) /cells/43/execution_count:[0m
[31m-  None
[32m+  20

[0m[34m## replaced (type changed from NoneType to int) /cells/44/execution_count:[0m
[31m-  None
[32m+  21

[0m[34m## replaced (type changed from NoneType to int) /cells/45/execution_count:[0m
[31m-  None
[32m+  22

[0m[34m## inserted before /cells/45/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      draft.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/47/execution_count:[0m
[31m-  None
[32m+  23

[0m[34m## replaced (type changed from NoneType to int) /cells/49/execution_count:[0m
[31m-  None
[32m+  24

[0m[34m## inserted before /cells/49/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/51/execution_count:[0m
[31m-  None
[32m+  25

[0m[34m## replaced (type changed from NoneType to int) /cells/53/execution_count:[0m
[31m-  None
[32m+  26

[0m[34m## replaced (type changed from NoneType to int) /cells/55/execution_count:[0m
[31m-  None
[32m+  27

[0m[34m## inserted before /cells/55/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/59/execution_count:[0m
[31m-  None
[32m+  28

[0m[34m## replaced (type changed from NoneType to int) /cells/60/execution_count:[0m
[31m-  None
[32m+  29

[0m[34m## inserted before /cells/60/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      quotes.txt  thesis/quotations.txt

[0m[34m## replaced (type changed from NoneType to int) /cells/62/execution_count:[0m
[31m-  None
[32m+  30

[0m[34m## replaced (type changed from NoneType to int) /cells/63/execution_count:[0m
[31m-  None
[32m+  31

[0m[34m## inserted before /cells/63/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      ls: cannot access 'quotes.txt': No such file or directory
[32m+      thesis/quotations.txt
[32m+  output:
[32m+    output_type: error
[32m+    evalue: 2

[0mnbdiff /tmp/vwSbTp_01-introduction-to-version-control_instructor.ipynb 02-git/01-introduction-to-version-control_instructor.ipynb
--- /tmp/vwSbTp_01-introduction-to-version-control_instructor.ipynb  2018-08-30 12:07:39.195485
+++ 02-git/01-introduction-to-version-control_instructor.ipynb  2018-08-30 12:07:29.392262
[34m## replaced (type changed from NoneType to int) /cells/7/execution_count:[0m
[31m-  None
[32m+  1

[0m[34m## inserted before /cells/7/outputs/0:[0m
[32m+  output:
[32m+    output_type: stream
[32m+    name: stdout
[32m+    text:
[32m+      user.name=Stuart Mumford
[32m+      user.email=stuart@cadair.com
[32m+      user.signingkey=E6276769
[32m+      commit.gpgsign=true
[32m+      push.default=simple
[32m+      alias.log=log --show-signature
[32m+      difftool.latex.cmd=latexdiff  $LOCAL $REMOTE
[32m+      difftool.latexadd.cmd=latexdiff --graphics-markup=none -t BOLD -f IDENTICAL -s COLOR -X caption $LOCAL $REMOTE
[32m+      difftool.prompt=false
[32m+      alias.ldiff=difftool -t latex
[32m+      alias.ldiffadd=difftool -t latexadd
[32m+      alias.tree=log --decorate --graph --show-signature
[32m+      alias.wdiff=diff
[32m+      credential.helper=/usr/lib/git-core/git-credential-gnome-keyring
[32m+      filter.lfs.clean=git-lfs clean %f
[32m+      filter.lfs.smudge=git-lfs smudge %f
[32m+      filter.lfs.required=true
[32m+      color.ui=auto
[32m+      core.editor=vim
[32m+      github.user=Cadair
[32m+      github.oauth-token=1f70bdc8ea2446bd1f2fd3c30fefa8ce1b31e676
[32m+      url.git@github.com:.insteadof=gh:
[32m+      url.git@gitlab.com:.insteadof=gl:
[32m+      diff.jupyternotebook.command=git-nbdiffdriver diff
[32m+      merge.jupyternotebook.driver=git-nbmergedriver merge %O %A %B %L %P
[32m+      merge.jupyternotebook.name=jupyter notebook merge driver
[32m+      difftool.nbdime.cmd=git-nbdifftool diff "$LOCAL" "$REMOTE"
[32m+      mergetool.nbdime.cmd=git-nbmergetool merge "$BASE" "$LOCAL" "$REMOTE" "$MERGED"
[32m+      mergetool.prompt=false
[32m+      magithub.online=false
[32m+      magithub.status.includestatusheader=false
[32m+      magithub.status.includepullrequestssection=false
[32m+      magithub.status.includeissuessection=false
[32m+      core.repositoryformatversion=0
[32m+      core.filemode=true
[32m+      core.bare=false
[32m+      core.logallrefupdates=true
[32m+      core.worktree=../../../notebooks
[32m+      remote.origin.url=https://github.com/cadair/rcsc_notebooks
[32m+      remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
[32m+      branch.master.remote=origin
[32m+      branch.master.merge=refs/heads/master
[32m+      

[0m

```

There is no output: as far as Git can tell, there’s no difference between what it’s been asked to save permanently and what’s currently in the directory. However, if we do this:


{:.input_area}
```xonsh
git diff --staged
```

{:.output_stream}
```


```

it shows us the difference between the last committed change and what’s in the staging area. Let’s save our changes:


{:.input_area}
```xonsh
git commit -m "Discuss concerns about Mars' climate for Mummy"
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit


```

check our status:


{:.input_area}
```xonsh
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   02-git/01-introduction-to-version-control_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

and look at the history of what we’ve done so far:


{:.input_area}
```xonsh
git log
```

{:.output_stream}
```
[33mcommit f68b2a3223f18d25a1e63380893d73b1cd30abc1[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 12:03:19 2018 +0100

    update notebooks

[33mcommit e11ebdc8bf78e2f52229b57d144967a4f99f88b6[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:59:41 2018 +0100

    update notebooks

[33mcommit 8809182d0e0e353f09367556d01b92de1ec450a4[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:50:41 2018 +0100

    update notebooks

[33mcommit c53a36e0edfeb20a335c2a41b2103fe7f19b6bd0[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:27:13 2018 +0100

    update notebooks

[33mcommit 0492cd39d704c9505f11d273c08cbb7c56024258[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:09:11 2018 +0100

    clean old image

[33mcommit 5077f80a291ee911d249b903a264ee40fb590b65[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 11:07:55 2018 +0100

    update notebooks

[33mcommit 39dd5be002135b4db35c2a216be5bbeb31a7c256[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 10:58:27 2018 +0100

    update notebooks

[33mcommit cf909a51854d650a70f87811f0c47668ab7eae6d[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Thu Aug 30 10:46:13 2018 +0100

    update notebooks

[33mcommit ebf6c876ee828a4b1d7e6d0ada2a3228232b71c6[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:37:25 2018 +0100

    update notebooks

[33mcommit 2e2caef43b2c47352ebdefbf55436eeb08f65f24[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:26:13 2018 +0100

    update notebooks

[33mcommit 9b727a7acbd4b7ec231cbaa0a469e4b0cf0ab507[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:17:05 2018 +0100

    remove old part 1 files

[33mcommit 965532dda2db870e8a97615b6d3de0e00815c11f[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 16:07:49 2018 +0100

    update notebooks

[33mcommit 94821cff313d14dda904524abae6ce792c6a70f0[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Wed Aug 29 15:58:10 2018 +0100

    update notebooks

[33mcommit 72c8550e9eb6cec7f26fa725b3e5d03f189e86db[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 15:32:21 2018 +0100

    update notebooks

[33mcommit c425f76ebea51c7bc98cc51b31fd863cc06cf02c[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 14:37:22 2018 +0100

    remove old checkpoints

[33mcommit 85d4a6e3502e186960ea3e07efc1634d3b7af4a2[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 14:36:53 2018 +0100

    add an ignore

[33mcommit 012340795d6728194a442430e64d128155e05991[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 14:14:54 2018 +0100

    update notebooks

[33mcommit f1717d7c38bd17655f463507bba9d13d3e7d9985[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 13:25:06 2018 +0100

    update notebooks

[33mcommit 166a8d60458d2ceeda27fb1c5ed079936590e918[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 13:22:54 2018 +0100

    update notebooks

[33mcommit 34268e85dbe4bbfac0117bec784ac506ef180d85[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 13:16:44 2018 +0100

    update notebooks

[33mcommit e1cfe1d6622718d3143023ceb840c05d7871d8af[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 11:59:19 2018 +0100

    update notebooks

[33mcommit 19eef9b9716460f7ef77f26cfc0169d81f891054[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 29 11:53:37 2018 +0100

    update notebooks

[33mcommit e5b43481e35f616f088e1654d66880617f7ea36c[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 18:13:58 2018 +0100

    update notebooks

[33mcommit f73be5b9f60dd0ee613ad15fbc3231048a03cf3e[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 18:03:01 2018 +0100

    update notebooks

[33mcommit 7bdabf6834f532e4e5de1e1a9e85422407b75888[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 17:54:50 2018 +0100

    update notebooks

[33mcommit c250be1783d071580fda3d2891628c8df853b137[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 15:25:09 2018 +0100

    update notebooks

[33mcommit fc10d58c600d177dc926edc61dc1b301ee74d070[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 15:17:46 2018 +0100

    update notebooks

[33mcommit 28a17be8c094e79639f869b56bc765f149b6f855[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 15:09:46 2018 +0100

    update notebooks

[33mcommit fa3dd411dc0cb59bc8c0216fd9fb8487cdc6b9ad[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Tue Aug 21 14:52:41 2018 +0100

    update notebooks

[33mcommit acb9d1ddad4f4655b6843ad9f5d4dc0fb4c1a8d9[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Tue Aug 21 14:05:23 2018 +0100

    update notebooks

[33mcommit c55fe06c415a14e4ab66e59dfd69f96f33bddb00[m
Author: Drew Leonard <andy.j.leonard@gmail.com>
Date:   Tue Aug 21 14:01:21 2018 +0100

    update notebooks

[33mcommit 83d22fb72dfe2cb97c889f9eee27d6e59029fd15[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 12:46:10 2018 +0100

    update notebooks

[33mcommit 1352289e11215e0cf06e4e9b198f2571b87f3634[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Aug 21 10:20:43 2018 +0100

    update notebooks

[33mcommit b148b305b6e687c965eba8a940b6ae7120415f97[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 19:44:41 2018 +0100

    update notebooks

[33mcommit 78a9d78eb0ca9ad231a59832329da4f586639edf[m
Merge: d25859c 8b09b5b
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:44:05 2018 +0100

    Merge branch 'master' of github.com:Cadair/rcsc_notebooks

[33mcommit d25859c54c981f7ad5bfda39cab74ded27ee47ac[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:43:42 2018 +0100

    update notebooks

[33mcommit 6b2f4ce898c4cd01fd95e5845459cbb39c5fbc8f[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:43:12 2018 +0100

    update notebooks

[33mcommit 8b09b5bb88eaca994de7891453c3e51f6506b40f[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:38:23 2018 +0100

    remove old setup instructions notebook

[33mcommit b0f041be189f301d0a30b320d8e3bcec8d9b9999[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:34:41 2018 +0100

    remove old files

[33mcommit 50d31acffc688854e363d30cb7d91bfd8d515e70[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Aug 20 11:29:55 2018 +0100

    update notebooks

[33mcommit 12ba0802861674559bb85e7f84c6464c2086663d[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 15 13:19:13 2018 +0100

    Add the environment file for binder

[33mcommit a4f3524945c89174cbabe8ce7f99494feea5f629[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 15 11:41:18 2018 +0100

    update notebooks

[33mcommit 3331567c4ba480f95db6e3a054a6534f412b225b[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Wed Aug 15 11:24:51 2018 +0100

    update notebooks

[33mcommit 3931f8dc17f956ed0679689911ac3bea815e7ea1[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Fri Jul 27 15:08:53 2018 +0100

    update notebooks

[33mcommit e7f170a42d7c39070b626315443539dcec24ddf9[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Fri Jul 27 15:08:33 2018 +0100

    update notebooks

[33mcommit 032584df56650bcd5d902cc91bfc243b9d7a35ce[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 23:06:27 2018 +0100

    update notebooks

[33mcommit e070aca61aada496596cc4a7fce647f076de7189[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 23:06:12 2018 +0100

    what the shit

[33mcommit cc7ffecf0dc9cd00522ba4542b83e300acdbf22c[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 22:54:18 2018 +0100

    update notebooks

[33mcommit ca7243f1f46cbabf40a8206ce8b857c25452e5eb[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Jul 24 22:50:37 2018 +0100

    Add readme


```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Word-based diffing</h2>
</div>


<div class="panel-body">

<p>Sometimes, e.g. in the case of the text documents a line-wise diff is too coarse. That is where the --color-words option of git diff comes in very useful as it highlights the changed words using colors.</p>

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Paging the Log</h2>
</div>


<div class="panel-body">

<p>When the output of git log is too long to fit in your screen, git uses a program to split it into pages of the size of your screen. When this “pager” is called, you will notice that the last line in your screen is a :, instead of your usual prompt.</p>
<ul>
<li>To get out of the pager, press Q.</li>
<li>To move to the next page, press Spacebar.</li>
<li>To search for some_word in all pages, press / and type some_word. Navigate through matches pressing N.</li>
</ul>

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Limit Log Size</h2>
</div>


<div class="panel-body">

<p>To avoid having git log cover your entire terminal screen, you can limit the number of commits that Git lists by using -N, where N is the number of commits that you want to view. For example, if you only want information from the last commit you can use:</p>
<div class="codehilite"><pre><span></span>$ git log -1

commit 005937fbe2a98fb83f0ade869025dc2636b4dad5
Author: Vlad Dracula &lt;vlad@tran.sylvan.ia&gt;
Date:   Thu Aug <span class="m">22</span> <span class="m">10</span>:14:07 <span class="m">2013</span> -0400

   Discuss concerns about Mars<span class="err">&#39;</span> climate <span class="k">for</span> Mummy
</pre></div>


<p>You can also reduce the quantity of information using the --oneline option:</p>
<div class="codehilite"><pre><span></span>$ git log --oneline

 * 005937f Discuss concerns about Mars<span class="s1">&#39; climate for Mummy</span>
<span class="s1"> * 34961b1 Add concerns about effects of Mars&#39;</span> moons on Wolfman
 * f22b25e Start notes on Mars as a base
</pre></div>


<p>You can also combine the --oneline options with others. One useful combination is:</p>
<div class="codehilite"><pre><span></span><span class="nv">$</span> <span class="nv">git</span> <span class="nb">log</span> <span class="o">--</span><span class="n">oneline</span> <span class="o">--</span><span class="n">graph</span> <span class="o">--</span><span class="n">all</span> <span class="o">--</span><span class="n">decorate</span>

<span class="o">*</span> <span class="mo">005</span><span class="mi">937</span><span class="n">f</span> <span class="n">Discuss</span> <span class="n">concerns</span> <span class="n">about</span> <span class="n">Mars</span><span class="s">&#39; climate for Mummy (HEAD, master)</span>
<span class="s">* 34961b1 Add concerns about effects of Mars&#39;</span> <span class="n">moons</span> <span class="n">on</span> <span class="n">Wolfman</span>
<span class="o">*</span> <span class="n">f22b25e</span> <span class="n">Start</span> <span class="n">notes</span> <span class="n">on</span> <span class="n">Mars</span> <span class="n">as</span> <span class="n">a</span> <span class="n">base</span>
</pre></div>

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Directories</h2>
</div>


<div class="panel-body">

<p>Two important facts you should know about directories in Git.</p>
<ol>
<li>Git does not track directories on their own, only files within them. Try it for yourself:</li>
</ol>
<div class="codehilite"><pre><span></span>$ mkdir directory
$ git status
$ git add directory
$ git status
</pre></div>


<p>Note, our newly created empty directory directory does not appear in the list of untracked files even if we explicitly add it (via git add) to our repository. This is the reason why you will sometimes see .gitkeep files in otherwise empty directories. Unlike .gitignore, these files are not special and their sole purpose is to populate a directory so that Git adds it to the repository. In fact, you can name such files anything you like.</p>
<ol>
<li>If you create a directory in your Git repository and populate it with files, you can add all files in the directory at once by:</li>
</ol>
<div class="codehilite"><pre><span></span>git add &lt;directory-with-files&gt;
</pre></div>

</div>

</section>


To recap, when we want to add changes to our repository, we first need to add the changed files to the staging area (git add) and then commit the staged changes to the repository (git commit):

![](http://swcarpentry.github.io/git-novice/fig/git-committing.svg)


<section class="challange panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Choosing a Commit Message</h2>
</div>


<div class="panel-body">

<p>Which of the following commit messages would be most appropriate for the last commit made to mars.txt?</p>
<ul>
<li>“Changes”</li>
<li>“Added line ‘But the Mummy will appreciate the lack of humidity’ to mars.txt”</li>
<li>“Discuss effects of Mars’ climate on the Mummy”</li>
</ul>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>Answer 1 is not descriptive enough, and the purpose of the commit is unclear; and answer 2 is redundant to using “git diff” to see what changed in this commit; but answer 3 is good: short, descriptive, and imperative.</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Committing Changes to Git</h2>
</div>


<div class="panel-body">

<p>Which command(s) below would save the changes of myfile.txt to my local Git repository?</p>
<div class="codehilite"><pre><span></span>$ git commit -m <span class="s2">&quot;my recent changes&quot;</span>

$ git init myfile.txt
$ git commit -m <span class="s2">&quot;my recent changes&quot;</span>

$ git add myfile.txt
$ git commit -m <span class="s2">&quot;my recent changes&quot;</span>

$ git commit -m myfile.txt <span class="s2">&quot;my recent changes&quot;</span>
</pre></div>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<ul>
<li>Would only create a commit if files have already been staged.</li>
<li>Would try to create a new repository.</li>
<li>Is correct: first add the file to the staging area, then commit.</li>
<li>Would try to commit a file “my recent changes” with the message myfile.txt.</li>
</ul>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Committing Multiple Files</h2>
</div>


<div class="panel-body">

<p>The staging area can hold changes from any number of files that you want to commit as a single snapshot.</p>
<ol>
<li>Add some text to mars.txt noting your decision to consider Venus as a base</li>
<li>Create a new file venus.txt with your initial thoughts about Venus as a base for you and your friends</li>
<li>Add changes from both files to the staging area, and commit those changes.</li>
</ol>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>First we make our changes to the mars.txt and venus.txt files:</p>
<div class="codehilite"><pre><span></span>$ nano mars.txt
$ cat mars.txt

Maybe I should start with a base on Venus.

$ nano venus.txt
$ cat venus.txt

Venus is a nice planet and I definitely should consider it as a base.
</pre></div>


<p>Now you can add both files to the staging area. We can do that in one line:</p>
<div class="codehilite"><pre><span></span>$ git add mars.txt venus.txt
</pre></div>


<p>Or with multiple commands:</p>
<div class="codehilite"><pre><span></span>$ git add mars.txt
$ git add venus.txt
</pre></div>


<p>Now the files are ready to commit. You can check that using git status. If you are ready to commit use:</p>
<div class="codehilite"><pre><span></span><span class="err">$</span> <span class="n">git</span> <span class="n">commit</span> <span class="o">-</span><span class="n">m</span> <span class="s">&quot;Write plans to start a base on Venus&quot;</span>

<span class="p">[</span><span class="n">master</span> <span class="n">cc127c2</span><span class="p">]</span>
 <span class="n">Write</span> <span class="n">plans</span> <span class="n">to</span> <span class="n">start</span> <span class="n">a</span> <span class="n">base</span> <span class="n">on</span> <span class="n">Venus</span>
 <span class="mi">2</span> <span class="n">files</span> <span class="n">changed</span><span class="p">,</span> <span class="mi">2</span> <span class="n">insertions</span><span class="p">(</span><span class="o">+</span><span class="p">)</span>
 <span class="n">create</span> <span class="n">mode</span> <span class="mi">100644</span> <span class="n">venus</span><span class="p">.</span><span class="n">txt</span>
</pre></div>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # `bio` Repository</h2>
</div>


<div class="panel-body">

<ul>
<li>Create a new Git repository on your computer called bio.</li>
<li>Write a three-line biography for yourself in a file called me.txt, commit your changes</li>
<li>Modify one line, add a fourth line</li>
<li>Display the differences between its updated state and its original state.</li>
</ul>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>If needed, move out of the planets folder:</p>
<div class="codehilite"><pre><span></span>$ <span class="nb">cd</span> ..
</pre></div>


<p>Create a new folder called bio and ‘move’ into it:</p>
<div class="codehilite"><pre><span></span>$ mkdir bio
$ <span class="nb">cd</span> bio
</pre></div>


<p>Initialise git:</p>
<div class="codehilite"><pre><span></span>$ git init
</pre></div>


<p>Create your biography file me.txt using nano or another text editor. Once in place, add and commit it to the repository:</p>
<div class="codehilite"><pre><span></span>$ git add me.txt
$ git commit -m<span class="s1">&#39;Adding biography file&#39;</span>
</pre></div>


<p>Modify the file as described (modify one line, add a fourth line). To display the differences between its updated state and its original state, use git diff:</p>
<div class="codehilite"><pre><span></span>$ git diff me.txt
</pre></div>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Author and Committer</h2>
</div>


<div class="panel-body">

<p>For each of the commits you have done, Git stored your name twice. You are named as the author and as the committer. You can observe that by telling Git to show you more information about your last commits:</p>
<div class="codehilite"><pre><span></span>$ git log --format<span class="o">=</span>full
</pre></div>


<p>When committing you can name someone else as the author:</p>
<div class="codehilite"><pre><span></span>$ git commit --author<span class="o">=</span><span class="s2">&quot;Vlad Dracula &lt;vlad@tran.sylvan.ia&gt;&quot;</span>
</pre></div>


<p>Create a new repository and create two commits: one without the --author option and one by naming a colleague of yours as the author. Run git log and git log --format=full. Think about ways how that can allow you to collaborate with your colleagues.</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<div class="codehilite"><pre><span></span>$ git add me.txt
$ git commit -m <span class="s2">&quot;Update Vlad&#39;s bio.&quot;</span> --author<span class="o">=</span><span class="s2">&quot;Frank N. Stein &lt;franky@monster.com&gt;&quot;</span>

<span class="o">[</span>master 4162a51<span class="o">]</span> Update Vlad<span class="s1">&#39;s bio.</span>
<span class="s1">Author: Frank N. Stein &lt;franky@monster.com&gt;</span>
<span class="s1">1 file changed, 2 insertions(+), 2 deletions(-)</span>

<span class="s1">$ git log --format=full</span>
<span class="s1">commit 4162a51b273ba799a9d395dd70c45d96dba4e2ff</span>
<span class="s1">Author: Frank N. Stein &lt;franky@monster.com&gt;</span>
<span class="s1">Commit: Vlad Dracula &lt;vlad@tran.sylvan.ia&gt;</span>

<span class="s1">Update Vlad&#39;</span>s bio.

commit aaa3271e5e26f75f11892718e83a3e2743fab8ea
Author: Vlad Dracula &lt;vlad@tran.sylvan.ia&gt;
Commit: Vlad Dracula &lt;vlad@tran.sylvan.ia&gt;

Vlad<span class="err">&#39;</span>s initial bio.
</pre></div>

</div>

</section>



<section class="keypoints panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-exclamation-circle"></span> # Key Points</h2>
</div>


<div class="panel-body">

<ul>
<li>git status shows the status of a repository.</li>
<li>Files can be stored in a project’s working directory (which users see), the staging area (where the next commit is being built up) and the local repository (where commits are permanently recorded).</li>
<li>git add puts files in the staging area.</li>
<li>git commit saves the staged content as a new commit in the local repository.</li>
<li>Write a commit message that accurately describes your changes.</li>
</ul>

</div>

</section>

