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
00-lessons.ipynb             [0m[01;34m01-bash[0m  [01;34m03-fundamentals-of-python[0m  [01;34m05-writing-effective-tests[0m  [01;34m07-collaborating-with-git[0m  [01;34m12-images-and-visualisation[0m  LICENCE  environment.yml
00-lessons_instructor.ipynb  [01;34m02-git[0m   [01;34m04-further-python[0m          [01;34m06-approximating-pi[0m         [01;34m09-units[0m                   [01;34m13-images-in-astronomy[0m       README


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

	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

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

	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

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
	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

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

	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

it tells us everything is up to date. If we want to know what we’ve done recently, we can ask Git to show us the project’s history using `git log`:


{:.input_area}
```xonsh
git log
```

{:.output_stream}
```
[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Sep 4 08:41:44 2018 +0100

    update notebooks

[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Sep 3 13:24:05 2018 +0100

    update notebooks

[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 19:25:16 2018 +0100

    update notebooks

[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 14:51:57 2018 +0100

    rename to avoid website issues

[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 14:43:57 2018 +0100

    update notebooks

[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 14:43:13 2018 +0100

    update notebooks

[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 13:46:49 2018 +0100

    Add licence and readme to the lessons repo

[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 12:59:07 2018 +0100

    Add initial dump of rendered lessons


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

	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

The last line is the key phrase: “no changes added to commit”. We have changed this file, but we haven’t told Git we will want to save those changes (which we do with `git add`) nor have we saved them (which we do with `git commit`). So let’s do that now. It is good practice to always review our changes before saving them. We do this using git diff. This shows us the differences between the current state of the file and the most recently saved version:


{:.input_area}
```xonsh
git diff
```

{:.output_stream}
```
[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb[m
[1mindex 0a7156d..4996fde 100644[m
[1m--- a/02-git/02-creating-repositories_instructor.ipynb[m
[1m+++ b/02-git/02-creating-repositories_instructor.ipynb[m
[36m@@ -22,9 +22,32 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 1,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/bin/mkdir: cannot create directory ‘planets’: File exists\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cd ~/Desktop\n",[m
     "mkdir planets\n",[m
[36m@@ -40,9 +63,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 2,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git init"[m
    ][m
[36m@@ -56,9 +88,17 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 3,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls"[m
    ][m
[36m@@ -72,9 +112,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 4,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[0m\u001b[01;34m.\u001b[0m  \u001b[01;34m..\u001b[0m  \u001b[01;34m.git\u001b[0m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls -a"[m
    ][m
[36m@@ -90,9 +139,22 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 5,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "No commits yet\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "nothing to commit (create/copy files and use \"git add\" to track)\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[1mdiff --git a/02-git/03-tracking-changes_instructor.ipynb b/02-git/03-tracking-changes_instructor.ipynb[m
[1mindex 1f99d29..c9b6cac 100644[m
[1m--- a/02-git/03-tracking-changes_instructor.ipynb[m
[1m+++ b/02-git/03-tracking-changes_instructor.ipynb[m
[36m@@ -23,9 +23,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 1,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/home/stuart/Git/Aperio/stfc_website/notebooks/02-git\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "pwd"[m
    ][m
[36m@@ -39,18 +48,35 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 2,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/home/stuart/Git/Aperio/stfc_website/notebooks/02-git\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "pwd"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 3,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cd .."[m
    ][m
[36m@@ -74,18 +100,43 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 4,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "00-lessons.ipynb             \u001b[0m\u001b[01;34m01-bash\u001b[0m  \u001b[01;34m03-fundamentals-of-python\u001b[0m  \u001b[01;34m05-writing-effective-tests\u001b[0m  \u001b[01;34m07-collaborating-with-git\u001b[0m  \u001b[01;34m12-images-and-visualisation\u001b[0m  LICENCE  environment.yml\n",[m
[32m+[m[32m      "00-lessons_instructor.ipynb  \u001b[01;34m02-git\u001b[0m   \u001b[01;34m04-further-python\u001b[0m          \u001b[01;34m06-approximating-pi\u001b[0m         \u001b[01;34m09-units\u001b[0m                   \u001b[01;34m13-images-in-astronomy\u001b[0m       README\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 5,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cat mars.txt"[m
    ][m
[36m@@ -99,9 +150,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 6,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -115,9 +184,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 7,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: pathspec 'mars.txt' did not match any files\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git add mars.txt"[m
    ][m
[36m@@ -131,9 +215,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 8,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -147,9 +249,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 9,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Start notes on Mars as a base\""[m
    ][m
[36m@@ -169,9 +286,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 10,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -185,9 +320,64 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 11,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668\u001b[m\u001b[33m (\u001b[m\u001b[1;36mHEAD -> \u001b[m\u001b[1;32mmaster\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/master\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/HEAD\u001b[m\u001b[33m)\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Tue Sep 4 08:41:44 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Mon Sep 3 13:24:05 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 19:25:16 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:51:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    rename to avoid website issues\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:13 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 13:46:49 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add licence and readme to the lessons repo\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 12:59:07 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add initial dump of rendered lessons\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git log"[m
    ][m
[36m@@ -228,9 +418,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 12,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -255,9 +467,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 13,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -271,9 +501,143 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 14,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff"[m
    ][m
[36m@@ -294,9 +658,35 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 15,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Add concerns about effects of Mars' moons on Wolfman\"\n",[m
     "git status"[m
[36m@@ -356,9 +746,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 16,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -366,9 +778,143 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 17,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff"[m
    ][m
[36m@@ -382,9 +928,151 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 18,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: pathspec 'mars.txt' did not match any files\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git add mars.txt\n",[m
     "git diff"[m
[36m@@ -399,9 +1087,17 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 19,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff --staged"[m
    ][m
[36m@@ -415,9 +1111,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 20,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Discuss concerns about Mars' climate for Mummy\""[m
    ][m
[36m@@ -431,9 +1142,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 21,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -447,9 +1176,64 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 22,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668\u001b[m\u001b[33m (\u001b[m\u001b[1;36mHEAD -> \u001b[m\u001b[1;32mmaster\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/master\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/HEAD\u001b[m\u001b[33m)\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Tue Sep 4 08:41:44 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Mon Sep 3 13:24:05 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 19:25:16 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:51:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    rename to avoid website issues\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:13 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 13:46:49 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add licence and readme to the lessons repo\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 12:59:07 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add initial dump of rendered lessons\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git log"[m
    ][m
[1mdiff --git a/02-git/04-exploring-history_instructor.ipynb b/02-git/04-exploring-history_instructor.ipynb[m
[1mindex 24e0c80..e766d19 100644[m
[1m--- a/02-git/04-exploring-history_instructor.ipynb[m
[1m+++ b/02-git/04-exploring-history_instructor.ipynb[m
[36m@@ -18,9 +18,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 1,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -35,9 +57,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 2,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD mars.txt"[m
    ][m
[36m@@ -51,9 +90,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 3,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD~1 mars.txt"[m
    ][m
[36m@@ -67,9 +123,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 4,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD~2 mars.txt"[m
    ][m
[36m@@ -93,9 +166,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 5,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: bad object f22b25e3233b4645dabd0d81e651fe074bd8e73b\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b mars.txt"[m
    ][m
[36m@@ -109,9 +197,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 6,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'f22b25e': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff f22b25e mars.txt"[m
    ][m
[36m@@ -125,9 +230,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 7,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -142,9 +269,28 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 8,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   03-tracking-changes_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -158,9 +304,38 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 9,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout HEAD mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -175,27 +350,77 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 10,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'f22b25e' did not match any file(s) known to git.\n",[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout f22b25e mars.txt"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 11,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cat mars.txt"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 12,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   03-tracking-changes_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -209,9 +434,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 13,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout HEAD mars.txt"[m
    ][m


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
	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

no changes added to commit

On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

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
[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb[m
[1mindex 0a7156d..4996fde 100644[m
[1m--- a/02-git/02-creating-repositories_instructor.ipynb[m
[1m+++ b/02-git/02-creating-repositories_instructor.ipynb[m
[36m@@ -22,9 +22,32 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 1,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/bin/mkdir: cannot create directory ‘planets’: File exists\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cd ~/Desktop\n",[m
     "mkdir planets\n",[m
[36m@@ -40,9 +63,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 2,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git init"[m
    ][m
[36m@@ -56,9 +88,17 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 3,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls"[m
    ][m
[36m@@ -72,9 +112,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 4,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[0m\u001b[01;34m.\u001b[0m  \u001b[01;34m..\u001b[0m  \u001b[01;34m.git\u001b[0m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls -a"[m
    ][m
[36m@@ -90,9 +139,22 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 5,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "No commits yet\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "nothing to commit (create/copy files and use \"git add\" to track)\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[1mdiff --git a/02-git/03-tracking-changes_instructor.ipynb b/02-git/03-tracking-changes_instructor.ipynb[m
[1mindex 1f99d29..c9b6cac 100644[m
[1m--- a/02-git/03-tracking-changes_instructor.ipynb[m
[1m+++ b/02-git/03-tracking-changes_instructor.ipynb[m
[36m@@ -23,9 +23,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 1,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/home/stuart/Git/Aperio/stfc_website/notebooks/02-git\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "pwd"[m
    ][m
[36m@@ -39,18 +48,35 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 2,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/home/stuart/Git/Aperio/stfc_website/notebooks/02-git\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "pwd"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 3,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cd .."[m
    ][m
[36m@@ -74,18 +100,43 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 4,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "00-lessons.ipynb             \u001b[0m\u001b[01;34m01-bash\u001b[0m  \u001b[01;34m03-fundamentals-of-python\u001b[0m  \u001b[01;34m05-writing-effective-tests\u001b[0m  \u001b[01;34m07-collaborating-with-git\u001b[0m  \u001b[01;34m12-images-and-visualisation\u001b[0m  LICENCE  environment.yml\n",[m
[32m+[m[32m      "00-lessons_instructor.ipynb  \u001b[01;34m02-git\u001b[0m   \u001b[01;34m04-further-python\u001b[0m          \u001b[01;34m06-approximating-pi\u001b[0m         \u001b[01;34m09-units\u001b[0m                   \u001b[01;34m13-images-in-astronomy\u001b[0m       README\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 5,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cat mars.txt"[m
    ][m
[36m@@ -99,9 +150,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 6,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -115,9 +184,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 7,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: pathspec 'mars.txt' did not match any files\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git add mars.txt"[m
    ][m
[36m@@ -131,9 +215,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 8,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -147,9 +249,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 9,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Start notes on Mars as a base\""[m
    ][m
[36m@@ -169,9 +286,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 10,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -185,9 +320,64 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 11,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668\u001b[m\u001b[33m (\u001b[m\u001b[1;36mHEAD -> \u001b[m\u001b[1;32mmaster\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/master\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/HEAD\u001b[m\u001b[33m)\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Tue Sep 4 08:41:44 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Mon Sep 3 13:24:05 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 19:25:16 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:51:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    rename to avoid website issues\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:13 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 13:46:49 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add licence and readme to the lessons repo\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 12:59:07 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add initial dump of rendered lessons\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git log"[m
    ][m
[36m@@ -228,9 +418,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 12,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -255,9 +467,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 13,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -271,9 +501,143 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 14,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff"[m
    ][m
[36m@@ -294,9 +658,35 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 15,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Add concerns about effects of Mars' moons on Wolfman\"\n",[m
     "git status"[m
[36m@@ -356,9 +746,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 16,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -366,9 +778,143 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 17,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff"[m
    ][m
[36m@@ -382,9 +928,151 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 18,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: pathspec 'mars.txt' did not match any files\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git add mars.txt\n",[m
     "git diff"[m
[36m@@ -399,9 +1087,17 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 19,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff --staged"[m
    ][m
[36m@@ -415,9 +1111,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 20,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Discuss concerns about Mars' climate for Mummy\""[m
    ][m
[36m@@ -431,9 +1142,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 21,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -447,9 +1176,64 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 22,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668\u001b[m\u001b[33m (\u001b[m\u001b[1;36mHEAD -> \u001b[m\u001b[1;32mmaster\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/master\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/HEAD\u001b[m\u001b[33m)\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Tue Sep 4 08:41:44 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Mon Sep 3 13:24:05 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 19:25:16 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:51:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    rename to avoid website issues\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:13 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 13:46:49 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add licence and readme to the lessons repo\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 12:59:07 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add initial dump of rendered lessons\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git log"[m
    ][m
[1mdiff --git a/02-git/04-exploring-history_instructor.ipynb b/02-git/04-exploring-history_instructor.ipynb[m
[1mindex 24e0c80..e766d19 100644[m
[1m--- a/02-git/04-exploring-history_instructor.ipynb[m
[1m+++ b/02-git/04-exploring-history_instructor.ipynb[m
[36m@@ -18,9 +18,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 1,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -35,9 +57,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 2,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD mars.txt"[m
    ][m
[36m@@ -51,9 +90,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 3,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD~1 mars.txt"[m
    ][m
[36m@@ -67,9 +123,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 4,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD~2 mars.txt"[m
    ][m
[36m@@ -93,9 +166,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 5,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: bad object f22b25e3233b4645dabd0d81e651fe074bd8e73b\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b mars.txt"[m
    ][m
[36m@@ -109,9 +197,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 6,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'f22b25e': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff f22b25e mars.txt"[m
    ][m
[36m@@ -125,9 +230,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 7,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -142,9 +269,28 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 8,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   03-tracking-changes_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -158,9 +304,38 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 9,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout HEAD mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -175,27 +350,77 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 10,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'f22b25e' did not match any file(s) known to git.\n",[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout f22b25e mars.txt"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 11,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cat mars.txt"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 12,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   03-tracking-changes_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -209,9 +434,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 13,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout HEAD mars.txt"[m
    ][m


```

So far, so good: we’ve added one line to the end of the file (shown with a + in the first column). Now let’s put that change in the staging area and see what git diff reports:


{:.input_area}
```xonsh
git add mars.txt
git diff
```

{:.output_stream}
```

[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb[m
[1mindex 0a7156d..4996fde 100644[m
[1m--- a/02-git/02-creating-repositories_instructor.ipynb[m
[1m+++ b/02-git/02-creating-repositories_instructor.ipynb[m
[36m@@ -22,9 +22,32 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 1,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/bin/mkdir: cannot create directory ‘planets’: File exists\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cd ~/Desktop\n",[m
     "mkdir planets\n",[m
[36m@@ -40,9 +63,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 2,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git init"[m
    ][m
[36m@@ -56,9 +88,17 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 3,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls"[m
    ][m
[36m@@ -72,9 +112,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 4,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[0m\u001b[01;34m.\u001b[0m  \u001b[01;34m..\u001b[0m  \u001b[01;34m.git\u001b[0m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls -a"[m
    ][m
[36m@@ -90,9 +139,22 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[32m+[m[32m   "execution_count": 5,[m
    "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "No commits yet\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "nothing to commit (create/copy files and use \"git add\" to track)\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[1mdiff --git a/02-git/03-tracking-changes_instructor.ipynb b/02-git/03-tracking-changes_instructor.ipynb[m
[1mindex 1f99d29..c9b6cac 100644[m
[1m--- a/02-git/03-tracking-changes_instructor.ipynb[m
[1m+++ b/02-git/03-tracking-changes_instructor.ipynb[m
[36m@@ -23,9 +23,18 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 1,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/home/stuart/Git/Aperio/stfc_website/notebooks/02-git\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "pwd"[m
    ][m
[36m@@ -39,18 +48,35 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 2,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "/home/stuart/Git/Aperio/stfc_website/notebooks/02-git\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "pwd"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 3,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cd .."[m
    ][m
[36m@@ -74,18 +100,43 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 4,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "00-lessons.ipynb             \u001b[0m\u001b[01;34m01-bash\u001b[0m  \u001b[01;34m03-fundamentals-of-python\u001b[0m  \u001b[01;34m05-writing-effective-tests\u001b[0m  \u001b[01;34m07-collaborating-with-git\u001b[0m  \u001b[01;34m12-images-and-visualisation\u001b[0m  LICENCE  environment.yml\n",[m
[32m+[m[32m      "00-lessons_instructor.ipynb  \u001b[01;34m02-git\u001b[0m   \u001b[01;34m04-further-python\u001b[0m          \u001b[01;34m06-approximating-pi\u001b[0m         \u001b[01;34m09-units\u001b[0m                   \u001b[01;34m13-images-in-astronomy\u001b[0m       README\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "ls"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 5,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cat mars.txt"[m
    ][m
[36m@@ -99,9 +150,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 6,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -115,9 +184,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 7,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: pathspec 'mars.txt' did not match any files\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git add mars.txt"[m
    ][m
[36m@@ -131,9 +215,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 8,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -147,9 +249,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 9,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Start notes on Mars as a base\""[m
    ][m
[36m@@ -169,9 +286,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 10,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -185,9 +320,64 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 11,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668\u001b[m\u001b[33m (\u001b[m\u001b[1;36mHEAD -> \u001b[m\u001b[1;32mmaster\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/master\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/HEAD\u001b[m\u001b[33m)\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Tue Sep 4 08:41:44 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Mon Sep 3 13:24:05 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 19:25:16 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:51:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    rename to avoid website issues\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:13 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 13:46:49 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add licence and readme to the lessons repo\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 12:59:07 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add initial dump of rendered lessons\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git log"[m
    ][m
[36m@@ -228,9 +418,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 12,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -255,9 +467,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 13,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -271,9 +501,143 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 14,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff"[m
    ][m
[36m@@ -294,9 +658,35 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 15,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Add concerns about effects of Mars' moons on Wolfman\"\n",[m
     "git status"[m
[36m@@ -356,9 +746,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 16,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -366,9 +778,143 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 17,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff"[m
    ][m
[36m@@ -382,9 +928,151 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 18,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: pathspec 'mars.txt' did not match any files\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[1mdiff --git a/02-git/02-creating-repositories_instructor.ipynb b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1mindex 0a7156d..4996fde 100644\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m--- a/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[1m+++ b/02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -22,9 +22,32 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 1,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stderr\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"/bin/mkdir: cannot create directory ‘planets’: File exists\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    },\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"cd ~/Desktop\\n\",\u001b[m\n",[m
[32m+[m[32m      "     \"mkdir planets\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -40,9 +63,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 2,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"Reinitialized existing Git repository in /home/stuart/Desktop/planets/.git/\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git init\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -56,9 +88,17 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 3,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -72,9 +112,18 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 4,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\u001b[0m\\u001b[01;34m.\\u001b[0m  \\u001b[01;34m..\\u001b[0m  \\u001b[01;34m.git\\u001b[0m\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"ls -a\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[36m@@ -90,9 +139,22 @@\u001b[m\n",[m
[32m+[m[32m      "   },\u001b[m\n",[m
[32m+[m[32m      "   {\u001b[m\n",[m
[32m+[m[32m      "    \"cell_type\": \"code\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"execution_count\": null,\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"execution_count\": 5,\u001b[m\n",[m
[32m+[m[32m      "    \"metadata\": {},\u001b[m\n",[m
[32m+[m[32m      "\u001b[31m-   \"outputs\": [],\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   \"outputs\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    {\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"name\": \"stdout\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"output_type\": \"stream\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     \"text\": [\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"On branch master\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"No commits yet\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"nothing to commit (create/copy files and use \\\"git add\\\" to track)\\n\",\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m      \"\\n\"\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m     ]\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m    }\u001b[m\n",[m
[32m+[m[32m      "\u001b[32m+\u001b[m\u001b[32m   ],\u001b[m\n",[m
[32m+[m[32m      "    \"source\": [\u001b[m\n",[m
[32m+[m[32m      "     \"git status\"\u001b[m\n",[m
[32m+[m[32m      "    ]\u001b[m\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git add mars.txt\n",[m
     "git diff"[m
[36m@@ -399,9 +1087,17 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 19,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff --staged"[m
    ][m
[36m@@ -415,9 +1111,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 20,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git commit -m \"Discuss concerns about Mars' climate for Mummy\""[m
    ][m
[36m@@ -431,9 +1142,27 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 21,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-git/02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -447,9 +1176,64 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 22,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\u001b[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668\u001b[m\u001b[33m (\u001b[m\u001b[1;36mHEAD -> \u001b[m\u001b[1;32mmaster\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/master\u001b[m\u001b[33m, \u001b[m\u001b[1;31morigin/HEAD\u001b[m\u001b[33m)\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Tue Sep 4 08:41:44 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Mon Sep 3 13:24:05 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 19:25:16 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:51:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    rename to avoid website issues\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:57 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 14:43:13 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    update notebooks\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 13:46:49 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add licence and readme to the lessons repo\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\u001b[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6\u001b[m\n",[m
[32m+[m[32m      "Author: Stuart Mumford <stuart@cadair.com>\n",[m
[32m+[m[32m      "Date:   Sun Sep 2 12:59:07 2018 +0100\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "    Add initial dump of rendered lessons\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git log"[m
    ][m
[1mdiff --git a/02-git/04-exploring-history_instructor.ipynb b/02-git/04-exploring-history_instructor.ipynb[m
[1mindex 24e0c80..e766d19 100644[m
[1m--- a/02-git/04-exploring-history_instructor.ipynb[m
[1m+++ b/02-git/04-exploring-history_instructor.ipynb[m
[36m@@ -18,9 +18,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 1,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -35,9 +57,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 2,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD mars.txt"[m
    ][m
[36m@@ -51,9 +90,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 3,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD~1 mars.txt"[m
    ][m
[36m@@ -67,9 +123,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 4,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'mars.txt': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff HEAD~2 mars.txt"[m
    ][m
[36m@@ -93,9 +166,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 5,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: bad object f22b25e3233b4645dabd0d81e651fe074bd8e73b\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b mars.txt"[m
    ][m
[36m@@ -109,9 +197,26 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 6,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "fatal: ambiguous argument 'f22b25e': unknown revision or path not in the working tree.\n",[m
[32m+[m[32m      "Use '--' to separate paths from revisions, like this:\n",[m
[32m+[m[32m      "'git <command> [<revision>...] -- [<file>...]'\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git diff f22b25e mars.txt"[m
    ][m
[36m@@ -125,9 +230,31 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 7,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "nano mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -142,9 +269,28 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 8,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   03-tracking-changes_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -158,9 +304,38 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 9,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout HEAD mars.txt\n",[m
     "cat mars.txt"[m
[36m@@ -175,27 +350,77 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 10,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'f22b25e' did not match any file(s) known to git.\n",[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout f22b25e mars.txt"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 11,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "cat: No such file or directory: mars.txt\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "cat mars.txt"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 12,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "On branch master\n",[m
[32m+[m[32m      "Your branch is up to date with 'origin/master'.\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "Changes not staged for commit:\n",[m
[32m+[m[32m      "  (use \"git add <file>...\" to update what will be committed)\n",[m
[32m+[m[32m      "  (use \"git checkout -- <file>...\" to discard changes in working directory)\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   02-creating-repositories_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\t\u001b[31mmodified:   03-tracking-changes_instructor.ipynb\u001b[m\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n",[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git status"[m
    ][m
[36m@@ -209,9 +434,24 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": null,[m
[31m-   "metadata": {},[m
[31m-   "outputs": [],[m
[32m+[m[32m   "execution_count": 13,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stderr",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "error: pathspec 'mars.txt' did not match any file(s) known to git.\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "name": "stdout",[m
[32m+[m[32m     "output_type": "stream",[m
[32m+[m[32m     "text": [[m
[32m+[m[32m      "\n"[m
[32m+[m[32m     ][m
[32m+[m[32m    }[m
[32m+[m[32m   ],[m
    "source": [[m
     "git checkout HEAD mars.txt"[m
    ][m


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
	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

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

	[31mmodified:   02-git/02-creating-repositories_instructor.ipynb[m
	[31mmodified:   02-git/03-tracking-changes_instructor.ipynb[m
	[31mmodified:   02-git/04-exploring-history_instructor.ipynb[m

no changes added to commit (use "git add" and/or "git commit -a")


```

and look at the history of what we’ve done so far:


{:.input_area}
```xonsh
git log
```

{:.output_stream}
```
[33mcommit 5bb6f9a228823fb5890d2c0d6b2e9c0b03673668[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Tue Sep 4 08:41:44 2018 +0100

    update notebooks

[33mcommit dd2848367dff52dd13db252e688a085b0638d2c7[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Mon Sep 3 13:24:05 2018 +0100

    update notebooks

[33mcommit d3568a1b07b9bf76d89803e610c8ece8d4b94a81[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 19:25:16 2018 +0100

    update notebooks

[33mcommit f5844e2671a8c7a2b212214a4f6c8bd72428f7c3[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 14:51:57 2018 +0100

    rename to avoid website issues

[33mcommit ffe8c9dd48510cd2dcbb964c8ead21b93912be21[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 14:43:57 2018 +0100

    update notebooks

[33mcommit 801632edee8fc310d8500bfaeea8651f099283b3[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 14:43:13 2018 +0100

    update notebooks

[33mcommit 9c74198bf838b7f7127d8fab527e4d96aab72e08[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 13:46:49 2018 +0100

    Add licence and readme to the lessons repo

[33mcommit 08b3d7073b526396de7e31ec6e8bd65d075207b6[m
Author: Stuart Mumford <stuart@cadair.com>
Date:   Sun Sep 2 12:59:07 2018 +0100

    Add initial dump of rendered lessons


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


---
The material in this notebook is derived from the Software Carpentry lessons
&copy; [Software Carpentry](http://software-carpentry.org/) under the terms
of the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
