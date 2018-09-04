---
interact_link: 03-fundamentals-of-python/06-functions_instructor.ipynb
title: 'Functions'
permalink: 'chapters/03-fundamentals-of-python/06-functions'
previouschapter:
  url: chapters/03-fundamentals-of-python/05-making-choices
  title: 'Making Choices'
nextchapter:
  url: chapters/03-fundamentals-of-python/07-comments-and-docs
  title: 'Comments and Docs'
redirect_from:
  - 'chapters/03-fundamentals-of-python/06-functions'
---

# Working with functions


<section class="objectives panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-certificate"></span> Learning Objectives:</h2>
</div>


<div class="panel-body">

<ul>
<li>Define a function that takes parameters.</li>
<li>Return a value from a function.</li>
<li>Test and debug a function.</li>
<li>Set default values for function parameters.</li>
<li>Explain why we should divide programs into small, single-purpose
  functions.</li>
</ul>

</div>

</section>


At this point, we've written code to draw some interesting features in our inflammation data, loop over all our data files to quickly draw these plots for each of them, and have Python make decisions based on what it sees in our data. But, our code is getting pretty long and complicated; what if we had thousands of datasets, and didn't want to generate a  figure for every single one? Commenting out the figure-drawing code is a nuisance. Also, what if we want to use that code again, on a different dataset or at a different point in our program? Cutting and pasting it is going to make our code get very long and very repetitive, very quickly. We'd like a way to package our code so that it is easier to reuse, and Python provides for this by letting us define things called 'functions' - a shorthand way of re-executing longer pieces of code.

Let's start by defining a function `kelvin_to_celsius` that converts temperatures from Kelvin to Celsius:


{:.input_area}
```python
def kelvin_to_celsius(temp):
    return temp - 273.15
```

The function definition opens with the word `def`, which is followed by the name of the function and a parenthesised list of parameter names. The body of the function - the statements that are executed when it runs - is indented below the definition line, typically by four spaces.

When we call the function, the values we pass to it are assigned to those variables so that we can use them inside the function. Inside the function, we use a **return statement** to send a result back to whoever asked for it.

Let's try running our function. Calling our own function is no different from calling any other function:


{:.input_area}
```python
print('absolute zero in Celsius:', kelvin_to_celsius(0.0))
```

{:.output_stream}
```
absolute zero in Celsius: -273.15

```

We've successfully called the function that we defined, and we have access to the value that we returned.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Integer division</h2>
</div>


<div class="panel-body">

<p>We are using Python 3 division, which always returns a floating point number:</p>
<div class="codehilite"><pre><span></span><span class="k">print</span><span class="p">(</span><span class="mi">5</span><span class="o">/</span><span class="mi">9</span><span class="p">)</span>
</pre></div>


<p>Unfortunately, this wasn't the case in Python 2:</p>
<div class="codehilite"><pre><span></span><span class="err">!</span><span class="n">python2</span> <span class="o">-</span><span class="n">c</span> <span class="s2">&quot;print 5/9&quot;</span>
</pre></div>


<p>If you are using Python 2 and want to keep the fractional part of division you need to convert one or the other number to floating point:</p>
<div class="codehilite"><pre><span></span><span class="nb">float</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span> <span class="o">/</span> <span class="mi">9</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="mi">5</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="mi">9</span><span class="p">)</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="mf">5.0</span> <span class="o">/</span> <span class="mi">9</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="mi">5</span> <span class="o">/</span> <span class="mf">9.0</span>
</pre></div>


<p>And if you want an integer result from division in Python 3, use a double-slash:</p>
<div class="codehilite"><pre><span></span><span class="mi">4</span> <span class="o">//</span> <span class="mi">2</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="mi">3</span> <span class="o">//</span> <span class="mi">2</span>
</pre></div>

</div>

</section>


## Composing Functions

Now that we've seen how to turn Kelvin into Celsius, let's try converting Celsius to Fahrenheit:


{:.input_area}
```python
def celsius_to_fahr(temp):
    return temp * (9/5) + 32

print('freezing point of water:', celsius_to_fahr(0))
print('boiling point of water:', celsius_to_fahr(100))
```

{:.output_stream}
```
freezing point of water: 32.0
boiling point of water: 212.0

```

What about converting Kelvin to Fahrenheit? We could write out the formula, but we don't need to. Instead, we can compose the two functions we have already created:


{:.input_area}
```python
def kelvin_to_fahr(temp):
    temp_c = kelvin_to_celsius(temp)
    result = celsius_to_fahr(temp_c)
    return result

print('freezing point of water in Fahrenheit:', kelvin_to_fahr(273.15))
print('absolute zero in Fahrenheit:', kelvin_to_fahr(0))
```

{:.output_stream}
```
freezing point of water in Fahrenheit: 32.0
absolute zero in Fahrenheit: -459.66999999999996

```

This is our first taste of how larger programs are built: we define basic operations, then combine them in ever-larger chunks to get the effect we want. Real-life functions will usually be larger than the ones shown here - typically half a dozen to a few dozen lines - but they shouldn't ever be much longer than that, or the next person who reads it won't be able to understand what's going on.

## Tidying up

Now that we know how to wrap bits of code up in functions, we can make our inflammation analyasis easier to read and easier to reuse. First, let's make an `analyse` function that generates our plots:


{:.input_area}
```python
def analyse(filename):

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()
    plt.show(fig)
```

and another function called `detect_problems` that checks for those systematics we noticed:


{:.input_area}
```python
def detect_problems(filename):

    data = np.loadtxt(fname=filename, delimiter=',')

    if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif data.min(axis=0).sum() == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
```

Notice that rather than jumbling this code together in one giant `for` loop, we can now read and reuse both ideas separately. We can reproduce the previous analysis with a much simpler `for` loop:


{:.input_area}
```python
import glob
# First redefine our list of filenames from the last lesson
filenames = sorted(glob.glob('data/inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analyse(f)
    detect_problems(f)
```

By giving our functions human-readable names, we can more easily read and understand what is happening in the `for` loop. Even better, if at some later date we want to use either of those pieces of code again, we can do so in a single line.

## Defining Defaults

We have passed parameters to functions in two ways: directly, as in `type(data)`, and by name, as in `np.loadtxt(fname='something.csv', delimiter=',')`. In fact, we can pass the filename to `loadtxt` without the `fname=`:


{:.input_area}
```python
import numpy as np

np.loadtxt('data/inflammation-01.csv', delimiter=',')
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
<ipython-input-8-9470a9548300> in <module>()
      1 import numpy as np
      2 
----> 3 np.loadtxt('data/inflammation-01.csv', delimiter=',')

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
OSError: data/inflammation-01.csv not found.
```


but we still need to say `delimiter=`:


{:.input_area}
```python
np.loadtxt('data/inflammation-01.csv', ',')
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
<ipython-input-9-6f078e8cd017> in <module>()
----> 1 np.loadtxt('data/inflammation-01.csv', ',')

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
OSError: data/inflammation-01.csv not found.
```


To understand what's going on, and make our own functions easier to use, let's re-define our center function like this:


{:.input_area}
```python
def centre(data, desired=0.0):
    '''Return a new array containing the original data centered around the desired value (0 by default).
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - data.mean()) + desired
```

The key change is that the second parameter is now written `desired=0.0` instead of just `desired`. If we call the function with two arguments, it works as it did before:


{:.input_area}
```python
test_data = np.zeros((2, 2))
print(centre(test_data, 3))
```

{:.output_stream}
```
[[3. 3.]
 [3. 3.]]

```

But we can also now call it with just one parameter, in which case `desired` is automatically assigned the default value of 0.0:


{:.input_area}
```python
more_data = 5 + np.zeros((2, 2))
print('data before centering:')
print(more_data)
print('centered data:')
print(centre(more_data))
```

{:.output_stream}
```
data before centering:
[[5. 5.]
 [5. 5.]]
centered data:
[[0. 0.]
 [0. 0.]]

```

This is handy: if we usually want a function to work one way, but occasionally need it to do something else, we can allow people to pass a parameter when they need to but provide a default to make the normal case easier. The example below shows how Python matches values to parameters:


{:.input_area}
```python
def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('no parameters:')
display()
print('one parameter:')
display(55)
print('two parameters:')
display(55, 66)
```

{:.output_stream}
```
no parameters:
a: 1 b: 2 c: 3
one parameter:
a: 55 b: 2 c: 3
two parameters:
a: 55 b: 66 c: 3

```

As this example shows, parameters are matched up from left to right, and any that haven't been given a value explicitly get their default value. We can override this behavior by naming the value as we pass it in:


{:.input_area}
```python
print('only setting the value of c')
display(c=77)
```

{:.output_stream}
```
only setting the value of c
a: 1 b: 2 c: 77

```

With that in hand, let's look at the help for numpy.loadtxt:


{:.input_area}
```python
help(np.loadtxt)
```

{:.output_stream}
```
Help on function loadtxt in module numpy.lib.npyio:

loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes')
    Load data from a text file.
    
    Each row in the text file must have the same number of values.
    
    Parameters
    ----------
    fname : file, str, or pathlib.Path
        File, filename, or generator to read.  If the filename extension is
        ``.gz`` or ``.bz2``, the file is first decompressed. Note that
        generators should return byte strings for Python 3k.
    dtype : data-type, optional
        Data-type of the resulting array; default: float.  If this is a
        structured data-type, the resulting array will be 1-dimensional, and
        each row will be interpreted as an element of the array.  In this
        case, the number of columns used must match the number of fields in
        the data-type.
    comments : str or sequence of str, optional
        The characters or list of characters used to indicate the start of a
        comment. None implies no comments. For backwards compatibility, byte
        strings will be decoded as 'latin1'. The default is '#'.
    delimiter : str, optional
        The string used to separate values. For backwards compatibility, byte
        strings will be decoded as 'latin1'. The default is whitespace.
    converters : dict, optional
        A dictionary mapping column number to a function that will parse the
        column string into the desired value.  E.g., if column 0 is a date
        string: ``converters = {0: datestr2num}``.  Converters can also be
        used to provide a default value for missing data (but see also
        `genfromtxt`): ``converters = {3: lambda s: float(s.strip() or 0)}``.
        Default: None.
    skiprows : int, optional
        Skip the first `skiprows` lines; default: 0.
    usecols : int or sequence, optional
        Which columns to read, with 0 being the first. For example,
        ``usecols = (1,4,5)`` will extract the 2nd, 5th and 6th columns.
        The default, None, results in all columns being read.
    
        .. versionchanged:: 1.11.0
            When a single column has to be read it is possible to use
            an integer instead of a tuple. E.g ``usecols = 3`` reads the
            fourth column the same way as ``usecols = (3,)`` would.
    unpack : bool, optional
        If True, the returned array is transposed, so that arguments may be
        unpacked using ``x, y, z = loadtxt(...)``.  When used with a structured
        data-type, arrays are returned for each field.  Default is False.
    ndmin : int, optional
        The returned array will have at least `ndmin` dimensions.
        Otherwise mono-dimensional axes will be squeezed.
        Legal values: 0 (default), 1 or 2.
    
        .. versionadded:: 1.6.0
    encoding : str, optional
        Encoding used to decode the inputfile. Does not apply to input streams.
        The special value 'bytes' enables backward compatibility workarounds
        that ensures you receive byte arrays as results if possible and passes
        'latin1' encoded strings to converters. Override this value to receive
        unicode arrays and pass strings as input to converters.  If set to None
        the system default is used. The default value is 'bytes'.
    
        .. versionadded:: 1.14.0
    
    Returns
    -------
    out : ndarray
        Data read from the text file.
    
    See Also
    --------
    load, fromstring, fromregex
    genfromtxt : Load data with missing values handled as specified.
    scipy.io.loadmat : reads MATLAB data files
    
    Notes
    -----
    This function aims to be a fast reader for simply formatted files.  The
    `genfromtxt` function provides more sophisticated handling of, e.g.,
    lines with missing values.
    
    .. versionadded:: 1.10.0
    
    The strings produced by the Python float.hex method can be used as
    input for floats.
    
    Examples
    --------
    >>> from io import StringIO   # StringIO behaves like a file object
    >>> c = StringIO(u"0 1\n2 3")
    >>> np.loadtxt(c)
    array([[ 0.,  1.],
           [ 2.,  3.]])
    
    >>> d = StringIO(u"M 21 72\nF 35 58")
    >>> np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),
    ...                      'formats': ('S1', 'i4', 'f4')})
    array([('M', 21, 72.0), ('F', 35, 58.0)],
          dtype=[('gender', '|S1'), ('age', '<i4'), ('weight', '<f4')])
    
    >>> c = StringIO(u"1,0,2\n3,0,4")
    >>> x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
    >>> x
    array([ 1.,  3.])
    >>> y
    array([ 2.,  4.])


```

There's a lot of information here, but the most important part is the first couple of lines:

```python
loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None,
          unpack=False, ndmin=0)
```

This tells us that loadtxt has one parameter called fname that doesn't have a default value, and eight others that do. If we call the function like this:


{:.input_area}
```python
np.loadtxt('data/inflammation-01.csv', ',')
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
<ipython-input-16-6f078e8cd017> in <module>()
----> 1 np.loadtxt('data/inflammation-01.csv', ',')

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
OSError: data/inflammation-01.csv not found.
```


then the filename is assigned to `fname` (which is what we want), but the delimiter string `','` is assigned to `dtype` rather than `delimiter`, because `dtype` is the second parameter in the list. However ',' isn't a known `dtype` so our code produced an error message when we tried to run it. When we call `loadtxt` we don't have to provide `fname=` for the filename because it's the first item in the list, but if we want the ',' to be assigned to the variable `delimiter`, we *do* have to provide `delimiter=` for the second parameter since `delimiter` is not the second parameter in the list.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Combining strings</h2>
</div>


<div class="panel-body">

<p>"Adding" two strings produces their concatenation: <code>'a'</code> + <code>'b'</code> is <code>'ab'</code>. Write a function called <code>fence</code> that takes two parameters called <code>original</code> and <code>wrapper</code> and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:</p>
<div class="codehilite"><pre><span></span><span class="k">print</span><span class="p">(</span><span class="n">fence</span><span class="p">(</span><span class="s1">&#39;name&#39;</span><span class="p">,</span> <span class="s1">&#39;*&#39;</span><span class="p">))</span>

<span class="o">*</span><span class="n">name</span><span class="o">*</span>
</pre></div>

</div>

</section>



{:.input_area}
```python
def fence(original, wrapper='#'):
    """Return a new string which consists of the original string with the wrapper character before and after"""
    return wrapper + original + wrapper

print(fence('name', '*'))
```

{:.output_stream}
```
*name*

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Selecting characters from strings</h2>
</div>


<div class="panel-body">

<p>If the variable <code>s</code> refers to a string, then <code>s[0]</code> is the string's first
character and <code>s[-1]</code> is its last. Write a function called <code>outer</code> that
returns a string made up of just the first and last characters of its
input. A call to your function should look like this:</p>
<div class="codehilite"><pre><span></span><span class="k">print</span><span class="p">(</span><span class="n">outer</span><span class="p">(</span><span class="s1">&#39;helium&#39;</span><span class="p">))</span>

<span class="n">hm</span>
</pre></div>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Rescaling an array</h2>
</div>


<div class="panel-body">

<p>Write a function <code>rescale</code> that takes an array as input and returns a corresponding array of values scaled to lie in the range 0.0 to 1.0. (Hint: If L and H are the lowest and highest values in the original array, then the replacement for a value v should be (v − L)/(H − L).)</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Defining defaults</h2>
</div>


<div class="panel-body">

<p>Rewrite the <code>rescale</code> function so that it scales data to lie between 0.0 and 1.0 by default, but will allow the caller to specify lower and upper bounds if they want. Compare your implementation to your neighbor's: do the two functions always behave the same way?</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Variables inside and outside functions</h2>
</div>


<div class="panel-body">

<p>What does the following piece of code display when run - and why?</p>
<div class="codehilite"><pre><span></span><span class="n">f</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">k</span> <span class="o">=</span> <span class="mi">0</span>

<span class="k">def</span> <span class="nf">f2k</span><span class="p">(</span><span class="n">f</span><span class="p">):</span>
  <span class="n">k</span> <span class="o">=</span> <span class="p">((</span><span class="n">f</span><span class="o">-</span><span class="mi">32</span><span class="p">)</span><span class="o">*</span><span class="p">(</span><span class="mf">5.0</span><span class="o">/</span><span class="mf">9.0</span><span class="p">))</span> <span class="o">+</span> <span class="mf">273.15</span>
  <span class="k">return</span> <span class="n">k</span>

<span class="n">f2k</span><span class="p">(</span><span class="mi">8</span><span class="p">)</span>
<span class="n">f2k</span><span class="p">(</span><span class="mi">41</span><span class="p">)</span>
<span class="n">f2k</span><span class="p">(</span><span class="mi">32</span><span class="p">)</span>

<span class="k">print</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
</pre></div>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> The Old Switcheroo</h2>
</div>


<div class="panel-body">

<p>Consider this code:</p>
<div class="codehilite"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="mi">3</span>
<span class="n">b</span> <span class="o">=</span> <span class="mi">7</span>

<span class="k">def</span> <span class="nf">swap</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="n">temp</span> <span class="o">=</span> <span class="n">a</span>
    <span class="n">a</span> <span class="o">=</span> <span class="n">b</span>
    <span class="n">b</span> <span class="o">=</span> <span class="n">temp</span>

<span class="n">swap</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span>

<span class="k">print</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span>
</pre></div>


<p>Which of the following would be printed if you were to run this code? Why did you pick this answer?</p>
<ul>
<li><code>7 3</code></li>
<li><code>3 7</code></li>
<li><code>3 3</code></li>
<li><code>7 7</code></li>
</ul>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p><code>3, 7</code> is correct. Initially <code>a</code> has a value of 3 and <code>b</code> has a value of 7. When the <code>swap</code> function is called, it creates local variables (also called <code>a</code> and <code>b</code> in this case) and trades their values. The function does not return any values and does not alter <code>a</code> or <code>b</code> outside of its local copy. Therefore the original values of <code>a</code> and <code>b</code> remain unchanged.</p>

</div>

</section>



<section class="keypoints panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-exclamation-circle"></span> Key Points</h2>
</div>


<div class="panel-body">

<ul>
<li>Define a function using <code>def function_name(parameter)</code>.</li>
<li>The body of a function must be indented.</li>
<li>Call a function using <code>function_name(value)</code>.</li>
<li>Numbers are stored as integers or floating-point numbers.</li>
<li>Variables defined within a function can only be seen and used within the body of the function.</li>
<li>If a variable is not defined within the function it is used, Python looks for a definition before the function call</li>
<li>Specify default values for parameters when defining a function using <code>name=value</code> in the parameter list.</li>
<li>Parameters can be passed by matching based on name, by position, or by omitting them (in which case the default value is used).</li>
<li>Put code whose parameters change frequently in a function, then call it with different parameter values to customize its behavior.</li>
</ul>

</div>

</section>


---
The material in this notebook is derived from the Software Carpentry lessons
&copy; [Software Carpentry](http://software-carpentry.org/) under the terms
of the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
