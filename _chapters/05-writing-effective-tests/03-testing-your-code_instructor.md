---
interact_link: 05-writing-effective-tests/03-testing-your-code_instructor.ipynb
title: 'Testing Your Code'
permalink: 'chapters/05-writing-effective-tests/03-testing-your-code'
previouschapter:
  url: chapters/05-writing-effective-tests/02-explicit-exceptions
  title: 'Explicit Exceptions'
nextchapter:
  url: chapters/05-writing-effective-tests/04-testing-your-code-with-pytest
  title: 'Testing Your Code With Pytest'
redirect_from:
  - 'chapters/05-writing-effective-tests/03-testing-your-code'
---

# Tests and Exceptions

In this lesson we will look at how to make your code more reliable by writing tests. Tests when used cleverly can give you a lot of confidence in your code and therefore your results!

Lets start with our (broken) square function from the last lesson:


{:.input_area}
```python
def square(x):
    return x**3
```

Tests can take many forms, they can compare your code against known results i.e. ones in a published paper, or they can just test that the result of some function returns the type of object you expect or even just check that your code results always stays the same, so you know if something breaks.

A simple test for our square function we defined above might look like:


{:.input_area}
```python
def test_square():
    assert square(10) == 10*10
```


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> The `assert` statement</h2>
</div>


<div class="panel-body">

<p>As we will see later, the way to make a test fail is to raise an error. Therefore the <code>assert</code> statement in Python is a useful shortcut when writing tests.</p>
<p>The <code>assert</code> statement will raise an error if a condition is not satisfied. The general form of the assert statement is:</p>
<div class="codehilite"><pre><span></span><span class="k">assert</span> <span class="n">condition</span><span class="p">,</span> <span class="s2">&quot;message&quot;</span>
</pre></div>


<p>i.e.</p>
<div class="codehilite"><pre><span></span><span class="k">assert</span> <span class="mi">5</span> <span class="o">==</span> <span class="mi">6</span><span class="p">,</span> <span class="s2">&quot;Five is not equal to six&quot;</span>
</pre></div>

</div>

</section>


We can run our test function the same way that we run any other function. Although this dosent scale very well to thousands of tests!


{:.input_area}
```python
test_square()
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
AssertionError                            Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-3-5351b87f150c> in <module>()
----> 1 test_square()

```

{:.output_traceback_line}
```
<ipython-input-2-0fd7f2671b21> in test_square()
      1 def test_square():
----> 2     assert square(10) == 10*10

```

{:.output_traceback_line}
```
AssertionError: 
```



<section class="challange panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> </h2>
</div>


<div class="panel-body">

<h1>Writing Tests</h1>
<p>The following function has bugs in it. Write some tests below the function to find all the bugs.</p>

</div>

</section>



{:.input_area}
```python
def quadratic(a, b, c):
    return ((-1* b) * np.sqrt(b**2 - 4*a*c) / (2 * a))
```


{:.input_area}
```python
import numpy as np
```


{:.input_area}
```python
def test_quadratic():
    assert(quadratic(1,1,-1)) == -1.118033988749895

test_quadratic()
```

# Running Tests Automatically with pytest

Once you have a few test functions written, you will probably start getting bored with typing out their names and running them one-by-one. There are a few different modules to help you write and run tests. The one we will be using is called [`pytest`](https://docs.pytest.org/en/latest/). 

For the next section of this session we will be using the two Python (`.py`) files named `askdl.py` and `lsadkj.py`.
