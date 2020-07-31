from PIL import Image

im = Image.open('result_image.png')

print(im.size)
width, height = im.size
print(width* height)