---
interact_link: 02-git/04-exploring-history_instructor.ipynb
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

# Exploring History

As we saw in the previous lesson, we can refer to commits by their identifiers. You can refer to the most recent commit of the working directory by using the identifier HEAD.

We’ve been adding one line at a time to mars.txt, so it’s easy to track our progress by looking, so let’s do that using our HEADs. Before we start, let’s make a change to mars.txt.


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
```

{:.output_stream}
```



```

Now, let’s see what we get.


{:.input_area}
```xonsh
git diff HEAD mars.txt
```

{:.output_stream}
```


```

which is the same as what you would get if you leave out HEAD (try it). The real goodness in all this is when you can refer to previous commits. We do that by adding ~1 (where “~” is “tilde”, pronounced [til-duh]) to refer to the commit one before HEAD.


{:.input_area}
```xonsh
git diff HEAD~1 mars.txt
```

{:.output_stream}
```


```

If we want to see the differences between older commits we can use git diff again, but with the notation HEAD~1, HEAD~2, and so on, to refer to them:


{:.input_area}
```xonsh
git diff HEAD~2 mars.txt
```

{:.output_stream}
```


```

We could also use git show which shows us what changes we made at an older commit as well as the commit message, rather than the differences between a commit and our working directory that we see by using git diff.
git show HEAD~2 mars.txt

In this way, we can build up a chain of commits. The most recent end of the chain is referred to as HEAD; we can refer to previous commits using the ~ notation, so HEAD~1 means “the previous commit”, while HEAD~123 goes back 123 commits from where we are now.

We can also refer to commits using those long strings of digits and letters that git log displays. These are unique IDs for the changes, and “unique” really does mean unique: every change to any set of files on any computer has a unique 40-character identifier. Our first commit was given the ID f22b25e3233b4645dabd0d81e651fe074bd8e73b, so let’s try this:


{:.input_area}
```xonsh
git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b mars.txt
```

{:.output_stream}
```


```

That’s the right answer, but typing out random 40-character strings is annoying, so Git lets us use just the first few characters:


{:.input_area}
```xonsh
git diff f22b25e mars.txt
```

{:.output_stream}
```


```

All right! So we can save changes to files and see what we’ve changed—now how can we restore older versions of things? Let’s suppose we accidentally overwrite our file:


{:.input_area}
```xonsh
nano mars.txt
cat mars.txt
```

{:.output_stream}
```



```

git status now tells us that the file has been changed, but those changes haven’t been staged:


{:.input_area}
```xonsh
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	[32mnew file:   a.dat[m

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   ../01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   ../01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   ../01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-introduction-to-version-control_instructor.ipynb[m
	[31mmodified:   02-creating-repositories_instructor.ipynb[m
	[31mmodified:   03-tracking-changes_instructor.ipynb[m
	[31mmodified:   05-ignoring_instructor.ipynb[m

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	[31mb.dat[m
	[31mc.dat[m
	[31mresults/[m



```

We can put things back the way they were by using git checkout:


{:.input_area}
```xonsh
git checkout HEAD mars.txt
cat mars.txt
```

{:.output_stream}
```



```

As you might guess from its name, git checkout checks out (i.e., restores) an old version of a file. In this case, we’re telling Git that we want to recover the version of the file recorded in HEAD, which is the last saved commit. If we want to go back even further, we can use a commit identifier instead:


{:.input_area}
```xonsh
git checkout f22b25e mars.txt
```

{:.output_stream}
```


```


{:.input_area}
```xonsh
cat mars.txt
```

{:.output_stream}
```


```


{:.input_area}
```xonsh
git status
```

{:.output_stream}
```
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	[32mnew file:   a.dat[m

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	[31mmodified:   ../01-bash/01-introducing-the-shell_instructor.ipynb[m
	[31mmodified:   ../01-bash/02-files-and-directories_instructor.ipynb[m
	[31mmodified:   ../01-bash/03-working-with-files-and-directories_instructor.ipynb[m
	[31mmodified:   01-introduction-to-version-control_instructor.ipynb[m
	[31mmodified:   02-creating-repositories_instructor.ipynb[m
	[31mmodified:   03-tracking-changes_instructor.ipynb[m
	[31mmodified:   05-ignoring_instructor.ipynb[m

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	[31mb.dat[m
	[31mc.dat[m
	[31mresults/[m



```

Notice that the changes are on the staged area. Again, we can put things back the way they were by using git checkout:


{:.input_area}
```xonsh
git checkout HEAD mars.txt
```

{:.output_stream}
```


```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Don’t Lose Your HEAD</h2>
</div>


<div class="panel-body">

<p>Above we used</p>
<div class="codehilite"><pre><span></span>$ git checkout f22b25e mars.txt
</pre></div>


<p>to revert mars.txt to its state after the commit f22b25e. But be careful! The command checkout has other important functionalities and Git will misunderstand your intentions if you are not accurate with the typing. For example, if you forget mars.txt in the previous command.</p>
<div class="codehilite"><pre><span></span>$ git checkout f22b25e
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">Note</span><span class="o">:</span> <span class="n">checking</span> <span class="n">out</span> <span class="s1">&#39;f22b25e&#39;</span><span class="o">.</span>

<span class="n">You</span> <span class="n">are</span> <span class="k">in</span> <span class="s1">&#39;detached HEAD&#39;</span> <span class="n">state</span><span class="o">.</span> <span class="n">You</span> <span class="n">can</span> <span class="n">look</span> <span class="n">around</span><span class="o">,</span> <span class="n">make</span> <span class="n">experimental</span>
<span class="n">changes</span> <span class="n">and</span> <span class="n">commit</span> <span class="n">them</span><span class="o">,</span> <span class="n">and</span> <span class="n">you</span> <span class="n">can</span> <span class="n">discard</span> <span class="n">any</span> <span class="n">commits</span> <span class="n">you</span> <span class="n">make</span> <span class="k">in</span> <span class="k">this</span>
<span class="n">state</span> <span class="n">without</span> <span class="n">impacting</span> <span class="n">any</span> <span class="n">branches</span> <span class="n">by</span> <span class="n">performing</span> <span class="n">another</span> <span class="n">checkout</span><span class="o">.</span>

<span class="n">If</span> <span class="n">you</span> <span class="n">want</span> <span class="n">to</span> <span class="n">create</span> <span class="n">a</span> <span class="k">new</span> <span class="n">branch</span> <span class="n">to</span> <span class="n">retain</span> <span class="n">commits</span> <span class="n">you</span> <span class="n">create</span><span class="o">,</span> <span class="n">you</span> <span class="n">may</span>
<span class="k">do</span> <span class="n">so</span> <span class="o">(</span><span class="n">now</span> <span class="n">or</span> <span class="n">later</span><span class="o">)</span> <span class="n">by</span> <span class="n">using</span> <span class="o">-</span><span class="n">b</span> <span class="k">with</span> <span class="n">the</span> <span class="n">checkout</span> <span class="n">command</span> <span class="n">again</span><span class="o">.</span> <span class="n">Example</span><span class="o">:</span>

 <span class="n">git</span> <span class="n">checkout</span> <span class="o">-</span><span class="n">b</span> <span class="o">&lt;</span><span class="k">new</span><span class="o">-</span><span class="n">branch</span><span class="o">-</span><span class="n">name</span><span class="o">&gt;</span>

<span class="n">HEAD</span> <span class="k">is</span> <span class="n">now</span> <span class="n">at</span> <span class="n">f22b25e</span> <span class="n">Start</span> <span class="n">notes</span> <span class="n">on</span> <span class="n">Mars</span> <span class="k">as</span> <span class="n">a</span> <span class="n">base</span>
</pre></div>


<p>The “detached HEAD” is like “look, but don’t touch” here, so you shouldn’t make any changes in this state. After investigating your repo’s past state, reattach your HEAD with git checkout master.</p>

</div>

</section>


It’s important to remember that we must use the commit number that identifies the state of the repository before the change we’re trying to undo. A common mistake is to use the number of the commit in which we made the change we’re trying to get rid of. In the example below, we want to retrieve the state from before the most recent commit (HEAD~1), which is commit f22b25e:

![](http://swcarpentry.github.io/git-novice/fig/git-checkout.svg)

So, to put it all together, here’s how Git works in cartoon form:

![](http://swcarpentry.github.io/git-novice/fig/git_staging.svg)


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Simplifying the Common Case</h2>
</div>


<div class="panel-body">

<p>If you read the output of git status carefully, you’ll see that it includes this hint:</p>
<div class="codehilite"><pre><span></span>(use &quot;git checkout -- &lt;file&gt;...&quot; to discard changes in working directory)
</pre></div>


<p>As it says, git checkout without a version identifier restores files to the state saved in HEAD. The double dash -- is needed to separate the names of the files being recovered from the command itself: without it, Git would try to use the name of the file as the commit identifier.</p>

</div>

</section>


The fact that files can be reverted one by one tends to change the way people organize their work. If everything is in one large document, it’s hard (but not impossible) to undo changes to the introduction without also undoing changes made later to the conclusion. If the introduction and conclusion are stored in separate files, on the other hand, moving backward and forward in time becomes much easier.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Recovering Older Versions of a File</h2>
</div>


<div class="panel-body">

<p>Jennifer has made changes to the Python script that she has been working on for weeks, and the modifications she made this morning “broke” the script and it no longer runs. She has spent ~ 1hr trying to fix it, with no luck…</p>
<p>Luckily, she has been keeping track of her project’s versions using Git! Which commands below will let her recover the last committed version of her Python script called data_cruncher.py?</p>
<ol>
<li><code>$ git checkout HEAD</code></li>
<li><code>$ git checkout HEAD data_cruncher.py</code></li>
<li><code>$ git checkout HEAD~1 data_cruncher.py</code></li>
<li><code>$ git checkout &lt;unique ID of last commit&gt; data_cruncher.py</code></li>
<li>Both 2 and 4</li>
</ol>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Reverting a Commit</h2>
</div>


<div class="panel-body">

<p>Jennifer is collaborating on her Python script with her colleagues and realizes her last commit to the group repository is wrong and wants to undo it. Jennifer needs to undo correctly so everyone in the group repository gets the correct change. git revert [wrong commit ID] will make a new commit that undoes Jennifer’s previous wrong commit. Therefore git revert is different than git checkout [commit ID] because checkout is for local changes not committed to the group repository. Below are the right steps and explanations for Jennifer to use git revert, what is the missing command?</p>
<ol>
<li><code>________ # Look at the git history of the project to find the commit ID</code></li>
<li>Copy the ID (the first few characters of the ID, e.g. 0b1d055).</li>
<li><code>git revert [commit ID]</code></li>
<li>Type in the new commit message.</li>
<li>Save and close</li>
</ol>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Understanding Workflow and History</h2>
</div>


<div class="panel-body">

<p>What is the output of the last command in</p>
<div class="codehilite"><pre><span></span>$ <span class="nb">cd</span> planets
$ <span class="nb">echo</span> <span class="s2">&quot;Venus is beautiful and full of love&quot;</span> &gt; venus.txt
$ git add venus.txt
$ <span class="nb">echo</span> <span class="s2">&quot;Venus is too hot to be suitable as a base&quot;</span> &gt;&gt; venus.txt
$ git commit -m <span class="s2">&quot;Comment on Venus as an unsuitable base&quot;</span>
$ git checkout HEAD venus.txt
$ cat venus.txt <span class="c1">#this will print the contents of venus.txt to the screen</span>
</pre></div>


<ol>
<li><code>Venus is too hot to be suitable as a base</code></li>
<li><code>Venus is beautiful and full of love</code></li>
<li><code>Venus is beautiful and full of love
   Venus is too hot to be suitable as a base</code></li>
<li>Error because you have changed venus.txt without committing the changes</li>
</ol>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>The answer is 2 because git add venus.txt was used only before add the line Venus is too hot to be suitable as a base which was lost when git checkout was executed. Using the flag -a with git commit would have prevented the lost.</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Checking Understanding of git diff</h2>
</div>


<div class="panel-body">

<p>Consider this command: git diff HEAD~3 mars.txt. What do you predict this command will do if you execute it? What happens when you do execute it? Why?</p>
<p>Try another command, git diff [ID] mars.txt, where [ID] is replaced with the unique identifier for your most recent commit. What do you think will happen, and what does happen?</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Getting Rid of Staged Changes</h2>
</div>


<div class="panel-body">

<p>git checkout can be used to restore a previous commit when unstaged changes have been made, but will it also work for changes that have been staged but not committed? Make a change to mars.txt, add that change, and use git checkout to see if you can remove your change.</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Explore and Summarize Histories</h2>
</div>


<div class="panel-body">

<p>Exploring history is an important part of git, often it is a challenge to find the right commit ID, especially if the commit is from several months ago.</p>
<p>Imagine the planets project has more than 50 files. You would like to find a commit with specific text in mars.txt is modified. When you type git log, a very long list appeared, How can you narrow down the search?</p>
<p>Recall that the git diff command allow us to explore one specific file, e.g. git diff mars.txt. We can apply a similar idea here.</p>
<div class="codehilite"><pre><span></span>$ git log mars.txt
</pre></div>


<p>Unfortunately some of these commit messages are very ambiguous e.g. update files. How can you search through these files?</p>
<p>Both git diff and git log are very useful and they summarize a different part of the history for you. Is it possible to combine both? Let’s try the following:</p>
<div class="codehilite"><pre><span></span>$ git log --patch mars.txt
</pre></div>


<p>You should get a long list of output, and you should be able to see both commit messages and the difference between each commit.</p>
<p>Question: What does the following command do?</p>
<div class="codehilite"><pre><span></span>$ git log --patch HEAD~3 *.txt
</pre></div>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> # Key Points</h2>
</div>


<div class="panel-body">

<ul>
<li>git diff displays differences between commits.</li>
<li>git checkout recovers old versions of files.</li>
</ul>

</div>

</section>

