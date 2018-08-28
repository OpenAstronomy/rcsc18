---
interact_link: 06-writing-effective-tests/02-explicit-exceptions.ipynb
title: 'Explicit Exceptions'
permalink: 'chapters/06-writing-effective-tests/02-explicit-exceptions'
previouschapter:
  url: chapters/06-writing-effective-tests/01-errors-and-exceptions
  title: 'Errors And Exceptions'
nextchapter:
  url: 
  title: 'Approximating Pi'
redirect_from:
  - 'chapters/06-writing-effective-tests/02-explicit-exceptions'
---

# Raising Errors

It is possible to tell Python to generate an error. This is useful if you want to verify input to a function or handle a situation your code does not know how to handle.


{:.input_area}
```python
def square(x):
    if isinstance(x, str):
        raise ValueError("x can not be a string")
    else:
        return x**2
```


{:.input_area}
```python
square(10)
```




{:.output_data_text}
```
100
```




{:.input_area}
```python
square("aksdj")
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-3-0c38ed1bd00a> in <module>()
----> 1 square("aksdj")

```

{:.output_traceback_line}
```
<ipython-input-1-8050da5c4611> in square(x)
      1 def square(x):
      2     if isinstance(x, str):
----> 3         raise ValueError("x can not be a string")
      4     else:
      5         return x**2

```

{:.output_traceback_line}
```
ValueError: x can not be a string
```


You can raise many different kinds of exception, however `ValueError` is generally the most useful. Other useful types of error are:


{:.input_area}
```python
raise TypeError("This is not a number")
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-4-7cceb7db3229> in <module>()
----> 1 raise TypeError("This is not a number")

```

{:.output_traceback_line}
```
TypeError: This is not a number
```



{:.input_area}
```python
raise FileNotFoundError("This is not a file")
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
FileNotFoundError                         Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-5-b933b80c1c6d> in <module>()
----> 1 raise FileNotFoundError("This is not a file")

```

{:.output_traceback_line}
```
FileNotFoundError: This is not a file
```



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> What Type of Error?</h2>
</div>


<div class="panel-body">

<p>The example above:</p>
<div class="codehilite"><pre><span></span><span class="k">def</span> <span class="nf">square</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;x can not be a string&quot;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span>
</pre></div>


<p>uses <code>ValueError</code>, what type of error would be more appropriate?</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p><code>TypeError</code> should be raised when the type (i.e. <code>str</code>, <code>float</code>, <code>int</code>) is incorrect.</p>

</div>

</section>


## Silent Errors

Not all programming errors raise an exception, some are errors in the functioning of the code. i.e. this:


{:.input_area}
```python
def square(x):
    return x**3
```


{:.input_area}
```python
square(10)
```




{:.output_data_text}
```
1000
```



This is obviously incorrect, but Python does not know any difference, it executes the code as written and returns a result.

Most logical errors or "bugs" like this are not so easy to spot! As the complexity of your code increases the odds that mistakes and errors creep in increases. The best way to detect and prevent this kind of error is by writing tests.

## Tests

Tests can take many forms, they can compare your code against known results i.e. ones in a published paper, or they can just test that the result of some function returns the type of object you expect or even just check that your code results always stays the same, so you know if something breaks.

A simple test for our square function we defined above might look like:


{:.input_area}
```python
def test_square():
    assert square(10) == 10*10
```


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
<ipython-input-9-5351b87f150c> in <module>()
----> 1 test_square()

```

{:.output_traceback_line}
```
<ipython-input-8-0fd7f2671b21> in test_square()
      1 def test_square():
----> 2     assert square(10) == 10*10

```

{:.output_traceback_line}
```
AssertionError: 
```



<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> The `assert` statement</h2>
</div>


<div class="panel-body">

<p>As we will see later, the way to make a test fail is to raise an error. Therefore the <code>assert</code> statement in Python is a useful shortcut when writing tests.</p>
<p>The <code>assert</code> statement will raise an error if a condition is not satisfied. The general form of the assert statement is:</p>
<div class="codehilite"><pre><span></span><span class="k">assert</span> <span class="n">condition</span><span class="p">,</span> <span class="n">message</span>
</pre></div>


<p>i.e.</p>
<div class="codehilite"><pre><span></span><span class="k">assert</span> <span class="mi">5</span> <span class="o">==</span> <span class="mi">6</span><span class="p">,</span> <span class="s2">&quot;Five is not equal to six&quot;</span>
</pre></div>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> </h2>
</div>


<div class="panel-body">

<h1>Writing Tests</h1>
<p>Write tests for the following function. Try to think of ways that the function could do things that are not expected.</p>

</div>

</section>

