from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

me = Image.open("/Users/kantel/git/python-schulung/sources/atomipython/images/jkantel2.jpg")
arr = np.array(me.getdata(), np.uint8).reshape(me.size[1], me.size[0], 3)

plt.imshow(arr)
plt.colorbar()
plt.show()
