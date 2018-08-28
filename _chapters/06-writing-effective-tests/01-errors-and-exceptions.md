---
interact_link: 06-writing-effective-tests/01-errors-and-exceptions.ipynb
title: 'Errors And Exceptions'
permalink: 'chapters/06-writing-effective-tests/01-errors-and-exceptions'
previouschapter:
  url: 
  title: 'Writing Effective Tests'
nextchapter:
  url: chapters/06-writing-effective-tests/02-explicit-exceptions
  title: 'Explicit Exceptions'
redirect_from:
  - 'chapters/06-writing-effective-tests/01-errors-and-exceptions'
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
<h2 class="fa fa-thumb-tack"> Long Tracebacks</h2>
</div>


<div class="panel-body">


Sometimes, you might see a traceback that is very long -- sometimes they might even be 20 levels deep!
This can make it seem like something horrible happened,
but really it just means that your program called many functions before it ran into the error.
Most of the time,
you can just pay attention to the bottom-most level,
which is the actual place where the error occurred.
{: .callout}

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

Both `SyntaxError` and `IndentationError` indicate a problem with the syntax of your program,
but an `IndentationError` is more specific:
it *always* means that there is a problem with how your code is indented.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2 class="fa fa-thumb-tack"> Tabs and Spaces</h2>
</div>


<div class="panel-body">

Some indentation errors are harder to spot than others.
In particular, mixing spaces and tabs can be difficult to spot
because they are both whitespace.
In the example below, the first two lines in the body of the function
`some_function` are indented with tabs, while the third line &mdash; with spaces.
If you're working in a Jupyter notebook, be sure to copy and paste this example
rather than trying to type it in manually because Jupyter automatically replaces
tabs with spaces.

```python
def some_function():
	msg = "hello, world!"
	print(msg)
        return msg
```

Visually it is impossible to spot the error.
Fortunately, Python does not allow you to mix tabs and spaces.

```
  File "<ipython-input-5-653b36fbcd41>", line 4
    return msg
              ^
TabError: inconsistent use of tabs and spaces in indentation
```

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

The second is that you just forgot to create the variable before using it.
In the following example,
`count` should have been defined (e.g., with `count = 0`) before the for loop:


{:.input_area}
```python
for number in range(10):
    count = count + number
print("The count is:", count)
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

These are the most common errors with files,
though many others exist.
If you get an error that you've never seen before,
searching the Internet for that error type
often reveals common reasons why you might get that error.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> Reading Error Messages</h2>
</div>


<div class="panel-body">

Read the python code and the resulting traceback below, and answer the following questions:

1.  How many levels does the traceback have?
2.  What is the function name where the error occurred?
3.  On which line number in this function did the error occurr?
4.  What is the type of error?
5.  What is the error message?

```python
# This code has an intentional error. Do not type it directly;
# use it for reference to understand the error message below.
def print_message(day):
    messages = {
        "monday": "Hello, world!",
        "tuesday": "Today is tuesday!",
        "wednesday": "It is the middle of the week.",
        "thursday": "Today is Donnerstag in German!",
        "friday": "Last day of the week!",
        "saturday": "Hooray for the weekend!",
        "sunday": "Aw, the weekend is almost over."
    }
    print(messages[day])

def print_friday_message():
    print_message("Friday")

print_friday_message()
```

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-1-4be1945adbe2> in <module>()
     14     print_message("Friday")
     15
---> 16 print_friday_message()

<ipython-input-1-4be1945adbe2> in print_friday_message()
     12
     13 def print_friday_message():
---> 14     print_message("Friday")
     15
     16 print_friday_message()

<ipython-input-1-4be1945adbe2> in print_message(day)
      9         "sunday": "Aw, the weekend is almost over."
     10     }
---> 11     print(messages[day])
     12
     13 def print_friday_message():

KeyError: 'Friday'
```

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


1. 3 levels
2. `print_message`
3. 11
4. `KeyError`
5. There isn't really a message; you're supposed to infer that `Friday` is not a key in `messages`.

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> Identifying Syntax Errors</h2>
</div>


<div class="panel-body">

1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the code, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.

```python
def another_function
  print("Syntax errors are annoying.")
   print("But at least python tells us about them!")
  print("So they are usually not too hard to fix.")
```

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">

`SyntaxError` for missing `():` at end of first line,
ndentationError` for mismatch between second and third lines.
A fixed version is:

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
<h2 class="fa fa-pencil"> Identifying Variable Name Errors</h2>
</div>


<div class="panel-body">


1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the code, and read the error message.
   What type of `NameError` do you think this is?
   In other words, is it a string with no quotes,
   a misspelled variable,
   or a variable that should have been defined but was not?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.

```python
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + "b"
print(message)
```

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


3 `NameError`s for `number` being misspelled, for `message` not defined, and for `a` not being in quotes.
Fixed version:

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


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2 class="fa fa-pencil"> Identifying Index Errors</h2>
</div>


<div class="panel-body">


1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the code, and read the error message. What type of error is it?
3. Fix the error.

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])
```

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2 class="fa fa-eye"> Solution</h2>
</div>


<div class="panel-body">


`IndexError`; the last entry is `seasons[3]`, so `seasons[4]` doesn't make sense.
A fixed version is:

</div>

</section>



{:.input_area}
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[-1])
```
