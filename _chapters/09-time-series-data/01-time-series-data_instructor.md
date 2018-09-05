---
interact_link: 09-time-series-data/01-time-series-data_instructor.ipynb
title: 'Time Series Data'
permalink: 'chapters/09-time-series-data/01-time-series-data'
previouschapter:
  url: 
  title: 'Time Series Data'
nextchapter:
  url: 
  title: 'Data'
redirect_from:
  - 'chapters/09-time-series-data/01-time-series-data'
---

# Handling Data over time

There's a widespread trend in solar physics at the moment for correlation over actual science, so being able to handle data over time spans is a skill we all need to have. Python has ample support for this so lets have a look at what we can use.


<section class="objectives panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-certificate"></span> Learning Objectives</h2>
</div>


<div class="panel-body">

<ul>
<li>Understand and use Sunpy Time Series data.</li>
<li>Create a pandas dataframe.</li>
<li>Utilise the datetime package.</li>
<li>Use the pandas dataframe to plot the data within it.</li>
</ul>

</div>

</section>


## Sunpy Time Series

SunPy provides a lightcurve object to handle this type of time series data. The module has a number of instruments associated with it, including:

* GOES XRS LightCurve
* SDO EVE LightCurve for level 0CS data
* Proba-2 LYRA LightCurve
* NOAA Solar Cycle monthly indices.
* Nobeyama Radioheliograph Correlation LightCurve.
* RHESSI X-ray Summary LightCurve.

We're going to examine the lightcurves created by a solar flare on June 7th 2011.

Lets begin with the import statements:


{:.input_area}
```python
import numpy as np
import sunpy
import sunpy.data.sample
import sunpy.timeseries as ts
import matplotlib.pyplot as plt
%matplotlib inline
```

Now lets look at some test series data, in this case we can utilitse the sunpy sample data. Do this with `import sunpy.data.sample`


{:.input_area}
```python
goes_ts = ts.TimeSeries(sunpy.data.sample.GOES_XRS_TIMESERIES, source='XRS')
```

Now goes data is a sunpy time seris object so we can inspect the object


{:.input_area}
```python
goes_ts.meta
```




{:.output_data_text}
```
|-------------------------------------------------------------------------------------------------|
|TimeRange                  | Columns         | Meta                                              |
|-------------------------------------------------------------------------------------------------|
|2011-06-06 23:59:59.961999 | xrsa            | simple: True                                      |
|            to             | xrsb            | bitpix: 8                                         |
|2011-06-07 23:59:57.631999 |                 | naxis: 0                                          |
|                           |                 | extend: True                                      |
|                           |                 | date: 26/06/2012                                  |
|                           |                 | numext: 3                                         |
|                           |                 | telescop: GOES 15                                 |
|                           |                 | instrume: X-ray Detector                          |
|                           |                 | object: Sun                                       |
|                           |                 | origin: SDAC/GSFC                                 |
|                           |                 | ...                                               |
|-------------------------------------------------------------------------------------------------|
```



NB: not all sources provide meta data so this may be empty.

The actual data is accessible tthrough the attributes of the timeseries object. Part of the advantage of using these inbuilt functions we can get a quicklook at our data using short commands:


{:.input_area}
```python
goes_ts.peek()
```


![png](../../images/chapters/09-time-series-data/01-time-series-data_instructor_9_0.png)


### Accessing and using the data

More custom plots can be made easily by accessing the data in the timeseries functionality. Both the time information and the data are contained within the lightcurve.data code, which is a pandas dataframe. We can see what data is contained in the dataframe by finding which columns it contains and also asking what's in the meta data: 


{:.input_area}
```python
goes_data = goes_ts.data
goes_data.columns
```




{:.output_data_text}
```
Index(['xrsa', 'xrsb'], dtype='object')
```




<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> On Dictionaries</h2>
</div>


<div class="panel-body">

<p>We can create keyword-data pairs to form a dictionary (shock horror) of values. In this case we have defined some strings and number to represent temperatures across europe</p>
<div class="codehilite"><pre><span></span>temps = {&#39;Brussles&#39;: 9, &#39;London&#39;: 3, &#39;Barcelona&#39;: 13, &#39;Rome&#39;: 16}
temps[&#39;Rome&#39;]
16
</pre></div>


<p>We can also find out what keywords are associated with a given dictionary, In this case:</p>
<div class="codehilite"><pre><span></span>temps.keys()
dict_keys([&#39;London&#39;, &#39;Barcelona&#39;, &#39;Rome&#39;, &#39;Brussles&#39;])
</pre></div>


<p>Dictionaries will crop up more and more often, typically as a part of differnt file structure such as <code>ynl</code> and <code>json</code>.</p>

</div>

</section>


## Pandas

In its own words Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. Pandas has two forms of structures, 1D series and 2D dataframe. It also has its own functions associated with it.

It is also amazing.

Timeseries uses these in built Pandas functions, so we can find out things like the maximum of curves:



{:.input_area}
```python
# max time argument taken from long and short GOES channels
max_t_goes_long = goes_data['xrsb'].idxmax()
max_t_goes_short = goes_data.xrsa.idxmax()

print('GOES long : {}'.format(max_t_goes_long))
print('GOES short : {}'.format(max_t_goes_short))
```

{:.output_stream}
```
GOES long : 2011-06-07 06:41:24.118999
GOES short : 2011-06-07 06:39:00.761999

```

So lets plot them on the graph


{:.input_area}
```python
# create figure with raw curves
fig, ax = plt.subplots(figsize=(16,10))
goes_data.xrsa.plot(kind='line')
goes_data.xrsb.plot(kind='line')
plt.legend()
plt.ylabel('Flux (Wm^2)')

# max lines
plt.axvline(max_t_goes_long, color='green', linestyle='dashed',linewidth=2)
plt.axvline(max_t_goes_short, color='black', linestyle='dashed',linewidth=2)
```




{:.output_data_text}
```
<matplotlib.lines.Line2D at 0x7f7869f74f98>
```




![png](../../images/chapters/09-time-series-data/01-time-series-data_instructor_16_1.png)


## Reading in Tablulated data

Now we have seen a little of what Pandas can do, lets read in some of our own data. In this case we are going to use data from Bennett et al. 2015, ApJ, a truly ground breaking work. Now the data we are reading in here is a structured Array.



{:.input_area}
```python
data = np.genfromtxt('data/macrospicules.csv', skip_header=1, dtype=None, delimiter=',')
```

Now, the above line imports information on some solar features over a sample time period. Specifically we have, maximum length, lifetime and time at which they occured. Now if we type `data[0]` what will happen?


{:.input_area}
```python
data[0]
```




{:.output_data_text}
```
(27.02261709, 13.6, b'2010-06-01T13:00:14.120000')
```



This is the first row of the array, containing the first element of our three properties. This particular example is a stuctured array, so the columns and rows can have properties and assign properties to the header. We can ask what the title of these columns is by using a `dtype` command:


{:.input_area}
```python
data.dtype.names
```




{:.output_data_text}
```
('f0', 'f1', 'f2')
```



Unhelpful, so lets give them something more recognisable. We can use the docs to look up syntax and change the names of the column lables.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Google your troubles away</h2>
</div>


<div class="panel-body">

<p>So the docs are <a href="http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.genfromtxt.html">here</a>. Find the syntax to change to names to better to represent maximum length, lifetime and point in time which they occured.</p>

</div>

</section>



{:.input_area}
```python
data.dtype.names = ('max_len', 'ltime', 'sample_time')
data.
```


{:.output_traceback_line}
```
  File "<ipython-input-11-b98b320362d9>", line 2
    data.
         ^
SyntaxError: invalid syntax

```


## DataFrame

Now a pandas DataFrame takes two arguments as a minimum, index and data. In this case the index will be our time within the sample and the maximum length and lifetime will be our data. So lets import pandas and use the dataframe:

Pandas reads a dictionary when we want to input multiple data columns. Therefore we need to make a dictionary of our data and read that into a pandas data frame. First we need to import pandas.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Dictionaries</h2>
</div>


<div class="panel-body">

<p>So we covered dictionaries earlier. We can create keyword data pairs to form a dictionary (shock horror) of values. In this case </p>
<div class="codehilite"><pre><span></span>temps = {&#39;Brussles&#39;: 9, &#39;London&#39;: 3, &#39;Barcelona&#39;: 13, &#39;Rome&#39;: 16}
temps[&#39;Rome&#39;]
16
</pre></div>


<p>We can also find out what keywords are associated with a given dictionary, In this case:</p>
<div class="codehilite"><pre><span></span>temps.keys()
dict_keys([&#39;London&#39;, &#39;Barcelona&#39;, &#39;Rome&#39;, &#39;Brussles&#39;])
</pre></div>

</div>

</section>


First, let's import Pandas:


{:.input_area}
```python
import pandas as pd

d = {'max_len': data['max_len'], 'ltime': data['ltime']}

df = pd.DataFrame(data=d, index=data['sample_time'])
print(df.head())
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
<ipython-input-12-1f26293446d4> in <module>()
      1 import pandas as pd
      2 
----> 3 d = {'max_len': data['max_len'], 'ltime': data['ltime']}
      4 
      5 df = pd.DataFrame(data=d, index=data['sample_time'])

```

{:.output_traceback_line}
```
ValueError: no field of name max_len
```


## Datetime Objects

Notice that the time for the sample is in a strange format. It is a string containing the date in YYYY-MM-DD and time in HH-MM-SS-mmmmmm. These datetime objects have their own set of methods associated with them. Python appreciates that these are built this way and can use them for the indexing easily. 

We can use this module to create date objects (representing just year, month, day). We can also get information about universal time, such as the time and date today.

NOTE: Datetime objects are NOT strings. They are objects which print out as strings.




{:.input_area}
```python
import datetime
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
lunchtime = datetime.time(12,30)
the_date = datetime.date(2005, 7, 14)
dinner = datetime.datetime.combine(the_date, lunchtime)

print("When is dinner? {}".format(dinner))
```

{:.output_stream}
```
2018-09-05 22:30:35.407788
2018-09-05 21:30:35.407909
When is dinner? 2005-07-14 12:30:00

```

Looking back at when we discussed the first element of data, and the format of the time index was awkward to use so lets do something about that. 


{:.input_area}
```python
print(df.index[0])
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
<ipython-input-14-fbb9075eea54> in <module>()
----> 1 print(df.index[0])

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```


So this is a byte rather than a string so we'll need to convert that using the string handling functionality in pandas


{:.input_area}
```python
df['time'] = df.index.astype(str)
df.iloc[0].time
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
<ipython-input-15-35dba3aa50fc> in <module>()
----> 1 df['time'] = df.index.astype(str)
      2 df.iloc[0].time

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```


This is a string and python will just treat it as such. We need to use datetime to pick this string appart and change it into an oject we can use.

[To the Docs!](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior)

So we use the formatting commands to match up with the string we have.


{:.input_area}
```python
dt_obj = datetime.datetime.strptime(df.iloc[0].time, '%Y-%m-%dT%H:%M:%S.%f')
print(dt_obj)
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
<ipython-input-16-59058002e7a5> in <module>()
----> 1 dt_obj = datetime.datetime.strptime(df.iloc[0].time, '%Y-%m-%dT%H:%M:%S.%f')
      2 print(dt_obj)

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```


We can now get attributes from this such as the hour, month, second and so on


{:.input_area}
```python
print(dt_obj.second)
print(dt_obj.month)
print(dt_obj.weekday())
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
<ipython-input-17-61223efe8b52> in <module>()
----> 1 print(dt_obj.second)
      2 print(dt_obj.month)
      3 print(dt_obj.weekday())

```

{:.output_traceback_line}
```
NameError: name 'dt_obj' is not defined
```


Now the next logical step would be to make a for loop and iterate over the index and reassign it.

*HOWEVER* there is almost always a better way. And Pandas has a `to_dateime()` method that we can feed the time columns:


{:.input_area}
```python
df['datetime'] = pd.to_datetime(df.time)
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
<ipython-input-18-d77fa28270ad> in <module>()
----> 1 df['datetime'] = pd.to_datetime(df.time)

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```


There is also one of the most powerful featues of python, Apply. 
Apply will take a function and apply it to all rows in a dataframe or column. The easiest way to do this is with a lambda function


{:.input_area}
```python
df['other_datetime'] = df.time.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f'))
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
<ipython-input-19-311b6b5ab151> in <module>()
----> 1 df['other_datetime'] = df.time.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f'))

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```



{:.input_area}
```python
df.head()
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
<ipython-input-20-c42a15b2c7cf> in <module>()
----> 1 df.head()

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```


Both these are much cleaner and faster due to pandas' optimisation. We can now set one of these as the index


{:.input_area}
```python
df.set_index('datetime', inplace=True)
df.head()
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
<ipython-input-21-3c8de251e79c> in <module>()
----> 1 df.set_index('datetime', inplace=True)
      2 df.head()

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```


Now that there are official datetime objects on the index we can start operating based on the time of the frame


{:.input_area}
```python
l_bins = df.groupby([df.index.year, df.index.month])
print(len(l_bins))
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
<ipython-input-22-702d9c2c6b00> in <module>()
----> 1 l_bins = df.groupby([df.index.year, df.index.month])
      2 print(len(l_bins))

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```


Here we have used the groupby command to take the `'max_len'` column, called as a dictionary key, and create bins for our data to sit in according to year and then month. 

The object `l_bins` has `mean`, `max`, `std` etc. attributes in the same way as the numpy arrays we handled the other day.


{:.input_area}
```python
agg_spicules = df.groupby([df.index.year, df.index.month]).agg({'max_len': np.mean,
                                                                'max_len': np.std})

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
<ipython-input-23-0184c60d6c05> in <module>()
----> 1 agg_spicules = df.groupby([df.index.year, df.index.month]).agg({'max_len': np.mean,
      2                                                                 'max_len': np.std})

```

{:.output_traceback_line}
```
NameError: name 'df' is not defined
```



{:.input_area}
```python
agg_spicules
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
<ipython-input-24-3fc94dd5b3f0> in <module>()
----> 1 agg_spicules

```

{:.output_traceback_line}
```
NameError: name 'agg_spicules' is not defined
```


Now we have all this data we can build a lovely bargraph with error bars and wonderful things like that.

Remember, these pandas objects have functions associated with them, and one of them is a plot command.


{:.input_area}
```python
fig, ax = plt.subplots()
fig.autofmt_xdate()
l_mean.plot(kind='bar', ax=ax, yerr=l_std, grid=False, legend=False)

plt.show()
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
<ipython-input-25-0e03c5148a98> in <module>()
      1 fig, ax = plt.subplots()
      2 fig.autofmt_xdate()
----> 3 l_mean.plot(kind='bar', ax=ax, yerr=l_std, grid=False, legend=False)
      4 
      5 plt.show()

```

{:.output_traceback_line}
```
NameError: name 'l_mean' is not defined
```



![png](../../images/chapters/09-time-series-data/01-time-series-data_instructor_53_1.png)


Note that the date on the x-axis is a little messed up we can fix with `fig.autofmt_xdate()`




<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> How do the lifetimes change?</h2>
</div>


<div class="panel-body">

<p>Now that we have the plot for the maximum length, now make a bar graph of the lifetimes of the features.</p>

</div>

</section>



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Exoplanet Data</h2>
</div>


<div class="panel-body">

<p>Now, to all the astronomers out there, let us process some real data. We have some txt files containing the lightcurve from a recent paper. Can you process the data and show us the planet?</p>
<p>HINT: You'll need to treat this data slightly differently. The date here is in Julian Day so you will need to use <a href="http://docs.astropy.org/en/v1.1.1/api/astropy.time.Time.html">these</a> docs to convert it to a sensible datetime object, before you make the DataFrame.</p>

</div>

</section>



{:.input_area}
```python
import numpy as np
ep_data = np.loadtxt('data/XO1_wl_transit_FLUX.txt')

```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
OSError                                   Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-26-9af143cb8fd6> in <module>()
      1 import numpy as np
----> 2 ep_data = np.loadtxt('data/XO1_wl_transit_FLUX.txt')

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/numpy/lib/npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin, encoding)
    924             fname = str(fname)
    925         if _is_string_like(fname):
--> 926             fh = np.lib._datasource.open(fname, 'rt', encoding=encoding)
    927             fencoding = getattr(fh, 'encoding', 'latin1')
    928             fh = iter(fh)

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/numpy/lib/_datasource.py in open(path, mode, destpath, encoding, newline)
    260 
    261     ds = DataSource(destpath)
--> 262     return ds.open(path, mode, encoding=encoding, newline=newline)
    263 
    264 

```

{:.output_traceback_line}
```
/opt/miniconda/envs/stfc/lib/python3.6/site-packages/numpy/lib/_datasource.py in open(self, path, mode, encoding, newline)
    616                                       encoding=encoding, newline=newline)
    617         else:
--> 618             raise IOError("%s not found." % path)
    619 
    620 

```

{:.output_traceback_line}
```
OSError: data/XO1_wl_transit_FLUX.txt not found.
```



{:.input_area}
```python
ep_dict = {'flux':ep_data[:, 1], 
           'err_flux':ep_data[:, 2]}
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
<ipython-input-27-d45090fc219d> in <module>()
----> 1 ep_dict = {'flux':ep_data[:, 1], 
      2            'err_flux':ep_data[:, 2]}

```

{:.output_traceback_line}
```
NameError: name 'ep_data' is not defined
```



{:.input_area}
```python
ep_df = pd.DataFrame(data=ep_dict, index=ep_data[:,0])
ep_df.index = pd.to_datetime(ep_df.index)
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
<ipython-input-28-cd9c5ddfe9fb> in <module>()
----> 1 ep_df = pd.DataFrame(data=ep_dict, index=ep_data[:,0])
      2 ep_df.index = pd.to_datetime(ep_df.index)

```

{:.output_traceback_line}
```
NameError: name 'ep_dict' is not defined
```



{:.input_area}
```python
from astropy.time import Time
t = Time(ep_data[:, 0], format='jd')
UTC = t.datetime
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
<ipython-input-29-9b7b9b5c029b> in <module>()
      1 from astropy.time import Time
----> 2 t = Time(ep_data[:, 0], format='jd')
      3 UTC = t.datetime

```

{:.output_traceback_line}
```
NameError: name 'ep_data' is not defined
```



{:.input_area}
```python
ep_df.index = UTC
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
<ipython-input-30-74bafffb0dea> in <module>()
----> 1 ep_df.index = UTC

```

{:.output_traceback_line}
```
NameError: name 'UTC' is not defined
```



{:.input_area}
```python
ep_df
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
<ipython-input-31-ba24905120da> in <module>()
----> 1 ep_df

```

{:.output_traceback_line}
```
NameError: name 'ep_df' is not defined
```

