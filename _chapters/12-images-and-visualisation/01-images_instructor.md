---
interact_link: 12-images-and-visualisation/01-images_instructor.ipynb
title: 'Images'
permalink: 'chapters/12-images-and-visualisation/01-images'
previouschapter:
  url: 
  title: 'Images and Visualisation'
nextchapter:
  url: 
  title: 'Images in Astronomy'
redirect_from:
  - 'chapters/12-images-and-visualisation/01-images'
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
import matplotlib.pyplot as plt
from astropy.io import fits
```


{:.input_area}
```python
# Get the example data for this lesson
from astropy.utils.data import download_file
cube_file = download_file("http://data.sunpy.org/sunkit-sst/CRISP_TXY_Cube.fits.gz", cache=True)
```

The above command will download the example data if it isn't present, and store it in a FITS file. We will read the data from this file, but for this lesson we will not be considering any coordinate information in the header. We will be covering that tomorrow.


{:.input_area}
```python
# Check the file exists
cube_file
```




{:.output_data_text}
```
'/home/stuart/.astropy/cache/download/py3/a2460f944e47f8d2bca6f8e366f2004c'
```




{:.input_area}
```python
# Load the data
cube = fits.getdata(cube_file)
```

This file is a time, solar-x, solar-y cube. To start off with we will be using the first image.


{:.input_area}
```python
# Check what dimensions our data have so we know how to slice the array
cube.shape
```




{:.output_data_text}
```
(50, 966, 980)
```




{:.input_area}
```python
sunspot = cube[0]
sunspot.shape
```




{:.output_data_text}
```
(966, 980)
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

{:.output_stream}
```
Image min: 0.0 ; Image mean: 1875.7292 ; Image max:  8677.0
Data type: >f4
Image size: (966, 980)

```

## Plotting images

While storing an image as a grid of numbers is very useful for analysis, we still need to be able to visually inspect the image. This can be achieved with `plt.imshow()`, which allocates a colour to every element in the array according to its value.


{:.input_area}
```python
# Display image array with imshow()
plt.imshow(sunspot)
```




{:.output_data_text}
```
<matplotlib.image.AxesImage at 0x7f654e86b668>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_15_1.png)


When plotting an image in this way, you will often need to know what actual values correspond to the colours. To find this out, we can draw a colour bar alongside the image which indicates the mapping of values to colours:


{:.input_area}
```python
plt.imshow(sunspot)
plt.colorbar()
```




{:.output_data_text}
```
<matplotlib.colorbar.Colorbar at 0x7f654e485b70>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_17_1.png)


Fortunately, matplotlib provides a large variety of colour maps which are suitable for various different purposes (more on this later). `plt.imshow()` has a `cmap` keyword argument which can be passed a string defining the desired colour map.


{:.input_area}
```python
# Display the image with a more monochrome colour map.
plt.imshow(sunspot, cmap='gray')
plt.colorbar()
```




{:.output_data_text}
```
<matplotlib.colorbar.Colorbar at 0x7f654e3ba5f8>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_19_1.png)


The full list of available colour maps (for matplotlib 2.2.3) and some discussion on how to use them can be found [here](https://matplotlib.org/tutorials/colors/colormaps.html).


<section class="callout panel panel-warning">
<div class="panel-heading">
<h2><span class="fa fa-thumb-tack"></span> Colourmaps</h2>
</div>


<div class="panel-body">

<p>As the images above demonstrate, the choice of colour map can make a significant difference to how your image appears, and is therefore extremely important. This is partly due to discrepancies between how quickly the colour map changes and how quickly the data changes, and partly due to the fact that <a href="https://en.wikipedia.org/wiki/The_dress_%28viral_phenomenon%29">different people see colour differently</a>.<br/><br/></p>
<p>In particular, the <code>'jet'</code> (rainbow) colour map used as a default in many plotting packages (including matplotlib 1.x) is notoriously bad for displaying data. This is because it is not designed taking into account how the human eye percieves colour. This leads to some parts of the colour map appearing to change very slowly, while other parts of the colour map shift from one hue to another in a very short space. The practical effect of this is to both smooth some parts of the image, obscuring the data, and to create artificial features in the image where the data is smooth.<br/><br/></p>
<p>There is no single 'best' colour map - different colour maps display different kinds of image most clearly - but the <code>'jet'</code> map is almost never an appropriate choice for displaying any data. In general, colour maps which vary luminosity uniformly (such as the <code>'gray'</code> colour map above or the <code>'cubehelix'</code> colour map) tend to be better. Plots of various colour maps' luminosities can be found <a href="http://matplotlib.org/users/colormaps.html">here</a>. If you're not sure what colour map to use, the main defaults in matplotlib 2.x are well designed and are generally safe bets. Older versions use <code>'jet'</code> as the default, so be aware of that.<br/><br/></p>
<p>For a good background on this topic and a description of a decent all-round colour map scheme, see <a href="http://www.kennethmoreland.com/color-maps/ColorMapsExpanded.pdf">this paper</a>.</p>
<p><strong>TL;DR: never use a rainbow colour map.</strong></p>

</div>

</section>



<section class="challange panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Load and plot an image</h2>
</div>


<div class="panel-body">

<p>Plot a Time-Space slice of the array (try plotting the ~720th row of the data across the sunspot)
Change the colour map and add a colour bar. Also add axis labels.</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>

</section>



{:.input_area}
```python
# 1

plt.imshow(cube[:,720,:].T, aspect='auto')
```




{:.output_data_text}
```
<matplotlib.image.AxesImage at 0x7f654e323f60>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_24_1.png)



{:.input_area}
```python
# 2

# Display my image
plt.imshow(cube[:,720,:].T, aspect='auto', cmap='magma')
plt.colorbar()
plt.xlabel("Time")
plt.ylabel("y pixels")
```




{:.output_data_text}
```
Text(0,0.5,'y pixels')
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_25_1.png)


### Value limits

The default behaviour of `imshow()` in terms of colour mapping is that the colours cover the full range of the data so that the lower end (blue, in the plots above) represents the smallest value in the array, and the higher end (red) represents the greatest value.

This is fine if rest of the values are fairly evenly spaced between these extremes. However, if we have a very low minimum or very high maximum compared to the rest of the image, this default scaling is unhelpful. To deal with this problem, `imshow()` allows you to set the minimum and maximum values used for the scaling with the `vmin` and `vmax` keywords.


{:.input_area}
```python
plt.imshow(sunspot, cmap='gray', vmin=75, vmax=6000)
plt.colorbar()
```




{:.output_data_text}
```
<matplotlib.colorbar.Colorbar at 0x7f654e95fa90>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_28_1.png)


As you can see, this allows us to increase the contrast of the image at the cost of discounting extreme values, or we can include a broader range of values but see less detail. Similar effects can also be achieved with the `norm` keyword, which allows you to set how `imshow()` scales values in order to map them to colours (linear or logarithmic scaling, for example).

### Axes

You will notice in the above plots that the axes are labelled with the pixel coordinates of the image. You will also notice that the origin of the axes is in the top left corner rather than the bottom left. This is a convention in image-drawing, but can be changed if necessary by setting the `origin` keyword to `'lower'` when calling `imshow()`:


{:.input_area}
```python
plt.imshow(sunspot, cmap='gray', origin='lower')
```




{:.output_data_text}
```
<matplotlib.image.AxesImage at 0x7f654e192710>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_32_1.png)


`imshow()` also allows you to change the upper and lower values of each axis, and the appropriate tick labels will be drawn. This feature can be used to apply physical spatial scales to the image (if you know them) rather than going purely on pixel positions, which may be less useful. This is done with the `extent` keyword, which takes a list of values corresponding to lower and upper x values and the lower and upper y values (in that order).


{:.input_area}
```python
plt.imshow(sunspot, cmap='gray', origin='lower', extent=[413, 470, 223, 277])
```




{:.output_data_text}
```
<matplotlib.image.AxesImage at 0x7f654e16a048>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_34_1.png)



<section class="challenge panel panel-success">
<div class="panel-heading">
<h2><span class="fa fa-pencil"></span> Value and axes limits</h2>
</div>


<div class="panel-body">

<p>Plot your chosen image again. Try changing the upper and lower limits of the plotted values to adjust how the image appears.</p>

</div>

</section>



<section class="solution panel panel-primary">
<div class="panel-heading">
<h2><span class="fa fa-eye"></span> Solution</h2>
</div>

</section>



{:.input_area}
```python
# 1 

# Display the coins image with adjusted value range
plt.imshow(sunspot, cmap='magma', vmin=60, vmax=5000)
plt.colorbar()
```




{:.output_data_text}
```
<matplotlib.colorbar.Colorbar at 0x7f654c27d4e0>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_37_1.png)


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
<matplotlib.image.AxesImage at 0x7f654c167ac8>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_40_1.png)


This can be a useful way to change how the image appears. For instance, if the exact values of the data are extremely important, little or no interpolation may be appropriate so the original values are easier to discern, whereas a high level of interpolation can be used if the smoothness of the image is more important than the actual numbers.

Note that that `'none'` in the `imshow()` call above is NOT the same as `None`. `None` tells `imshow()` you are not passing it a variable for the `interpolation` keyword, so it uses the default, whereas `'none'` explicitly tells it not to interpolate.

## SunPy Cube Explorer

SunPy has an `ImageAnimator` class that will create sliders for each axis not used for plotting the image. By default it uses the last two axes of the array to plot the image.


{:.input_area}
```python
from sunpy.visualization.imageanimator import ImageAnimator
```


{:.input_area}
```python
ImageAnimator(cube, colorbar=True, cmap="plasma")
```




{:.output_data_text}
```
<sunpy.visualization.imageanimator.ImageAnimator at 0x7f6546ee4ac8>
```




![png](../../images/chapters/12-images-and-visualisation/01-images_instructor_45_1.png)

