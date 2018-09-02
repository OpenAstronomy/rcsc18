---
interact_link: 03-fundamentals-of-python/03-lists_instructor.ipynb
title: 'Lists'
permalink: 'chapters/03-fundamentals-of-python/03-lists'
previouschapter:
  url: chapters/03-fundamentals-of-python/02-repeating-actions
  title: 'Repeating Actions'
nextchapter:
  url: chapters/03-fundamentals-of-python/04-processing-files
  title: 'Processing Files'
redirect_from:
  - 'chapters/03-fundamentals-of-python/03-lists'
---

# Storing Multiple Values in Lists

Just as a `for` loop is a way to do operations many times,
a list is a way to store many values.
Unlike NumPy arrays,
lists are built into the language (so we don't have to load a library
to use them).
We create a list by putting values inside square brackets and separating the values with commas:


{:.input_area}
```python
odds = [1, 3, 5, 7]
print('odds are:', odds)
```

{:.output_stream}
```
odds are: [1, 3, 5, 7]

```

We select individual elements from lists by indexing them:


{:.input_area}
```python
print('first and last:', odds[0], odds[-1])
```

{:.output_stream}
```
first and last: 1 7

```

and if we loop over a list,
the loop variable is assigned elements one at a time:


{:.input_area}
```python
for number in odds:
    print(number)
```

{:.output_stream}
```
1
3
5
7

```

There is one important difference between lists and strings:
we can change the values in a list,
but we cannot change individual characters in a string.
For example:


{:.input_area}
```python
names = ['Curie', 'Darwing', 'Turing']  # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin'  # correct the name
print('final value of names:', names)
```

{:.output_stream}
```
names is originally: ['Curie', 'Darwing', 'Turing']
final value of names: ['Curie', 'Darwin', 'Turing']

```

works, but:


{:.input_area}
```python
name = 'Darwin'
name[0] = 'd'
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
<ipython-input-5-9030064e45ad> in <module>()
      1 name = 'Darwin'
----> 2 name[0] = 'd'

```

{:.output_traceback_line}
```
TypeError: 'str' object does not support item assignment
```


does not.

## Ch-Ch-Ch-Ch-Changes

Data which can be modified in place is called mutable,
while data which cannot be modified is called immutable.
Strings and numbers are immutable. This does not mean that variables with string or number values
are constants, but when we want to change the value of a string or number variable, we can only
replace the old value with a completely new value.
Lists and arrays, on the other hand, are mutable: we can modify them after they have been
created. We can change individual elements, append new elements, or reorder the whole list. For
some operations, like sorting, we can choose whether to use a function that modifies the data
in-place or a function that returns a modified copy and leaves the original unchanged.
Be careful when modifying data in-place. If two variables refer to the same list, and you modify
the list value, it will change for both variables!


{:.input_area}
```python
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = salsa        # <-- my_salsa and salsa point to the *same* list data in memory
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', my_salsa)
```

{:.output_stream}
```
Ingredients in my salsa: ['hot peppers', 'onions', 'cilantro', 'tomatoes']

```

If you want variables with mutable values to be independent, you
must make a copy of the value when you assign it.


{:.input_area}
```python
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = list(salsa)        # <-- makes a *copy* of the list
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', my_salsa)
```

{:.output_stream}
```
Ingredients in my salsa: ['peppers', 'onions', 'cilantro', 'tomatoes']

```

Because of pitfalls like this, code which modifies data in place can be more difficult to
understand. However, it is often far more efficient to modify a large data structure in place
than to create a modified copy for every small change. You should consider both of these aspects
when writing your code.

## Nested Lists
Since lists can contain any Python variable, it can even contain other lists.
For example, we could represent the products in the shelves of a small grocery shop:



{:.input_area}
```python
x = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
```

Here is a visual example of how indexing a list of lists `x` works:
[![The first element of a list. Adapted from @hadleywickham.](https://pbs.twimg.com/media/CO2_qPVWsAAErbv.png:large)](https://twitter.com/hadleywickham/status/643381054758363136)

Using the previously declared list `x`, these would be the results of the
index operations shown in the image:

*Thanks to [Hadley Wickham](https://twitter.com/hadleywickham/status/643381054758363136) for the image above.*


{:.input_area}
```python
print([x[0]])
```

{:.output_stream}
```
[['pepper', 'zucchini', 'onion']]

```


{:.input_area}
```python
print(x[0])
```

{:.output_stream}
```
['pepper', 'zucchini', 'onion']

```


{:.input_area}
```python
print(x[0][0])
```

{:.output_stream}
```
pepper

```

## Heterogeneous Lists

Lists in Python can contain elements of different types. Example:
```python
sample_ages = [10, 12.5, 'Unknown']
```


There are many ways to change the contents of lists besides assigning new values to
individual elements:


{:.input_area}
```python
odds.append(11)
print('odds after adding a value:', odds)
```

{:.output_stream}
```
odds after adding a value: [1, 3, 5, 7, 11]

```


{:.input_area}
```python
del odds[0]
print('odds after removing the first element:', odds)
```

{:.output_stream}
```
odds after removing the first element: [3, 5, 7, 11]

```


{:.input_area}
```python
odds.reverse()
print('odds after reversing:', odds)
```

{:.output_stream}
```
odds after reversing: [11, 7, 5, 3]

```

While modifying in place, it is useful to remember that Python treats lists in a slightly
counter-intuitive way.

If we make a list and (attempt to) copy it then modify in place, we can cause all sorts of trouble:


{:.input_area}
```python
odds = [1, 3, 5, 7]
primes = odds
primes.append(2)
print('primes:', primes)
print('odds:', odds)
```

{:.output_stream}
```
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7, 2]

```

This is because Python stores a list in memory, and then can use multiple names to refer to the
same list. If all we want to do is copy a (simple) list, we can use the `list` function, so we do
not modify a list we did not mean to:


{:.input_area}
```python
odds = [1, 3, 5, 7]
primes = list(odds)
primes.append(2)
print('primes:', primes)
print('odds:', odds)
```

{:.output_stream}
```
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7]

```

This is different from how variables worked in lesson 1, and more similar to how a spreadsheet
works.


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge: Turn a String Into a List</h2>
</div>


<div class="panel-body">

<p>Use a for-loop to convert the string "hello" into a list of letters:</p>
<div class="codehilite"><pre><span></span><span class="p">[</span><span class="s2">&quot;h&quot;</span><span class="p">,</span> <span class="s2">&quot;e&quot;</span><span class="p">,</span> <span class="s2">&quot;l&quot;</span><span class="p">,</span> <span class="s2">&quot;l&quot;</span><span class="p">,</span> <span class="s2">&quot;o&quot;</span><span class="p">]</span>
</pre></div>


<p>Hint: You can create an empty list like this:</p>
<div class="codehilite"><pre><span></span><span class="n">my_list</span> <span class="o">=</span> <span class="p">[]</span>
</pre></div>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>

</section>



{:.input_area}
```python
my_list = []
for char in "hello":
    my_list.append(char)
print(my_list)
```

{:.output_stream}
```
['h', 'e', 'l', 'l', 'o']

```

Subsets of lists and strings can be accessed by specifying ranges of values in brackets,
similar to how we accessed ranges of positions in a NumPy array.
This is commonly referred to as "slicing" the list/string.


{:.input_area}
```python
binomial_name = "Drosophila melanogaster"
group = binomial_name[0:10]
print("group:", group)

species = binomial_name[11:24]
print("species:", species)

chromosomes = ["X", "Y", "2", "3", "4"]
autosomes = chromosomes[2:5]
print("autosomes:", autosomes)

last = chromosomes[-1]
print("last:", last)
```

{:.output_stream}
```
group: Drosophila
species: melanogaster
autosomes: ['2', '3', '4']
last: 4

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge: Slicing From the End</h2>
</div>


<div class="panel-body">

<p>Use slicing to access only the last four characters of the following string and the last four entries of the following list.</p>

</div>

</section>



{:.input_area}
```python
string_for_slicing = "Observation date: 02-Feb-2013"
list_for_slicing = [["fluorine", "F"], ["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
```

Would your solution work regardless of whether you knew beforehand
the length of the string or list
(e.g. if you wanted to apply the solution to a set of lists of different lengths)?
If not, try to change your approach to make it more robust.


<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>Use negative indices to count elements from the end of a container (such as list or string):</p>

</div>

</section>



{:.input_area}
```python
string_for_slicing[-4:]
list_for_slicing[-4:]
```




{:.output_data_text}
```
[['chlorine', 'Cl'], ['bromine', 'Br'], ['iodine', 'I'], ['astatine', 'At']]
```



## Non-Continuous Slices
So far we've seen how to use slicing to take single blocks
of successive entries from a sequence.
But what if we want to take a subset of entries
that aren't next to each other in the sequence?

You can achieve this by providing a third argument
to the range within the brackets, called the _step size_.
The example below shows how you can take every third entry in a list:



{:.input_area}
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[0:12:3]
print("subset", subset)
```

{:.output_stream}
```
subset [2, 7, 17, 29]

```

Notice that the slice taken begins with the first entry in the range,
followed by entries taken at equally-spaced intervals (the steps) thereafter.
If you wanted to begin the subset with the third entry,
you would need to specify that as the starting point of the sliced range:


{:.input_area}
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[2:12:3]
print("subset", subset)
```

{:.output_stream}
```
subset [5, 13, 23, 37]

```


<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge:</h2>
</div>


<div class="panel-body">

<p>Use the step size argument to create a new string
that contains only every other character in the string
"In an octopus's garden in the shade"</p>

</div>

</section>



{:.input_area}
```python
beatles = "In an octopus's garden in the shade"
```


<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>


<div class="panel-body">

<p>To obtain every other character you need to provide a slice with the step
size of 2:</p>

</div>

</section>



{:.input_area}
```python
beatles[0:35:2]
```




{:.output_data_text}
```
'I notpssgre ntesae'
```



You can also leave out the beginning and end of the slice to take the whole string
and provide only the step argument to go every second
element:


{:.input_area}
```python
beatles[::2]
```




{:.output_data_text}
```
'I notpssgre ntesae'
```



If you want to take a slice from the beginning of a sequence, you can omit the first index in the
range:


{:.input_area}
```python
date = "Monday 4 January 2016"
day = date[0:6]
print("Using 0 to begin range:", day)
day = date[:6]
print("Omitting beginning index:", day)
```

{:.output_stream}
```
Using 0 to begin range: Monday
Omitting beginning index: Monday

```

And similarly, you can omit the ending index in the range to take a slice to the very end of the
sequence:


{:.input_area}
```python
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
sond = months[8:12]
print("With known last position:", sond)
sond = months[8:len(months)]
print("Using len() to get last entry:", sond)
sond = months[8:]
print("Omitting ending index:", sond)
```

{:.output_stream}
```
With known last position: ['sep', 'oct', 'nov', 'dec']
Using len() to get last entry: ['sep', 'oct', 'nov', 'dec']
Omitting ending index: ['sep', 'oct', 'nov', 'dec']

```

## Overloading

`+` usually means addition, but when used on strings or lists, it means "concatenate".
Given that, what do you think the multiplication operator `*` does on lists?
In particular, what will be the output of the following code?

```python
counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)
```

1.  `[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]`
2.  `[4, 8, 12, 16, 20]`
3.  `[[2, 4, 6, 8, 10],[2, 4, 6, 8, 10]]`
4.  `[2, 4, 6, 8, 10, 4, 8, 12, 16, 20]`

The technical term for this is *operator overloading*:
a single operator, like `+` or `*`,
can do different things depending on what it's applied to.

## Solution

The multiplication operator `*` used on a list replicates elements of the list and concatenates
them together:


{:.input_area}
```python
counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)
```

{:.output_stream}
```
[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]

```

It's equivalent to:


{:.input_area}
```python
counts + counts
```




{:.output_data_text}
```
[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]
```



---
The material in this notebook is derived from the Software Carpentry lessons
&copy; [Software Carpentry](http://software-carpentry.org/) under the terms
of the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
