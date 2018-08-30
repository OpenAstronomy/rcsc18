---
interact_link: 04-further-python/01-scripts_instructor.ipynb
title: 'Scripts'
permalink: 'chapters/04-further-python/01-scripts'
previouschapter:
  url: 
  title: 'Further Python'
nextchapter:
  url: chapters/04-further-python/02-modules
  title: 'Modules'
redirect_from:
  - 'chapters/04-further-python/01-scripts'
---

# Working with scripts

So far this week we've been running all our Python commands in the notebook, which is a kind of combination between a command-line Python interpreter and a text editor. This works well as a teaching environment (and also for writing up things like blogs or code demonstrations, since you can combine plain text with code and its output), but it's actually not commonly used for day-to-day programming work. More commonly, you will want to create dedicated Python files. (These files are often called 'scripts', or 'codes' - we will be using all of these terms interchangeably.) Some text editors like Spyder include a Python interpreter which allows you to run your Python files inside the editor itself, as we have been with the Jupyter notebooks. However, you may not always have this option and will need to learn how to work with Python scripts through the command line.

For this lesson we will be working in a text editor. For this we recommend you use the one you were using yesterday with bash and git, but if you already have another editor you prefer to use for writing Python files, feel free to use that instead. Open your text editor now and open a new file. Call it something like `rcsc18-data-analysis.py` (descriptive filenames are usually a good idea). Here, the `.py` file extension indicates that this is a Python file - you should always include this in the names of your Python scripts.

In this file, let's recreate some of the work we did in the last lesson, analysing data and detecting problems. Here's some of the code we wrote:


{:.input_area}
```python
import glob
import numpy as np
import matplotlib.pyplot as plt

def analyse(filename):
    """
    Reads data from the specified file and plots the average, maximum and minimum along the first axis of the data.
    
    Parameters
    ----------
    filename : str
        Name or path to a file containing data to be plotted. Data should be 2-dimensional and values should be
        separated by commas.
    
    Examples
    --------
    >>> analyse('/path/to/mydata.dat')
    """

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()


def detect_problems(filename):
    """
    Tests data stored in the specified file for spurious or unexpected values.
    
    Parameters
    ----------
    filename : str
        Name or path to a file containing data to tested. Data should be 2-dimensional and values should be
        separated by commas.
        
    Examples
    --------
    >>> analyse('/path/to/mydata.dat')
    """
    data = numpy.loadtxt(fname=filename, delimiter=',')

    if np.max(data, axis=0)[0] == 0 and np.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif np.sum(np.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')


filenames = sorted(glob.glob('inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analyse(f)
    detect_problems(f)

```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Copying code</h2>
</div>


<div class="panel-body">

<p>From time to time, you will end up being in a situation where you want to use code from somewhere else, perhaps from another script you've written, from some code like the above that you are being given, or from an online forum. When you do this we recommend that you copy and paste the code rather than retyping it all out yourself. This is often much faster, of course, but just as importantly it reduces the chance of mistyping something and introducing errors into the code (assuming it was correct to start with, of course). If you're working in a command-line editor you may find that the keyboard shortcut for pasting text is not the one you're used to, but if you can't find the appropriate keys, right-clicking the mouse and selecting 'Paste' should still work.</p>
<p><strong>ALWAYS</strong> check carefully that you have permission to use whatever code you're copying before doing so. This will depend on where you're getting the code from, what you intend to use it for and what license it's published under, if any (more on licenses in a later lesson).</p>

</div>

</section>


Copy the above into your new file and save it. Now, go to the command line (if you are editing your Python file in vim, nano or another command-line editor, either close it or open a new terminal and navigate to where your file is saved). We saw earlier that you can access the Python interpreter in the terminal with the `python` command, but this command can also take a filename as an argument, like this:

```bash
python rcsc18-data-analysis.py
```

Used like this, Python will read the contents of the file and start running the commands it contains from the top, until it gets to the bottom of the file or encounters an error. Run the command above now. You should get all the same output produced by that code when you ran it in the notebook, but now this output appears in the terminal instead.

There are a number of advantages to running code from a script rather than in the notebook. First, with this approach we can now use all the tricks we learned in the [bash session](link to the bash session) - we can pass flags to the `python` command to change its behaviour, we can capture the output and pipe it to another command or a file, and so on. Also, if you find that you have to do some work on a remote server to which you only have command-line access (not an uncommon occurrence), you will have to be comfortable using Python in the terminal, since graphical interfaces like the notebook will not be available. Finally, and perhaps most importantly for the purposes of this summer school, plain-text formats such as `.py` files are much easier to track with git than notebooks are (because notebooks contain a lot of additional formatting as well as the text itself).
