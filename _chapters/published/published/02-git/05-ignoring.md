---
interact_link: notebooks/published/published/02-git/05-ignoring.ipynb
title: 'Ignoring'
permalink: 'chapters/published/published/02-git/05-ignoring'
previouschapter:
  url: chapters/published/published/02-git/04-exploring-history
  title: 'Exploring History'
nextchapter:
  url: chapters/published/published/02-git/06-remotes
  title: 'Remotes'
redirect_from:
  - 'chapters/published/published/02-git/05-ignoring'
---

## Ignoring Things

What if we have files that we do not want Git to track for us, like backup files created by our editor or intermediate files created during data analysis? Let’s create a few dummy files:


{:.input_area}
```xonsh
mkdir results
touch a.dat b.dat c.dat results/a.out results/b.out
```

and see what Git says:


{:.input_area}
```xonsh
git status
```

Putting these files under version control would be a waste of disk space. What’s worse, having them all listed could distract us from changes that actually matter, so let’s tell Git to ignore them.

We do this by creating a file in the root directory of our project called .gitignore:


{:.input_area}
```xonsh
nano .gitignore
cat .gitignore
```

These patterns tell Git to ignore any file whose name ends in .dat and everything in the results directory. (If any of these files were already being tracked, Git would continue to track them.)

Once we have created this file, the output of git status is much cleaner:


{:.input_area}
```xonsh
git status
```

The only thing Git notices now is the newly-created .gitignore file. You might think we wouldn’t want to track it, but everyone we’re sharing our repository with will probably want to ignore the same things that we’re ignoring. Let’s add and commit .gitignore:


{:.input_area}
```xonsh
git add .gitignore
git commit -m "Ignore data files and the results folder."
git status
```

As a bonus, using .gitignore helps us avoid accidentally adding to the repository files that we don’t want to track:


{:.input_area}
```xonsh
git add a.dat
```

If we really want to override our ignore settings, we can use git add -f to force Git to add something. For example, git add -f a.dat. We can also always see the status of ignored files if we want:


{:.input_area}
```xonsh
git status --ignored
```

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h3>Ignoring Nested Files</h3>
<p>Given a directory structure that looks like:</p>
<p>`results/data
results/plots`</p>
<p>How would you ignore only results/plots and not results/data?</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h4>Solution</h4>
<p>As with most programming issues, there are a few ways that you could solve this. If you only want to ignore the contents of results/plots, you can change your .gitignore to ignore only the /plots/ subfolder by adding the following line to your .gitignore:</p>
<p>`results/plots/`</p>
<p>If, instead, you want to ignore everything in /results/, but wanted to track results/data, then you can add results/ to your .gitignore and create an exception for the results/data/ folder. The next challenge will cover this type of solution.</p>
<p>Sometimes the <strong> pattern comes in handy, too, which matches multiple directory levels. E.g. </strong>/results/plots/* would make git ignore the results/plots directory in any root directory.</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h3>Including Specific Files</h3>
<p>How would you ignore all .data files in your root directory except for final.data? Hint: Find out what ! (the exclamation point operator) does</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h4>Solution</h4>
<p>You would add the following two lines to your .gitignore:</p>
<p>`*.data           # ignore all data files
!final.data      # except final.data`</p>
<p>The exclamation point operator will include a previously excluded entry.</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h3>Ignoring all data Files in a Directory</h3>
<p>Given a directory structure that looks like:</p>
<p>`results/data/position/gps/a.data
results/data/position/gps/b.data
results/data/position/gps/c.data
results/data/position/gps/info.txt
results/plots`</p>
<p>What’s the shortest .gitignore rule you could write to ignore all .data files in result/data/position/gps? Do not ignore the info.txt.</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h4>Solution</h4>
<p>Appending results/data/position/gps/*.data will match every file in results/data/position/gps that ends with .data. The file results/data/position/gps/info.txt will not be ignored.</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h3>The Order of Rules</h3>
<p>Given a .gitignore file with the following contents:</p>
<p>`*.data
!*.data`</p>
<p>What will be the result?</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h4>Solution</h4>
<p>The ! modifier will negate an entry from a previously defined ignore pattern. Because the !*.data entry negates all of the previous .data files in the .gitignore, none of them will be ignored, and all .data files will be tracked.</p></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h3>Log Files</h3>
<p>You wrote a script that creates many intermediate log-files of the form log_01, log_02, log_03, etc. You want to keep them but you do not want to track them through git.</p>
<ol>
<li>Write one .gitignore entry that excludes files of the form log_01, log_02, etc.</li>
<li>Test your “ignore pattern” by creating some dummy files of the form log_01, etc.</li>
<li>
<p>You find that the file log_01 is very important after all, add it to the tracked files without changing the .gitignore again.</p>
</li>
<li>
<p>Discuss with your neighbor what other types of files could reside in your directory that you do not want to track and thus would exclude via .gitignore.</p>
</li>
</ol></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h3>Solution</h3>
<ol>
<li>append either log_<em> or log</em> as a new entry in your .gitignore</li>
<li>track log_01 using git add -f log_01</li>
</ol></div></div></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><p>Key Points</p>
<ul>
<li>The .gitignore file tells Git what files to ignore.</li>
</ul></div></div></div>
