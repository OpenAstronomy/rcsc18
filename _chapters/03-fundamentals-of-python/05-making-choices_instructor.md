---
interact_link: 03-fundamentals-of-python/05-making-choices_instructor.ipynb
title: 'Making Choices'
permalink: 'chapters/03-fundamentals-of-python/05-making-choices'
previouschapter:
  url: chapters/03-fundamentals-of-python/04-processing-files
  title: 'Processing Files'
nextchapter:
  url: chapters/03-fundamentals-of-python/06-functions
  title: 'Functions'
redirect_from:
  - 'chapters/03-fundamentals-of-python/05-making-choices'
---

# Making Choices

In our last lesson, we discovered something suspicious was going on in our
inflammation data by drawing some plots. How can we use Python to automatically
recognize the different features we saw, and take a different action for each?
In this lesson, we'll learn how to write code that runs only when certain
conditions are true.

## Conditionals

We can ask Python to take different actions, depending on a condition, with an `if` statement:


{:.input_area}
```python
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')
```

{:.output_stream}
```
not greater
done

```

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows the `if` statement is true,
the body of the `if`
(i.e., the lines indented underneath it) are executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:

![Executing a Conditional](./python-flowchart-conditional.png)

Conditional statements don't have to include an `else`.
If there isn't one, Python simply does nothing if the test is false:


{:.input_area}
```python
num = 53
print('before conditional...')
if num > 100:
    print(num,' is greater than 100')
print('...after conditional')
```

{:.output_stream}
```
before conditional...
...after conditional

```

We can also chain several tests together using `elif`,
which is short for "else if".
The following Python code uses `elif` to print the sign of a number.


{:.input_area}
```python
num = -3

if num > 0:
    print(num, 'is positive')
elif num == 0:
    print(num, 'is zero')
else:
    print(num, 'is negative')
```

{:.output_stream}
```
-3 is negative

```

Note that to test for equality we use a double equals sign `==`
rather than a single equals sign `=` which is used to assign values.

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:


{:.input_area}
```python
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')
```

{:.output_stream}
```
at least one part is false

```

while `or` is true if at least one part is true:


{:.input_area}
```python
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
```

{:.output_stream}
```
at least one test is true

```

## `True` and `False`
`True` and `False` are special words in Python called `booleans`,
which represent truth values. A statement such as `1 < 0` returns
the value `False`, while `-1 < 0` returns the value `True`.

callout

## Checking our Data

Now that we've seen how conditionals work,
we can use them to check for the suspicious features we saw in our inflammation data.
We are about to use functions provided by the `numpy` module again.
Therefore, if you're working in a new Python session, make sure to load the 
module with:


{:.input_area}
```python
import numpy as np
```


{:.input_area}
```python
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
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
<ipython-input-7-7ad694d53aff> in <module>()
----> 1 data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

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
OSError: inflammation-01.csv not found.
```


From the first couple of plots, we saw that maximum daily inflammation exhibits
a strange behavior and raises one unit a day.
Wouldn't it be a good idea to detect such behavior and report it as suspicious?
Let's do that! 
However, instead of checking every single day of the study, let's merely check
if maximum inflammation in the beginning (day 0) and in the middle (day 20) of 
the study are equal to the corresponding day numbers.


{:.input_area}
```python
max_inflammation_0 = np.max(data, axis=0)[0]
max_inflammation_20 = np.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-8-c4e2d7ef3971> in <module>()
----> 1 max_inflammation_0 = np.max(data, axis=0)[0]
      2 max_inflammation_20 = np.max(data, axis=0)[20]
      3 
      4 if max_inflammation_0 == 0 and max_inflammation_20 == 20:
      5     print('Suspicious looking maxima!')

```

{:.output_traceback_line}
```
NameError: name 'data' is not defined
```


We also saw a different problem in the third dataset;
the minima per day were all zero (looks like a healthy person snuck into our study).
We can also check for this with an `elif` condition:


{:.input_area}
```python
if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif np.sum(np.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-9-b50e51cf5286> in <module>()
----> 1 if max_inflammation_0 == 0 and max_inflammation_20 == 20:
      2     print('Suspicious looking maxima!')
      3 elif np.sum(np.min(data, axis=0)) == 0:
      4     print('Minima add up to zero!')

```

{:.output_traceback_line}
```
NameError: name 'max_inflammation_0' is not defined
```


And if neither of these conditions are true, we can use `else` to give the all-clear:


{:.input_area}
```python
if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif np.sum(np.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-10-d6411099f0d0> in <module>()
----> 1 if max_inflammation_0 == 0 and max_inflammation_20 == 20:
      2     print('Suspicious looking maxima!')
      3 elif np.sum(np.min(data, axis=0)) == 0:
      4     print('Minima add up to zero!')
      5 else:

```

{:.output_traceback_line}
```
NameError: name 'max_inflammation_0' is not defined
```


In this way,
we have asked Python to do something different depending on the condition of our data.
Here we printed messages in all cases,
but we could also imagine not using the `else` catch-all
so that messages are only printed when something is wrong,
freeing us from having to manually examine every plot for features we've seen before.

## How Many Paths?
Consider this code:



{:.input_area}
```python
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
```

{:.output_stream}
```
C

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge:</h2>
</div>


<div class="panel-body">

<p>Which of the following would be printed if you were to run this code?
Why did you pick this answer?</p>
<ol>
<li>A</li>
<li>B</li>
<li>C</li>
<li>B and C</li>
</ol>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>C gets printed because the first two conditions, <code>4 &gt; 5</code> and <code>4 == 5</code>, are not
true, but <code>4 &lt; 5</code> is true.</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge: What Is Truth?</h2>
</div>


<div class="panel-body">

<p><code>True</code> and <code>False</code> booleans are not the only values in Python that are true and false.
In fact, <em>any</em> value can be used in an <code>if</code> or <code>elif</code>.
After reading and running the code below,
explain what the rule is for which values are considered true and which are considered false.</p>

</div>

</section>



{:.input_area}
```python
if '':
    print('empty string is true')
if 'word':
    print('word is true')
if []:
    print('empty list is true')
if [1, 2, 3]:
    print('non-empty list is true')
if 0:
    print('zero is true')
if 1:
    print('one is true')
```

{:.output_stream}
```
word is true
non-empty list is true
one is true

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge: That's Not Not What I Meant</h2>
</div>


<div class="panel-body">

<p>Sometimes it is useful to check whether some condition is not true. The Boolean
operator <code>not</code> can do this explicitly. After reading and running the code below,
write some <code>if</code> statements that use <code>not</code> to test the rule that you formulated
in the previous challenge.</p>

</div>

</section>



{:.input_area}
```python
if not '':
    print('empty string is not true')
if not 'word':
    print('word is not true')
if not not True:
    print('not not True is true')
```

{:.output_stream}
```
empty string is not true
not not True is true

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge: Close Enough</h2>
</div>


<div class="panel-body">

<p>Write some conditions that print <code>True</code> if the variable <code>a</code> is within 10% of the variable <code>b</code>
and <code>False</code> otherwise.
Compare your implementation with your partner's:
do you get the same answer for all possible pairs of numbers?</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution 1</h2>
</div>

</section>



{:.input_area}
```python
a = 5
b = 5.1

if abs(a - b) < 0.1 * abs(b):
    print('True')
else:
    print('False')
```

{:.output_stream}
```
True

```


<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution 2</h2>
</div>

</section>



{:.input_area}
```python
print(abs(a - b) < 0.1 * abs(b))
```

{:.output_stream}
```
True

```


<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> </h2>
</div>


<div class="panel-body">

<p>This works because the Booleans <code>True</code> and <code>False</code> have string representations
which can be printed.</p>

</div>

</section>


## In-Place Operators
Python (and most other languages in the C family) provides in-place operators
that work like this:



{:.input_area}
```python
x = 1  # original value
x += 1 # add one to x, assigning result back to x
x *= 3 # multiply x by 3
print(x)
```

{:.output_stream}
```
6

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge:</h2>
</div>


<div class="panel-body">

<p>Write some code that sums the positive and negative numbers in a list separately,
using in-place operators.
Do you think the result is more or less readable than writing the same without in-place operators?</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>

</section>



{:.input_area}
```python
positive_sum = 0
negative_sum = 0
test_list = [3, 4, 6, 1, -1, -5, 0, 7, -8]
for num in test_list:
    if num > 0:
        positive_sum += num
    elif num == 0:
        pass
    else:
        negative_sum += num
print(positive_sum, negative_sum)
```

{:.output_stream}
```
21 -14

```

Here `pass` means "don't do anything".
In this particular case, it's not actually needed, since if `num == 0` neither
sum needs to change, but it illustrates the use of `elif` and `pass`.

## Sorting a List Into Buckets
In our `data` folder, large data sets are stored in files whose names start with
"inflammation-" and small data sets -- in files whose names start with "small-". We
also have some other files that we do not care about at this point. We'd like to break all
these files into three lists called `large_files`, `small_files`, and `other_files`,
respectively.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge:</h2>
</div>


<div class="panel-body">

<p>Add code to the template below to do this. Note that the string method
<a href="https://docs.python.org/3.5/library/stdtypes.html#str.startswith"><code>startswith</code></a>
returns <code>True</code> if and only if the string it is called on starts with the string
passed as an argument, that is:</p>

</div>

</section>



{:.input_area}
```python
"String".startswith("Str")
```




{:.output_data_text}
```
True
```



But


{:.input_area}
```python
"String".startswith("str")
```




{:.output_data_text}
```
False
```



Use the following Python code as your starting point:


{:.input_area}
```python
files = ['inflammation-01.csv', 'myscript.py', 'inflammation-02.csv', 'small-01.csv', 'small-02.csv']
large_files = []
small_files = []
other_files = []
```

Your solution should:
1.  loop over the names of the files
2.  figure out which group each filename belongs
3.  append the filename to that list

In the end the three lists should be:

```python
large_files = ['inflammation-01.csv', 'inflammation-02.csv']
small_files = ['small-01.csv', 'small-02.csv']
other_files = ['myscript.py']
```



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>

</section>



{:.input_area}
```python
for file in files:
    if file.startswith('inflammation-'):
        large_files.append(file)
    elif file.startswith('small-'):
        small_files.append(file)
    else:
        other_files.append(file)

print('large_files:', large_files)
print('small_files:', small_files)
print('other_files:', other_files)
```

{:.output_stream}
```
large_files: ['inflammation-01.csv', 'inflammation-02.csv']
small_files: ['small-01.csv', 'small-02.csv']
other_files: ['myscript.py']

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge: Counting Vowels</h2>
</div>


<div class="panel-body">

<ol>
<li>Write a loop that counts the number of vowels in a character string.</li>
<li>Test it on a few individual words and full sentences.</li>
<li>Once you are done, compare your solution to your neighbor's.
   Did you make the same decisions about how to handle the letter 'y'
   (which some people think is a vowel, and some do not)?</li>
</ol>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>

</section>



{:.input_area}
```python
vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print("The number of vowels in this string is " + str(count))
```

{:.output_stream}
```
The number of vowels in this string is 6

```

---
The material in this notebook is derived from the Software Carpentry lessons
&copy; [Software Carpentry](http://software-carpentry.org/) under the terms
of the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
