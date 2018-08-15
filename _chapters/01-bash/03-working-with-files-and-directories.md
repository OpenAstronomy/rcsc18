---
interact_link: 01-bash/03-working-with-files-and-directories.ipynb
title: 'Working With Files And Directories'
permalink: 'chapters/01-bash/03-working-with-files-and-directories'
previouschapter:
  url: chapters/01-bash/02-files-and-directories
  title: 'Files And Directories'
nextchapter:
  url: 
  title: 'Git'
redirect_from:
  - 'chapters/01-bash/03-working-with-files-and-directories'
---

# Working With Files and Directories

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #daee84; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #daee84, #def090); border-color: #daee84; margin-top: 0px; margin-left: -5px;'> &#8263; Overview</h2>
<p>Questions:</p>
<ul>
<li>How can I create, copy, and delete files and directories?</li>
<li>How can I edit files?</li>
</ul>
<p>Objectives:</p>
<ul>
<li>Create a directory hierarchy that matches a given diagram.</li>
<li>Create files in that hierarchy using an editor or by copying and renaming existing files.</li>
<li>Delete specified files and/or directories.</li>
</ul>
<p>Keypoints:</p>
<ul>
<li>`cp old new` copies a file.</li>
<li>`mkdir path` creates a new directory.</li>
<li>`mv old new` moves (renames) a file or directory.</li>
<li>`rm path` removes (deletes) a file.</li>
<li>Use of the Control key may be described in many ways, including `Ctrl-X`, `Control-X`, and `^X`.</li>
<li>The shell does not have a trash bin: once something is deleted, it's really gone.</li>
<li>Depending on the type of work you do, you may need a more powerful text editor than Nano.</li>
</ul></div>

We now know how to explore files and directories,
but how do we create them in the first place?
Let's go back to our `data-shell` directory on the Desktop
and use `ls -F` to see what it contains:


{:.input_area}
```bash
pwd
```

{:.output_stream}
```
/home/stuart/Git/Aperio/stfc/01-bash

```


{:.input_area}
```bash
ls -F
```

{:.output_stream}
```
01-Introduction.ipynb		03-working-with-files-and-directories.ipynb
02-files-and-directories.ipynb

```

Let's create a new directory called `thesis` using the command `mkdir thesis` (which has no output):


{:.input_area}
```bash
mkdir thesis
```

As you might guess from its name, `mkdir` means "make directory". Since `thesis`
is a relative path (i.e., doesn't have a leading slash), the new directory is
created in the current working directory:


{:.input_area}
```bash
ls -F
```

{:.output_stream}
```
01-Introduction.ipynb		03-working-with-files-and-directories.ipynb
02-files-and-directories.ipynb	thesis/

```

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #f4fd9c, #f5fda6); border-color: #f4fd9c; margin-top: 0px; margin-left: -5px;'> &#128204; Two ways of doing the same thing</h2>
<p>Using the shell to create a directory is no different than using a file explorer.
If you open the current directory using your operating system's graphical file explorer,
the `thesis` directory will appear there too.
While they are two different ways of interacting with the files,
the files and directories themselves are the same.</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #f4fd9c, #f5fda6); border-color: #f4fd9c; margin-top: 0px; margin-left: -5px;'> &#128204; Good names for files and directories</h2>
<p>Complicated names of files and directories can make your life painful
when working on the command line. Here we provide a few useful
tips for the names of your files.</p>
<ol>
<li>Don't use whitespaces.</li>
</ol>
<p>Whitespaces can make a name more meaningful
   but since whitespace is used to break arguments on the command line
   it is better to avoid them in names of files and directories.
   You can use `-` or `_` instead of whitespace.</p>
<ol>
<li>Don't begin the name with `-` (dash).</li>
</ol>
<p>Commands treat names starting with `-` as options.</p>
<ol>
<li>Stick with letters, numbers, `.` (period or 'full stop'), `-` (dash) and `_` (underscore).</li>
</ol>
<p>Many other characters have special meanings on the command line.
   We will learn about some of these during this lesson.
   There are special characters that can cause your command to not work as
   expected and can even result in data loss.</p>
<p>If you need to refer to names of files or directories that have whitespace
or another non-alphanumeric character, you should surround the name in quotes (`""`).</p></div>

Since we've just created the `thesis` directory, there's nothing in it yet:


{:.input_area}
```bash
$ ls -F thesis
```

Let's change our working directory to `thesis` using `cd`,
then run a text editor called Nano to create a file called `draft.txt`:


{:.input_area}
```bash
cd thesis
```


{:.input_area}
```bash
nano draft.txt
```

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #f4fd9c, #f5fda6); border-color: #f4fd9c; margin-top: 0px; margin-left: -5px;'> &#128204; Which Editor?</h2>
<p>When we say, "`nano` is a text editor," we really do mean "text": it can
only work with plain character data, not tables, images, or any other
human-friendly media. We use it in examples because it is one of the 
least complex text editors. However, because of this trait, it may 
not be powerful enough or flexible enough for the work you need to do
after this workshop. On Unix systems (such as Linux and Mac OS X),
many programmers use <a href="http://www.gnu.org/software/emacs/">Emacs</a> or
<a href="http://www.vim.org/">Vim</a> (both of which require more time to learn), 
or a graphical editor such as
<a href="http://projects.gnome.org/gedit/">Gedit</a>. On Windows, you may wish to
use <a href="http://notepad-plus-plus.org/">Notepad++</a>.  Windows also has a built-in
editor called `notepad` that can be run from the command line in the same
way as `nano` for the purposes of this lesson.  </p>
<p>No matter what editor you use, you will need to know where it searches
for and saves files. If you start it from the shell, it will (probably)
use your current working directory as its default location. If you use
your computer's start menu, it may want to save files in your desktop or
documents directory instead. You can change this by navigating to
another directory the first time you "Save As..."</p></div>

Let's type in a few lines of text.
Once we're happy with our text, we can press `Ctrl-O` (press the Ctrl or Control key and, while
holding it down, press the O key) to write our data to disk
(we'll be asked what file we want to save this to:
press Return to accept the suggested default of `draft.txt`).
![Nano in Action](../fig/nano-screenshot.png)

Once our file is saved, we can use `Ctrl-X` to quit the editor and
return to the shell.


<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #f4fd9c, #f5fda6); border-color: #f4fd9c; margin-top: 0px; margin-left: -5px;'> &#128204; Control, Ctrl, or ^ Key</h2>
<p>The Control key is also called the "Ctrl" key. There are various ways
in which using the Control key may be described. For example, you may
see an instruction to press the Control key and, while holding it down,
press the X key, described as any of:</p>
<ul>
<li>`Control-X`</li>
<li>`Control+X`</li>
<li>`Ctrl-X`</li>
<li>`Ctrl+X`</li>
<li>`^X`</li>
<li>`C-x`</li>
</ul>
<p>In nano, along the bottom of the screen you'll see `^G Get Help ^O WriteOut`.
This means that you can use `Control-G` to get help and `Control-O` to save your
file.</p></div>

`nano` doesn't leave any output on the screen after it exits,
but `ls` now shows that we have created a file called `draft.txt`:


{:.input_area}
```bash
ls
```

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Creating Files a Different Way</h2>
<p>We have seen how to create text files using the `nano` editor.
Now, try the following command in your home directory:</p>
<p>`$ cd                  # go to your home directory
$ touch my_file.txt`</p>
<ol>
<li>
<p>What did the touch command do?
    When you look at your home directory using the GUI file explorer,
    does the file show up?</p>
</li>
<li>
<p>Use `ls -l` to inspect the files.  How large is `my_file.txt`?</p>
</li>
<li>
<p>When might you want to create a file this way?</p>
</li>
</ol></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<ol>
<li>The touch command generates a new file called 'my_file.txt' in
    your home directory.  If you are in your home directory, you
    can observe this newly generated file by typing 'ls' at the 
    command line prompt.  'my_file.txt' can also be viewed in your
    GUI file explorer.</li>
<li>
<p>When you inspect the file with 'ls -l', note that the size of
    'my_file.txt' is 0kb.  In other words, it contains no data.
    If you open 'my_file.txt' using your text editor it is blank.</p>
</li>
<li>
<p>Some programs do not generate output files themselves, but
    instead require that empty files have already been generated.
    When the program is run, it searches for an existing file to
    populate with its output.  The touch command allows you to
    efficiently generate a blank text file to be used by such
    programs.</p>
</li>
</ol></div>

Returning to the `data-shell` directory,
let's tidy up the `thesis` directory by removing the draft we created:


{:.input_area}
```bash
cd thesis
```


{:.input_area}
```bash
rm draft.txt
```

This command removes files (`rm` is short for "remove"). If we run `ls` again,
its output is empty once more, which tells us that our file is gone:


{:.input_area}
```bash
ls
```

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #f4fd9c, #f5fda6); border-color: #f4fd9c; margin-top: 0px; margin-left: -5px;'> &#128204; Deleting Is Forever</h2>
<p>The Unix shell doesn't have a trash bin that we can recover deleted
files from (though most graphical interfaces to Unix do).  Instead,
when we delete files, they are unhooked from the file system so that
their storage space on disk can be recycled. Tools for finding and
recovering deleted files do exist, but there's no guarantee they'll
work in any particular situation, since the computer may recycle the
file's disk space right away.</p></div>

Let's re-create that file
and then move up one directory to `/Users/nelle/Desktop/data-shell` using `cd ..`:


{:.input_area}
```bash
pwd
```


{:.input_area}
```bash
nano draft.txt
```


{:.input_area}
```bash
ls
```


{:.input_area}
```bash
cd ..
```

If we try to remove the entire `thesis` directory using `rm thesis`,
we get an error message:


{:.input_area}
```bash
rm thesis
```

This happens because `rm` by default only works on files, not directories.

To really get rid of `thesis` we must also delete the file `draft.txt`.
We can do this with the [recursive](https://en.wikipedia.org/wiki/Recursion) option for `rm`:


{:.input_area}
```bash
rm -r thesis
```

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Using `rm` Safely</h2>
<p>What happens when we type `rm -i thesis/quotations.txt`?
Why would we want this protection when using `rm`?</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<p>`$ rm: remove regular file 'thesis/quotations.txt'?`
The -i option will prompt before every removal. 
The Unix shell doesn't have a trash bin, so all the files removed will disappear forever. 
By using the -i flag, we have the chance to check that we are deleting only the files that we want to remove.</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #f4fd9c, #f5fda6); border-color: #f4fd9c; margin-top: 0px; margin-left: -5px;'> &#128204; With Great Power Comes Great Responsibility</h2>
<p>Removing the files in a directory recursively can be a very dangerous
operation. If we're concerned about what we might be deleting we can
add the "interactive" flag `-i` to `rm` which will ask us for confirmation
before each step</p>
<p>`$ rm -r -i thesis
rm: descend into directory ‘thesis’? y
rm: remove regular file ‘thesis/draft.txt’? y
rm: remove directory ‘thesis’? y`</p>
<p>This removes everything in the directory, then the directory itself, asking
at each step for you to confirm the deletion.</p></div>

Let's create that directory and file one more time.
(Note that this time we're running `nano` with the path `thesis/draft.txt`,
rather than going into the `thesis` directory and running `nano` on `draft.txt` there.)


{:.input_area}
```bash
pwd
```


{:.input_area}
```bash
mkdir thesis
```


{:.input_area}
```bash
nano thesis/draft.txt
```


{:.input_area}
```bash
ls thesis
```

`draft.txt` isn't a particularly informative name,
so let's change the file's name using `mv`,
which is short for "move":


{:.input_area}
```bash
mv thesis/draft.txt thesis/quotes.txt
```

The first argument tells `mv` what we're "moving",
while the second is where it's to go.
In this case,
we're moving `thesis/draft.txt` to `thesis/quotes.txt`,
which has the same effect as renaming the file.
Sure enough,
`ls` shows us that `thesis` now contains one file called `quotes.txt`:


{:.input_area}
```bash
ls thesis
```

{: .language-bash}

The effect is to move the file from the directory it was in to the current working directory.
`ls` now shows us that `thesis` is empty:


{:.input_area}
```bash
mv thesis/quotes.txt .
```

One has to be careful when specifying the target file name, since `mv` will
silently overwrite any existing file with the same name, which could
lead to data loss. An additional flag, `mv -i` (or `mv --interactive`),
can be used to make `mv` ask you for confirmation before overwriting.

Just for the sake of consistency,
`mv` also works on directories

Let's move `quotes.txt` into the current working directory.
We use `mv` once again,
but this time we'll just use the name of a directory as the second argument
to tell `mv` that we want to keep the filename,
but put the file somewhere new.
(This is why the command is called "move".)
In this case,
the directory name we use is the special directory name `.` that we mentioned earlier.


{:.input_area}
```bash
ls thesis
```

Further,
`ls` with a filename or directory name as an argument only lists that file or directory.
We can use this to see that `quotes.txt` is still in our current directory:


{:.input_area}
```bash
ls quotes.txt
```

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Moving to the Current Folder</h2>
<p>After running the following commands,
Jamie realizes that she put the files `sucrose.dat` and `maltose.dat` into the wrong folder:</p>
<p>`$ ls -F
 analyzed/ raw/
$ ls -F analyzed
fructose.dat glucose.dat maltose.dat sucrose.dat
$ cd raw/`</p>
<p>Fill in the blanks to move these files to the current folder
(i.e., the one she is currently in):</p>
<p>`$ mv ___/sucrose.dat  ___/maltose.dat ___`</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<p>`$ mv ../analyzed/sucrose.dat ../analyzed/maltose.dat .`</p>
<p>Recall that `..` refers to the parent directory (i.e. one above the current directory)
and that `.` refers to the current directory.</p></div>

The `cp` command works very much like `mv`,
except it copies a file instead of moving it.
We can check that it did the right thing using `ls`
with two paths as arguments --- like most Unix commands,
`ls` can be given multiple paths at once:


{:.input_area}
```bash
cp quotes.txt thesis/quotations.txt
```


{:.input_area}
```bash
ls quotes.txt thesis/quotations.txt
```

To prove that we made a copy,
let's delete the `quotes.txt` file in the current directory
and then run that same `ls` again.


{:.input_area}
```bash
rm quotes.txt
```


{:.input_area}
```bash
ls quotes.txt thesis/quotations.txt
```

This time it tells us that it can't find `quotes.txt` in the current directory,
but it does find the copy in `thesis` that we didn't delete.

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #f4fd9c; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #f4fd9c, #f5fda6); border-color: #f4fd9c; margin-top: 0px; margin-left: -5px;'> &#128204; What's In A Name?</h2>
<p>You may have noticed that all of Nelle's files' names are "something dot
something", and in this part of the lesson, we always used the extension
`.txt`.  This is just a convention: we can call a file `mythesis` or
almost anything else we want. However, most people use two-part names
most of the time to help them (and their programs) tell different kinds
of files apart. The second part of such a name is called the
<strong>filename extension</strong>, and indicates
what type of data the file holds: `.txt` signals a plain text file, `.pdf`
indicates a PDF document, `.cfg` is a configuration file full of parameters
for some program or other, `.png` is a PNG image, and so on.</p>
<p>This is just a convention, albeit an important one. Files contain
bytes: it's up to us and our programs to interpret those bytes
according to the rules for plain text files, PDF documents, configuration
files, images, and so on.</p>
<p>Naming a PNG image of a whale as `whale.mp3` doesn't somehow
magically turn it into a recording of whalesong, though it <em>might</em>
cause the operating system to try to open it with a music player
when someone double-clicks it.</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Renaming Files</h2>
<p>Suppose that you created a `.txt` file in your current directory to contain a list of the
statistical tests you will need to do to analyze your data, and named it: `statstics.txt`
After creating and saving this file you realize you misspelled the filename! You want to
correct the mistake, which of the following commands could you use to do so?</p>
<ol>
<li>`cp statstics.txt statistics.txt`</li>
<li>`mv statstics.txt statistics.txt`</li>
<li>`mv statstics.txt .`</li>
<li>`cp statstics.txt .`</li>
</ol></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<ol>
<li>No.  While this would create a file with the correct name, the incorrectly named file still exists in the directory
and would need to be deleted.</li>
<li>Yes, this would work to rename the file.</li>
<li>No, the period(.) indicates where to move the file, but does not provide a new file name; identical file names
cannot be created.</li>
<li>No, the period(.) indicates where to copy the file, but does not provide a new file name; identical file names
cannot be created.</li>
</ol></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Moving and Copying</h2>
<p>What is the output of the closing `ls` command in the sequence shown below?</p>
<p>`$ pwd`</p>
<p>`/Users/jamie/data`</p>
<p>`$ ls`</p>
<p>`proteins.dat`</p>
<p>`$ mkdir recombine
$ mv proteins.dat recombine/
$ cp recombine/proteins.dat ../proteins-saved.dat
$ ls`</p>
<ol>
<li>`proteins-saved.dat recombine`</li>
<li>`recombine`</li>
<li>`proteins.dat recombine`</li>
<li>`proteins-saved.dat`</li>
</ol></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<p>We start in the `/Users/jamie/data` directory, and create a new folder called `recombine`.
The second line moves (`mv`) the file `proteins.dat` to the new folder (`recombine`).
The third line makes a copy of the file we just moved.  The tricky part here is where the file was
copied to.  Recall that `..` means "go up a level", so the copied file is now in `/Users/jamie`.
Notice that `..` is interpreted with respect to the current working
directory, <strong>not</strong> with respect to the location of the file being copied.
So, the only thing that will show using ls (in `/Users/jamie/data`) is the recombine folder.</p>
<ol>
<li>No, see explanation above.  `proteins-saved.dat` is located at `/Users/jamie`</li>
<li>Yes</li>
<li>No, see explanation above.  `proteins.dat` is located at `/Users/jamie/data/recombine`</li>
<li>No, see explanation above.  `proteins-saved.dat` is located at `/Users/jamie`</li>
</ol></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Organizing Directories and Files</h2>
<p>Jamie is working on a project and she sees that her files aren't very well
organized:</p>
<p>`$ ls -F`</p>
<p>`analyzed/  fructose.dat    raw/   sucrose.dat`</p>
<p>The `fructose.dat` and `sucrose.dat` files contain output from her data
analysis. What command(s) covered in this lesson does she need to run so that the commands below will
produce the output shown?</p>
<p>`$ ls -F`</p>
<p>`analyzed/   raw/`</p>
<p>`$ ls analyzed`</p>
<p>`fructose.dat    sucrose.dat`</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<p>`mv *.dat analyzed`</p>
<p>Jamie needs to move her files `fructose.dat` and `sucrose.dat` to the `analyzed` directory.
The shell will expand *.dat to match all .dat files in the current directory.
The `mv` command then moves the list of .dat files to the "analyzed" directory.</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Copy with Multiple Filenames</h2>
<p>For this exercise, you can test the commands in the `data-shell/data` directory.</p>
<p>In the example below, what does `cp` do when given several filenames and a directory name?</p>
<p>`$ mkdir backup
$ cp amino-acids.txt animals.txt backup/`</p>
<p>In the example below, what does `cp` do when given three or more file names?</p>
<p>`$ ls -F`</p>
<p>`amino-acids.txt  animals.txt  backup/  elements/  morse.txt  pdb/  planets.txt  salmon.txt  sunspot.txt`</p>
<p>`$ cp amino-acids.txt animals.txt morse.txt`</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<p>If given more than one file name followed by a directory name (i.e. the destination directory must 
be the last argument), `cp` copies the files to the named directory.</p>
<p>If given three file names, `cp` throws an error because it is expecting a directory
name as the last argument.</p>
<p>`cp: target ‘morse.txt’ is not a directory`</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Copy a folder structure but not the files</h2>
<p>You're starting a new experiment, and would like to duplicate the file
structure from your previous experiment without the data files so you can
add new data.</p>
<p>Assume that the file structure is in a folder called '2016-05-18-data',
which contains a `data` folder that in turn contains folders named `raw` and
`processed` that contain data files.  The goal is to copy the file structure
of the `2016-05-18-data` folder into a folder called `2016-05-20-data` and
remove the data files from the directory you just created.</p>
<p>Which of the following set of commands would achieve this objective?
What would the other commands do?</p>
<p>`$ cp -r 2016-05-18-data/ 2016-05-20-data/
$ rm 2016-05-20-data/raw/*
$ rm 2016-05-20-data/processed/*`</p>
<p>`$ rm 2016-05-20-data/raw/*
$ rm 2016-05-20-data/processed/*
$ cp -r 2016-05-18-data/ 2016-5-20-data/`</p>
<p>`$ cp -r 2016-05-18-data/ 2016-05-20-data/
$ rm -r -i 2016-05-20-data/`</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2>
<p>The first set of commands achieves this objective.
First we have a recursive copy of a data folder.
Then two `rm` commands which remove all files in the specified directories.
The shell expands the '*' wild card to match all files and subdirectories.</p>
<p>The second set of commands have the wrong order: 
attempting to delete files which haven't yet been copied,
followed by the recursive copy command which would copy them.</p>
<p>The third set of commands would achieve the objective, but in a time-consuming way:
the first command copies the directory recursively, but the second command deletes
interactively, prompting for confirmation for each file and directory.</p></div>
