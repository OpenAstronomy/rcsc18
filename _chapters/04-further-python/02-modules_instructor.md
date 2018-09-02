---
interact_link: 04-further-python/02-modules_instructor.ipynb
title: 'Modules'
permalink: 'chapters/04-further-python/02-modules'
previouschapter:
  url: chapters/04-further-python/01-scripts
  title: 'Scripts'
nextchapter:
  url: chapters/04-further-python/03-imports-and-namespaces
  title: 'Imports and Namespaces'
redirect_from:
  - 'chapters/04-further-python/02-modules'
---

# Modules and Modularity

## Modularity in larger code projects

We've already discussed the concept of modularity in programming - the idea that code should be divided into manageable blocks, each of which should ideally perform a single, self-contained task. So far we've applied this concept to group parts of our code into functions, but when we wrote a script in the last lesson, we still kept these functions in the same script as the code that was calling them. This is often completely fine, particularly for small projects - in our case we only had two functions, plus a few lines of other code. But as you try to do more and more with your code, you may quickly find that you end up with dozens of functions, which may perform very different tasks and some of which will likely call others. This situation can be very difficult to manange, especially when you encounter bugs, since following the flow of the code becomes harder the more code you have.

We also need to consider how much of our code we will want to re-use later. A very domain-specific function which performs some particular analysis may only be useful for one project, in which case it's perfectly reasonable to define it in the same script as the code that calls it. But many functions are (and should be) much more general than this. A function to calculate the mean of an array, for example, is universal and could be used in any project, so you wouldn't want to have to define one every time you needed it. Of course, we've seen already that such a function exists in NumPy, and this demonstrates how Python allows us to make our codes more modular - by importing code from external scripts.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Python and modularity</h2>
</div>


<div class="panel-body">

<p>Like most of the content of this summer school, modularity is a concept which can, and should, be applied to your work no matter what programming language you're using. But one of the reasons this school uses Python - and why it's such a popular choice of language generally - is that the concept of modularity is built into Python at a fundamental level, as we'll explore in this lesson. The core Python language on its own actually doesn't really do very much at all, but being able to import functionality from elsewhere makes it extremely powerful, since it allows you to draw from a large standard library and a vast extended ecosystem of third-party libraries, without forcing you to install anything you don't need.</p>

</div>

</section>


## Imports and modules

As noted above, we've already seen some cases of importing in action - for example:


{:.input_area}
```python
import numpy as np
```

\- but we haven't really discussed in detail what is actually happening here. In short, Python's `import` statement allows you to fetch the contents of another Python script. So in your script (or in the notebook), when you run the command above, Python goes and finds the file it associates with the name `numpy`, runs that file and creates a variable `np` in your code which contains the variables and functions defined in that file.

For installed packages like `numpy`, there the installation process places the scripts needed for each package in a folder somewhere on your computer and tells Python where it can access them. But it also works on a smaller scale - the `import` statement can also import any arbitrary script from within the same folder, by specifying the name of that file without the `.py` extension.

To demonstrate how this can be useful for you in your research, let's go back to the script we wrote in the last lesson, `rcsc18-data-analysis.py`. Copy the functions defined in that file and put them into a new file called `analysis_tools.py`. Also copy the import statements for NumPy and matplotlib, as the functions require these to run correctly. Then save and close the new file. Make sure both files are located in this folder.

Now that we have a separate file which defines the functions for our analysis, we can import that just like the installed libraries we've used before:


{:.input_area}
```python
import analysis_tools
```

And we can interact with the functions we've defined there:


{:.input_area}
```python
help(analysis_tools.detect_problems)
```

{:.output_stream}
```
Help on function detect_problems in module analysis_tools:

detect_problems(filename)
    Tests data stored in the specified file for spurious or unexpected values.
    
    Parameters
    ----------
    filename : str
        Name or path to a file containing data to tested. Data should be 2-dimensional and values
        should be separated by commas.
    
    Examples
    --------
    >>> detect_problems('/path/to/mydata.csv')


```


{:.input_area}
```python
analysis_tools.analyse('somedata.dat')
analysis_tools.detect_problems('somedata.dat')
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
OSError                                   Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-4-12a96289d2f8> in <module>()
----> 1 analysis_tools.analyse('somedata.dat')
      2 analysis_tools.detect_problems('somedata.dat')

```

{:.output_traceback_line}
```
~/Git/Aperio/stfc_website/notebooks/04-further-python/analysis_tools.py in analyse(filename)
     19     """
     20 
---> 21     data = np.loadtxt(fname=filename, delimiter=',')
     22 
     23     fig = plt.figure(figsize=(10.0, 3.0))

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/numpy/lib/npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin, encoding)
    924             fname = str(fname)
    925         if _is_string_like(fname):
--> 926             fh = np.lib._datasource.open(fname, 'rt', encoding=encoding)
    927             fencoding = getattr(fh, 'encoding', 'latin1')
    928             fh = iter(fh)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/numpy/lib/_datasource.py in open(path, mode, destpath, encoding, newline)
    260 
    261     ds = DataSource(destpath)
--> 262     return ds.open(path, mode, encoding=encoding, newline=newline)
    263 
    264 

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/numpy/lib/_datasource.py in open(self, path, mode, encoding, newline)
    616                                       encoding=encoding, newline=newline)
    617         else:
--> 618             raise IOError("%s not found." % path)
    619 
    620 

```

{:.output_traceback_line}
```
OSError: somedata.dat not found.
```


So we can see this setup works in the notebook, but it's supposed to help us with our analysis script, so let's go back to that. Open your script, `rcsc18-data-analysis.py` and delete the functions defined there if you haven't already - you won't need them here since they're being defined elsewhere and imported. Then, add `import analysis_tools` to the top of the script with the other import statements (you can also remove the imports for packages used in the functions, since these are no longer required in this script). Finally, you will need to change your function calls so that they use the functions from the imported file, like we've done above - otherwise your script will not be able to find these functions. After these changes, your analysis script should look like this:


{:.input_area}
```python
!cat rcsc18-data-analysis.py
```

{:.output_stream}
```
import glob

import analysis_tools


filenames = sorted(glob.glob('inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analysis_tools.analyse(f)
    analysis_tools.detect_problems(f)

```

Now if you run this script in the command line with `python rcsc18-data-analysis.py`, it should behave exactly as it did when you ran it in the last lesson. We haven't changed any of the code, only rearranged it, in the same way as when we moved parts of the code into functions earlier.
