---
interact_link: 14-searching-and-downloading-data/01-searching-and-downloading-data_instructor.ipynb
title: 'Searching and Downloading Data'
permalink: 'chapters/14-searching-and-downloading-data/01-searching-and-downloading-data'
previouschapter:
  url: 
  title: 'Searching and Downloading Data'
nextchapter:
  url: 
  title: 'Final Exercise'
redirect_from:
  - 'chapters/14-searching-and-downloading-data/01-searching-and-downloading-data'
---

# Getting at Data

Both SunPy and Astropy have utilities for downloading data for your delectation. They are simple and easy to use, however increasing levels of computing will allow a great deal of personalisation and selection. Let us begin with SunPy

## Aquiring Data with SunPy

### Fido

The Federated Internet Data Obtainer (Fido) is the SunPy interface for downloading data from a wide variety of sources.

So what do we need?


{:.input_area}
```python
import astropy.units as u
from sunpy.net import Fido, attrs as a
```

This is your client object. This is effectively the intermediary between yourself and the treasure chest of solar data available. You query VSO, then VSO querys all data providers which fit the limiations you imposed during your search command. The VSO client also handles the particulars of dowloading the data onto your machiene. 

## Making a query

Lets kick off with an example, lets ask the veteran of solar imaging, SoHO for some EIS data, between the dates of between January 1st and 2nd, 2001,


{:.input_area}
```python
qr = Fido.search(a.Time('2001/1/1', '2001/1/2'), a.Instrument('eit'))
```

`qr` is the results of our search, it holds all the records that have been returned from all the services that matched the query.


{:.input_area}
```python
qr
```

### Break it down

So we can pass many attributes to the VSO, in this case we started with time

`a.Time('2001/1/1','2001/1/2')`

Start and end times for the query as strings, any date/time function can be understood by SunPy's parse_time function e.g. the datetime onjects we will look at later. Next we give it the instrument we want:

`a.Instrument('eit')`

You don't have to pass it an instrument, the client will find all available missions in the parameter you've defined if you like. Next, wavelength:

`a.Wave(14.2*u.nm, 12.3*u.nm)`

We pass it a min and max wavelength. This has to be an astropy units quantity (in SI for the love of coffee). If you don't you will get an error.
 
For a full list of attributes that vso can take use:


{:.input_area}
```python
a
```

## More Complex Searching

In this example we will use the logical operators to combine attributes into a complex multi-instrument query.

You can use the & and operator or the `|` or operator to make queries. In the previous example all arguments to `Fido.search` had the and operator applied, we performed a search where the Instrument and the Wavelength and the time matched. We could have done this explicitly like this:


{:.input_area}
```python
mysearch = a.Time("2016/02/03", "2016/02/03T00:10:00") & a.Instrument('AIA')
Fido.search(mysearch)
```

If we want to do the same query but for two seperate wavelengths we can use the `|` or operator:


{:.input_area}
```python
instrument = a.Time("2016/02/03", "2016/02/03T00:10:00") & a.Instrument('AIA')
wavelength = a.Wavelength(17.1*u.nm, 17.1*u.nm) | a.Wavelength(304*u.AA, 304*u.AA)
mysearch = instrument & wavelength

Fido.search(mysearch)
```

### Multiple Instruments

In this example we want to download one image from STEREO A EUVI and one image from SDO AIA as close together in time as we can. To do this we will define a search for the AIA image and a search for the EUVI image then 'or' them together.


{:.input_area}
```python
stereo = (a.vso.Source('STEREO_B') &
          a.Instrument('EUVI') &
          a.Time('2011-01-01', '2011-01-01T00:10:00'))

aia = (a.Instrument('AIA') &
       a.Sample(24 * u.hour) &
       a.Time('2011-01-01', '2011-01-02'))

wave = a.Wavelength(30 * u.nm, 31 * u.nm)
```


{:.input_area}
```python
results = Fido.search(stereo | aia, wave)
results
```


{:.input_area}
```python
files = Fido.fetch(results)
files
```

## HEK

The Heliophysics Event Knowledgebase (HEK) is a repository of feature and event information about the Sun. Entries are generated both by automated algorithms and human observers.

We need to set up HEK:


{:.input_area}
```python
from sunpy.net import hek
hek_client = hek.HEKClient()
```

Creating a very similar client as we saw with VSO above.

Given that HEK is a database of solar events of interest, the query has different requirements to VSO. It needs start and end times, and an event type. Again time objects can be defined as datetime objects or correctly formatted strings.

Event types are specified as uppercase two letter strings found on [the HEK website](http://www.lmsal.com/hek/VOEvent_Spec.html)


{:.input_area}
```python
tstart = '2011/08/09 07:23:56'
tend = '2011/08/09 12:40:29'
event_type = 'FL'
result = hek_client.search(hek.attrs.Time(tstart,tend),
                           hek.attrs.EventType(event_type))
```

Notice that the HEK query is extremely similar to the VSO query style, with our attributes defined accordingly.

Instead of returning a list, HEK returns a list of dictionary objects. Each entry in the dictionary sis a pair of key-value pairs that exactly correspond to the parameters. We can return the key words using:


{:.input_area}
```python
result[0].keys()
```

Remember, the HEK query we made returns all the flares in the time-range stored in the HEK, regardless of the feature recognition method. The HEK parameter which stores the the feature recognition method is called “frm_name”. Using list comprehensions (which are very cool), it is easy to get a list of the feature recognition methods used to find each of the flares in the result object, for example:


{:.input_area}
```python
for elem in result: 
    print(elem["frm_name"])
```

This way we can avoid troublesome doubling up of results. We can do the same `help(hek.attrs)` command as VSO to fins out further options. 

## Aquiring data with AstroQuery

Astroquery supports a plethora of [services](https://astroquery.readthedocs.org/en/latest/#using-astroquery), all of which follow roughly the same API (application program interface). In its simplest for the API involves queries based on coordinates or object names e.g. using SIMBAD:


{:.input_area}
```python
from astroquery.simbad import Simbad
result_table = Simbad.query_object("m1")
result_table.pprint(show_unit=True)
```

In this case the query is looking at a specific set of coordinates


{:.input_area}
```python
from astropy import coordinates
import astropy.units as u
c = coordinates.SkyCoord("05h35m17.3s -05d23m28s", frame='icrs')
r = 5 * u.arcminute
result = Simbad.query_region(c, radius=r)
result.pprint(show_unit=True, max_width=80, max_lines=5)
```

These methods can be expanded to all the following modules


*    SIMBAD Queries (astroquery.simbad)
*    IRSA Dust Extinction Service Queries (astroquery.irsa_dust)
*    NED Queries (astroquery.ned)
*    Splatalogue Queries (astroquery.splatalogue)
*    IRSA Image Server program interface (IBE) Queries (astroquery.ibe)
*    IRSA Queries (astroquery.irsa)
*    UKIDSS Queries (astroquery.ukidss)
*    MAGPIS Queries (astroquery.magpis)
*    NRAO Queries (astroquery.nrao)
*    Besancon Queries (astroquery.besancon)
*    NIST Queries (astroquery.nist)
*    NVAS Queries (astroquery.nvas)
*    GAMA Queries (astroquery.gama)
*    ESO Queries (astroquery.eso)
*    Atomic Line List (astroquery.atomic)
*    ALMA Queries (astroquery.alma)
*    Skyview Queries (astroquery.skyview)
*    NASA ADS Queries (astroquery.nasa_ads)
*    HEASARC Queries (astroquery.heasarc)



# Combining Queries and Plotting

Using astroquery and wcsaxes together we can download both an image and a star field and over plot them. To download an image we can use the Simbad service:


{:.input_area}
```python
from astroquery.skyview import SkyView#
import astropy.units as u
```


{:.input_area}
```python
m42_images = SkyView.get_images(position='M42', survey=['2MASS-K'],
                                pixels=2000)
```


{:.input_area}
```python
m42_images
```

<section class="objectives panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Plot this image using WCSAxes </h2>
</div>
<ul>
<li>
Create a WCS object.
</li>
<li>
Create a figure with the projection set to the WCS object
</li>
<li>
Plot the image.
</li>
</ul>
</section>


{:.input_area}
```python
from astropy.wcs import WCS
import matplotlib.pyplot as plt
%matplotlib notebook
```


{:.input_area}
```python
m42 = m42_images[0]
```


{:.input_area}
```python
wcs = WCS(m42[0].header)
```


{:.input_area}
```python
fig, ax = plt.subplots(subplot_kw={'projection':wcs})
im = ax.imshow(m42[0].data, cmap='gray', vmax=900)
plt.colorbar(im)
```

Download some catalog data:


{:.input_area}
```python
from astroquery.irsa import Irsa
```


{:.input_area}
```python
Irsa.ROW_LIMIT = 1e6
```


{:.input_area}
```python
table = Irsa.query_region("m42", catalog="fp_psc", spatial="Cone",
                          radius=15*u.arcmin)
```


{:.input_area}
```python
table.show_in_notebook()
```


{:.input_area}
```python
table2 = table[table['h_m']< 12.]
```


{:.input_area}
```python
fig, ax = plt.subplots(subplot_kw={'projection':wcs})
im = ax.imshow(m42[0].data, cmap='gray', vmax=900, interpolation='none')

ax.set_autoscale_on(False)

sc = plt.scatter(table2['ra'], table2['dec'], c=table2['h_m'],
                 cmap='viridis', transform=ax.get_transform('fk5'))
plt.colorbar(sc)
```
