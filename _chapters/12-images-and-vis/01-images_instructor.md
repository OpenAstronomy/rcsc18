---
interact_link: 12-images-and-vis/01-images_instructor.ipynb
title: 'Images'
permalink: 'chapters/12-images-and-vis/01-images'
previouschapter:
  url: 
  title: 'Images and Vis'
nextchapter:
  url: 
  title: ''
redirect_from:
  - 'chapters/12-images-and-vis/01-images'
---

# Images and Image Plotting

## Learning Objectives

- Read a FITS file
- Load and display an image
- Use array slicing operations to display part of a cube
- Use SunPy to explore a multi-dimensional array

## Arrays as images

All photographic images represent a measurement of how much light hits the receiver. For instance, the [Hubble image](http://imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/21572/full_jpg.jpg) below is obtained by measuring the brightnesses of distant stars:

![Hubble image](hubble.jpg)

With traditional optical cameras, this measurement results in an image which is continuous, as it is projected directly onto paper or some other object. In order to store images digitally, they need to be divided into discrete chunks, pixels, each of which contains the value of the measurement in that small portion of the image. In this representation, an image is simply a grid of numbers, which allows it to be easily stored as an array with a shape equal to the resolution of the image.

SunPy has some example data that we'll be using to demontrate this principle.


{:.input_area}
```python
# Usual imports
%matplotlib notebook
import matplotlib.pyplot as plt
from astropy.io import fits
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ModuleNotFoundError                       Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-1-08ea5d21a751> in <module>()
      2 get_ipython().run_line_magic('matplotlib', 'notebook')
      3 import matplotlib.pyplot as plt
----> 4 from astropy.io import fits

```

{:.output_traceback_line}
```
ModuleNotFoundError: No module named 'astropy'
```



{:.input_area}
```python
# Get the example data for this lesson
from astropy.utils.data import download_file
cube_file = download_file("http://data.sunpy.org/sunkit-sst/CRISP_TXY_Cube.fits.gz", cache=True)
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ModuleNotFoundError                       Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-2-6cdda762ffd3> in <module>()
      1 # Get the example data for this lesson
----> 2 from astropy.utils.data import download_file
      3 cube_file = download_file("http://data.sunpy.org/sunkit-sst/CRISP_TXY_Cube.fits.gz", cache=True)

```

{:.output_traceback_line}
```
ModuleNotFoundError: No module named 'astropy'
```


The above command will download the example data if it isn't present, and store it in a FITS file. We will read the data from this file, but for this lesson we will not be considering any coordinate information in the header. We will be covering that tomorrow.


{:.input_area}
```python
# Check the file exists
cube_file
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
<ipython-input-3-e437870bd844> in <module>()
      1 # Check the file exists
----> 2 cube_file

```

{:.output_traceback_line}
```
NameError: name 'cube_file' is not defined
```



{:.input_area}
```python
# Load the data
cube = fits.getdata(cube_file)
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
<ipython-input-4-20998eba63f6> in <module>()
      1 # Load the data
----> 2 cube = fits.getdata(cube_file)

```

{:.output_traceback_line}
```
NameError: name 'fits' is not defined
```


This file is a time, solar-x, solar-y cube. To start off with we will be using the first image.


{:.input_area}
```python
# Check what dimensions our data have so we know how to slice the array
cube.shape
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
<ipython-input-5-1c34774ae451> in <module>()
      1 # Check what dimensions our data have so we know how to slice the array
----> 2 cube.shape

```

{:.output_traceback_line}
```
NameError: name 'cube' is not defined
```



{:.input_area}
```python
sunspot = cube[0]
sunspot.shape
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
<ipython-input-6-acd9ded3c24b> in <module>()
----> 1 sunspot = cube[0]
      2 sunspot.shape

```

{:.output_traceback_line}
```
NameError: name 'cube' is not defined
```


Once read in as an array, the image can be processed in the same ways as any other array. For instance, we can easily find the highest, lowest and mean values of the image, the type of the variables stored in the array, and the resolution of the image:


{:.input_area}
```python
# Output the image minimum, mean and maximum.
print('Image min:', sunspot.min(), '; Image mean:', sunspot.mean(), '; Image max: ', sunspot.max())

# Output the array dtype.
print('Data type:', sunspot.dtype)

# Output image size.
print('Image size:', sunspot.shape)
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
<ipython-input-7-6739a02eb598> in <module>()
      1 # Output the image minimum, mean and maximum.
----> 2 print('Image min:', sunspot.min(), '; Image mean:', sunspot.mean(), '; Image max: ', sunspot.max())
      3 
      4 # Output the array dtype.
      5 print('Data type:', sunspot.dtype)

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


## Plotting images

While storing an image as a grid of numbers is very useful for analysis, we still need to be able to visually inspect the image. This can be achieved with `plt.imshow()`, which allocates a colour to every element in the array according to its value.


{:.input_area}
```python
# Display image array with imshow()
plt.imshow(sunspot)
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
<ipython-input-8-1eae2b9b1d6f> in <module>()
      1 # Display image array with imshow()
----> 2 plt.imshow(sunspot)

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


When plotting an image in this way, you will often need to know what actual values correspond to the colours. To find this out, we can draw a colour bar alongside the image which indicates the mapping of values to colours:


{:.input_area}
```python
plt.imshow(sunspot)
plt.colorbar()
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
<ipython-input-9-f3c12b8f90bb> in <module>()
----> 1 plt.imshow(sunspot)
      2 plt.colorbar()

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


Fortunately, matplotlib provides a large variety of colour maps which are suitable for various different purposes (more on this later). `plt.imshow()` has a `cmap` keyword argument which can be passed a string defining the desired colour map.


{:.input_area}
```python
# Display the image with a more monochrome colour map.
plt.imshow(sunspot, cmap='gray')
plt.colorbar()
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
<ipython-input-10-a7f633b71da0> in <module>()
      1 # Display the image with a more monochrome colour map.
----> 2 plt.imshow(sunspot, cmap='gray')
      3 plt.colorbar()

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


The full list of available colour maps (for matplotlib 2.2.3) and some discussion on how to use them can be found [here](https://matplotlib.org/tutorials/colors/colormaps.html).

<section class="callout panel panel-info">
<div class="panel-heading">
<h3><span class="fa fa-certificate"></span> Colour maps </h3>
</div>

As the images above demonstrate, the choice of colour map can make a significant difference to how your image appears, and is therefore extremely important. This is partly due to discrepancies between how quickly the colour map changes and how quickly the data changes, and partly due to the fact that [different people see colour differently](https://en.wikipedia.org/wiki/The_dress_%28viral_phenomenon%29).<br/><br/>

In particular, the `'jet'` (rainbow) colour map used as a default in many plotting packages (including matplotlib 1.x) is notoriously bad for displaying data. This is because it is not designed taking into account how the human eye percieves colour. This leads to some parts of the colour map appearing to change very slowly, while other parts of the colour map shift from one hue to another in a very short space. The practical effect of this is to both smooth some parts of the image, obscuring the data, and to create artificial features in the image where the data is smooth.<br/><br/>

There is no single 'best' colour map - different colour maps display different kinds of image most clearly - but the `'jet'` map is almost never an appropriate choice for displaying any data. In general, colour maps which vary luminosity uniformly (such as the `'gray'` colour map above or the `'cubehelix'` colour map) tend to be better. Plots of various colour maps' luminosities can be found [here](http://matplotlib.org/users/colormaps.html). If you're not sure what colour map to use, the main defaults in matplotlib 2.x are well designed and are generally safe bets. Older versions use `'jet'` as the default, so be aware of that.<br/><br/>

For a good background on this topic and a description of a decent all-round colour map scheme, see [this paper](http://www.kennethmoreland.com/color-maps/ColorMapsExpanded.pdf).

**TL;DR: never use a rainbow colour map.**

</section>

<section class="challenges panel panel-success">
<div class="panel-heading">
<h3><span class="fa fa-pencil"></span> Load and plot an image </h3>
</div>

<ol>
    <li> Plot a Time-Space slice of the array (try plotting the ~720th row of the data across the sunspot)</li>
    <li> Change the colour map and add a colour bar. Also add axis labels.</li>
</ol>
</section>


{:.input_area}
```python
# 1

plt.imshow(cube[:,720,:].T, aspect='auto')
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
<ipython-input-11-1fc6c416be5e> in <module>()
      1 # 1
      2 
----> 3 plt.imshow(cube[:,720,:].T, aspect='auto')

```

{:.output_traceback_line}
```
NameError: name 'cube' is not defined
```



{:.input_area}
```python
# 2

# Display my image
plt.imshow(cube[:,720,:].T, aspect='auto', cmap='magma')
plt.colorbar()
plt.xlabel("Time")
plt.ylabel("y pixels")
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
<ipython-input-12-2260be29c877> in <module>()
      2 
      3 # Display my image
----> 4 plt.imshow(cube[:,720,:].T, aspect='auto', cmap='magma')
      5 plt.colorbar()
      6 plt.xlabel("Time")

```

{:.output_traceback_line}
```
NameError: name 'cube' is not defined
```


### Value limits

The default behaviour of `imshow()` in terms of colour mapping is that the colours cover the full range of the data so that the lower end (blue, in the plots above) represents the smallest value in the array, and the higher end (red) represents the greatest value.

This is fine if rest of the values are fairly evenly spaced between these extremes. However, if we have a very low minimum or very high maximum compared to the rest of the image, this default scaling is unhelpful. To deal with this problem, `imshow()` allows you to set the minimum and maximum values used for the scaling with the `vmin` and `vmax` keywords.


{:.input_area}
```python
plt.imshow(sunspot, cmap='gray', vmin=75, vmax=6000)
plt.colorbar()
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
<ipython-input-13-45581763362d> in <module>()
----> 1 plt.imshow(sunspot, cmap='gray', vmin=75, vmax=6000)
      2 plt.colorbar()

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


As you can see, this allows us to increase the contrast of the image at the cost of discounting extreme values, or we can include a broader range of values but see less detail. Similar effects can also be achieved with the `norm` keyword, which allows you to set how `imshow()` scales values in order to map them to colours (linear or logarithmic scaling, for example).

### Axes

You will notice in the above plots that the axes are labelled with the pixel coordinates of the image. You will also notice that the origin of the axes is in the top left corner rather than the bottom left. This is a convention in image-drawing, but can be changed if necessary by setting the `origin` keyword to `'lower'` when calling `imshow()`:


{:.input_area}
```python
plt.imshow(sunspot, cmap='gray', origin='lower')
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
<ipython-input-14-ed210a5ba203> in <module>()
----> 1 plt.imshow(sunspot, cmap='gray', origin='lower')

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


`imshow()` also allows you to change the upper and lower values of each axis, and the appropriate tick labels will be drawn. This feature can be used to apply physical spatial scales to the image (if you know them) rather than going purely on pixel positions, which may be less useful. This is done with the `extent` keyword, which takes a list of values corresponding to lower and upper x values and the lower and upper y values (in that order).


{:.input_area}
```python
plt.imshow(sunspot, cmap='gray', origin='lower', extent=[413, 470, 223, 277])
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
<ipython-input-15-7bc9830a179d> in <module>()
----> 1 plt.imshow(sunspot, cmap='gray', origin='lower', extent=[413, 470, 223, 277])

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


<section class="objectives panel panel-success">
<div class="panel-heading">
<h3><span class="fa fa-pencil"></span> Value and axes limits </h3>
</div>

<ol>
    <li>Plot your chosen image again. Try changing the upper and lower limits of the plotted values to adjust how the image appears.</li>
</ol>
</section>


{:.input_area}
```python
# 1 

# Display the coins image with adjusted value range
plt.imshow(sunspot, cmap='magma', vmin=60, vmax=5000)
plt.colorbar()
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
<ipython-input-16-5c69cdf59a64> in <module>()
      2 
      3 # Display the coins image with adjusted value range
----> 4 plt.imshow(sunspot, cmap='magma', vmin=60, vmax=5000)
      5 plt.colorbar()

```

{:.output_traceback_line}
```
NameError: name 'sunspot' is not defined
```


## Interpolation

In order to display a smooth image, `imshow()` automatically interpolates to find what values should be displayed between the given data points. The default interpolation scheme is `'linear'`, which interpolates linearly between points, as you might expect. The interpolation can be changed with yet another keyword in `imshow()`. Here are a few examples:


{:.input_area}
```python
fig, ax = plt.subplots(2, 2, figsize=(10, 10))
smallim = cube[10, 250:750, :]
ax[0, 0].imshow(smallim) # Default (linear) interpolation
ax[0, 1].imshow(smallim, interpolation='bicubic') # Bicubic interpolation
ax[1, 0].imshow(smallim, interpolation='nearest') # Nearest-neighbour interpolation
ax[1, 1].imshow(smallim, interpolation='none') # No interpolation
```


{:.output_data_text}
```
<IPython.core.display.Javascript object>
```



<div markdown="0">
<div id='be2cf350-a4a9-41d0-9e2e-9211c3ee21c0'></div>
</div>



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
<ipython-input-17-485fd812a2fa> in <module>()
      1 fig, ax = plt.subplots(2, 2, figsize=(10, 10))
----> 2 smallim = cube[10, 250:750, :]
      3 ax[0, 0].imshow(smallim) # Default (linear) interpolation
      4 ax[0, 1].imshow(smallim, interpolation='bicubic') # Bicubic interpolation
      5 ax[1, 0].imshow(smallim, interpolation='nearest') # Nearest-neighbour interpolation

```

{:.output_traceback_line}
```
NameError: name 'cube' is not defined
```


This can be a useful way to change how the image appears. For instance, if the exact values of the data are extremely important, little or no interpolation may be appropriate so the original values are easier to discern, whereas a high level of interpolation can be used if the smoothness of the image is more important than the actual numbers.

Note that that `'none'` in the `imshow()` call above is NOT the same as `None`. `None` tells `imshow()` you are not passing it a variable for the `interpolation` keyword, so it uses the default, whereas `'none'` explicitly tells it not to interpolate.

## SunPy Cube Explorer

SunPy has an `ImageAnimator` class that will create sliders for each axis not used for plotting the image. By default it uses the last two axes of the array to plot the image.


{:.input_area}
```python
from sunpy.visualization.imageanimator import ImageAnimator
```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ModuleNotFoundError                       Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-18-432750cb5719> in <module>()
----> 1 from sunpy.visualization.imageanimator import ImageAnimator

```

{:.output_traceback_line}
```
ModuleNotFoundError: No module named 'sunpy'
```



{:.input_area}
```python
ImageAnimator(cube, colorbar=True, cmap="plasma")
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
<ipython-input-19-f60eda19b263> in <module>()
----> 1 ImageAnimator(cube, colorbar=True, cmap="plasma")

```

{:.output_traceback_line}
```
NameError: name 'ImageAnimator' is not defined
```

