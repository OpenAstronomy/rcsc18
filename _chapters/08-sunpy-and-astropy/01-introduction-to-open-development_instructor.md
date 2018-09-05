---
interact_link: 08-sunpy-and-astropy/01-introduction-to-open-development_instructor.ipynb
title: 'Introduction to Open Development'
permalink: 'chapters/08-sunpy-and-astropy/01-introduction-to-open-development'
previouschapter:
  url: 
  title: 'Sunpy and Astropy'
nextchapter:
  url: 
  title: 'Time Series Data'
redirect_from:
  - 'chapters/08-sunpy-and-astropy/01-introduction-to-open-development'
---

# SunPy and Astropy
## Open Development in Astrophysics

# Open Source

* Publically Accessible Code
* Freedoms to run and modify the code (explicitly set by a licence)
* Free as in zero cost

# Open Development

Where the development of the code is done in the open.

Including:

* Bug reports
* Feature Requests
* Commit logs
* Code review

**Enables anyone to contribute**

![a](sunpyorg.png)

![](./sunpy_header.png)
![](./sunpy_contributors.png)

![](cadair_contribution.png)

![](astropy_header.png)
![](numpy_header.png)
![](skimage_header.png)

# Get Involved!!

* https://sunpy.org/contribute.html
* http://www.astropy.org/contribute.html
* http://yt-project.org/
* https://numfocus.org/

# Demos!


{:.input_area}
```python
%matplotlib inline
import matplotlib.pyplot as plt
```


{:.input_area}
```python
from sunpy.data.sample import AIA_171_ROLL_IMAGE
import sunpy.map

m = sunpy.map.Map(AIA_171_ROLL_IMAGE)
m.peek()
plt.show()
```


![png](../../images/chapters/08-sunpy-and-astropy/01-introduction-to-open-development_instructor_10_0.png)


## Astropy and SunPy 😍


{:.input_area}
```python
import astropy.units as u
from astropy.coordinates import SkyCoord
```


{:.input_area}
```python
a_point = SkyCoord(200*u.arcsec, 300*u.arcsec, frame=m.coordinate_frame)
a_point
```




{:.output_data_text}
```
<SkyCoord (Helioprojective: obstime=2014-04-09 06:00:12.970000, rsun=696000000.0 m, observer=<HeliographicStonyhurst Coordinate (obstime=2014-04-09 06:00:12.970000): (lon, lat, radius) in (deg, deg, m)
    (0., -6.047074, 1.49860274e+11)>): (Tx, Ty) in arcsec
    (200., 300.)>
```




{:.input_area}
```python
im = m.plot()
ax = plt.gca()
ax.plot_coord(a_point, "o", markersize=12)
plt.show()
```


![png](../../images/chapters/08-sunpy-and-astropy/01-introduction-to-open-development_instructor_14_0.png)


# TimeSeries


{:.input_area}
```python
from sunpy.data.sample import GOES_XRS_TIMESERIES
```


{:.input_area}
```python
from sunpy.timeseries import TimeSeries
goes = TimeSeries(GOES_XRS_TIMESERIES)
goes.peek()
```


![png](../../images/chapters/08-sunpy-and-astropy/01-introduction-to-open-development_instructor_17_0.png)

