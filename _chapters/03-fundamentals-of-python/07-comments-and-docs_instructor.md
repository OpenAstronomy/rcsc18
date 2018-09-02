---
interact_link: 03-fundamentals-of-python/07-comments-and-docs_instructor.ipynb
title: 'Comments and Docs'
permalink: 'chapters/03-fundamentals-of-python/07-comments-and-docs'
previouschapter:
  url: chapters/03-fundamentals-of-python/06-functions
  title: 'Functions'
nextchapter:
  url: 
  title: 'Further Python'
redirect_from:
  - 'chapters/03-fundamentals-of-python/07-comments-and-docs'
---

# Comments and documentation

## Commenting code

- Confirm comment character if haven't seen it already (unlikely)
- Purpose of comments
- Where/why/how to write comments
- cat/dog picture
- go back through code and make sure it's commented

## Documentation

- Broad concept of why there should be docs (large scale)
- smaller scale reasons for having docs
- docstrings, etc
- go back through code and doc it
- see docstring challenges in swc function material

## Documenting code

Now that we've started thinking about re-using parts of our code, we need to think about what that will actually involve for the user. At the moment, the user is yourself, and you've only just written the function, so it doesn't take a lot to remember what the function does and what parameters it takes.

But re-using code doesn't just mean within a single project in the short term. You might have some task you want to do many times over several projects over the next few years, in which case the user may be future-you. Will you remember in two weeks' time what parameters your function takes? How about in two months? Two years? If you make your code available to others to use, they will also want to know how to use your functions.

One way of figuring out how to use a function is to simply look at the code, but this isn't ideal. It means finding the particular file where the function is written and looking through the whole function to see what all the variables do, which is time-consuming and can be difficult in large or complex functions. A much better solution is documentation - writing down what your code does as you write it.

Some large software packages may have a manual, or narrative documentation which describes conceptually how and why to use different parts of that software. These are useful and an important aspect of documentation. But for now we'll focus more on documenting the code itself, which is more likely to be helpful when working on a smaller or personal project. To do this we'll use two things: comments, which we've already seen, and **docstrings**.

For this lesson we'll use a new function to demonstrate documentation. It will take a NumPy array and shift it such that the mean is offset to some user-defined value.


{:.input_area}
```python
import numpy as np

def offset_mean(data, target_mean_value):
    return (data - np.mean(data)) + target_mean_value
```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> # Comments - reminder</h2>
</div>


<div class="panel-body">

<p>Comments are lines in a code which are ignored when the code is run. They're usually indicated by a comment character at the start of the line (in Python's case, a hash, '<code>#</code>'), and they're a crucial part of documenting code.</p>

</div>

</section>


### How not to use comments

![](https://matrix.org/_matrix/media/v1/download/cadair.com/JtaDnstvdkcNHasPpOzqzOSr)

Comments are important but they have to be carefully considered. This picture demonstrates a common way in which comments are misused, by simply describing exactly what the corresponding code does. For the function we wrote above, such a comment might look something like this:


{:.input_area}
```python
def offset_mean(data, target_mean_value):
    # Subtract the mean of the data from the data, then add the target mean value to the result and return that
    return (data - np.mean(data)) + target_mean_value
```

At best, this is no better than not having a comment, since it is essentially just repeating the code. In fact, the code itself arguably a clearer and more concise description of what the comment is trying to express anyway. Similarly, it's easy for comments to be too brief or vague:


{:.input_area}
```python
def offset_mean(data, target_mean_value):
    # Return solution
    return (data - np.mean(data)) + target_mean_value
```

This is just as unhelpful - just like the last comment, it doesn't provide any new information to the user. Even worse would be this:


{:.input_area}
```python
def offset_mean(data, target_mean_value):
    # Add the mean of the data to the data, then add the target mean value to the result and return that
    return (data - np.mean(data)) + target_mean_value
```

You might not think this kind of comment is particularly likely, but it's actually very easy for comments to be left behind when code changes. This may also seem like an easy mistake to spot and to ignore, but again, the best case scenario here is that you realise the comment is wrong, in which case the comment may as well not be there. Also, what if the comment isn't wrong? Maybe we changed the comment and then neglected to change the code. However it happens, if the code and comment don't match up, would you be able to determine which one is correct? This is just a difficult task in any situation, but it is made far more difficult when the comment only (incorrectly) describes what the following code does.

### How to use comments

Comments should always be used liberally throughout your code (with the caveat of avoiding unhelpful ones as described above). Most importantly they should describe _why_ and _how_ the code is doing what it's doing. The aim is for someone reading your code (which might be you) to be able to _understand_ what is happening, not simply to describe mechanically what any particular part of it does. For example, we might more usefully document our function from above like this:


{:.input_area}
```python
# offset_mean(data, target_mean_value): 
# return a new array containing the original data with its mean offset to match the desired value.
def offset_mean(data, target_mean_value):
    return (data - np.mean(data)) + target_mean_value
```

In these comments we have a description of how to call the fuction, what output the user can expect from the function, and what the function achieves. The description of the function call may seem redundant, but we'll see in a moment how it can be made more useful. Also note here that we're documenting the function itself here, not the code within it. Smaller blocks of code certainly should be commented, especially in a larger function than this, but it's very easy to fall into the traps described above, and it's more important to comment chunks of code than individual lines. With a very short function like this, it can reasonably be commented as a single block.

## Docstrings



So now we've seen 
There’s a better way, though. If the first thing in a function is a string that isn’t assigned to a variable, that string is attached to the function as its documentation:


{:.input_area}
```python
# offset_mean(data, target_mean_value): 
# return a new array containing the original data with its mean offset to match the desired value.
def offset_mean(data, target_mean_value):
    return (data - np.mean(data)) + target_mean_value
```

There’s a better way, though. If the first thing in a function is a string that isn’t assigned to a variable, that string is attached to the function as its documentation:


{:.input_area}
```python
def offset_mean(data, target_mean_value):
    """Return a new array containing the original data with its mean offset to match the desired value."""
    return (data - np.mean(data)) + target_mean_value
```

This is better because we can now ask Python’s built-in help system to show us the documentation for the function:


{:.input_area}
```python
help(offset_mean)
```

{:.output_stream}
```
Help on function offset_mean in module __main__:

offset_mean(data, target_mean_value)
    Return a new array containing the original data with its mean offset to match the desired value.


```

A string like this is called a **docstring**. We don’t need to use triple quotes when we write one, but if we do, we can break the string across multiple lines:


{:.input_area}
```python
def offset_mean(data, target_mean_value):
    """
    Return a new array containing the original data
       with its mean offset to match the desired value.
    
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]
    """
    
    return (data - np.mean(data)) + target_mean_value

help(offset_mean)
```

{:.output_stream}
```
Help on function offset_mean in module __main__:

offset_mean(data, target_mean_value)
    Return a new array containing the original data
       with its mean offset to match the desired value.
    
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]


```

## Readable functions

Consider these two functions:

```python
def s(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m) * (v - m)
    return np.sqrt(d / (len(p) - 1))

def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return np.sqrt(sum_squared_devs / (len(sample) - 1))
```

The functions `s` and `std_dev` are computationally equivalent (they both calculate the sample standard deviation), but to a human reader, they look very different. You probably found `std_dev` much easier to read and understand than `s`.

As this example illustrates, both documentation and a programmer’s _coding style_ combine to determine how easy it is for others to read and understand the programmer’s code. Choosing meaningful variable names and using blank spaces to break the code into logical “chunks” are helpful techniques for producing _readable code_. This is useful not only for sharing code with others, but also for the original programmer. If you need to revisit code that you wrote months ago and haven’t thought about since then, you will appreciate the value of readable code!


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Testing and Documenting Your Function</h2>
</div>


<div class="panel-body">

<p>Run the commands <code>help(np.arange)</code> and <code>help(np.linspace)</code> to see how to use these functions to generate regularly-spaced values, then use those values to test your <code>rescale</code> function. Once you’ve successfully tested your function, add a docstring that explains what it does.</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> # Solution</h2>
</div>


<div class="panel-body">

<div class="codehilite"><pre><span></span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd">Takes an array as input, and returns a corresponding array scaled so that 0 corresponds to the minimum and 1 to the maximum value of the input array.</span>

<span class="sd">Examples:</span>
<span class="sd">&gt;&gt;&gt; rescale(numpy.arange(10.0))</span>
<span class="sd">array([ 0.        ,  0.11111111,  0.22222222,  0.33333333,  0.44444444,</span>
<span class="sd">        0.55555556,  0.66666667,  0.77777778,  0.88888889,  1.        ])</span>
<span class="sd">&gt;&gt;&gt; rescale(numpy.linspace(0, 100, 5))</span>
<span class="sd">array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> # Readable Code</h2>
</div>


<div class="panel-body">

<p>Revise a function you wrote for one of the previous exercises to try to make the code more readable. Then, collaborate with one of your neighbors to critique each other’s functions and discuss how your function implementations could be further improved to make them more readable.</p>

</div>

</section>


Key Points

- Use `help(thing)` to view help for something.
- Put docstrings in functions to provide help for that function.
