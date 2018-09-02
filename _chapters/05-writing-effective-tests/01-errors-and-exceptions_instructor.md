---
interact_link: 05-writing-effective-tests/01-errors-and-exceptions_instructor.ipynb
title: 'Errors and Exceptions'
permalink: 'chapters/05-writing-effective-tests/01-errors-and-exceptions'
previouschapter:
  url: 
  title: 'Writing Effective Tests'
nextchapter:
  url: chapters/05-writing-effective-tests/02-explicit-exceptions
  title: 'Explicit Exceptions'
redirect_from:
  - 'chapters/05-writing-effective-tests/01-errors-and-exceptions'
---

# Errors and Exceptions

Every programmer encounters errors, both those who are just beginning, and those
who have been programming for years. Encountering errors and exceptions can be
very frustrating at times, and can make coding feel like a hopeless endeavour.
However, understanding what the different types of errors are and when you are
likely to encounter them can help a lot. Once you know *why* you get certain
types of errors, they become much easier to fix.

Errors in Python have a very specific form, called a traceback. Let's examine
one:


{:.input_area}
```python
# This code has an intentional error. You can type it directly or
# use it for reference to understand the error message below.
def favorite_ice_cream():
    ice_creams = [
        "chocolate",
        "vanilla",
        "strawberry"
    ]
    print(ice_creams[3])

favorite_ice_cream()
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
IndexError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-1-d9c4f1bc4564> in <module>()
      9     print(ice_creams[3])
     10 
---> 11 favorite_ice_cream()

```

{:.output_traceback_line}
```
<ipython-input-1-d9c4f1bc4564> in favorite_ice_cream()
      7         "strawberry"
      8     ]
----> 9     print(ice_creams[3])
     10 
     11 favorite_ice_cream()

```

{:.output_traceback_line}
```
IndexError: list index out of range
```


This particular traceback has two levels.
You can determine the number of levels by looking for the number of arrows on the left hand side.
In this case:
1.  The first shows code from the cell above,
    with an arrow pointing to Line 8 (which is `favorite_ice_cream()`).

2.  The second shows some code in the function `favorite_ice_cream`,
    with an arrow pointing to Line 6 (which is `print(ice_creams[3])`).

The last level is the actual place where the error occurred.
The other level(s) show what function the program executed to get to the next level down.
So, in this case, the program first performed a function call to the function `favorite_ice_cream`.
Inside this function,
the program encountered an error on Line 6, when it tried to run the code `print(ice_creams[3])`.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Long Tracebacks</h2>
</div>


<div class="panel-body">

<p>Sometimes, you might see a traceback that is very long -- sometimes they might even be 20 levels deep!
This can make it seem like something horrible happened,
but really it just means that your program called many functions before it ran into the error.
Most of the time,
you can just pay attention to the bottom-most level,
which is the actual place where the error occurred.</p>

</div>

</section>


So what error did the program actually encounter?

In the last line of the traceback, Python helpfully tells us the category or
type of error (in this case, it is an `IndexError`) and a more detailed error
message (in this case, it says "list index out of range"). If you encounter an
error and don't know what it means, it is still important to read the traceback
closely. That way, if you fix the error, but encounter a new one, you can tell
that the error changed. Additionally, sometimes just knowing *where* the error
occurred is enough to fix it, even if you don't entirely understand the message.

If you do encounter an error you don't recognize, try looking at the [official
documentation on errors](http://docs.python.org/3/library/exceptions.html).
However, note that you may not always be able to find the error there, as it is
possible to create custom errors. In that case, hopefully the custom error
message is informative enough to help you figure out what went wrong.

## Syntax Errors

When you forget a colon at the end of a line,
accidentally add one space too many when indenting under an `if` statement,
or forget a parenthesis,
you will encounter a syntax error.
This means that Python couldn't figure out how to read your program.
This is similar to forgetting punctuation in English:
for example,
this text is difficult to read there is no punctuation there is also no capitalization
why is this hard because you have to figure out where each sentence ends
you also have to figure out where each sentence begins
to some extent it might be ambiguous if there should be a sentence break or not

People can typically figure out what is meant by text with no punctuation,
but people are much smarter than computers.
If Python doesn't know how to read the program,
it will just give up and inform you with an error.
For example:


{:.input_area}
```python
def some_function()
    msg = "hello, world!"
    print(msg)
     return msg
```


{:.output_traceback_line}
```
  File "<ipython-input-2-95d391d879b2>", line 1
    def some_function()
                       ^
SyntaxError: invalid syntax

```


Here, Python tells us that there is a `SyntaxError` on line 1,
and even puts a little arrow in the place where there is an issue.
In this case the problem is that the function definition is missing a colon at the end.

Actually, the function above has *two* issues with syntax.
If we fix the problem with the colon,
we see that there is *also* an `IndentationError`,
which means that the lines in the function definition do not all have the same indentation:


{:.input_area}
```python
def some_function():
    msg = "hello, world!"
    print(msg)
     return msg
```


{:.output_traceback_line}
```
  File "<ipython-input-3-18d6e2304f63>", line 4
    return msg
    ^
IndentationError: unexpected indent

```


Both `SyntaxError` and `IndentationError` indicate a problem with the syntax of your program,
but an `IndentationError` is more specific:
it *always* means that there is a problem with how your code is indented.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Tabs and Spaces</h2>
</div>


<div class="panel-body">

<p>Some indentation errors are harder to spot than others.
In particular, mixing spaces and tabs can be difficult to spot
because they are both whitespace.
In the example below, the first two lines in the body of the function
<code>some_function</code> are indented with tabs, while the third line &mdash; with spaces.
If you're working in a Jupyter notebook, be sure to copy and paste this example
rather than trying to type it in manually because Jupyter automatically replaces
tabs with spaces.</p>
<div class="codehilite"><pre><span></span><span class="k">def</span> <span class="nf">some_function</span><span class="p">():</span>
    <span class="n">msg</span> <span class="o">=</span> <span class="s2">&quot;hello, world!&quot;</span>
    <span class="k">print</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">msg</span>
</pre></div>


<p>Visually it is impossible to spot the error.
Fortunately, Python does not allow you to mix tabs and spaces.</p>
<div class="codehilite"><pre><span></span>  File &quot;&lt;ipython-input-5-653b36fbcd41&gt;&quot;, line 4
    return msg
              ^
TabError: inconsistent use of tabs and spaces in indentation
</pre></div>

</div>

</section>


## Variable Name Errors

Another very common type of error is called a `NameError`,
and occurs when you try to use a variable that does not exist.
For example:


{:.input_area}
```python
print(a)
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
<ipython-input-4-bca0e2660b9f> in <module>()
----> 1 print(a)

```

{:.output_traceback_line}
```
NameError: name 'a' is not defined
```


Variable name errors come with some of the most informative error messages,
which are usually of the form "name 'the_variable_name' is not defined".

Why does this error message occur?
That's a harder question to answer,
because it depends on what your code is supposed to do.
However,
there are a few very common reasons why you might have an undefined variable.
The first is that you meant to use a string, but forgot to put quotes around it:


{:.input_area}
```python
print(hello)
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
<ipython-input-5-1cd80308eb4c> in <module>()
----> 1 print(hello)

```

{:.output_traceback_line}
```
NameError: name 'hello' is not defined
```


The second is that you just forgot to create the variable before using it.
In the following example,
`count` should have been defined (e.g., with `count = 0`) before the for loop:


{:.input_area}
```python
for number in range(10):
    count = count + number
print("The count is:", count)
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
<ipython-input-6-223ed4c94391> in <module>()
      1 for number in range(10):
----> 2     count = count + number
      3 print("The count is:", count)

```

{:.output_traceback_line}
```
NameError: name 'count' is not defined
```


Finally, the third possibility is that you made a typo when you were writing your code.
Let's say we fixed the error above by adding the line `Count = 0` before the for loop.
Frustratingly, this actually does not fix the error.
Remember that variables are case-sensitive,
so the variable `count` is different from `Count`. We still get the same error, because we still have not defined `count`:


{:.input_area}
```python
Count = 0
for number in range(10):
    count = count + number
print("The count is:", count)
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
<ipython-input-7-52704ad2ac41> in <module>()
      1 Count = 0
      2 for number in range(10):
----> 3     count = count + number
      4 print("The count is:", count)

```

{:.output_traceback_line}
```
NameError: name 'count' is not defined
```


## Index Errors

Next up are errors having to do with containers (like lists and strings) and the items within them.
If you try to access an item in a list or a string that does not exist,
then you will get an error.
This makes sense:
if you asked someone what day they would like to get coffee,
and they answered "caturday",
you might be a bit annoyed.
Python gets similarly annoyed if you try to ask it for an item that doesn't exist:


{:.input_area}
```python
letters = ['a', 'b', 'c']
print("Letter #1 is", letters[0])
print("Letter #2 is", letters[1])
print("Letter #3 is", letters[2])
print("Letter #4 is", letters[3])
```

{:.output_stream}
```
Letter #1 is a
Letter #2 is b
Letter #3 is c

```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
IndexError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-8-9624ce6f7f87> in <module>()
      3 print("Letter #2 is", letters[1])
      4 print("Letter #3 is", letters[2])
----> 5 print("Letter #4 is", letters[3])

```

{:.output_traceback_line}
```
IndexError: list index out of range
```


Here, Python is telling us that there is an `IndexError` in our code, meaning we
tried to access a list index that did not exist.

## File Errors

The last type of error we'll cover today
are those associated with reading and writing files: `FileNotFoundError`.
If you try to read a file that does not exist,
you will receive a `FileNotFoundError` telling you so.
If you attempt to write to a file that was opened read-only, Python 3
returns an `UnsupportedOperationError`.
More generally, problems with input and output manifest as
`IOError`s or `OSError`s, depending on the version of Python you use.


{:.input_area}
```python
file_handle = open('myfile.txt', 'r')
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
<ipython-input-9-080b0e91cc46> in <module>()
----> 1 file_handle = open('myfile.txt', 'r')

```

{:.output_traceback_line}
```
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
```


One reason for receiving this error is that you specified an incorrect path to the file.
For example,
if I am currently in a folder called `myproject`,
and I have a file in `myproject/writing/myfile.txt`,
but I try to just open `myfile.txt`,
this will fail.
The correct path would be `writing/myfile.txt`.
It is also possible (like with `NameError`) that you just made a typo.

A related issue can occur if you use the "read" flag instead of the "write" flag.
Python will not give you an error if you try to open a file for writing when the file does not exist.
However,
if you meant to open a file for reading,
but accidentally opened it for writing,
and then try to read from it,
you will get an `UnsupportedOperation` error
telling you that the file was not opened for reading:


{:.input_area}
```python
file_handle = open('myfile.txt', 'w')
file_handle.read()
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
UnsupportedOperation                      Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-10-063a9999adc0> in <module>()
      1 file_handle = open('myfile.txt', 'w')
----> 2 file_handle.read()

```

{:.output_traceback_line}
```
UnsupportedOperation: not readable
```


These are the most common errors with files,
though many others exist.
If you get an error that you've never seen before,
searching the Internet for that error type
often reveals common reasons why you might get that error.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Reading Error Messages</h2>
</div>


<div class="panel-body">

<p>Read the python code and the resulting traceback below, and answer the following questions:</p>
<ol>
<li>How many levels does the traceback have?</li>
<li>What is the function name where the error occurred?</li>
<li>On which line number in this function did the error occurr?</li>
<li>What is the type of error?</li>
<li>What is the error message?</li>
</ol>
<div class="codehilite"><pre><span></span><span class="c1"># This code has an intentional error. Do not type it directly;</span>
<span class="c1"># use it for reference to understand the error message below.</span>
<span class="k">def</span> <span class="nf">print_message</span><span class="p">(</span><span class="n">day</span><span class="p">):</span>
    <span class="n">messages</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">&quot;monday&quot;</span><span class="p">:</span> <span class="s2">&quot;Hello, world!&quot;</span><span class="p">,</span>
        <span class="s2">&quot;tuesday&quot;</span><span class="p">:</span> <span class="s2">&quot;Today is tuesday!&quot;</span><span class="p">,</span>
        <span class="s2">&quot;wednesday&quot;</span><span class="p">:</span> <span class="s2">&quot;It is the middle of the week.&quot;</span><span class="p">,</span>
        <span class="s2">&quot;thursday&quot;</span><span class="p">:</span> <span class="s2">&quot;Today is Donnerstag in German!&quot;</span><span class="p">,</span>
        <span class="s2">&quot;friday&quot;</span><span class="p">:</span> <span class="s2">&quot;Last day of the week!&quot;</span><span class="p">,</span>
        <span class="s2">&quot;saturday&quot;</span><span class="p">:</span> <span class="s2">&quot;Hooray for the weekend!&quot;</span><span class="p">,</span>
        <span class="s2">&quot;sunday&quot;</span><span class="p">:</span> <span class="s2">&quot;Aw, the weekend is almost over.&quot;</span>
    <span class="p">}</span>
    <span class="k">print</span><span class="p">(</span><span class="n">messages</span><span class="p">[</span><span class="n">day</span><span class="p">])</span>

<span class="k">def</span> <span class="nf">print_friday_message</span><span class="p">():</span>
    <span class="n">print_message</span><span class="p">(</span><span class="s2">&quot;Friday&quot;</span><span class="p">)</span>

<span class="n">print_friday_message</span><span class="p">()</span>
</pre></div>


<div class="codehilite"><pre><span></span>---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
&lt;ipython-input-1-4be1945adbe2&gt; in &lt;module&gt;()
     14     print_message(&quot;Friday&quot;)
     15
---&gt; 16 print_friday_message()

&lt;ipython-input-1-4be1945adbe2&gt; in print_friday_message()
     12
     13 def print_friday_message():
---&gt; 14     print_message(&quot;Friday&quot;)
     15
     16 print_friday_message()

&lt;ipython-input-1-4be1945adbe2&gt; in print_message(day)
      9         &quot;sunday&quot;: &quot;Aw, the weekend is almost over.&quot;
     10     }
---&gt; 11     print(messages[day])
     12
     13 def print_friday_message():

KeyError: &#39;Friday&#39;
</pre></div>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<ol>
<li>3 levels</li>
<li><code>print_message</code></li>
<li>11</li>
<li><code>KeyError</code></li>
<li>There isn't really a message; you're supposed to infer that <code>Friday</code> is not a key in <code>messages</code>.</li>
</ol>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Identifying Syntax Errors</h2>
</div>


<div class="panel-body">

<ol>
<li>Read the code below, and (without running it) try to identify what the errors are.</li>
<li>Run the code, and read the error message. Is it a <code>SyntaxError</code> or an <code>IndentationError</code>?</li>
<li>Fix the error.</li>
<li>Repeat steps 2 and 3, until you have fixed all the errors.</li>
</ol>
<div class="codehilite"><pre><span></span><span class="k">def</span> <span class="nf">another_function</span>
  <span class="k">print</span><span class="p">(</span><span class="s2">&quot;Syntax errors are annoying.&quot;</span><span class="p">)</span>
   <span class="k">print</span><span class="p">(</span><span class="s2">&quot;But at least python tells us about them!&quot;</span><span class="p">)</span>
  <span class="k">print</span><span class="p">(</span><span class="s2">&quot;So they are usually not too hard to fix.&quot;</span><span class="p">)</span>
</pre></div>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p><code>SyntaxError</code> for missing <code>():</code> at end of first line,
ndentationError` for mismatch between second and third lines.
A fixed version is:</p>

</div>

</section>



{:.input_area}
```python
def another_function():
    print("Syntax errors are annoying.")
    print("But at least python tells us about them!")
    print("So they are usually not too hard to fix.")
```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Identifying Variable Name Errors</h2>
</div>


<div class="panel-body">

<ol>
<li>Read the code below, and (without running it) try to identify what the errors are.</li>
<li>Run the code, and read the error message.
   What type of <code>NameError</code> do you think this is?
   In other words, is it a string with no quotes,
   a misspelled variable,
   or a variable that should have been defined but was not?</li>
<li>Fix the error.</li>
<li>Repeat steps 2 and 3, until you have fixed all the errors.</li>
</ol>
<div class="codehilite"><pre><span></span><span class="k">for</span> <span class="n">number</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
    <span class="c1"># use a if the number is a multiple of 3, otherwise use b</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">Number</span> <span class="o">%</span> <span class="mi">3</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">message</span> <span class="o">=</span> <span class="n">message</span> <span class="o">+</span> <span class="n">a</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">message</span> <span class="o">=</span> <span class="n">message</span> <span class="o">+</span> <span class="s2">&quot;b&quot;</span>
<span class="k">print</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</pre></div>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>3 <code>NameError</code>s for:</p>
<ul>
<li><code>number</code> being misspelled</li>
<li><code>message</code> not defined</li>
<li><code>a</code> not being in quotes.</li>
</ul>
<p>Fixed version:</p>

</div>

</section>



{:.input_area}
```python
message = ""
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)
```

{:.output_stream}
```
abbabbabba

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Identifying Index Errors</h2>
</div>


<div class="panel-body">

<ol>
<li>Read the code below, and (without running it) try to identify what the errors are.</li>
<li>Run the code, and read the error message. What type of error is it?</li>
<li>Fix the error.</li>
</ol>
<div class="codehilite"><pre><span></span><span class="n">seasons</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Spring&#39;</span><span class="p">,</span> <span class="s1">&#39;Summer&#39;</span><span class="p">,</span> <span class="s1">&#39;Fall&#39;</span><span class="p">,</span> <span class="s1">&#39;Winter&#39;</span><span class="p">]</span>
<span class="k">print</span><span class="p">(</span><span class="s1">&#39;My favorite season is &#39;</span><span class="p">,</span> <span class="n">seasons</span><span class="p">[</span><span class="mi">4</span><span class="p">])</span>
</pre></div>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p><code>IndexError</code>; the last entry is <code>seasons[3]</code>, so <code>seasons[4]</code> doesn't make sense.
A fixed version is:</p>

</div>

</section>



{:.input_area}
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[-1])
```

{:.output_stream}
```
My favorite season is  Winter

```
