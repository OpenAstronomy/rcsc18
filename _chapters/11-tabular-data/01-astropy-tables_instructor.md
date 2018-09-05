---
interact_link: 11-tabular-data/01-astropy-tables_instructor.ipynb
title: 'Astropy Tables'
permalink: 'chapters/11-tabular-data/01-astropy-tables'
previouschapter:
  url: 
  title: 'Tabular Data'
nextchapter:
  url: 
  title: 'Images and Visualisation'
redirect_from:
  - 'chapters/11-tabular-data/01-astropy-tables'
---

# Astropy: Tables


<section class="objectives panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-certificate"></span> Objectives</h2>
</div>


<div class="panel-body">

<ul>
<li>Create tables</li>
<li>Access data in tables</li>
<li>Combining tables</li>
<li>Aggregation</li>
<li>Masking</li>
<li>Reading/writing</li>
</ul>

</div>

</section>


## Documentation

For more information about the features presented below, you can read the
[astropy.table](http://docs.astropy.org/en/stable/table/index.html) docs.

## Creating tables


{:.input_area}
```python
import numpy as np
from astropy.table import Table
```


{:.input_area}
```python
# Creating a table from scratch
t1 = Table()
t1['name'] = ['source 1', 'source 2', 'source 3']
t1['flux'] = [1.2, 2.2, 3.1]
```


{:.input_area}
```python
# Looking at the table
t1
```




<div markdown="0">
<i>Table length=3</i>
<table id="table140152145569328" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>flux</th></tr></thead>
<thead><tr><th>str8</th><th>float64</th></tr></thead>
<tr><td>source 1</td><td>1.2</td></tr>
<tr><td>source 2</td><td>2.2</td></tr>
<tr><td>source 3</td><td>3.1</td></tr>
</table>
</div>




{:.input_area}
```python
# Adding a column
t1['size'] = [1,5,4]
t1
```




<div markdown="0">
<i>Table length=3</i>
<table id="table140152145569328" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>flux</th><th>size</th></tr></thead>
<thead><tr><th>str8</th><th>float64</th><th>int64</th></tr></thead>
<tr><td>source 1</td><td>1.2</td><td>1</td></tr>
<tr><td>source 2</td><td>2.2</td><td>5</td></tr>
<tr><td>source 3</td><td>3.1</td><td>4</td></tr>
</table>
</div>




{:.input_area}
```python
# Accessing a column
t1['size']
```




<div markdown="0">
&lt;Column name=&apos;size&apos; dtype=&apos;int64&apos; length=3&gt;
<table>
<tr><td>1</td></tr>
<tr><td>5</td></tr>
<tr><td>4</td></tr>
</table>
</div>




{:.input_area}
```python
# Converting to a Numpy array
np.array(t1['size'])
```




{:.output_data_text}
```
array([1, 5, 4])
```




{:.input_area}
```python
# Accessing a cell
t1['size'][0]
```




{:.output_data_text}
```
1
```




{:.input_area}
```python
# Accessing a row
t1[0]
```




<div markdown="0">
<i>Row index=0</i>
<table id="table140152145569328">
<thead><tr><th>name</th><th>flux</th><th>size</th></tr></thead>
<thead><tr><th>str8</th><th>float64</th><th>int64</th></tr></thead>
<tr><td>source 1</td><td>1.2</td><td>1</td></tr>
</table>
</div>



## Units in tables


{:.input_area}
```python
# Set unit on column
t1['size'].unit = 'cm'
t1
```




<div markdown="0">
<i>Table length=3</i>
<table id="table140152145569328" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>flux</th><th>size</th></tr></thead>
<thead><tr><th></th><th></th><th>cm</th></tr></thead>
<thead><tr><th>str8</th><th>float64</th><th>int64</th></tr></thead>
<tr><td>source 1</td><td>1.2</td><td>1</td></tr>
<tr><td>source 2</td><td>2.2</td><td>5</td></tr>
<tr><td>source 3</td><td>3.1</td><td>4</td></tr>
</table>
</div>



Some unitful operations will then work:


{:.input_area}
```python
t1['size'].to('m')
```




$[0.01,~0.05,~0.04] \; \mathrm{m}$



However, you may run into unexpected behavior, so if you are planning on using table columns as Quantities, we recommend that you use the ``QTable`` class:


{:.input_area}
```python
type(t1['size'])
```




{:.output_data_text}
```
astropy.table.column.Column
```




{:.input_area}
```python
from astropy.table import QTable
qt1 = QTable(t1)
type(qt1['size'])
```




{:.output_data_text}
```
astropy.units.quantity.Quantity
```




<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge</h2>
</div>


<div class="panel-body">

<ol>
<li>Make a table that contains three columns: <code>spectral type</code>, <code>temperature</code>, and <code>radius</code>, and incude 5 rows with fake data (or real data if you like, for example from <a href="http://www.atlasoftheuniverse.com/startype.html">here</a>). Try including units on the columns that can have them.</li>
<li>Find the mean temperature and the maximum radius</li>
<li>Try and find out how to add and remove rows</li>
<li>Add a new column which gives the luminosity (using $L=4\pi R^2 \sigma T^4$)</li>
</ol>

</div>

</section>



{:.input_area}
```python
#1
from astropy import units as u
t = QTable()
t['spectral type'] = ['O5', 'B5', 'A5', 'F5', 'G5']
t['radius'] = [12, 3.9, 1.7, 1.3, 0.92] * u.R_sun
t['temperature'] = [45000, 15000, 8200, 6400, 5700] * u.K
t
```




<div markdown="0">
<i>QTable length=5</i>
<table id="table140152142724008" class="table-striped table-bordered table-condensed">
<thead><tr><th>spectral type</th><th>radius</th><th>temperature</th></tr></thead>
<thead><tr><th></th><th>solRad</th><th>K</th></tr></thead>
<thead><tr><th>str2</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>O5</td><td>12.0</td><td>45000.0</td></tr>
<tr><td>B5</td><td>3.9</td><td>15000.0</td></tr>
<tr><td>A5</td><td>1.7</td><td>8200.0</td></tr>
<tr><td>F5</td><td>1.3</td><td>6400.0</td></tr>
<tr><td>G5</td><td>0.92</td><td>5700.0</td></tr>
</table>
</div>




{:.input_area}
```python
#2
print('Mean temperature:', np.mean(t['temperature']))
print('Maximum radius:', np.mean(t['radius']))
```

{:.output_stream}
```
Mean temperature: 16060.0 K
Maximum radius: 3.964000000000001 solRad

```


{:.input_area}
```python
#3
t.add_row({'spectral type': 'K5',
           'temperature': 4300 * u.K,
           'radius': 0.72 * u.R_sun})
t.remove_row(0)
t
```




<div markdown="0">
<i>QTable length=5</i>
<table id="table140152142724008" class="table-striped table-bordered table-condensed">
<thead><tr><th>spectral type</th><th>radius</th><th>temperature</th></tr></thead>
<thead><tr><th></th><th>solRad</th><th>K</th></tr></thead>
<thead><tr><th>str2</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>B5</td><td>3.9</td><td>15000.0</td></tr>
<tr><td>A5</td><td>1.7</td><td>8200.0</td></tr>
<tr><td>F5</td><td>1.3</td><td>6400.0</td></tr>
<tr><td>G5</td><td>0.92</td><td>5700.0</td></tr>
<tr><td>K5</td><td>0.72</td><td>4300.0</td></tr>
</table>
</div>




{:.input_area}
```python
#4
from numpy import pi
from astropy.constants import sigma_sb
t['luminosity'] = (4 * pi * t['radius'] ** 2 * sigma_sb * t['temperature'] ** 4).to(u.L_sun)
t
```




<div markdown="0">
<i>QTable length=5</i>
<table id="table140152142724008" class="table-striped table-bordered table-condensed">
<thead><tr><th>spectral type</th><th>radius</th><th>temperature</th><th>luminosity</th></tr></thead>
<thead><tr><th></th><th>solRad</th><th>K</th><th>solLum</th></tr></thead>
<thead><tr><th>str2</th><th>float64</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>B5</td><td>3.9</td><td>15000.0</td><td>693.7250235023215</td></tr>
<tr><td>A5</td><td>1.7</td><td>8200.0</td><td>11.7718945281512</td></tr>
<tr><td>F5</td><td>1.3</td><td>6400.0</td><td>2.554463553120115</td></tr>
<tr><td>G5</td><td>0.92</td><td>5700.0</td><td>0.8049486705065919</td></tr>
<tr><td>K5</td><td>0.72</td><td>4300.0</td><td>0.15967316182594046</td></tr>
</table>
</div>



## Iterating over tables

It is possible to iterate over rows or over columns. To iterate over rows, simply iterate over the table itself:


{:.input_area}
```python
for row in t1:
    print(row)
```

{:.output_stream}
```
  name   flux size
               cm 
-------- ---- ----
source 1  1.2    1
  name   flux size
               cm 
-------- ---- ----
source 2  2.2    5
  name   flux size
               cm 
-------- ---- ----
source 3  3.1    4

```

Rows can act like dictionaries, so you can access specific columns from a row:


{:.input_area}
```python
for row in t1:
    print(row['name'])
```

{:.output_stream}
```
source 1
source 2
source 3

```

Iterating over columns is also easy:


{:.input_area}
```python
for colname in t1.columns:
    column = t1[colname]
    print(column)
```

{:.output_stream}
```
  name  
--------
source 1
source 2
source 3
flux
----
 1.2
 2.2
 3.1
size
 cm 
----
   1
   5
   4

```

Accessing specific rows from a column object can also be done with the item notation:


{:.input_area}
```python
for colname in t1.columns:
    column = t1[colname]
    print(column[0])
```

{:.output_stream}
```
source 1
1.2
1

```

## Joining tables


{:.input_area}
```python
from astropy.table import join
```


{:.input_area}
```python
t2 = Table()
t2['name'] = ['source 1', 'source 3']
t2['flux2'] = [1,9]
```


{:.input_area}
```python
t3 = join(t1, t2, join_type='outer')
t3
```




<div markdown="0">
<i>Table masked=True length=3</i>
<table id="table140152142724624" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>flux</th><th>size</th><th>flux2</th></tr></thead>
<thead><tr><th></th><th></th><th>cm</th><th></th></tr></thead>
<thead><tr><th>str8</th><th>float64</th><th>int64</th><th>int64</th></tr></thead>
<tr><td>source 1</td><td>1.2</td><td>1</td><td>1</td></tr>
<tr><td>source 2</td><td>2.2</td><td>5</td><td>--</td></tr>
<tr><td>source 3</td><td>3.1</td><td>4</td><td>9</td></tr>
</table>
</div>




{:.input_area}
```python
np.mean(t3['flux2'])
```




{:.output_data_text}
```
5.0
```



## Masked tables


{:.input_area}
```python
t4 = Table(masked=True)
t4['name'] = ['source 1', 'source 2', 'source 3']
t4['flux'] = [1.2, 2.2, 3.1]
```


{:.input_area}
```python
t4['flux'].mask = [1,0,1]
t4
```




<div markdown="0">
<i>Table masked=True length=3</i>
<table id="table140152142763680" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>flux</th></tr></thead>
<thead><tr><th>str8</th><th>float64</th></tr></thead>
<tr><td>source 1</td><td>--</td></tr>
<tr><td>source 2</td><td>2.2</td></tr>
<tr><td>source 3</td><td>--</td></tr>
</table>
</div>



## Slicing

Tables can be sliced like Numpy arrays:


{:.input_area}
```python
obs = Table.read("""name    obs_date    mag_b  mag_v
                    M31     2012-01-02  17.0   17.5
                    M31     2012-01-02  17.1   17.4
                    M101    2012-01-02  15.1   13.5
                    M82     2012-02-14  16.2   14.5
                    M31     2012-02-14  16.9   17.3
                    M82     2012-02-14  15.2   15.5
                    M101    2012-02-14  15.0   13.6
                    M82     2012-03-26  15.7   16.5
                    M101    2012-03-26  15.1   13.5
                    M101    2012-03-26  14.8   14.3
                    """, format='ascii')
```


{:.input_area}
```python
obs[1:4]
```




<div markdown="0">
<i>Table length=3</i>
<table id="table140152142722832" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>obs_date</th><th>mag_b</th><th>mag_v</th></tr></thead>
<thead><tr><th>str4</th><th>str10</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>M31</td><td>2012-01-02</td><td>17.1</td><td>17.4</td></tr>
<tr><td>M101</td><td>2012-01-02</td><td>15.1</td><td>13.5</td></tr>
<tr><td>M82</td><td>2012-02-14</td><td>16.2</td><td>14.5</td></tr>
</table>
</div>




{:.input_area}
```python
obs[obs['mag_b'] > 16]
```




<div markdown="0">
<i>Table length=4</i>
<table id="table140152142764632" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>obs_date</th><th>mag_b</th><th>mag_v</th></tr></thead>
<thead><tr><th>str4</th><th>str10</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>M31</td><td>2012-01-02</td><td>17.0</td><td>17.5</td></tr>
<tr><td>M31</td><td>2012-01-02</td><td>17.1</td><td>17.4</td></tr>
<tr><td>M82</td><td>2012-02-14</td><td>16.2</td><td>14.5</td></tr>
<tr><td>M31</td><td>2012-02-14</td><td>16.9</td><td>17.3</td></tr>
</table>
</div>




{:.input_area}
```python
obs['mag_b', 'mag_v']
```




<div markdown="0">
<i>Table length=10</i>
<table id="table140152142764520" class="table-striped table-bordered table-condensed">
<thead><tr><th>mag_b</th><th>mag_v</th></tr></thead>
<thead><tr><th>float64</th><th>float64</th></tr></thead>
<tr><td>17.0</td><td>17.5</td></tr>
<tr><td>17.1</td><td>17.4</td></tr>
<tr><td>15.1</td><td>13.5</td></tr>
<tr><td>16.2</td><td>14.5</td></tr>
<tr><td>16.9</td><td>17.3</td></tr>
<tr><td>15.2</td><td>15.5</td></tr>
<tr><td>15.0</td><td>13.6</td></tr>
<tr><td>15.7</td><td>16.5</td></tr>
<tr><td>15.1</td><td>13.5</td></tr>
<tr><td>14.8</td><td>14.3</td></tr>
</table>
</div>




<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge</h2>
</div>


<div class="panel-body">

<p>Starting from the <code>obs</code> table:</p>
<ol>
<li>Make a new table that shows every other row, starting with the second row? (that is, the second, fourth, sixth, etc. rows).</li>
<li>Make a new table the only contains rows where <code>name</code> is <code>M31</code></li>
</ol>

</div>

</section>



{:.input_area}
```python
#1
subset1 = obs[1::2]
subset1
```




<div markdown="0">
<i>Table length=5</i>
<table id="table140152142765752" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>obs_date</th><th>mag_b</th><th>mag_v</th></tr></thead>
<thead><tr><th>str4</th><th>str10</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>M31</td><td>2012-01-02</td><td>17.1</td><td>17.4</td></tr>
<tr><td>M82</td><td>2012-02-14</td><td>16.2</td><td>14.5</td></tr>
<tr><td>M82</td><td>2012-02-14</td><td>15.2</td><td>15.5</td></tr>
<tr><td>M82</td><td>2012-03-26</td><td>15.7</td><td>16.5</td></tr>
<tr><td>M101</td><td>2012-03-26</td><td>14.8</td><td>14.3</td></tr>
</table>
</div>




{:.input_area}
```python
#2
subset2 = obs[obs['name'] == 'M31']
subset2
```




<div markdown="0">
<i>Table length=3</i>
<table id="table140152142764072" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>obs_date</th><th>mag_b</th><th>mag_v</th></tr></thead>
<thead><tr><th>str4</th><th>str10</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>M31</td><td>2012-01-02</td><td>17.0</td><td>17.5</td></tr>
<tr><td>M31</td><td>2012-01-02</td><td>17.1</td><td>17.4</td></tr>
<tr><td>M31</td><td>2012-02-14</td><td>16.9</td><td>17.3</td></tr>
</table>
</div>



## Grouping and Aggregation


{:.input_area}
```python
obs_by_name = obs.group_by('name')
```


{:.input_area}
```python
obs_by_name
```




<div markdown="0">
<i>Table length=10</i>
<table id="table140152142914224" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>obs_date</th><th>mag_b</th><th>mag_v</th></tr></thead>
<thead><tr><th>str4</th><th>str10</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>M101</td><td>2012-01-02</td><td>15.1</td><td>13.5</td></tr>
<tr><td>M101</td><td>2012-02-14</td><td>15.0</td><td>13.6</td></tr>
<tr><td>M101</td><td>2012-03-26</td><td>15.1</td><td>13.5</td></tr>
<tr><td>M101</td><td>2012-03-26</td><td>14.8</td><td>14.3</td></tr>
<tr><td>M31</td><td>2012-01-02</td><td>17.0</td><td>17.5</td></tr>
<tr><td>M31</td><td>2012-01-02</td><td>17.1</td><td>17.4</td></tr>
<tr><td>M31</td><td>2012-02-14</td><td>16.9</td><td>17.3</td></tr>
<tr><td>M82</td><td>2012-02-14</td><td>16.2</td><td>14.5</td></tr>
<tr><td>M82</td><td>2012-02-14</td><td>15.2</td><td>15.5</td></tr>
<tr><td>M82</td><td>2012-03-26</td><td>15.7</td><td>16.5</td></tr>
</table>
</div>




{:.input_area}
```python
for group in obs_by_name.groups:
    print(group)
    print("")
```

{:.output_stream}
```
name  obs_date  mag_b mag_v
---- ---------- ----- -----
M101 2012-01-02  15.1  13.5
M101 2012-02-14  15.0  13.6
M101 2012-03-26  15.1  13.5
M101 2012-03-26  14.8  14.3

name  obs_date  mag_b mag_v
---- ---------- ----- -----
 M31 2012-01-02  17.0  17.5
 M31 2012-01-02  17.1  17.4
 M31 2012-02-14  16.9  17.3

name  obs_date  mag_b mag_v
---- ---------- ----- -----
 M82 2012-02-14  16.2  14.5
 M82 2012-02-14  15.2  15.5
 M82 2012-03-26  15.7  16.5


```


{:.input_area}
```python
obs_by_name.groups.aggregate(np.mean)
```




<div markdown="0">
<i>Table length=3</i>
<table id="table140152142914336" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>mag_b</th><th>mag_v</th></tr></thead>
<thead><tr><th>str4</th><th>float64</th><th>float64</th></tr></thead>
<tr><td>M101</td><td>15.000000000000002</td><td>13.725000000000001</td></tr>
<tr><td>M31</td><td>17.0</td><td>17.400000000000002</td></tr>
<tr><td>M82</td><td>15.699999999999998</td><td>15.5</td></tr>
</table>
</div>



## Writing data


{:.input_area}
```python
obs.write('test.fits', overwrite=True)
```


{:.input_area}
```python
obs.write('test.vot', format='votable', overwrite=True)
```

## Reading data


{:.input_area}
```python
t4 = Table.read('2mass.tbl', format='ascii.ipac')
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
<ipython-input-39-18e675545f97> in <module>()
----> 1 t4 = Table.read('2mass.tbl', format='ascii.ipac')

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in read(cls, *args, **kwargs)
   2531         passed through to the underlying data reader (e.g. `~astropy.io.ascii.read`).
   2532         """
-> 2533         out = io_registry.read(cls, *args, **kwargs)
   2534         # For some readers (e.g., ascii.ecsv), the returned `out` class is not
   2535         # guaranteed to be the same as the desired output `cls`.  If so,

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/io/registry.py in read(cls, format, *args, **kwargs)
    515 
    516         reader = get_reader(format, cls)
--> 517         data = reader(*args, **kwargs)
    518 
    519         if not isinstance(data, cls):

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/io/ascii/connect.py in io_read(format, filename, **kwargs)
     35     from .ui import read
     36     format = re.sub(r'^ascii\.', '', format)
---> 37     return read(filename, format=format, **kwargs)
     38 
     39 

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/io/ascii/ui.py in read(table, guess, **kwargs)
    383                                              ' with fast (no guessing)'})
    384         else:
--> 385             dat = reader.read(table)
    386             _read_trace.append({'kwargs': new_kwargs,
    387                                 'Reader': reader.__class__,

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/io/ascii/core.py in read(self, table)
   1144 
   1145         # Get a list of the lines (rows) in the table
-> 1146         self.lines = self.inputter.get_lines(table)
   1147 
   1148         # Set self.data.data_lines to a slice of lines contain the data rows

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/io/ascii/core.py in get_lines(self, table)
    291                     ('\n' not in table + '' and '\r' not in table + '')):
    292                 with get_readable_fileobj(table,
--> 293                                           encoding=self.encoding) as fileobj:
    294                     table = fileobj.read()
    295             lines = table.splitlines()

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/contextlib.py in __enter__(self)
     79     def __enter__(self):
     80         try:
---> 81             return next(self.gen)
     82         except StopIteration:
     83             raise RuntimeError("generator didn't yield") from None

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/utils/data.py in get_readable_fileobj(name_or_obj, encoding, cache, show_progress, remote_timeout)
    191                 name_or_obj, cache=cache, show_progress=show_progress,
    192                 timeout=remote_timeout)
--> 193         fileobj = io.FileIO(name_or_obj, 'r')
    194         if is_url and not cache:
    195             delete_fds.append(fileobj)

```

{:.output_traceback_line}
```
FileNotFoundError: [Errno 2] No such file or directory: '2mass.tbl'
```



{:.input_area}
```python
t4
```




<div markdown="0">
<i>Table masked=True length=3</i>
<table id="table140152142763680" class="table-striped table-bordered table-condensed">
<thead><tr><th>name</th><th>flux</th></tr></thead>
<thead><tr><th>str8</th><th>float64</th></tr></thead>
<tr><td>source 1</td><td>--</td></tr>
<tr><td>source 2</td><td>2.2</td></tr>
<tr><td>source 3</td><td>--</td></tr>
</table>
</div>




<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Challenge</h2>
</div>


<div class="panel-body">

<p>Using the <code>t4</code> table above:</p>
<ol>
<li>
<p>Make a plot that shows <code>j_m</code>-<code>h_m</code> on the x-axis, and <code>h_m</code>-<code>k_m</code> on the y-axis</p>
</li>
<li>
<p>Make a new table that contains the subset of rows where the <code>j_snr</code>, <code>h_snr</code>, and <code>k_snr</code> columns, which give the signal-to-noise-ratio in the J, H, and K band, are greater than 10, and try and show these points in red in the plot you just made.</p>
</li>
<li>
<p>Make a new table (based on the full table) that contains only the RA, Dec, and the <code>j_m</code>, <code>h_m</code> and <code>k_m</code> columns, then try and write out this catalog into a format that you can read into another software package. For example, try and write out the catalog into CSV format, then read it into a spreadsheet software package (e.g. Excel, Google Docs, Numbers, OpenOffice). You may run into an issue at this point - if so, take a look at https://github.com/astropy/astropy/issues/7357 to see how to fix it.</p>
</li>
</ol>

</div>

</section>



{:.input_area}
```python
#1
import matplotlib.pyplot as plt
plt.scatter(t4['j_m'] - t4['h_m'], t4['h_m'] - t4['k_m'], )
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
KeyError                                  Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-41-cdf60162d075> in <module>()
      1 #1
      2 import matplotlib.pyplot as plt
----> 3 plt.scatter(t4['j_m'] - t4['h_m'], t4['h_m'] - t4['k_m'], )

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
   1220     def __getitem__(self, item):
   1221         if isinstance(item, str):
-> 1222             return self.columns[item]
   1223         elif isinstance(item, (int, np.integer)):
   1224             return self.Row(self, item)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
    104         """
    105         if isinstance(item, str):
--> 106             return OrderedDict.__getitem__(self, item)
    107         elif isinstance(item, (int, np.integer)):
    108             return self.values()[item]

```

{:.output_traceback_line}
```
KeyError: 'j_m'
```



{:.input_area}
```python
#2
subset = t4[(t4['j_snr'] > 10) & (t4['h_snr'] > 10) & (t4['k_snr'] > 10)]
subset
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
KeyError                                  Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-42-9b689e5db8db> in <module>()
      1 #2
----> 2 subset = t4[(t4['j_snr'] > 10) & (t4['h_snr'] > 10) & (t4['k_snr'] > 10)]
      3 subset

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
   1220     def __getitem__(self, item):
   1221         if isinstance(item, str):
-> 1222             return self.columns[item]
   1223         elif isinstance(item, (int, np.integer)):
   1224             return self.Row(self, item)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
    104         """
    105         if isinstance(item, str):
--> 106             return OrderedDict.__getitem__(self, item)
    107         elif isinstance(item, (int, np.integer)):
    108             return self.values()[item]

```

{:.output_traceback_line}
```
KeyError: 'j_snr'
```



{:.input_area}
```python
#2 (continued)
import matplotlib.pyplot as plt
plt.scatter(t4['j_m'] - t4['h_m'],
            t4['h_m'] - t4['k_m'],
            s=5, color='black')
plt.scatter(subset['j_m'] - subset['h_m'],
            subset['h_m'] - subset['k_m'],
            s=30, color='red', alpha=0.5)
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
KeyError                                  Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-43-5fb859521933> in <module>()
      1 #2 (continued)
      2 import matplotlib.pyplot as plt
----> 3 plt.scatter(t4['j_m'] - t4['h_m'],
      4             t4['h_m'] - t4['k_m'],
      5             s=5, color='black')

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
   1220     def __getitem__(self, item):
   1221         if isinstance(item, str):
-> 1222             return self.columns[item]
   1223         elif isinstance(item, (int, np.integer)):
   1224             return self.Row(self, item)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
    104         """
    105         if isinstance(item, str):
--> 106             return OrderedDict.__getitem__(self, item)
    107         elif isinstance(item, (int, np.integer)):
    108             return self.values()[item]

```

{:.output_traceback_line}
```
KeyError: 'j_m'
```



{:.input_area}
```python
#3
simple = t4['ra', 'dec', 'j_m', 'h_m', 'k_m']
simple
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
KeyError                                  Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-44-031ed6fa7e5f> in <module>()
      1 #3
----> 2 simple = t4['ra', 'dec', 'j_m', 'h_m', 'k_m']
      3 simple

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
   1226             return self.Row(self, item.item())
   1227         elif self._is_list_or_tuple_of_str(item):
-> 1228             out = self.__class__([self[x] for x in item],
   1229                                  meta=deepcopy(self.meta),
   1230                                  copy_indices=self._copy_indices)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in <listcomp>(.0)
   1226             return self.Row(self, item.item())
   1227         elif self._is_list_or_tuple_of_str(item):
-> 1228             out = self.__class__([self[x] for x in item],
   1229                                  meta=deepcopy(self.meta),
   1230                                  copy_indices=self._copy_indices)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
   1220     def __getitem__(self, item):
   1221         if isinstance(item, str):
-> 1222             return self.columns[item]
   1223         elif isinstance(item, (int, np.integer)):
   1224             return self.Row(self, item)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/astropy/table/table.py in __getitem__(self, item)
    104         """
    105         if isinstance(item, str):
--> 106             return OrderedDict.__getitem__(self, item)
    107         elif isinstance(item, (int, np.integer)):
    108             return self.values()[item]

```

{:.output_traceback_line}
```
KeyError: 'ra'
```



{:.input_area}
```python
#3 (continued)
simple.write('2mass_subset.csv', format='ascii.csv', overwrite=True, comment='#')
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
<ipython-input-45-ae75b9be004a> in <module>()
      1 #3 (continued)
----> 2 simple.write('2mass_subset.csv', format='ascii.csv', overwrite=True, comment='#')

```

{:.output_traceback_line}
```
NameError: name 'simple' is not defined
```

