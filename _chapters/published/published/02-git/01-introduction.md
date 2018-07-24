---
interact_link: notebooks/published/published/02-git/01-introduction.ipynb
title: 'Introduction'
permalink: 'chapters/published/published/02-git/01-introduction'
previouschapter:
  url: 
  title: 'Git'
nextchapter:
  url: chapters/published/published/02-git/02-creating-repos
  title: 'Creating Repos'
redirect_from:
  - 'chapters/published/published/02-git/01-introduction'
---

## Introduction to version control

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


{:.input_area}
```xonsh
git config --global user.name "Drew Leonard"
git config --global user.email "andy.j.leonard@gmail.com"
```

Please use your own name and email address instead of mine. This user name and email will be associated with your subsequent Git activity, which means that any changes pushed to GitHub, BitBucket, GitLab or another Git host server in a later lesson will include this information.

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h4>Line Endings</h4>
<p>As with other keys, when you hit Return on your keyboard, your computer encodes this input as a character. For reasons that are long to explain, different operating systems use different character(s) to represent the end of a line. (You may also hear these referred to as newlines or line breaks.) Because Git uses these characters to compare files, it may cause unexpected issues when editing a file on different machines.</p>
<p>You can change the way Git recognizes and encodes line endings using the core.autocrlf command to git config. The following settings are recommended:</p>
<p>On macOS and Linux:</p>
<p>`git config --global core.autocrlf input`</p>
<p>And on Windows:</p>
<p>`git config --global core.autocrlf true`</p>
<p>You can read more about this issue on this <a href="https://help.github.com/articles/dealing-with-line-endings/">GitHub page</a>.</p></div></div></div>

For these lessons, we will be interacting with GitHub and so the email address used should be the same as the one used when you set up your GitHub account later . If you are concerned about privacy, please review [GitHub’s instructions for keeping your email address private](https://help.github.com/articles/setting-your-commit-email-address-on-github/). If you elect to use a private email address with GitHub, then use that same email address for the user.email value, e.g. username@users.noreply.github.com replacing username with your GitHub one. You can change the email address later on by using the git config command again.

Dracula also has to set his favorite text editor, following this table:

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

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h4>Exiting Vim</h4>
<p>Note that Vim is the default editor for many programs. If you haven’t used Vim before and wish to exit a session without saving your changes, press `Esc` then type `:q!` and hit Return. If you want to save your changes and quit, press `Esc` then type `:wq` and hit Return.</p></div></div></div>

The four commands we just ran above only need to be run once: the flag --global tells Git to use the settings for every project, in your user account, on this computer.

You can check your settings at any time:


{:.input_area}
```xonsh
git config --list
```

You can change your configuration as many times as you want: just use the same commands to choose another editor or update your email address.

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h4>Proxy</h4>
<p>In some networks you need to use a proxy. If this is the case, you may also need to tell Git about the proxy:</p>
<p>`git config --global http.proxy proxy-url
git config --global https.proxy proxy-url`</p>
<p>To disable the proxy, use</p>
<p>`git config --global --unset http.proxy
git config --global --unset https.proxy`</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h4>Git Help and Manual</h4>
<p>Always remember that if you forget a git command, you can access the list of commands by using -h and access the Git manual by using --help :</p>
<p>`git config -h
git config --help`</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><h4>Key Points</h4>
<ul>
<li>Version control is like an unlimited ‘undo’.</li>
<li>Version control also allows many people to work in parallel.</li>
<li>Use git config with the --global option to configure a user name, email address, editor, and other preferences once per machine.</li>
</ul></div></div></div>
