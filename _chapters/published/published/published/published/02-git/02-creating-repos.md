---
interact_link: notebooks/published/published/published/published/02-git/02-creating-repos.ipynb
title: 'Creating Repos'
permalink: 'chapters/published/published/published/published/02-git/02-creating-repos'
previouschapter:
  url: chapters/published/published/published/published/02-git/01-introduction
  title: 'Introduction'
nextchapter:
  url: chapters/published/published/published/published/02-git/03-tracking-changes
  title: 'Tracking Changes'
redirect_from:
  - 'chapters/published/published/published/published/02-git/02-creating-repos'
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

{:.output_stream}
```
[0m[01;34m.[0m  [01;34m..[0m  [01;34m.git[0m

```

Git uses this special sub-directory to store all the information about the project, including all files and sub-directories located within the project’s directory. If we ever delete the .git sub-directory, we will lose the project’s history.

We can check that everything is set up correctly by asking Git to tell us the status of our project:


{:.input_area}
```xonsh
git status
```

If you are using a different version of git, the exact wording of the output might be slightly different.

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h4>Places to Create Git Repositories</h4>
<p>Along with tracking information about planets (the project we have already created), Dracula would also like to track information about moons. Despite Wolfman’s concerns, Dracula creates a moons project inside his planets project with the following sequence of commands:</p>
<p>`$ cd ~/Desktop   # return to Desktop directory
$ cd planets     # go into planets directory, which is already a Git repository
$ ls -a          # ensure the .git sub-directory is still present in the planets directory
$ mkdir moons    # make a sub-directory planets/moons
$ cd moons       # go into moons sub-directory
$ git init       # make the moons sub-directory a Git repository
$ ls -a          # ensure the .git sub-directory is present indicating we have created a new Git repository`</p>
<p>Is the `git init` command, run inside the moons sub-directory, required for tracking files stored in the moons sub-directory?</p></div></div></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h4>Solution</h4>
<p>No. Dracula does not need to make the moons sub-directory a Git repository because the planets repository will track all files, sub-directories, and sub-directory files under the planets directory. Thus, in order to track all information about moons, Dracula only needed to add the moons sub-directory to the planets directory.</p>
<p>Additionally, Git repositories can interfere with each other if they are “nested”: the outer repository will try to version-control the inner repository. Therefore, it’s best to create each new Git repository in a separate directory. To be sure that there is no conflicting repository in the directory, check the output of git status. If it looks like the following, you are good to go to create a new repository as shown above:</p>
<p>`$ git status`
`fatal: Not a git repository (or any of the parent directories): .git`</p></div></div></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h4>Correcting git init Mistakes</h4>
<p>Wolfman explains to Dracula how a nested repository is redundant and may cause confusion down the road. Dracula would like to remove the nested repository. How can Dracula undo his last git init in the moons sub-directory?</p></div></div></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h4>Solution – USE WITH CAUTION!</h4>
<p>To recover from this little mistake, Dracula can just remove the `.git` folder in the moons subdirectory by running the following command from inside the planets directory:</p>
<p>`$ rm -rf moons/.git`</p>
<p>But be careful! Running this command in the wrong directory, will remove the entire Git history of a project you might want to keep. Therefore, always check your current directory using the command `pwd`.</p></div></div></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><h4>Key Points</h4>
<ul>
<li>`git init` initializes a repository.</li>
<li>Git stores all of its repository data in the `.git` directory.</li>
</ul></div></div></div></div></div>
