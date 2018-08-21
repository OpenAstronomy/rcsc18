---
interact_link: 02-git/06-cloning.ipynb
title: 'Cloning'
permalink: 'chapters/02-git/06-cloning'
previouschapter:
  url: chapters/02-git/05-ignoring
  title: 'Ignoring'
nextchapter:
  url: chapters/02-git/06-remotes
  title: 'Remotes'
redirect_from:
  - 'chapters/02-git/06-cloning'
---

## Cloning repositories

So far we've only dealt with git repos which exist entirely locally - you've created a repo, added commits and navigated the history, all on your local machine. These are all important skills, but a powerful aspect of version control is in keeping a remote copy of your files somewhere else. Most commonly, this somewhere else will be a specific hosting service like [GitHub](https://github.com/), but in principle it can be any external computer you have access to or even a different location on your local machine (although this is less likely to be useful).

This allows you both to back up your files in case something happens to your local copy, and to share your code with others, so it's very important that we learn to interact with non-local versions of repositories. We'll be going into detail on a variety of ways to do this in later lessons, but for now the first thing you'll need to know about is **cloning** a repository.

### What is cloning and why do I care?

**Cloning** means creating a new repsository locally which is based on a remote one somewhere else. This is a vital part of collaboration with git because it allows you to make a copy of someonbody else's repo and to work on it locally without affecting that person's copy.

Often this will mean each of you working on seperate parts of a paper or code at the same time (and combining your changes later). Today, you'll be cloning this repository containing all the notebooks we're working from for this summer school. Again, this means you will have your own copy and can freely change any of the files locally without worrying about interfering with the original versions.

### How do I clone a repo?

The syntax for cloning a repo is

```
git clone <location_of_remote_repo>
```

which means we need to know where the repo we're cloning is. This will often be a github.com URL that looks something like `https://github.com/<username>/<repo-name>.git`, where `username` is the name of some GitHub user and `repo-name` is the name of the specific repo you want to clone. (Note the significance of this: repositories hosted on GitHub belong to users, so different users can own different versions and you can choose which one you want to clone.)

Before we run this command, note that it will create a new folder in the current directory for the repo you're cloning, complete with the `.git` and all the history. This means that the rules we've discussed previously about not creating repos within repos still apply, so make sure that you are not inside a git repo when you clone a new one.

So, with that in mind, go to the command line and navigate to the directory in which you want to clone the notebooks repo. You may want to create a directory to keep git repos in, but any non-repo directory will do (e.g. your home directory). If you change your mind you can move the repo later so don't worry about this too much now. Once you've done that, run the clone command:


{:.input_area}
```xonsh
git clone https://github.com/SolarDrew/STFC-summer-school-2018.git # or wherever this ends up being
```

You should see some output while the files copy onto your machine. Once this finishes, you can run `ls` and you should be able to see the new folder. Move into that folder now and run `git log` and you'll see that you have access to the full history of the master branch of the repo.

### Remotes

There is one final thing to note which you don't need to worry about too much now but which will become relevant later. Local repos can have one or more remote versions associated with them. This can be set up manually (more on that later), but the `git clone` command automatically sets the remote repo we've cloned as being associated with our local version. To see this you can use the following command:


{:.input_area}
```xonsh
git remote
```

which should show you

```
origin
```

This means we have one remote which has been named origin (because it's where we got the repo from). you can see more detail on this by using the 'verbose' version of this command:


{:.input_area}
```xonsh
git remote -v
```

For now we don't need to go into why there are two versions of this remote - the main thing to note is that the remote knows the URL it came from. Again, we'll cover ways in which we can use this information in later lessons.
