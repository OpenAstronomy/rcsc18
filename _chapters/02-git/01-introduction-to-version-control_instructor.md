---
interact_link: 02-git/01-introduction-to-version-control_instructor.ipynb
title: 'Introduction to Version Control'
permalink: 'chapters/02-git/01-introduction-to-version-control'
previouschapter:
  url: 
  title: 'Git'
nextchapter:
  url: chapters/02-git/02-creating-repositories
  title: 'Creating Repositories'
redirect_from:
  - 'chapters/02-git/01-introduction-to-version-control'
---

# Introduction to version control

### What is version control?

![Piled Higher and Deeper by Jorge Cham](http://phdcomics.com/comics/archive/phd101212s.gif)

Most of us have experienced some situation similar to the above, and this is the situation version control aims to solve.
Version control systems are a way to track and store changes to a document so that you can continually change one file without losing any of its previous contents.
Since all the changes are saved, it is possible to go back to an earlier state of the document and recover old versions of some or all of the file, without having to save multiple separate documents with different names.
This is extremely useful for both text documents, such as paper manuscripts, and code files, and makes it worth strongly considering using some kind of version control even if you expect to be the only person working on the file.

Another powerful aspect of version control is that you can make different changes separately and combine them together.
Again this can be extremely useful even when working alone, but where it really shines is in working with other people.
This is because the changes don't have to be made on the same computer, so several people can be working on a file at once and those changes can then be combined into your file locally.

You may have used some version tracking capability like the '`Track changes`' option in Word, for example, and if you have heard of or used Git you may also have heard of tools such as RCS, CVS, Subversion or Mercurial. All of these do some amount of version control in different ways, and all have advantages and disadvantages. We will be teaching Git in this course because it is very commonly used and has good tools available for sharing and collaboration, such as GitHub and GitLab.

## Getting set up

When we use Git on a new computer for the first time, we need to configure a few things. Below are a few examples of configurations we will set as we get started with Git:

- our name and email address,
- what our preferred text editor is,
- and that we want to use these settings globally (i.e. for every project).

On a command line, Git commands are written as git verb, where verb is what we actually want to do. So here is how I set up my new laptop:

```
git config --global user.name "Drew Leonard"
git config --global user.email "andy.j.leonard@gmail.com"
```

Please use your own name and email address instead of mine. This user name and email will be associated with your subsequent Git activity, which means that any changes pushed to GitHub, BitBucket, GitLab or another Git host server in a later lesson will include this information.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Line Endings</h2>
</div>


<div class="panel-body">

<p>As with other keys, when you hit Return on your keyboard, your computer encodes this input as a character. For reasons that are long to explain, different operating systems use different character(s) to represent the end of a line. (You may also hear these referred to as newlines or line breaks.) Because Git uses these characters to compare files, it may cause unexpected issues when editing a file on different machines.</p>
<p>You can change the way Git recognizes and encodes line endings using the core.autocrlf command to git config. The following settings are recommended:</p>
<p>On macOS and Linux:</p>
<div class="codehilite"><pre><span></span>git config --global core.autocrlf input
</pre></div>


<p>And on Windows:</p>
<div class="codehilite"><pre><span></span>git config --global core.autocrlf true
</pre></div>


<p>You can read more about this issue on this <a href="https://help.github.com/articles/dealing-with-line-endings/">GitHub page</a>.</p>

</div>

</section>


For these lessons, we will be interacting with GitHub and so the email address used should be the same as the one used when you set up your GitHub account later . If you are concerned about privacy, please review [GitHub’s instructions for keeping your email address private](https://help.github.com/articles/setting-your-commit-email-address-on-github/). If you elect to use a private email address with GitHub, then use that same email address for the user.email value, e.g. username@users.noreply.github.com replacing username with your GitHub one. You can change the email address later on by using the git config command again.

You should also set your favorite text editor now, following this table:

Editor|Configuration command
---|---
Atom|`$ git config --global core.editor "atom --wait"`
nano|`$ git config --global core.editor "nano -w"`
BBEdit (Mac, with command line tools)|`$ git config --global core.editor "bbedit -w"`
Sublime Text (Mac)|`$ git config --global core.editor "/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl -n -w"`
Sublime Text (Win, 32-bit install)|`$ git config --global core.editor "'c:/program files (x86)/sublime text 3/sublime_text.exe' -w"`
Sublime Text (Win, 64-bit install)|`$ git config --global core.editor "'c:/program files/sublime text 3/sublime_text.exe' -w"`
Notepad++ (Win, 32-bit install)|`$ git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`
Notepad++ (Win, 64-bit install)|`$ git config --global core.editor "'c:/program files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`
Kate (Linux)|`$ git config --global core.editor "kate"`
Gedit (Linux)|`$ git config --global core.editor "gedit --wait --new-window"`
Scratch (Linux)|`$ git config --global core.editor "scratch-text-editor"`
Emacs|`$ git config --global core.editor "emacs"`
Vim|`$ git config --global core.editor "vim"`

It is possible to reconfigure the text editor for Git whenever you want to change it.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Exiting Vim</h2>
</div>


<div class="panel-body">

<p>Note that Vim is the default editor for many programs. If you haven’t used Vim before and wish to exit a session without saving your changes, press <code>Esc</code> then type <code>:q!</code> and hit Return. If you want to save your changes and quit, press <code>Esc</code> then type <code>:wq</code> and hit Return.</p>

</div>

</section>


The four commands we just ran above only need to be run once: the flag --global tells Git to use the settings for every project, in your user account, on this computer.

You can check your settings at any time:


{:.input_area}
```xonsh
git config --list
```

{:.output_stream}
```
user.name=Stuart Mumford
user.email=stuart@cadair.com
user.signingkey=E6276769
commit.gpgsign=true
push.default=simple
alias.log=log --show-signature
difftool.latex.cmd=latexdiff  $LOCAL $REMOTE
difftool.latexadd.cmd=latexdiff --graphics-markup=none -t BOLD -f IDENTICAL -s COLOR -X caption $LOCAL $REMOTE
difftool.prompt=false
alias.ldiff=difftool -t latex
alias.ldiffadd=difftool -t latexadd
alias.tree=log --decorate --graph --show-signature
alias.wdiff=diff
credential.helper=/usr/lib/git-core/git-credential-gnome-keyring
filter.lfs.clean=git-lfs clean %f
filter.lfs.smudge=git-lfs smudge %f
filter.lfs.required=true
color.ui=auto
core.editor=vim
github.user=Cadair
github.oauth-token=1f70bdc8ea2446bd1f2fd3c30fefa8ce1b31e676
url.git@github.com:.insteadof=gh:
url.git@gitlab.com:.insteadof=gl:
diff.jupyternotebook.command=git-nbdiffdriver diff
merge.jupyternotebook.driver=git-nbmergedriver merge %O %A %B %L %P
merge.jupyternotebook.name=jupyter notebook merge driver
difftool.nbdime.cmd=git-nbdifftool diff "$LOCAL" "$REMOTE"
mergetool.nbdime.cmd=git-nbmergetool merge "$BASE" "$LOCAL" "$REMOTE" "$MERGED"
mergetool.prompt=false
magithub.online=false
magithub.status.includestatusheader=false
magithub.status.includepullrequestssection=false
magithub.status.includeissuessection=false
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.worktree=../../../notebooks
remote.origin.url=https://github.com/OpenAstronomy/rcsc18_lessons.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master


```

You can change your configuration as many times as you want: just use the same commands to choose another editor or update your email address.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Proxy</h2>
</div>


<div class="panel-body">

<p>In some networks you need to use a proxy. If this is the case, you may also need to tell Git about the proxy:</p>
<div class="codehilite"><pre><span></span>git config --global http.proxy proxy-url
git config --global https.proxy proxy-url
</pre></div>


<p>To disable the proxy, use</p>
<div class="codehilite"><pre><span></span>git config --global --unset http.proxy
git config --global --unset https.proxy
</pre></div>

</div>

</section>



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Git Help and Manual</h2>
</div>


<div class="panel-body">

<p>Always remember that if you forget a git command, you can access the list of commands by using -h and access the Git manual by using --help :</p>
<div class="codehilite"><pre><span></span>git config -h
git config --help
</pre></div>

</div>

</section>



<section class="keypoints panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-exclamation-circle"></span> Key Points</h2>
</div>


<div class="panel-body">

<ul>
<li>Version control is like an unlimited ‘undo’.</li>
<li>Version control also allows many people to work in parallel.</li>
<li>Use git config with the --global option to configure a user name, email address, editor, and other preferences once per machine.</li>
</ul>

</div>

</section>


---
The material in this notebook is derived from the Software Carpentry lessons
&copy; [Software Carpentry](http://software-carpentry.org/) under the terms
of the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
