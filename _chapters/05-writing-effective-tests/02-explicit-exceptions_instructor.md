---
interact_link: 05-writing-effective-tests/02-explicit-exceptions_instructor.ipynb
title: 'Explicit Exceptions'
permalink: 'chapters/05-writing-effective-tests/02-explicit-exceptions'
previouschapter:
  url: chapters/05-writing-effective-tests/01-errors-and-exceptions
  title: 'Errors and Exceptions'
nextchapter:
  url: chapters/05-writing-effective-tests/03-testing-your-code
  title: 'Testing Your Code'
redirect_from:
  - 'chapters/05-writing-effective-tests/02-explicit-exceptions'
---

# Raising Errors

It is possible to tell Python to generate an error. This is useful if you want to verify input to a function or stop your code running when something happens that your code does not know how to process.

Take this very simple function for example. This function is only designed to be used with numbers, so we want to make sure we dont pass a string.


{:.input_area}
```python
def square(x):
    if isinstance(x, str):
        raise ValueError("the argument x can not be a string")
    else:
        return x**2
```

The function works as expected with a number:


{:.input_area}
```python
square(10)
```




{:.output_data_text}
```
100
```



When it is passed a string it raises an error, telling the user that the argument x can not be a string.


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
<ipython-input-1-1e7b36c66a9f> in square(x)
      1 def square(x):
      2     if isinstance(x, str):
----> 3         raise ValueError("the argument x can not be a string")
      4     else:
      5         return x**2

```

{:.output_traceback_line}
```
ValueError: the argument x can not be a string
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
