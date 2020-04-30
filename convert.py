import numpy as np
import PIL
import cv2
f = np.fromfile('test.txt', dtype='uint8')

print(f.shape)
img = f.reshape(26, 95)
cv2.imwrite('bash1.png', img)

