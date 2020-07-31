import numpy
from PIL import Image

imarray = numpy.random.rand(10000,10000,3) * 255
im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
im.save('result_image.png')