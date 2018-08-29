---
interact_link: 02-git/02-creating-repos.ipynb
title: 'Creating Repos'
permalink: 'chapters/02-git/02-creating-repos'
previouschapter:
  url: chapters/02-git/01-introduction
  title: 'Introduction'
nextchapter:
  url: chapters/02-git/03-tracking-changes
  title: 'Tracking Changes'
redirect_from:
  - 'chapters/02-git/02-creating-repos'
---

## Creating a repo
Once Git is configured, we can start using it.

We will continue with the story of Wolfman and Dracula who are investigating if it is possible to send a planetary lander to Mars.

motivatingexample

First, let’s create a directory in Desktop folder for our work and then move into that directory:


{:.input_area}
```xonsh
cd ~/Desktop
mkdir planets
cd planets
```

Then we tell Git to make planets a repository—a place where Git can store versions of our files:


{:.input_area}
```xonsh
git init
```

If we use ls to show the directory’s contents, it appears that nothing has changed:


{:.input_area}
```xonsh
ls
```

But if we add the -a flag to show everything, we can see that Git has created a hidden directory within planets called .git:


{:.input_area}
```xonsh
ls -a
```

Git uses this special sub-directory to store all the information about the project, including all files and sub-directories located within the project’s directory. If we ever delete the .git sub-directory, we will lose the project’s history.

We can check that everything is set up correctly by asking Git to tell us the status of our project:


{:.input_area}
```xonsh
git status
```

If you are using a different version of git, the exact wording of the output might be slightly different.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Places to Create Git Repositories</h2>
</div>


<div class="panel-body">

<p>Along with tracking information about planets (the project we have already created), Dracula would also like to track information about moons. Despite Wolfman’s concerns, Dracula creates a moons project inside his planets project with the following sequence of commands:</p>
<div class="codehilite"><pre><span></span>$ <span class="nb">cd</span> ~/Desktop   <span class="c1"># return to Desktop directory</span>
$ <span class="nb">cd</span> planets     <span class="c1"># go into planets directory, which is already a Git repository</span>
$ ls -a          <span class="c1"># ensure the .git sub-directory is still present in the planets directory</span>
$ mkdir moons    <span class="c1"># make a sub-directory planets/moons</span>
$ <span class="nb">cd</span> moons       <span class="c1"># go into moons sub-directory</span>
$ git init       <span class="c1"># make the moons sub-directory a Git repository</span>
$ ls -a          <span class="c1"># ensure the .git sub-directory is present indicating we have created a new Git repository</span>
</pre></div>


<p>Is the <code>git init</code> command, run inside the moons sub-directory, required for tracking files stored in the moons sub-directory?</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>No. Dracula does not need to make the moons sub-directory a Git repository because the planets repository will track all files, sub-directories, and sub-directory files under the planets directory. Thus, in order to track all information about moons, Dracula only needed to add the moons sub-directory to the planets directory.</p>
<p>Additionally, Git repositories can interfere with each other if they are “nested”: the outer repository will try to version-control the inner repository. Therefore, it’s best to create each new Git repository in a separate directory. To be sure that there is no conflicting repository in the directory, check the output of git status. If it looks like the following, you are good to go to create a new repository as shown above:</p>
<div class="codehilite"><pre><span></span>$ git status
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">fatal</span><span class="o">:</span> <span class="n">Not</span> <span class="n">a</span> <span class="n">git</span> <span class="n">repository</span> <span class="o">(</span><span class="n">or</span> <span class="n">any</span> <span class="n">of</span> <span class="n">the</span> <span class="n">parent</span> <span class="n">directories</span><span class="o">):</span> <span class="o">.</span><span class="na">git</span>
</pre></div>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Correcting git init Mistakes</h2>
</div>


<div class="panel-body">

<p>Wolfman explains to Dracula how a nested repository is redundant and may cause confusion down the road. Dracula would like to remove the nested repository. How can Dracula undo his last git init in the moons sub-directory?</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution – USE WITH CAUTION!</h2>
</div>


<div class="panel-body">

<p>To recover from this little mistake, Dracula can just remove the <code>.git</code> folder in the moons subdirectory by running the following command from inside the planets directory:</p>
<div class="codehilite"><pre><span></span>$ rm -rf moons/.git
</pre></div>


<p>But be careful! Running this command in the wrong directory, will remove the entire Git history of a project you might want to keep. Therefore, always check your current directory using the command <code>pwd</code>.</p>

</div>

</section>



<section class="keypoints panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-exclamation-circle"></span> Key Points</h2>
</div>


<div class="panel-body">

<ul>
<li><code>git init</code> initializes a repository.</li>
<li>Git stores all of its repository data in the <code>.git</code> directory.</li>
</ul>

</div>

</section>

