---
interact_link: 03-fundamentals-of-python-part-1/04-files.ipynb
title: 'Files'
permalink: 'chapters/03-fundamentals-of-python-part-1/04-files'
previouschapter:
  url: chapters/03-fundamentals-of-python-part-1/03-lists
  title: 'Lists'
nextchapter:
  url: chapters/03-fundamentals-of-python-part-1/05-cond
  title: 'Cond'
redirect_from:
  - 'chapters/03-fundamentals-of-python-part-1/04-files'
---

# Analyzing Data from Multiple Files

We now have almost everything we need to process all our data files.
The only thing that's missing is a library with a rather unpleasant name:


{:.input_area}
```python
import glob
```

The `glob` library contains a function, also called `glob`,
that finds files and directories whose names match a pattern.
We provide those patterns as strings:
the character `*` matches zero or more characters,
while `?` matches any one character.
We can use this to get the names of all the CSV files in the current directory:


{:.input_area}
```python
print(glob.glob('inflammation*.csv'))
```

{:.output_stream}
```
['inflammation-01.csv', 'inflammation-06.csv', 'inflammation-04.csv', 'inflammation-03.csv', 'inflammation-05.csv', 'inflammation-07.csv', 'inflammation-02.csv', 'inflammation-08.csv', 'inflammation-12.csv', 'inflammation-09.csv', 'inflammation-11.csv', 'inflammation-10.csv']

```

As these examples show,
`glob.glob`'s result is a list of file and directory paths in arbitrary order.
This means we can loop over it
to do something with each filename in turn.
In our case,
the "something" we want to do is generate a set of plots for each file in our inflammation dataset.
If we want to start by analyzing just the first three files in alphabetical order, we can use the
`sorted` built-in function to generate a new sorted list from the `glob.glob` output:


{:.input_area}
```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
```


{:.input_area}
```python
filenames = sorted(glob.glob('inflammation*.csv'))
filenames = filenames[0:3]
for f in filenames:
    print(f)

    data = np.loadtxt(fname=f, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()
```

{:.output_stream}
```
inflammation-01.csv

```


![png](../../images/chapters/03-fundamentals-of-python-part-1/04-files_7_1.png)


{:.output_stream}
```
inflammation-02.csv

```


![png](../../images/chapters/03-fundamentals-of-python-part-1/04-files_7_3.png)


{:.output_stream}
```
inflammation-03.csv

```


![png](../../images/chapters/03-fundamentals-of-python-part-1/04-files_7_5.png)


Sure enough,
the maxima of the first two data sets show exactly the same ramp as the first,
and their minima show the same staircase structure;
a different situation has been revealed in the third dataset,
where the maxima are a bit less regular, but the minima are consistently zero.

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Challenge: Plotting Differences</h2>
<p>Plot the difference between the average of the first dataset
and the average of the second dataset,
i.e., the difference between the leftmost plot of the first two figures.</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2></div>


{:.input_area}
```python
import glob
import numpy as np
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('inflammation*.csv'))

data0 = np.loadtxt(fname=filenames[0], delimiter=',')
data1 = np.loadtxt(fname=filenames[1], delimiter=',')

fig = plt.figure(figsize=(10.0, 3.0))

plt.ylabel('Difference in average')
plt.plot(data0.mean(axis=0) - data1.mean(axis=0))

fig.tight_layout()
plt.show()
```


![png](../../images/chapters/03-fundamentals-of-python-part-1/04-files_11_0.png)


<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #eec275, #f0c883); border-color: #eec275; margin-top: 0px; margin-left: -5px;'> &#9998; Challenge: Generate Composite Statistics</h2>
<p>Use each of the files once to generate a dataset containing values averaged over all patients:</p></div>


{:.input_area}
```python
filenames = glob.glob('inflammation*.csv')
composite_data = numpy.zeros((60,40))
for f in filenames:
    # sum each new file's data into composite_data as it's read
    #
# and then divide the composite_data by number of samples
composite_data /= len(filenames)
```


{:.output_traceback_line}
```
  File "<ipython-input-5-82a1887129c2>", line 7
    composite_data /= len(filenames)
                 ^
IndentationError: expected an indented block

```


Then use pyplot to generate average, max, and min for all patients.

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #ded4b9; padding-bottom: 5px;'><h2 style='padding-top: 5px; padding-bottom: 5px; font-size: 20px; background: linear-gradient(to bottom, #ded4b9, #e1d8c0); border-color: #ded4b9; margin-top: 0px; margin-left: -5px;'> &#128065; Solution</h2></div>


{:.input_area}
```python
import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('inflammation*.csv')
composite_data = np.zeros((60,40))

for f in filenames:
    data = np.loadtxt(fname = f, delimiter=',')
    composite_data += data

composite_data/=len(filenames)

fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(np.mean(composite_data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(composite_data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(composite_data, axis=0))

fig.tight_layout()

plt.show()
```


![png](../../images/chapters/03-fundamentals-of-python-part-1/04-files_16_0.png)

