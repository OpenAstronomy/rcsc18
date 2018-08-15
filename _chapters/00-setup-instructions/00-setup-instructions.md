---
interact_link: 00-setup-instructions/00-setup-instructions.ipynb
title: 'Setup Instructions'
permalink: 'chapters/00-setup-instructions/00-setup-instructions'
previouschapter:
  url: 
  title: 'Setup Instructions'
nextchapter:
  url: 
  title: 'Bash'
redirect_from:
  - 'chapters/00-setup-instructions/00-setup-instructions'
---

# Setting up git

### The Bash Shell

Bash is a commonly-used shell that gives you the power to do simple tasks more quickly.

#### Windows
[Video Tutorial](https://www.youtube.com/watch?v=339AEqk9c-8)
1. Download the Git for Windows [installer](https://git-for-windows.github.io/).
1. Run the installer and follow the steps below:
    - Click on "Next".
    - Click on "Next".
    - **Keep "Use Git from the Windows Command Prompt" selected and click on "Next".** If you forgot to do this programs that you need for the workshop will not work properly. If this happens rerun the installer and select the appropriate option.
    - Click on "Next".
    - **Keep "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".**
    - **Keep "Use Windows' default console window" selected and click on "Next".**
    - Click on "Install".
    - Click on "Finish".
1. If your "HOME" environment variable is not set (or you don't know what this is):
    - Open command prompt (Open Start Menu then type `cmd` and press [Enter])
    - Type the following line into the command prompt window exactly as shown: `setx HOME "%USERPROFILE%"`
    - Press [Enter], you should see `SUCCESS: Specified value was saved.`
    - Quit command prompt by typing `exit` then pressing [Enter]

This will provide you with both Git and Bash in the Git Bash program.

#### macOS

The default shell in all versions of macOS is Bash, so no need to install anything. You access Bash from the Terminal (found in `/Applications/Utilities`). See the Git installation [video tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY) for an example on how to open the Terminal. You may want to keep Terminal in your dock for this workshop.

#### Linux

The default shell is usually Bash, but if your machine is set up differently you can run it by opening a terminal and typing `bash`. There is no need to install anything.

### Git

Git is a version control system that lets you track who made changes to what when and has options for easily updating a shared or public version of your code on [github.com](https://github.com/). You will need a [supported](https://help.github.com/articles/supported-browsers/) web browser (current versions of Chrome, Firefox or Safari, or Internet Explorer version 9 or above).

You will need an account at [github.com](https://github.com/) for parts of the Git lesson. Basic GitHub accounts are free. We encourage you to create a GitHub account if you don't have one already. Please consider what personal information you'd like to reveal. For example, you may want to review [these instructions for keeping your email address private](https://help.github.com/articles/keeping-your-email-address-private/) provided at GitHub.

#### Windows

Git should be installed on your computer as part of your Bash install (described above).

#### macOS
[Video Tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY)

**For OS X 10.9 and higher**, install Git for Mac by downloading and running the most recent "mavericks" installer from this list. After installing Git, there will not be anything in your `/Applications` folder, as Git is a command line program. **For older versions of OS X (10.5-10.8)** use the most recent available installer labelled "snow-leopard" available [here](http://sourceforge.net/projects/git-osx-installer/files/).

#### Linux

If Git is not already available on your machine you can try to install it via your distro's package manager. For Debian/Ubuntu run `sudo apt-get install git` and for Fedora run `sudo dnf install git`.

### Text Editor

When you're writing code, it's nice to have a text editor that is optimized for writing code, with features like automatic color-coding of key words. The default text editor on macOS and Linux is usually set to Vim, which is not famous for being intuitive. If you accidentally find yourself stuck in it, try typing the escape key, followed by `:q!` (colon, lower-case 'q', exclamation mark), then hitting [Enter] to return to the shell.

#### Windows
[Video Tutorial](https://www.youtube.com/watch?v=339AEqk9c-8)

nano is a basic editor and the default that instructors use in the workshop. To install it, download the [Windows installer](https://carpentries.github.io/workshop-template/) and double click on the file to run it. **This installer requires an active internet connection.**

Others editors that you can use are [Notepad++](https://notepad-plus-plus.org/) or [Sublime Text](https://www.sublimetext.com/). **Be aware that you must add its installation directory to your system path.** Please ask your instructor to help you do this.

#### macOS

nano is a basic editor and the default that instructors use in the workshop. See the Git installation [video tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY) for an example on how to open nano. It should be pre-installed.

Others editors that you can use are [Text Wrangler](https://www.barebones.com/products/textwrangler/) or [Sublime Text](https://www.sublimetext.com/).

#### Linux

nano is a basic editor and the default that instructors use in the workshop. It should be pre-installed.

Others editors that you can use are [Gedit](https://wiki.gnome.org/Apps/Gedit), [Kate](https://kate-editor.org/) or [Sublime Text](https://www.sublimetext.com/).

### Python

[Python](https://python.org/) is a popular language for research computing, and great for general-purpose programming as well. Installing all of its research packages individually can be a bit difficult, so we recommend [Anaconda](https://www.anaconda.com/distribution/), an all-in-one installer.

Regardless of how you choose to install it, **please make sure you install Python version 3.x** (e.g., 3.6 is fine).

We will teach Python using the [Jupyter notebook](https://jupyter.org/), a programming environment that runs in a web browser. For this to work you will need a reasonably up-to-date browser. The current versions of the Chrome, Safari and Firefox browsers are all [supported](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#browser-compatibility) (some older browsers, including Internet Explorer version 9 and below, are not).

#### Windows
[Video Tutorial](https://www.youtube.com/watch?v=xxQ0mzZ8UvA)
1. Open https://www.anaconda.com/download/#windows with your web browser.
1. Download the Python 3 installer for Windows.
1. Install Python 3 using all of the defaults for installation except make sure to check **Make Anaconda the default Python**.

#### macOS
[Video Tutorial](https://www.youtube.com/watch?v=TcSAln46u9U)
1. Open https://www.anaconda.com/download/#macos with your web browser.
1. Download the Python 3 installer for OS X.
1. Install Python 3 using all of the defaults for installation.

#### Linux
1. Open https://www.anaconda.com/download/#linux with your web browser.
1. Download the Python 3 installer for Linux. (The installation requires using the shell. If you aren't comfortable doing the installation yourself stop here and request help at the workshop.)
1. Open a terminal window.
1. Type
    `bash Anaconda3-`
    and then press tab. The name of the file you just downloaded should appear. If it does not, navigate to the folder where you downloaded the file, for example with:
    `cd Downloads`
    Then, try again.
1. Press enter. You will follow the text-only prompts. To move through the text, press the space key. Type `yes` and press [Enter] to approve the license. Press [Enter] to approve the default location for the files. Type `yes` and press [Enter] to prepend Anaconda to your `PATH` (this makes the Anaconda distribution the default Python).
1. Close the terminal window.

### Python packages

All the python libraries you will need for the workshop can be installed using Anaconda. Anaconda also provides the capability to install packages in distinct environments, and we will use this capability for the workshop.

#### Creating an environment

Before installing the packages you need, you should first create an environment into which they can be installed. This will act as a grouping of installed packages - using several such environments can allow you to have several instances of the same packages installed without them interfering with each other. This is useful, for example, if different things you are working on require different versions of the same package. 

For now, just create one environment for the workshop. To do this, open a terminal window and type

```
conda create -n stfc-summer-school python=3
```

then press [Enter]. This will create a new environment called stfc-summer-school and install the latest available version of Python 3 into it.

Although this command has created the environment, it isn't currenly active. To activate it, in your terminal type

```
source activate stfc-summer-school
```

and press [Enter]. Remember this command, as you will need to run it every time you open a new terminal if you want to use the packages installed in this environment. Now, to install the python libraries needed for the workshop, type

```
conda install numpy matplotlib jupyter sunpy astropy
```

and press [Enter]. This command may take a moment or two to process, after which you will be shown the packages which will be installed (there will be a lot, as it will include the packages required by those specified in the command above) and asked if you want to proceed. Press [Enter] again and the installation will begin, which may take some time.

[Put some info here on how to test that the installations have worked]
