---
interact_link: 09-time-series-data/08-Time-Series-Data_instructor.ipynb
title: 'Time Series Data'
permalink: 'chapters/09-time-series-data/08-Time-Series-Data'
previouschapter:
  url: chapters/09-time-series-data/01-time-series-data
  title: 'Time Series Data'
nextchapter:
  url: 
  title: 'Data'
redirect_from:
  - 'chapters/09-time-series-data/08-time-series-data'
---

# Handling Data over time

There's a widespread trend in solar physics at the moment for correlation over actual science, so being able to handle data over time spans is a skill we all need to have. Python has ample support for this so lets have a look at what we can use.

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


![png](../../images/chapters/09-time-series-data/08-Time-Series-Data_instructor_8_0.png)


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
<matplotlib.lines.Line2D at 0x7f0c9c521f60>
```




![png](../../images/chapters/09-time-series-data/08-Time-Series-Data_instructor_15_1.png)


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
data
```




{:.output_data_text}
```
array([(27.02261709, 13.6       , b'2010-06-01T13:00:14.120000'),
       (36.20809658,  8.4       , b'2010-06-01T12:58:02.120000'),
       (62.93289752, 24.19983333, b'2010-06-15T12:55:02.110000'),
       (38.97054949, 22.99966667, b'2010-07-07T12:23:50.110000'),
       (53.58942032, 21.79983333, b'2010-07-07T13:28:50.120000'),
       (30.6401107 , 17.40016667, b'2010-07-15T12:12:02.130000'),
       (34.62323773, 12.8       , b'2010-07-15T12:19:02.110000'),
       (25.76578452, 14.2       , b'2010-07-24T12:09:50.120000'),
       (42.55229885, 24.4       , b'2010-08-01T13:27:14.120000'),
       (43.78096232, 15.4       , b'2010-08-07T12:37:44.120000'),
       (32.07478058, 15.19983333, b'2010-08-15T13:10:32.120000'),
       (46.32895236, 18.59983333, b'2010-08-24T12:51:44.120000'),
       (41.81948071, 15.2       , b'2010-08-24T13:22:20.120000'),
       (36.15639728, 18.80016667, b'2010-09-01T12:43:44.120000'),
       (27.76449747, 17.2       , b'2010-09-15T12:21:20.120000'),
       (28.36338204, 20.2       , b'2010-09-15T12:26:08.120000'),
       (46.24264885, 18.80016667, b'2010-09-15T12:33:44.120000'),
       (31.66963787, 18.99983333, b'2010-09-15T13:06:32.130000'),
       (37.98509124, 18.4       , b'2010-09-24T12:36:56.120000'),
       (41.10763789, 17.79983333, b'2010-10-15T12:32:08.120000'),
       (36.31153664, 20.3995    , b'2010-10-24T12:37:08.130000'),
       (63.94515322, 26.59983333, b'2010-11-01T12:43:08.130000'),
       (33.20603032, 15.99983333, b'2010-11-01T12:55:20.130000'),
       (45.12547627, 20.        , b'2010-11-07T12:25:20.120000'),
       (45.59984305, 12.        , b'2010-11-07T13:18:08.120000'),
       (44.13747471, 15.        , b'2010-11-15T12:10:08.130000'),
       (39.05135355, 15.19983333, b'2010-11-15T12:14:44.140000'),
       (42.70997285, 22.4       , b'2010-12-01T13:45:20.140000'),
       (22.00943851, 12.8       , b'2010-12-07T12:09:08.120000'),
       (45.70103315, 25.4       , b'2010-12-15T12:17:08.130000'),
       (40.61460622, 26.6       , b'2010-12-24T12:30:32.120000'),
       (53.58952877, 14.8       , b'2010-12-24T13:22:08.120000'),
       (33.55068528, 19.2       , b'2011-01-01T13:06:56.130000'),
       (34.12704163,  9.80016667, b'2011-01-01T13:47:56.130000'),
       (28.84501455, 14.        , b'2011-01-15T12:09:32.120000'),
       (33.50857898, 14.        , b'2011-01-15T12:55:32.140000'),
       (33.04991294, 13.8       , b'2011-01-15T13:50:56.120000'),
       (43.14772776, 18.59983333, b'2011-01-24T12:22:56.130000'),
       (64.7263967 , 22.20033333, b'2011-01-24T12:44:44.130000'),
       (58.4113328 , 17.        , b'2011-01-24T13:33:56.130000'),
       (26.51897508, 13.40016667, b'2011-02-01T13:16:44.130000'),
       (38.16891551, 16.19983333, b'2011-02-01T13:37:32.120000'),
       (53.91004427, 16.79966667, b'2011-02-07T12:10:32.120000'),
       (38.66085552, 19.4       , b'2011-02-07T13:21:56.120000'),
       (27.32363074, 19.        , b'2011-02-15T13:51:08.120000'),
       (34.82350067, 13.59983333, b'2011-02-24T12:30:32.120000'),
       (49.29044968, 23.99983333, b'2011-02-24T12:54:08.130000'),
       (44.55780869, 18.39966667, b'2011-03-01T12:20:32.120000'),
       (30.01404343, 19.        , b'2011-03-01T13:20:56.120000'),
       (33.79223954,  6.99983333, b'2011-03-15T12:06:32.120000'),
       (37.02116485, 17.6       , b'2011-03-15T12:09:44.120000'),
       (28.72061961, 12.00016667, b'2011-03-15T13:14:32.120000'),
       (29.21863497, 17.60016667, b'2011-03-24T12:52:32.120000'),
       (55.72629452, 18.80016667, b'2011-03-24T13:50:20.120000'),
       (54.57759503, 21.00016667, b'2011-04-07T13:40:44.130000'),
       (45.33884703, 19.39983333, b'2011-04-15T12:54:20.120000'),
       (50.69244379, 17.80033333, b'2011-04-15T12:54:44.130000'),
       (33.25632341, 13.20016667, b'2011-04-24T12:31:56.120000'),
       (37.73000783, 18.60016667, b'2011-05-07T12:37:32.120000'),
       (26.92855622, 21.99983333, b'2011-05-07T13:42:20.120000'),
       (52.49096835, 18.2       , b'2011-05-15T13:27:56.130000'),
       (63.49966052, 25.8       , b'2011-07-01T13:06:08.120000'),
       (36.13680388,  9.99983333, b'2011-07-01T13:02:32.120000'),
       (61.63887853, 22.40016667, b'2011-07-01T13:32:32.120000'),
       (44.4662083 , 17.4       , b'2011-07-01T13:35:32.130000'),
       (29.52452638, 11.99983333, b'2011-07-07T12:56:08.120000'),
       (43.23969955, 24.        , b'2011-07-15T13:31:44.120000'),
       (41.65026311, 21.60016667, b'2011-07-24T12:54:56.120000'),
       (52.16598344, 19.6       , b'2011-08-01T12:41:32.120000'),
       (42.67412936, 14.03266667, b'2011-08-07T12:47:44.130000'),
       (41.81910611, 22.6       , b'2011-08-07T13:03:32.120000'),
       (34.49493977, 11.8       , b'2011-08-15T12:51:08.120000'),
       (35.78882006, 16.79966667, b'2011-08-24T12:52:44.130000'),
       (45.59188682, 19.60016667, b'2011-08-24T12:45:08.120000'),
       (39.26216985, 12.8       , b'2011-09-01T12:03:32.130000'),
       (35.10139159, 11.79983333, b'2011-09-24T12:51:20.120000'),
       (38.14667516, 13.8       , b'2011-10-01T12:28:08.120000'),
       (46.09430341, 16.59983333, b'2011-10-07T13:11:20.120000'),
       (50.44398261, 21.40016667, b'2011-10-15T12:17:56.120000'),
       (46.41930315, 21.19983333, b'2011-10-15T12:24:20.130000'),
       (43.99951416, 15.4       , b'2011-11-01T12:27:56.140000'),
       (31.10082419, 13.5995    , b'2011-11-01T13:11:20.120000'),
       (45.43674785, 13.20016667, b'2011-11-07T13:29:32.130000'),
       (38.78414481, 18.20016667, b'2011-11-07T13:35:32.130000'),
       (36.03072435, 14.40016667, b'2011-11-24T13:23:20.130000'),
       (39.52956702, 20.4       , b'2011-12-01T13:17:56.130000'),
       (28.94948495, 16.60016667, b'2011-12-07T13:45:56.130000'),
       (36.16831602, 13.8       , b'2011-12-15T13:41:44.120000'),
       (54.90157329, 18.2       , b'2012-01-01T12:52:32.120000'),
       (49.35714339, 22.80016667, b'2012-01-01T13:49:32.120000'),
       (45.9207131 , 23.40016667, b'2012-01-24T12:24:44.130000'),
       (36.33602522, 16.        , b'2012-02-01T12:15:08.120000'),
       (47.81325513, 18.        , b'2012-02-01T12:22:20.120000'),
       (30.02565172, 17.        , b'2012-02-01T12:34:44.120000'),
       (22.4376017 , 12.        , b'2012-02-01T12:45:44.120000'),
       (25.77671126, 26.60016667, b'2012-02-01T13:35:08.130000'),
       (22.09750136,  9.8       , b'2012-03-01T12:24:56.130000'),
       (51.10043568, 14.6       , b'2012-03-01T13:20:56.140000'),
       (52.13571082, 22.80033333, b'2012-03-07T12:32:44.120000'),
       (35.70298287, 15.99983333, b'2012-03-07T12:58:44.130000'),
       (34.73403574, 13.4       , b'2012-03-07T13:04:32.120000'),
       (40.74477779, 18.40033333, b'2012-04-01T13:01:08.120000'),
       (38.34861845, 10.80016667, b'2012-04-07T12:25:08.120000'),
       (22.82335936, 13.        , b'2012-04-24T12:42:08.120000'),
       (27.30678373, 11.4       , b'2012-04-24T13:32:20.120000'),
       (27.42834706, 16.19983333, b'2012-05-01T12:21:20.120000'),
       (23.27232254, 12.60016667, b'2012-05-01T12:45:44.120000'),
       (29.83005671, 11.8       , b'2012-05-01T12:46:56.120000'),
       (36.08121426, 18.        , b'2012-05-07T12:14:08.120000'),
       (50.04105014, 17.4       , b'2012-05-07T12:18:44.120000'),
       (33.14161453, 17.20016667, b'2012-05-15T12:11:44.130000'),
       (29.2621644 , 13.80016667, b'2012-05-15T13:10:56.120000'),
       (26.55148777, 14.39983333, b'2012-05-24T13:42:44.120000'),
       (36.15467202, 17.        , b'2012-06-01T12:14:56.120000'),
       (26.06766701, 15.8       , b'2012-06-01T12:25:20.130000'),
       (27.37302807, 16.        , b'2012-06-01T12:45:44.120000'),
       (30.56321175, 18.59983333, b'2012-06-07T13:35:20.120000'),
       (26.83143584, 21.00033333, b'2012-06-15T12:45:32.120000'),
       (37.11331356, 14.8       , b'2012-06-15T12:44:56.120000'),
       (30.79380358, 17.2       , b'2012-06-15T13:00:20.120000'),
       (32.89179738,  9.39983333, b'2012-06-24T13:17:56.130000'),
       (28.89730285, 18.2       , b'2012-07-15T12:21:07.130000'),
       (33.0527976 , 13.6       , b'2012-08-01T12:33:19.130000'),
       (25.57069612, 20.20016667, b'2012-08-01T13:01:43.120000'),
       (44.20414097, 30.8       , b'2012-08-01T13:37:19.120000'),
       (28.68038005, 12.4       , b'2012-08-07T12:16:43.130000'),
       (25.11419547, 14.59966667, b'2012-08-07T12:21:55.120000'),
       (23.78793994, 11.39983333, b'2012-08-24T12:06:43.130000'),
       (26.60399083, 20.        , b'2012-09-01T13:47:43.130000'),
       (36.72695416, 18.        , b'2012-09-01T13:12:55.120000'),
       (44.35566025,  9.6       , b'2012-09-07T12:05:43.120000'),
       (41.37507269, 18.4       , b'2012-09-07T13:32:07.120000'),
       (31.08485597, 21.59983333, b'2012-09-24T12:23:31.130000'),
       (39.71759583, 11.20016667, b'2012-09-24T13:46:19.120000'),
       (47.36372856, 27.2       , b'2012-10-01T12:53:19.140000'),
       (42.72431429, 18.59983333, b'2012-10-01T12:55:55.120000'),
       (30.49807689, 13.        , b'2012-10-07T13:01:43.120000'),
       (37.4604915 , 18.6       , b'2012-10-15T13:19:43.140000'),
       (39.65240926, 15.80016667, b'2012-10-24T12:08:19.120000'),
       (37.26885237, 20.39983333, b'2012-11-01T12:53:55.120000'),
       (41.50380626, 14.6       , b'2012-11-07T12:10:43.120000'),
       (29.8313709 , 16.40016667, b'2012-11-15T13:39:55.130000'),
       (43.02721083, 13.40016667, b'2012-12-01T12:57:19.120000'),
       (33.23966863, 22.6       , b'2012-12-01T13:07:43.120000'),
       (28.73848974,  9.99983333, b'2012-12-15T12:32:07.120000'),
       (41.28193776, 11.39983333, b'2013-01-07T12:14:07.140000'),
       (44.80971415, 16.        , b'2013-01-15T12:41:19.140000'),
       (50.10792885, 22.6       , b'2013-01-15T13:39:19.130000'),
       (37.79992144, 15.39983333, b'2013-01-15T13:51:19.130000'),
       (54.59165111, 34.        , b'2013-01-24T12:38:55.120000'),
       (31.60523881, 12.        , b'2013-02-01T13:04:31.140000'),
       (36.31252683, 14.8       , b'2013-02-15T12:13:19.120000'),
       (44.25298922, 14.6       , b'2013-03-01T12:23:55.130000'),
       (51.02121661, 20.6       , b'2013-04-01T12:13:19.120000'),
       (34.20351256, 14.        , b'2013-04-01T12:25:19.140000'),
       (39.24552078, 16.2       , b'2013-04-24T12:50:55.120000'),
       (43.71189706, 16.80016667, b'2013-05-07T13:30:19.120000'),
       (36.40843056, 11.60033333, b'2013-05-15T13:44:07.130000'),
       (34.02240796, 13.6       , b'2013-05-24T12:46:07.120000'),
       (39.27977921, 15.3995    , b'2013-06-01T13:48:55.120000'),
       (54.66979248, 19.19983333, b'2013-06-15T12:37:43.120000'),
       (65.7384905 , 23.59983333, b'2013-06-15T13:07:31.130000'),
       (53.01413049, 17.6       , b'2013-07-01T12:49:31.130000'),
       (34.17031127, 16.4       , b'2013-07-07T12:18:43.130000'),
       (47.00239714, 18.        , b'2013-07-15T13:22:43.130000'),
       (17.32168005, 11.8       , b'2013-08-01T13:19:43.120000'),
       (44.68585728, 16.2       , b'2013-08-07T12:15:31.130000'),
       (29.44389171,  9.2       , b'2013-08-07T12:41:55.130000'),
       (40.80497941, 27.6       , b'2013-08-15T12:34:07.120000'),
       (34.6572607 ,  9.79983333, b'2013-08-24T13:08:43.140000'),
       (42.62526043, 16.8       , b'2013-09-07T12:17:07.130000'),
       (37.36422913, 20.79983333, b'2013-09-07T13:04:55.130000'),
       (31.17786476, 12.19983333, b'2013-09-15T13:26:31.140000'),
       (28.12867393, 14.        , b'2013-10-01T12:43:07.120000'),
       (30.40163346, 19.8       , b'2013-10-07T12:11:31.130000'),
       (30.51526168, 10.        , b'2013-10-07T13:01:31.120000'),
       (35.9876376 , 23.19983333, b'2013-10-15T12:58:55.140000'),
       (23.08802156, 15.19983333, b'2013-11-07T12:23:19.120000'),
       (40.76121653, 22.8       , b'2013-11-07T12:39:19.120000'),
       (21.0614616 , 13.20016667, b'2013-11-07T12:34:31.140000'),
       (37.30928468, 17.8005    , b'2013-11-07T12:41:31.130000'),
       (33.74493288, 11.20033333, b'2013-11-15T12:27:55.120000'),
       (23.37625041, 15.6       , b'2013-11-15T13:05:43.130000'),
       (23.26285756, 12.        , b'2013-11-24T13:10:55.120000'),
       (21.90478831, 12.        , b'2013-11-24T13:11:07.130000'),
       (31.46692441, 18.8       , b'2013-12-01T12:42:19.130000'),
       (24.02288547, 11.80033333, b'2013-12-01T12:37:43.130000'),
       (32.79270784, 14.79983333, b'2013-12-01T13:45:55.120000'),
       (30.07317007, 15.6       , b'2013-12-07T12:31:19.120000'),
       (29.7039241 , 13.8       , b'2013-12-07T13:48:43.130000'),
       (34.13671581, 17.79983333, b'2013-12-15T13:03:07.120000'),
       (50.58575418, 20.8       , b'2013-12-15T13:15:55.120000'),
       (34.97447555, 11.4       , b'2013-12-15T13:08:07.120000'),
       (24.51408577, 14.4       , b'2013-12-15T13:27:07.120000'),
       (48.26530071, 21.79983333, b'2014-01-01T13:49:31.120000'),
       (41.1800655 , 21.6       , b'2014-01-07T13:15:19.120000'),
       (38.59687577, 18.6       , b'2014-01-15T12:18:07.120000'),
       (28.32914516, 14.        , b'2014-02-07T12:27:55.130000'),
       (26.86404795, 17.60016667, b'2014-02-07T12:53:55.130000'),
       (29.09491492, 13.80016667, b'2014-02-07T13:15:31.130000'),
       (22.1925731 , 15.6       , b'2014-02-24T13:31:31.120000'),
       (26.6573342 , 11.39983333, b'2014-03-01T12:41:31.120000'),
       (34.45652454, 14.2       , b'2014-03-01T13:15:19.130000'),
       (29.52441516, 18.2       , b'2014-03-01T13:17:55.130000'),
       (26.05330498, 14.59983333, b'2014-03-07T12:58:55.120000'),
       (16.91583914, 15.8       , b'2014-03-07T13:21:55.120000'),
       (24.09964195,  9.2       , b'2014-03-15T12:43:43.120000'),
       (27.83367552, 15.79966667, b'2014-03-15T13:03:43.120000'),
       (21.83934023, 14.19983333, b'2014-03-24T13:21:31.120000'),
       (24.08621306, 10.19983333, b'2014-04-01T12:15:07.130000'),
       (21.4539239 ,  8.8       , b'2014-04-07T12:16:19.120000'),
       (50.23369701, 35.4       , b'2014-04-24T12:38:43.120000'),
       (22.20207407, 10.40016667, b'2014-05-01T13:23:19.130000'),
       (24.5242085 , 12.        , b'2014-05-01T13:40:31.130000'),
       (28.29914756, 16.39983333, b'2014-05-15T13:31:43.120000'),
       (25.40145715,  6.80016667, b'2014-05-15T12:35:19.120000'),
       (35.59277051, 21.4       , b'2014-05-24T13:09:07.120000'),
       (32.59279863, 19.60033333, b'2014-06-01T12:58:07.120000'),
       (31.24484412, 20.2       , b'2014-06-07T12:25:07.120000'),
       (46.45496714, 21.        , b'2014-06-07T12:55:31.130000'),
       (25.81684312, 15.        , b'2014-06-15T12:52:07.120000'),
       (23.82663323, 17.4       , b'2014-06-24T13:26:43.130000'),
       (25.75515713, 17.99983333, b'2014-06-24T13:22:55.120000'),
       (27.49177445, 17.20016667, b'2014-07-07T12:30:43.120000'),
       (38.48352531, 17.00033333, b'2014-07-07T13:50:55.120000'),
       (29.50744816, 14.19983333, b'2014-07-15T12:10:07.120000'),
       (54.12496571, 21.79983333, b'2014-07-15T12:18:43.120000'),
       (40.63961711, 19.8       , b'2014-07-24T12:26:31.120000'),
       (37.23678458, 11.6       , b'2014-08-01T12:36:07.120000'),
       (34.68878712, 15.39983333, b'2014-08-01T12:55:31.130000'),
       (31.37594022, 18.80016667, b'2014-08-07T12:13:31.130000'),
       (26.97844296, 16.6       , b'2014-08-15T12:09:31.120000'),
       (38.23975554, 22.        , b'2014-08-15T12:39:07.120000'),
       (38.90287314, 21.4       , b'2014-08-15T13:28:55.120000'),
       (24.01076136, 17.60033333, b'2014-08-24T12:36:43.130000'),
       (37.26779816, 25.8       , b'2014-08-24T13:04:55.130000'),
       (35.0705135 , 16.20016667, b'2014-08-24T13:31:19.120000'),
       (29.1850186 , 15.20016667, b'2014-09-01T12:31:07.130000'),
       (40.49388844, 35.60033333, b'2014-09-01T12:49:31.130000'),
       (33.4466624 , 14.6       , b'2014-09-07T13:13:43.120000'),
       (28.94498308, 13.2       , b'2014-09-07T13:26:55.120000'),
       (22.75986112, 18.79983333, b'2014-09-07T13:48:19.130000'),
       (32.27371125, 15.00033333, b'2014-09-15T12:44:43.120000'),
       (27.51808194, 18.4       , b'2014-09-15T13:24:55.140000'),
       (45.9195814 , 19.2       , b'2014-09-24T12:48:19.130000'),
       (37.40509992, 21.        , b'2014-10-01T12:41:07.130000'),
       (36.5449928 , 13.2       , b'2014-10-01T12:58:19.120000'),
       (44.1242809 , 21.8       , b'2014-10-07T12:39:55.130000'),
       (41.54289686, 18.39983333, b'2014-10-24T12:10:43.130000'),
       (40.40254961, 21.6       , b'2014-11-01T12:29:31.130000'),
       (33.47264368, 10.79983333, b'2014-11-15T13:28:19.140000'),
       (34.01641674, 14.4       , b'2014-12-01T13:05:55.120000'),
       (37.52700525, 15.4       , b'2014-12-01T13:46:55.140000'),
       (44.02589254, 19.39966667, b'2014-12-07T12:20:55.140000'),
       (40.08500945, 13.2       , b'2014-12-07T13:11:07.120000'),
       (29.29270305, 13.4       , b'2014-12-15T12:07:19.130000'),
       (41.57391536, 13.2       , b'2014-12-15T12:41:19.130000'),
       (44.2470371 , 17.80016667, b'2014-12-15T13:13:19.130000'),
       (55.54916983, 16.99966667, b'2014-12-24T13:14:55.120000')],
      dtype=[('max_len', '<f8'), ('ltime', '<f8'), ('sample_time', 'S26')])
```



### DataFrame

Now a pandas DataFrame takes two arguments as a minimum, index and data. In this case the index will be our time within the sample and the maximum length and lifetime will be our data. So lets import pandas and use the dataframe:

Pandas reads a dictionary when we want to input multiple data columns. Therefore we need to make a dictionary of our data and read that into a pandas data frame. First we need to import pandas.


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Dictionaries</h2>
</div>


<div class="panel-body">

<p>So we covered dictionaries earlier. We can create keyword data pairs to form a dictionary of values. In this case </p>
<div class="codehilite"><pre><span></span>temps = {&#39;Brussles&#39;: 9, &#39;London&#39;: 3, &#39;Barcelona&#39;: 13, &#39;Rome&#39;: 16}
temps[&#39;Rome&#39;]
16
</pre></div>


<p>We can also find out what keywords are associated with a given dictionary, In this case:</p>
<div class="codehilite"><pre><span></span>temps.keys()
dict_keys([&#39;London&#39;, &#39;Barcelona&#39;, &#39;Rome&#39;, &#39;Brussles&#39;])
</pre></div>


<p>First, let's import Pandas:</p>

</div>

</section>



{:.input_area}
```python
import pandas as pd

d = {'max_len': data['max_len'], 'ltime': data['ltime']}

df = pd.DataFrame(data=d, index=data['sample_time'])
print(df.head())
```

{:.output_stream}
```
                                 max_len      ltime
b'2010-06-01T13:00:14.120000'  27.022617  13.600000
b'2010-06-01T12:58:02.120000'  36.208097   8.400000
b'2010-06-15T12:55:02.110000'  62.932898  24.199833
b'2010-07-07T12:23:50.110000'  38.970549  22.999667
b'2010-07-07T13:28:50.120000'  53.589420  21.799833

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
2018-09-06 12:26:02.054226
2018-09-06 11:26:02.054358
When is dinner? 2005-07-14 12:30:00

```

Looking back at when we discussed the first element of data, and the format of the time index was awkward to use so lets do something about that. 


{:.input_area}
```python
print(df.index[0])
```

{:.output_stream}
```
b'2010-06-01T13:00:14.120000'

```

So this is a byte rather than a string so we'll need to convert that using the string handling functionality in pandas


{:.input_area}
```python
df['time'] = df.index.astype(str)
df.iloc[0].time
```




{:.output_data_text}
```
'2010-06-01T13:00:14.120000'
```



This is a string and python will just treat it as such. We need to use datetime to pick this string appart and change it into an oject we can use.

[To the Docs!](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

So we use the formatting commands to match up with the string we have.


{:.input_area}
```python
dt_obj = datetime.datetime.strptime(df.iloc[0].time, '%Y-%m-%dT%H:%M:%S.%f')
print(dt_obj)
```

{:.output_stream}
```
2010-06-01 13:00:14.120000

```

We can now get attributes from this such as the hour, month, second and so on


{:.input_area}
```python
print(dt_obj.second)
print(dt_obj.month)
print(dt_obj.weekday())
```

{:.output_stream}
```
14
6
1

```

Now the next logical step would be to make a for loop and iterate over the index and reassign it.

*HOWEVER* there is almost always a better way. And Pandas has a `to_dateime()` method that we can feed the time columns:


{:.input_area}
```python
df['datetime'] = pd.to_datetime(df.time)
```

There is also one of the most powerful featues of python, Apply. 
Apply will take a function and apply it to all rows in a dataframe or column. The easiest way to do this is with a lambda function


{:.input_area}
```python
df['other_datetime'] = df.time.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f'))
```


{:.input_area}
```python
df.head()
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>max_len</th>
      <th>ltime</th>
      <th>time</th>
      <th>datetime</th>
      <th>other_datetime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b'2010-06-01T13:00:14.120000'</th>
      <td>27.022617</td>
      <td>13.600000</td>
      <td>2010-06-01T13:00:14.120000</td>
      <td>2010-06-01 13:00:14.120</td>
      <td>2010-06-01 13:00:14.120</td>
    </tr>
    <tr>
      <th>b'2010-06-01T12:58:02.120000'</th>
      <td>36.208097</td>
      <td>8.400000</td>
      <td>2010-06-01T12:58:02.120000</td>
      <td>2010-06-01 12:58:02.120</td>
      <td>2010-06-01 12:58:02.120</td>
    </tr>
    <tr>
      <th>b'2010-06-15T12:55:02.110000'</th>
      <td>62.932898</td>
      <td>24.199833</td>
      <td>2010-06-15T12:55:02.110000</td>
      <td>2010-06-15 12:55:02.110</td>
      <td>2010-06-15 12:55:02.110</td>
    </tr>
    <tr>
      <th>b'2010-07-07T12:23:50.110000'</th>
      <td>38.970549</td>
      <td>22.999667</td>
      <td>2010-07-07T12:23:50.110000</td>
      <td>2010-07-07 12:23:50.110</td>
      <td>2010-07-07 12:23:50.110</td>
    </tr>
    <tr>
      <th>b'2010-07-07T13:28:50.120000'</th>
      <td>53.589420</td>
      <td>21.799833</td>
      <td>2010-07-07T13:28:50.120000</td>
      <td>2010-07-07 13:28:50.120</td>
      <td>2010-07-07 13:28:50.120</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Both these are much cleaner and faster due to pandas' optimisation. We can now set one of these as the index


{:.input_area}
```python
df.set_index('datetime', inplace=True)
df.head()
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>max_len</th>
      <th>ltime</th>
      <th>time</th>
      <th>other_datetime</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-06-01 13:00:14.120</th>
      <td>27.022617</td>
      <td>13.600000</td>
      <td>2010-06-01T13:00:14.120000</td>
      <td>2010-06-01 13:00:14.120</td>
    </tr>
    <tr>
      <th>2010-06-01 12:58:02.120</th>
      <td>36.208097</td>
      <td>8.400000</td>
      <td>2010-06-01T12:58:02.120000</td>
      <td>2010-06-01 12:58:02.120</td>
    </tr>
    <tr>
      <th>2010-06-15 12:55:02.110</th>
      <td>62.932898</td>
      <td>24.199833</td>
      <td>2010-06-15T12:55:02.110000</td>
      <td>2010-06-15 12:55:02.110</td>
    </tr>
    <tr>
      <th>2010-07-07 12:23:50.110</th>
      <td>38.970549</td>
      <td>22.999667</td>
      <td>2010-07-07T12:23:50.110000</td>
      <td>2010-07-07 12:23:50.110</td>
    </tr>
    <tr>
      <th>2010-07-07 13:28:50.120</th>
      <td>53.589420</td>
      <td>21.799833</td>
      <td>2010-07-07T13:28:50.120000</td>
      <td>2010-07-07 13:28:50.120</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Now that there are official datetime objects on the index we can start operating based on the time of the frame


{:.input_area}
```python
l_bins = df.groupby([df.index.year, df.index.month])
print(len(l_bins))
```

{:.output_stream}
```
54

```

Here we have used the groupby command to take the `'max_len'` column, called as a dictionary key, and create bins for our data to sit in according to year and then month. 

The object `l_bins` has `mean`, `max`, `std` etc. attributes in the same way as the numpy arrays we handled the other day.


{:.input_area}
```python
agg_spicules = df.groupby([df.index.year, df.index.month]).agg({'max_len': np.mean,
                                                                'max_len': np.std})

```


{:.input_area}
```python
agg_spicules
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>max_len</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th>datetime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="7" valign="top">2010</th>
      <th>6</th>
      <td>18.655367</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10.618364</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5.440305</td>
    </tr>
    <tr>
      <th>9</th>
      <td>6.979722</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3.391356</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10.337633</td>
    </tr>
    <tr>
      <th>12</th>
      <td>11.664923</td>
    </tr>
    <tr>
      <th rowspan="11" valign="top">2011</th>
      <th>1</th>
      <td>13.310975</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10.294977</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.966492</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.281308</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.832214</td>
    </tr>
    <tr>
      <th>7</th>
      <td>12.569426</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6.505276</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2.942115</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.148206</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.866478</td>
    </tr>
    <tr>
      <th>12</th>
      <td>5.405979</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">2012</th>
      <th>1</th>
      <td>4.531475</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10.022291</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12.585824</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.614694</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8.301316</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.185172</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>7.679454</td>
    </tr>
    <tr>
      <th>9</th>
      <td>6.678510</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6.273834</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.908986</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7.305525</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">2013</th>
      <th>1</th>
      <td>6.730764</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.328555</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.630605</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.048431</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.288040</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9.625425</td>
    </tr>
    <tr>
      <th>8</th>
      <td>10.699844</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.729928</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3.339021</td>
    </tr>
    <tr>
      <th>11</th>
      <td>7.889644</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7.797334</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">2014</th>
      <th>1</th>
      <td>5.005861</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.093437</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.225323</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15.910663</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.172536</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8.333880</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10.603654</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5.246553</td>
    </tr>
    <tr>
      <th>9</th>
      <td>7.447101</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3.560158</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4.900183</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7.838396</td>
    </tr>
  </tbody>
</table>
</div>
</div>



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



![png](../../images/chapters/09-time-series-data/08-Time-Series-Data_instructor_51_1.png)


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

<p>Now, to all the astronomers out there, let us process some real data. We have some <code>.txt</code> files containing the lightcurve from a recent paper. Can you process the data and show us the planet?</p>
<p>HINT: You'll need to treat this data slightly differently. The date here is in Julian Day so you will need to use <a href="http://docs.astropy.org/en/stable/api/astropy.time.Time.html">these</a> docs to convert it to a sensible datetime object, before you make the DataFrame.</p>

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

