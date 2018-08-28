---
interact_link: 04-fundamentals-of-python-part-2/02-comments-and-docs.ipynb
title: 'Comments And Docs'
permalink: 'chapters/04-fundamentals-of-python-part-2/02-comments-and-docs'
previouschapter:
  url: chapters/04-fundamentals-of-python-part-2/01-functions
  title: 'Functions'
nextchapter:
  url: 
  title: 'Writing Effective Tests'
redirect_from:
  - 'chapters/04-fundamentals-of-python-part-2/02-comments-and-docs'
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

## Testing and Documenting

Once we start putting things in functions so that we can re-use them, we need to start testing that those functions are working correctly. To see how to do this, let’s write a function to offset a dataset so that it’s mean value shifts to a user-defined value:


{:.input_area}
```python
import numpy as np

def offset_mean(data, target_mean_value):
    return (data - np.mean(data)) + target_mean_value
```

We could test this on our actual data, but since we don’t know what the values ought to be, it will be hard to tell if the result was correct. Instead, let’s use NumPy to create a matrix of 0’s and then offset its values to have a mean value of 3:


{:.input_area}
```python
z = np.zeros((2,2))
print(offset_mean(z, 3))
```

That looks right, so let’s try `offset_mean` on our real data:


{:.input_area}
```python
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(offset_mean(data, 0))
```

It’s hard to tell from the default output whether the result is correct, but there are a few simple tests that will reassure us:


{:.input_area}
```python
print('original min, mean, and max are:', np.min(data), np.mean(data), np.max(data))
offset_data = offset_mean(data, 0)
print('min, mean, and max of offset data are:', 
      np.min(offset_data), 
      np.mean(offset_data), 
      np.max(offset_data))
```

That seems almost right: the original mean was about 6.1, so the lower bound from zero is now about -6.1. The mean of the offset data isn’t quite zero — we’ll explore why not in the challenges — but it’s pretty close. We can even go further and check that the standard deviation hasn’t changed:


{:.input_area}
```python
print('std dev before and after:', np.std(data), np.std(offset_data))
```

Those values look the same, but we probably wouldn’t notice if they were different in the sixth decimal place. Let’s do this instead:


{:.input_area}
```python
print('difference in standard deviations before and after:', 
      np.std(data) - np.std(offset_data))
```

Again, the difference is very small. It’s still possible that our function is wrong, but it seems unlikely enough that we should probably get back to doing our analysis. We have one more task first, though: we should write some documentation for our function to remind ourselves later what it’s for and how to use it.

The usual way to put documentation in software is to add comments like this:


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
<h2 class="fa fa-pencil"> # Testing and Documenting Your Function</h2>
</div>


<div class="panel-body">


Run the commands `help(np.arange)` and `help(np.linspace)` to see how to use these functions to generate regularly-spaced values, then use those values to test your `rescale` function. Once you’ve successfully tested your function, add a docstring that explains what it does.

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> # Solution</h2>
</div>


<div class="panel-body">


```python
"""
Takes an array as input, and returns a corresponding array scaled so that 0 corresponds to the minimum and 1 to the maximum value of the input array.

Examples:
>>> rescale(numpy.arange(10.0))
array([ 0.        ,  0.11111111,  0.22222222,  0.33333333,  0.44444444,
        0.55555556,  0.66666667,  0.77777778,  0.88888889,  1.        ])
>>> rescale(numpy.linspace(0, 100, 5))
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
"""
```

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> # Readable Code</h2>
</div>


<div class="panel-body">


Revise a function you wrote for one of the previous exercises to try to make the code more readable. Then, collaborate with one of your neighbors to critique each other’s functions and discuss how your function implementations could be further improved to make them more readable.

</div>

</section>


Key Points

- Use `help(thing)` to view help for something.
- Put docstrings in functions to provide help for that function.
