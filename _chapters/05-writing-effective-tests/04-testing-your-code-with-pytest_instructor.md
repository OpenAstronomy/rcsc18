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

In this lesson we will be going over some of the things we've learned so far about testing and demonstrate a useful Python library which you can use to expand your tests. We will be writing two Python scripts, one with a few functions in, and one with our tests.

We start off with a couple of implementations of a function to generate the Fibonacci sequence.


{:.input_area}
```python
# %load fibonacci.py
import numpy as np


def fib(n):
    fib = [0, 1]
    while len(fib) < n+1:
        fib.append(fib[-2] + fib[-1])
    return fib[1:]


def fib_numpy(n):
    fib = np.zeros(n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[1:]

```

The next thing we are going to do is write a test file to test these implementations.


{:.input_area}
```python
# %load test_fibonacci.py
import pytest

import numpy as np

from fibonacci import fib, fib_numpy


def test_fib_10():
    a = fib(10)
    assert len(a) == 10
    assert a == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fib_numpy_10():
    a = fib_numpy(10)
    assert len(a) == 10
    assert np.allclose(a, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


@pytest.mark.parametrize("f_fib", (fib, fib_numpy))
def test_random_fib(f_fib):
    n = np.random.randint(1, 1000)
    a = f_fib(n)
    n2 = np.random.randint(3, n)
    assert a[n2] == a[n2-1] + a[n2-2]

```

Next, let's add a third implementation of the Fibonacci sequence


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

<p>Add this third implementation to the <code>fibonacci.py</code> file and write tests for it to find the bugs and compare it's output to the previous implementations.</p>

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

This should also pass all the previous tests written. You may have also wanted to add tests that detect the `RecursionError` when $n==0$.


{:.input_area}
```python
def test_recursion_error():
    with pytest.raises(RecursionError):
        fib_recursive(0)
```
