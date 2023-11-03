"""

PixelMeaner is a simple script that takes the average of pixel RGB values.
For each image.
Extracts the RGB values of each pixel and stores them in a numpy array.
Averages each numpy array representation of the RGB values.
Stores the resulting averaged RBG values of each image file in a new numPy array.
Finally, it takes the average of the new array containing the averages of each image.
And creates a new image with the resulting averaged numpy array.

Copyright(C) 2023 Celal Umut Aydınoğlu

"""




import os
from PIL import Image
import numpy as np

input_dir = "flags"
output_dir = "avg_flags"


def avg_matrix(matrix):

    mean_r = np.mean(matrix[:, :, 0])
    mean_g = np.mean(matrix[:, :, 1])
    mean_b = np.mean(matrix[:, :, 2])

    avg_color = np.array([mean_r, mean_g, mean_b], dtype=np.uint8)

    return avg_color


def avg_flags(path, name):

    im = Image.open(path)

    if im.mode != "RGBA":
        im = im.convert("RGBA")

    matrix_im = np.array(im)

    average = avg_matrix(matrix_im)

    return average


array = np.empty((1, 1, 3))

for file in os.listdir(input_dir):

    average = avg_flags(os.path.join(input_dir, file), file).reshape(1, 1, 3)

    array = np.append(array, average, axis=1)


ro = array.round()
indices = np.where(~np.all(ro == [0., 0., 0.], axis=2))

formatted_array = ro[indices].astype(np.int32)
reshaped_array = formatted_array.reshape((-1, 250, 3))

final_array = avg_matrix(reshaped_array)

final_image = Image.new("RGB", (128, 64), tuple(final_array))
final_image.save("blend.png")





