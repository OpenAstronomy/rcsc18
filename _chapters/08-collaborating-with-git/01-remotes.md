---
interact_link: 08-collaborating-with-git/01-remotes.ipynb
title: 'Remotes'
permalink: 'chapters/08-collaborating-with-git/01-remotes'
previouschapter:
  url: 
  title: 'Collaborating With Git'
nextchapter:
  url: chapters/08-collaborating-with-git/02-making-work-public
  title: 'Making Work Public'
redirect_from:
  - 'chapters/08-collaborating-with-git/01-remotes'
---

## Remotes in GitHub

Version control really comes into its own when we begin to collaborate with other people. We already have most of the machinery we need to do this; the only thing missing is to copy changes from one repository to another.

Systems like Git allow us to move work between any two repositories. In practice, though, it’s easiest to use one copy as a central hub, and to keep it on the web rather than on someone’s laptop. Most programmers use hosting services like GitHub, BitBucket or GitLab to hold those master copies; we’ll explore the pros and cons of this in the final section of this lesson.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Getting a GitHub account</h2>
</div>


<div class="panel-body">


This lesson and the remainder of the workshop require you to have a GitHub account. If you have one already, make sure that you remember your username and password - check these now by logging in at [github.com](https://github.com/). If you don't already have an account, go to [github.com](https://github.com/) and make one.

</div>

</section>


Let’s start by sharing the changes we’ve made to our current project with the world. Log in to GitHub, then click on the icon in the top right corner to create a new repository called planets:

![](http://swcarpentry.github.io/git-novice/fig/github-create-repo-01.png)

Name your repository “planets” and then click “Create Repository”:

![](http://swcarpentry.github.io/git-novice/fig/github-create-repo-02.png)

As soon as the repository is created, GitHub displays a page with a URL and some information on how to configure your local repository:

![](http://swcarpentry.github.io/git-novice/fig/github-create-repo-03.png)

This effectively does the following on GitHub’s servers:

```
$ mkdir planets
$ cd planets
$ git init
```

If you remember back to the earlier lesson where we added and commited our earlier work on mars.txt, we had a diagram of the local repository which looked like this:

![](http://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)

Now that we have two repositories, we need a diagram like this:

![](http://swcarpentry.github.io/git-novice/fig/git-freshly-made-github-repo.svg)

Note that our local repository still contains our earlier work on mars.txt, but the remote repository on GitHub appears empty as it doesn’t contain any files yet.

The next step is to connect the two repositories. We do this by making the GitHub repository a remote for the local repository. The home page of the repository on GitHub includes the string we need to identify it:

![](http://swcarpentry.github.io/git-novice/fig/github-find-repo-string.png)

Click on the ‘HTTPS’ link to change the protocol from SSH to HTTPS.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # HTTPS vs. SSH</h2>
</div>


<div class="panel-body">


We use HTTPS here because it does not require additional configuration. After the workshop you may want to set up SSH access, which is a bit more secure, by following one of the great tutorials from GitHub, Atlassian/BitBucket and GitLab (this one has a screencast).

</div>

</section>


![](http://swcarpentry.github.io/git-novice/fig/github-change-repo-string.png)

Copy that URL from the browser, go into the local planets repository, and run this command:


{:.input_area}
```xonsh
git remote add origin https://github.com/vlad/planets.git
```

Make sure to use the URL for your repository rather than Vlad’s: the only difference should be your username instead of vlad.

We can check that the command has worked by running git remote -v:


{:.input_area}
```xonsh
git remote -v
```

The name origin is a local nickname for your remote repository. We could use something else if we wanted to, but origin is by far the most common choice.

Once the nickname origin is set up, this command will push the changes from our local repository to the repository on GitHub:


{:.input_area}
```xonsh
git push origin master
```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Proxy</h2>
</div>


<div class="panel-body">


If the network you are connected to uses a proxy, there is a chance that your last command failed with “Could not resolve hostname” as the error message. To solve this issue, you need to tell Git about the proxy:

```
$ git config --global http.proxy http://user:password@proxy.url
$ git config --global https.proxy http://user:password@proxy.url
```

When you connect to another network that doesn’t use a proxy, you will need to tell Git to disable the proxy using:

```
$ git config --global --unset http.proxy
$ git config --global --unset https.proxy
```

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # Password Managers</h2>
</div>


<div class="panel-body">


If your operating system has a password manager configured, git push will try to use it when it needs your username and password. For example, this is the default behavior for Git Bash on Windows. If you want to type your username and password at the terminal instead of using a password manager, type:

```
$ unset SSH_ASKPASS
```

in the terminal, before you run git push. Despite the name, git uses SSH_ASKPASS for all credential entry, so you may want to unset SSH_ASKPASS whether you are using git via SSH or https.

You may also want to add unset SSH_ASKPASS at the end of your ~/.bashrc to make git default to using the terminal for usernames and passwords.

</div>

</section>


Our local and remote repositories are now in this state:

![](http://swcarpentry.github.io/git-novice/fig/github-repo-after-first-push.svg)


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> # The ‘-u’ Flag</h2>
</div>


<div class="panel-body">


You may see a -u option used with git push in some documentation. This option is synonymous with the --set-upstream-to option for the git branch command, and is used to associate the current branch with a remote branch so that the git pull command can be used without any arguments. To do this, simply use git push -u origin master once the remote has been set up.

</div>

</section>


We can pull changes from the remote repository to the local one as well:


{:.input_area}
```xonsh
git pull origin master
```

Pulling has no effect in this case because the two repositories are already synchronized. If someone else had pushed some changes to the repository on GitHub, though, this command would download them to our local repository.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # GitHub GUI</h2>
</div>


<div class="panel-body">


Browse to your planets repository on GitHub. Under the Code tab, find and click on the text that says “XX commits” (where “XX” is some number). Hover over, and click on, the three buttons to the right of each commit. What information can you gather/explore from these buttons? How would you get that same information in the shell?

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


The left-most button (with the picture of a clipboard) copies the full identifier of the commit to the clipboard. In the shell, git log will show you the full commit identifier for each commit.

When you click on the middle button, you’ll see all of the changes that were made in that particular commit. Green shaded lines indicate additions and red ones removals. In the shell we can do the same thing with git diff. In particular, git diff ID1..ID2 where ID1 and ID2 are commit identifiers (e.g. git diff a3bf1e5..041e637) will show the differences between those two commits.

The right-most button lets you view all of the files in the repository at the time of that commit. To do this in the shell, we’d need to checkout the repository at that particular time. We can do this with git checkout ID where ID is the identifier of the commit we want to look at. If we do this, we need to remember to put the repository back to the right state afterwards!

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # GitHub Timestamp</h2>
</div>


<div class="panel-body">


Create a remote repository on GitHub. Push the contents of your local repository to the remote. Make changes to your local repository and push these changes. Go to the repo you just created on GitHub and check the timestamps of the files. How does GitHub record times, and why?

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


GitHub displays timestamps in a human readable relative format (i.e. “22 hours ago” or “three weeks ago”). However, if you hover over the timestamp, you can see the exact time at which the last change to the file occurred.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Push vs. Commit</h2>
</div>


<div class="panel-body">


In this lesson, we introduced the “git push” command. How is “git push” different from “git commit”?

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


When we push changes, we’re interacting with a remote repository to update it with the changes we’ve made locally (often this corresponds to sharing the changes we’ve made with others). Commit only updates your local repository.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Fixing Remote Settings</h2>
</div>


<div class="panel-body">


It happens quite often in practice that you made a typo in the remote URL. This exercise is about how to fix this kind of issue. First start by adding a remote with an invalid URL:

```
git remote add broken https://github.com/this/url/is/invalid
```

Do you get an error when adding the remote? Can you think of a command that would make it obvious that your remote URL was not valid? Can you figure out how to fix the URL (tip: use git remote -h)? Don’t forget to clean up and remove this remote once you are done with this exercise.

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


We don’t see any error message when we add the remote (adding the remote tells git about it, but doesn’t try to use it yet). As soon as we try to use git push we’ll see an error message. The command git remote set-url allows us to change the remote’s URL to fix it.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # GitHub License and README files</h2>
</div>


<div class="panel-body">


In this section we learned about creating a remote repository on GitHub, but when you initialized your GitHub repo, you didn’t add a README.md or a license file. If you had, what do you think would have happened when you tried to link your local and remote repositories?

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


In this case, since we already had a README file in our own (local) repository, we’d see a merge conflict (when git realises that there are two versions of the file and asks us to reconcile the differences).

</div>

</section>



<section class="keypoints panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-exclamation-circle"> # Key Points</h2>
</div>


<div class="panel-body">


- A local Git repository can be connected to one or more remote repositories.
- Use the HTTPS protocol to connect to remote repositories until you have learned how to set up SSH.
- git push copies changes from a local repository to a remote repository.
- git pull copies changes from a remote repository to a local repository.

</div>

</section>

