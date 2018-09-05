---
interact_link: 05-writing-effective-tests/04-testing-your-code-with-pytest_instructor.ipynb
title: 'Testing Your Code With Pytest'
permalink: 'chapters/05-writing-effective-tests/04-testing-your-code-with-pytest'
previouschapter:
  url: chapters/05-writing-effective-tests/03-testing-your-code
  title: 'Testing Your Code'
nextchapter:
  url: 
  title: 'Approximating Pi'
redirect_from:
  - 'chapters/05-writing-effective-tests/04-testing-your-code-with-pytest'
---

# Testing Code with pytest

In this lesson we will be going over some of the things we've learned so far about testing and demonstrate how to use pytest to expand your tests. We'll start by looking at some functions which have been provided for you, and then move on to testing them.

In your repo you should find a Python script called `fibonacci.py`, which contains a couple of functions providing slightly different implementations of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number). Each of these should take an integer input `n` and return the first `n` Fibonacci numbers.


{:.input_area}
```python
%load fibonacci.py
```


{:.input_area}
```python
import fibonacci as f

print(f.fib(15))
print(f.fib_numpy(15))
```

{:.output_stream}
```
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
[  1.   1.   2.   3.   5.   8.  13.  21.  34.  55.  89. 144. 233. 377.
 610.]

```

Once you've had a look at these functions and are happy with using them, let's move on to testing them.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Testing functions</h2>
</div>


<div class="panel-body">

<ol>
<li>
<p>Create a new script called <code>test_fibonacci.py</code>, or similar. In this script, write a test function for each of the Fibonacci implementations. Consider the following questions when writing your tests:</p>
<ul>
<li>How many different inputs do you need to test to be confident that the function is working as expected?</li>
<li>For a given input, is there a known, well-defined answer against which you can check the output?</li>
<li>Does the function output have any other qualities which might be wrong, and which should be tested?</li>
</ul>
<p>Remember that in order for your tests to call your functions, that script will need to import them.</p>
</li>
</ol>

</div>

</section>



{:.input_area}
```python
%load test_fibonacci1.py
```


{:.input_area}
```python
from test_fibonacci1 import test_fib_10, test_fib_numpy_10

test_fib_10()
test_fib_numpy_10()
```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Generalising the tests</h2>
</div>


<div class="panel-body">

<p>The approach we've used above, with one test for each function, is fine. But it's very specific to this particular scenario - if we introduced another implementation, we would have to write a new test function for it, which is not the point of modularity. Since our functions are supposed to give the same output, a better approach would be to have one generalised test function which could test any function we pass it.</p>
<ol>
<li>Combine your tests into one test function which takes a function as input and uses that as the function to be tested. Run your Fibonacci implementations through this new test and make sure they still pass.</li>
<li>The above solutions testing a specific input are fine in theory, but the point of tests is to find unexpected behaviour. Generalise your test function to test correct behaviour for a Fibonacci sequence of random length. You will probably want to look at the <code>numpy.random</code> module.</li>
</ol>

</div>

</section>



{:.input_area}
```python
%load test_fibonacci2.py
```


{:.input_area}
```python
from test_fibonacci2 import test_fib_10

test_fib_10(f.fib)
test_fib_10(f.fib_numpy)
```

Next, let's add a third implementation of the Fibonacci sequence.


{:.input_area}
```python
def fib_recursive(n):
    if n == 1 or n == 2:
        return 2
    return fib_recursive(n-1) + fib_recursive(n-1)

def fib_3(n):
    return [fib_recursive(i) for i in range(1, n)]
```


{:.input_area}
```python
fib_3(10)
```




{:.output_data_text}
```
[2, 2, 4, 8, 16, 32, 64, 128, 256]
```




<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Testing a Third Implementation</h2>
</div>


<div class="panel-body">

<p>Copy the functions above (exactly as shown here) into your <code>fibonacci.py</code> script. Use your tests to find the bugs and compare its output to the previous implementations.</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>

</section>


The actual `fib_recursive` function should read:


{:.input_area}
```python
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)
```

and should pass the tests.

## Introducing `pytest`

`pytest` is a Python module which contains a lot of tools for automating tests, rather than running the test for each function one at a time as we've done so far. We won't go into much detail with this, but you should know that it exists and to look into it if you need to write a large number of tests.

The most basic way to use `pytest` is with the command-line tool it provides. This command takes a filename as input, runs the functions defined there and reports whether they pass or fail.


{:.input_area}
```python
!pytest test_fibonacci1.py
```

{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.6, pytest-3.7.3, py-1.5.4, pluggy-0.7.1
rootdir: /home/stuart/Git/Aperio/stfc_website/notebooks/05-writing-effective-tests, inifile:
plugins: xonsh-0.7.7, remotedata-0.3.0, openfiles-0.3.0, mock-1.10.0, doctestplus-0.1.3, arraydiff-0.2, hypothesis-3.68.0
collected 2 items                                                              [0m

test_fibonacci1.py ..[36m                                                    [100%][0m

[32m[1m=========================== 2 passed in 0.03 seconds ===========================[0m

```

This works in this example because I've used a file containing only our first versions of the tests, which took no input. Using the new combined test, `pytest` doesn't know what input to provide, so it reports the test as having failed. However, there is a commonly-used feature in `pytest` which addresses this, which is the `parametrize` decorator. This allows you to specify inputs for the input parameters of your test functions. What makes it particularly useful though, is that you can specify several for each parameter and `pytest` will automatically run the test with all of those inputs. In this way you can automate testing your functions with a wide range of inputs without having to type out many different function calls yourself.

For our example, we can use this decorator to pass in the functions we wish to test, like this:


{:.input_area}
```python
# %load test_fibonacci3.py
import pytest

import numpy as np

from fibonacci import fib, fib_numpy


@pytest.mark.parametrize("f_fib", (fib, fib_numpy))
def test_random_fib(f_fib):
    n = np.random.randint(1, 1000)
    a = f_fib(n)
    n2 = np.random.randint(3, n)
    assert a[n2] == a[n2-1] + a[n2-2]

```

Now when we run this script with `pytest`, you'll notice that even though we have only defined one function, it still runs two tests, one with each of our Fibonacci functions as input.


{:.input_area}
```python
!pytest test_fibonacci3.py
```

{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.6, pytest-3.7.3, py-1.5.4, pluggy-0.7.1
rootdir: /home/stuart/Git/Aperio/stfc_website/notebooks/05-writing-effective-tests, inifile:
plugins: xonsh-0.7.7, remotedata-0.3.0, openfiles-0.3.0, mock-1.10.0, doctestplus-0.1.3, arraydiff-0.2, hypothesis-3.68.0
collected 2 items                                                              [0m

test_fibonacci3.py ..[36m                                                    [100%][0m

[32m[1m=========================== 2 passed in 0.08 seconds ===========================[0m

```

This should also pass all the previous tests written. You may have also wanted to add tests that detect the `RecursionError` when $n==0$.
