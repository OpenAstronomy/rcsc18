---
interact_link: 02-git/03-tracking-changes.ipynb
title: 'Tracking Changes'
permalink: 'chapters/02-git/03-tracking-changes'
previouschapter:
  url: chapters/02-git/02-creating-repos
  title: 'Creating Repos'
nextchapter:
  url: chapters/02-git/04-exploring-history
  title: 'Exploring History'
redirect_from:
  - 'chapters/02-git/03-tracking-changes'
---

## Adding files and the staging area
First let’s make sure we’re still in the right directory. You should be in the planets directory.


{:.input_area}
```xonsh
pwd
```

If you are still in moons, navigate back up to planets


{:.input_area}
```xonsh
pwd
```


{:.input_area}
```xonsh
cd ..
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


{:.input_area}
```xonsh
cat mars.txt
```

If we check the status of our project again, Git tells us that it’s noticed the new file:


{:.input_area}
```xonsh
git status
```

The “untracked files” message means that there’s a file in the directory that Git isn’t keeping track of. We can tell Git to track a file using git add:


{:.input_area}
```xonsh
git add mars.txt
```

and then check that the right thing happened:


{:.input_area}
```xonsh
git status
```

Git now knows that it’s supposed to keep track of mars.txt, but it hasn’t recorded these changes as a commit yet. To get it to do that, we need to run one more command:


{:.input_area}
```xonsh
git commit -m "Start notes on Mars as a base"
```

When we run `git commit`, Git takes everything we have told it to save by using `git add` and stores a copy permanently inside the special `.git` directory. This permanent copy is called a commit (or revision) and its short identifier is `f22b25e`. Your commit may have another identifier.

We use the `-m` flag (for “message”) to record a short, descriptive, and specific comment that will help us remember later on what we did and why. If we just run `git commit` without the `-m` option, Git will launch `nano` (or whatever other editor we configured as `core.editor`) so that we can write a longer message.

Good commit messages start with a brief (<50 characters) statement about the changes made in the commit. Generally, the message should complete the sentence “If applied, this commit will” . If you want to go into more detail, add a blank line between the summary line and your additional notes. Use this additional space to explain why you made changes and/or what their impact will be.

If we run `git status` now:


{:.input_area}
```xonsh
git status
```

it tells us everything is up to date. If we want to know what we’ve done recently, we can ask Git to show us the project’s history using `git log`:


{:.input_area}
```xonsh
git log
```

`git log` lists all commits made to a repository in reverse chronological order. The listing for each commit includes the commit’s full identifier (which starts with the same characters as the short identifier printed by the git commit command earlier), the commit’s author, when it was created, and the log message Git was given when the commit was created.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Where Are My Changes?</h2>
</div>


<div class="panel-body">

If we run `ls` at this point, we will still see just one file called `mars.txt`. That’s because Git saves information about files’ history in the special `.git` directory mentioned earlier so that our filesystem doesn’t become cluttered (and so that we can’t accidentally edit or delete an old version).

</div>

</section>


Now suppose Dracula adds more information to the file. (Again, we’ll edit with `nano` and then `cat` the file to show its contents; you may use a different editor, and don’t need to `cat`.)


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
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

The last line is the key phrase: “no changes added to commit”. We have changed this file, but we haven’t told Git we will want to save those changes (which we do with `git add`) nor have we saved them (which we do with `git commit`). So let’s do that now. It is good practice to always review our changes before saving them. We do this using git diff. This shows us the differences between the current state of the file and the most recently saved version:


{:.input_area}
```xonsh
git diff
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

Whoops: Git won’t commit because we didn’t use git add first. Let’s fix that:

git add mars.txt
git commit -m "Add concerns about effects of Mars' moons on Wolfman"

Git insists that we add files to the set we want to commit before actually committing anything. This allows us to commit our changes in stages and capture changes in logical portions rather than only large batches. For example, suppose we’re adding a few citations to relevant research to our thesis. We might want to commit those additions, and the corresponding bibliography entries, but not commit some of our work drafting the conclusion (which we haven’t finished yet).

To allow for this, Git has a special staging area where it keeps track of things that have been added to the current changeset but not yet committed.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Staging Area</h2>
</div>


<div class="panel-body">

If you think of Git as taking snapshots of changes over the life of a project, git add specifies what will go in a snapshot (putting things in the staging area), and git commit then actually takes the snapshot, and makes a permanent record of it (as a commit). If you don’t have anything staged when you type git commit, Git will prompt you to use git commit -a or git commit --all, which is kind of like gathering everyone for the picture! However, it’s almost always better to explicitly add things to the staging area, because you might commit changes you forgot you made. (Going back to snapshots, you might get the extra with incomplete makeup walking on the stage for the snapshot because you used -a!) Try to stage things manually, or you might find yourself searching for “git undo commit” more than you would like!

![](http://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)

</div>

</section>


Let’s watch as our changes to a file move from our editor to the staging area and into long-term storage. First, we’ll add another line to the file:


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
```


{:.input_area}
```xonsh
git diff
```

So far, so good: we’ve added one line to the end of the file (shown with a + in the first column). Now let’s put that change in the staging area and see what git diff reports:


{:.input_area}
```xonsh
git add mars.txt
git diff
```

There is no output: as far as Git can tell, there’s no difference between what it’s been asked to save permanently and what’s currently in the directory. However, if we do this:


{:.input_area}
```xonsh
git diff --staged
```

it shows us the difference between the last committed change and what’s in the staging area. Let’s save our changes:


{:.input_area}
```xonsh
git commit -m "Discuss concerns about Mars' climate for Mummy"
```

check our status:


{:.input_area}
```xonsh
git status
```

and look at the history of what we’ve done so far:


{:.input_area}
```xonsh
git log
```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Word-based diffing</h2>
</div>


<div class="panel-body">

Sometimes, e.g. in the case of the text documents a line-wise diff is too coarse. That is where the --color-words option of git diff comes in very useful as it highlights the changed words using colors.

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Paging the Log</h2>
</div>


<div class="panel-body">

When the output of git log is too long to fit in your screen, git uses a program to split it into pages of the size of your screen. When this “pager” is called, you will notice that the last line in your screen is a :, instead of your usual prompt.

- To get out of the pager, press Q.
- To move to the next page, press Spacebar.
- To search for some_word in all pages, press / and type some_word. Navigate through matches pressing N.

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Limit Log Size</h2>
</div>


<div class="panel-body">

To avoid having git log cover your entire terminal screen, you can limit the number of commits that Git lists by using -N, where N is the number of commits that you want to view. For example, if you only want information from the last commit you can use:

```
$ git log -1

commit 005937fbe2a98fb83f0ade869025dc2636b4dad5
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Thu Aug 22 10:14:07 2013 -0400

   Discuss concerns about Mars' climate for Mummy
```

You can also reduce the quantity of information using the --oneline option:

```
$ git log --oneline

 * 005937f Discuss concerns about Mars' climate for Mummy
 * 34961b1 Add concerns about effects of Mars' moons on Wolfman
 * f22b25e Start notes on Mars as a base
```

You can also combine the --oneline options with others. One useful combination is:

```
$ git log --oneline --graph --all --decorate

* 005937f Discuss concerns about Mars' climate for Mummy (HEAD, master)
* 34961b1 Add concerns about effects of Mars' moons on Wolfman
* f22b25e Start notes on Mars as a base
```

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Directories</h2>
</div>


<div class="panel-body">

Two important facts you should know about directories in Git.

1. Git does not track directories on their own, only files within them. Try it for yourself:

```
$ mkdir directory
$ git status
$ git add directory
$ git status
```

Note, our newly created empty directory directory does not appear in the list of untracked files even if we explicitly add it (via git add) to our repository. This is the reason why you will sometimes see .gitkeep files in otherwise empty directories. Unlike .gitignore, these files are not special and their sole purpose is to populate a directory so that Git adds it to the repository. In fact, you can name such files anything you like.

2. If you create a directory in your Git repository and populate it with files, you can add all files in the directory at once by:

```
git add <directory-with-files>
```

</div>

</section>


To recap, when we want to add changes to our repository, we first need to add the changed files to the staging area (git add) and then commit the staged changes to the repository (git commit):

![](http://swcarpentry.github.io/git-novice/fig/git-committing.svg)


<section class="challange panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Choosing a Commit Message</h2>
</div>


<div class="panel-body">

Which of the following commit messages would be most appropriate for the last commit made to mars.txt?

- “Changes”
- “Added line ‘But the Mummy will appreciate the lack of humidity’ to mars.txt”
- “Discuss effects of Mars’ climate on the Mummy”

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">

Answer 1 is not descriptive enough, and the purpose of the commit is unclear; and answer 2 is redundant to using “git diff” to see what changed in this commit; but answer 3 is good: short, descriptive, and imperative.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Committing Changes to Git</h2>
</div>


<div class="panel-body">

Which command(s) below would save the changes of myfile.txt to my local Git repository?

```
$ git commit -m "my recent changes"

$ git init myfile.txt
$ git commit -m "my recent changes"

$ git add myfile.txt
$ git commit -m "my recent changes"

$ git commit -m myfile.txt "my recent changes"
```

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">

- Would only create a commit if files have already been staged.
- Would try to create a new repository.
- Is correct: first add the file to the staging area, then commit.
- Would try to commit a file “my recent changes” with the message myfile.txt.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Committing Multiple Files</h2>
</div>


<div class="panel-body">

The staging area can hold changes from any number of files that you want to commit as a single snapshot.

1. Add some text to mars.txt noting your decision to consider Venus as a base
1. Create a new file venus.txt with your initial thoughts about Venus as a base for you and your friends
1. Add changes from both files to the staging area, and commit those changes.

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">

First we make our changes to the mars.txt and venus.txt files:

```
$ nano mars.txt
$ cat mars.txt

Maybe I should start with a base on Venus.

$ nano venus.txt
$ cat venus.txt

Venus is a nice planet and I definitely should consider it as a base.
```

Now you can add both files to the staging area. We can do that in one line:

```
$ git add mars.txt venus.txt
```

Or with multiple commands:

```
$ git add mars.txt
$ git add venus.txt
```

Now the files are ready to commit. You can check that using git status. If you are ready to commit use:

```
$ git commit -m "Write plans to start a base on Venus"

[master cc127c2]
 Write plans to start a base on Venus
 2 files changed, 2 insertions(+)
 create mode 100644 venus.txt
```

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # `bio` Repository</h2>
</div>


<div class="panel-body">

- Create a new Git repository on your computer called bio.
- Write a three-line biography for yourself in a file called me.txt, commit your changes
- Modify one line, add a fourth line
- Display the differences between its updated state and its original state.

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">

If needed, move out of the planets folder:

```
$ cd ..
```

Create a new folder called bio and ‘move’ into it:

```
$ mkdir bio
$ cd bio
```

Initialise git:

```
$ git init
```

Create your biography file me.txt using nano or another text editor. Once in place, add and commit it to the repository:

```
$ git add me.txt
$ git commit -m'Adding biography file'
```

Modify the file as described (modify one line, add a fourth line). To display the differences between its updated state and its original state, use git diff:

```
$ git diff me.txt
```

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Author and Committer</h2>
</div>


<div class="panel-body">

For each of the commits you have done, Git stored your name twice. You are named as the author and as the committer. You can observe that by telling Git to show you more information about your last commits:

```
$ git log --format=full
```

When committing you can name someone else as the author:

```
$ git commit --author="Vlad Dracula <vlad@tran.sylvan.ia>"
```

Create a new repository and create two commits: one without the --author option and one by naming a colleague of yours as the author. Run git log and git log --format=full. Think about ways how that can allow you to collaborate with your colleagues.

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">

```
$ git add me.txt
$ git commit -m "Update Vlad's bio." --author="Frank N. Stein <franky@monster.com>"

[master 4162a51] Update Vlad's bio.
Author: Frank N. Stein <franky@monster.com>
1 file changed, 2 insertions(+), 2 deletions(-)

$ git log --format=full
commit 4162a51b273ba799a9d395dd70c45d96dba4e2ff
Author: Frank N. Stein <franky@monster.com>
Commit: Vlad Dracula <vlad@tran.sylvan.ia>

Update Vlad's bio.

commit aaa3271e5e26f75f11892718e83a3e2743fab8ea
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Commit: Vlad Dracula <vlad@tran.sylvan.ia>

Vlad's initial bio.
```

</div>

</section>



<section class="keypoints panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-exclamation-circle"> # Key Points</h2>
</div>


<div class="panel-body">

- git status shows the status of a repository.
- Files can be stored in a project’s working directory (which users see), the staging area (where the next commit is being built up) and the local repository (where commits are permanently recorded).
- git add puts files in the staging area.
- git commit saves the staged content as a new commit in the local repository.
- Write a commit message that accurately describes your changes.

</div>

</section>

