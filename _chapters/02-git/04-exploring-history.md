---
interact_link: 02-git/04-exploring-history.ipynb
title: 'Exploring History'
permalink: 'chapters/02-git/04-exploring-history'
previouschapter:
  url: chapters/02-git/03-tracking-changes
  title: 'Tracking Changes'
nextchapter:
  url: chapters/02-git/05-ignoring
  title: 'Ignoring'
redirect_from:
  - 'chapters/02-git/04-exploring-history'
---

## Exploring History

As we saw in the previous lesson, we can refer to commits by their identifiers. You can refer to the most recent commit of the working directory by using the identifier HEAD.

We’ve been adding one line at a time to mars.txt, so it’s easy to track our progress by looking, so let’s do that using our HEADs. Before we start, let’s make a change to mars.txt.


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
```

Now, let’s see what we get.


{:.input_area}
```xonsh
git diff HEAD mars.txt
```

which is the same as what you would get if you leave out HEAD (try it). The real goodness in all this is when you can refer to previous commits. We do that by adding ~1 (where “~” is “tilde”, pronounced [til-duh]) to refer to the commit one before HEAD.


{:.input_area}
```xonsh
git diff HEAD~1 mars.txt
```

If we want to see the differences between older commits we can use git diff again, but with the notation HEAD~1, HEAD~2, and so on, to refer to them:


{:.input_area}
```xonsh
git diff HEAD~2 mars.txt
```

We could also use git show which shows us what changes we made at an older commit as well as the commit message, rather than the differences between a commit and our working directory that we see by using git diff.
git show HEAD~2 mars.txt

In this way, we can build up a chain of commits. The most recent end of the chain is referred to as HEAD; we can refer to previous commits using the ~ notation, so HEAD~1 means “the previous commit”, while HEAD~123 goes back 123 commits from where we are now.

We can also refer to commits using those long strings of digits and letters that git log displays. These are unique IDs for the changes, and “unique” really does mean unique: every change to any set of files on any computer has a unique 40-character identifier. Our first commit was given the ID f22b25e3233b4645dabd0d81e651fe074bd8e73b, so let’s try this:


{:.input_area}
```xonsh
git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b mars.txt
```

That’s the right answer, but typing out random 40-character strings is annoying, so Git lets us use just the first few characters:


{:.input_area}
```xonsh
git diff f22b25e mars.txt
```

All right! So we can save changes to files and see what we’ve changed—now how can we restore older versions of things? Let’s suppose we accidentally overwrite our file:


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
```

git status now tells us that the file has been changed, but those changes haven’t been staged:


{:.input_area}
```xonsh
git status
```

We can put things back the way they were by using git checkout:


{:.input_area}
```xonsh
git checkout HEAD mars.txt
cat mars.txt
```

As you might guess from its name, git checkout checks out (i.e., restores) an old version of a file. In this case, we’re telling Git that we want to recover the version of the file recorded in HEAD, which is the last saved commit. If we want to go back even further, we can use a commit identifier instead:


{:.input_area}
```xonsh
git checkout f22b25e mars.txt
```


{:.input_area}
```xonsh
cat mars.txt
```


{:.input_area}
```xonsh
git status
```

Notice that the changes are on the staged area. Again, we can put things back the way they were by using git checkout:


{:.input_area}
```xonsh
git checkout HEAD mars.txt
```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Don’t Lose Your HEAD</h2>
</div>


<div class="panel-body">


Above we used

```
$ git checkout f22b25e mars.txt
```

to revert mars.txt to its state after the commit f22b25e. But be careful! The command checkout has other important functionalities and Git will misunderstand your intentions if you are not accurate with the typing. For example, if you forget mars.txt in the previous command.

```
$ git checkout f22b25e
```
```
Note: checking out 'f22b25e'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

 git checkout -b <new-branch-name>

HEAD is now at f22b25e Start notes on Mars as a base
```

The “detached HEAD” is like “look, but don’t touch” here, so you shouldn’t make any changes in this state. After investigating your repo’s past state, reattach your HEAD with git checkout master.

</div>

</section>


It’s important to remember that we must use the commit number that identifies the state of the repository before the change we’re trying to undo. A common mistake is to use the number of the commit in which we made the change we’re trying to get rid of. In the example below, we want to retrieve the state from before the most recent commit (HEAD~1), which is commit f22b25e:

![](http://swcarpentry.github.io/git-novice/fig/git-checkout.svg)

So, to put it all together, here’s how Git works in cartoon form:

![](http://swcarpentry.github.io/git-novice/fig/git_staging.svg)


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Simplifying the Common Case</h2>
</div>


<div class="panel-body">


If you read the output of git status carefully, you’ll see that it includes this hint:

```
(use "git checkout -- <file>..." to discard changes in working directory)
```

As it says, git checkout without a version identifier restores files to the state saved in HEAD. The double dash -- is needed to separate the names of the files being recovered from the command itself: without it, Git would try to use the name of the file as the commit identifier.

</div>

</section>


The fact that files can be reverted one by one tends to change the way people organize their work. If everything is in one large document, it’s hard (but not impossible) to undo changes to the introduction without also undoing changes made later to the conclusion. If the introduction and conclusion are stored in separate files, on the other hand, moving backward and forward in time becomes much easier.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Recovering Older Versions of a File</h2>
</div>


<div class="panel-body">


Jennifer has made changes to the Python script that she has been working on for weeks, and the modifications she made this morning “broke” the script and it no longer runs. She has spent ~ 1hr trying to fix it, with no luck…

Luckily, she has been keeping track of her project’s versions using Git! Which commands below will let her recover the last committed version of her Python script called data_cruncher.py?

1. `$ git checkout HEAD`
1. `$ git checkout HEAD data_cruncher.py`
1. `$ git checkout HEAD~1 data_cruncher.py`
1. `$ git checkout <unique ID of last commit> data_cruncher.py`
1. Both 2 and 4

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Reverting a Commit</h2>
</div>


<div class="panel-body">


Jennifer is collaborating on her Python script with her colleagues and realizes her last commit to the group repository is wrong and wants to undo it. Jennifer needs to undo correctly so everyone in the group repository gets the correct change. git revert [wrong commit ID] will make a new commit that undoes Jennifer’s previous wrong commit. Therefore git revert is different than git checkout [commit ID] because checkout is for local changes not committed to the group repository. Below are the right steps and explanations for Jennifer to use git revert, what is the missing command?

1. `________ # Look at the git history of the project to find the commit ID`
1. Copy the ID (the first few characters of the ID, e.g. 0b1d055).
1. `git revert [commit ID]`
1. Type in the new commit message.
1. Save and close

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Understanding Workflow and History</h2>
</div>


<div class="panel-body">


What is the output of the last command in

```
$ cd planets
$ echo "Venus is beautiful and full of love" > venus.txt
$ git add venus.txt
$ echo "Venus is too hot to be suitable as a base" >> venus.txt
$ git commit -m "Comment on Venus as an unsuitable base"
$ git checkout HEAD venus.txt
$ cat venus.txt #this will print the contents of venus.txt to the screen
```

1. `Venus is too hot to be suitable as a base`
1. `Venus is beautiful and full of love`
1. 
```Venus is beautiful and full of love
   Venus is too hot to be suitable as a base
```
1. Error because you have changed venus.txt without committing the changes

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">

The answer is 2 because git add venus.txt was used only before add the line Venus is too hot to be suitable as a base which was lost when git checkout was executed. Using the flag -a with git commit would have prevented the lost.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Checking Understanding of git diff</h2>
</div>


<div class="panel-body">

Consider this command: git diff HEAD~3 mars.txt. What do you predict this command will do if you execute it? What happens when you do execute it? Why?

Try another command, git diff [ID] mars.txt, where [ID] is replaced with the unique identifier for your most recent commit. What do you think will happen, and what does happen?

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Getting Rid of Staged Changes</h2>
</div>


<div class="panel-body">

git checkout can be used to restore a previous commit when unstaged changes have been made, but will it also work for changes that have been staged but not committed? Make a change to mars.txt, add that change, and use git checkout to see if you can remove your change.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Explore and Summarize Histories</h2>
</div>


<div class="panel-body">

Exploring history is an important part of git, often it is a challenge to find the right commit ID, especially if the commit is from several months ago.

Imagine the planets project has more than 50 files. You would like to find a commit with specific text in mars.txt is modified. When you type git log, a very long list appeared, How can you narrow down the search?

Recall that the git diff command allow us to explore one specific file, e.g. git diff mars.txt. We can apply a similar idea here.

```
$ git log mars.txt
```

Unfortunately some of these commit messages are very ambiguous e.g. update files. How can you search through these files?

Both git diff and git log are very useful and they summarize a different part of the history for you. Is it possible to combine both? Let’s try the following:

```
$ git log --patch mars.txt
```

You should get a long list of output, and you should be able to see both commit messages and the difference between each commit.

Question: What does the following command do?

```
$ git log --patch HEAD~3 *.txt
```

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> # Key Points</h2>
</div>


<div class="panel-body">


- git diff displays differences between commits.
- git checkout recovers old versions of files.

</div>

</section>

