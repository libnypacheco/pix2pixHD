#Take two separate folder of images and compare them to find the common images. Delete the images that are not common in both the folders.
# The images in the folder are in the format of .png
# The images are compared based on the image name and deleted if not common in both the folders.

import os
import shutil

# Path of the folder containing the images
folder1 = '/Users/libnypacheco/Documents/GitHub/pix2pixHD/datasets/w/train_A'
folder2 = '/Users/libnypacheco/Documents/GitHub/pix2pixHD/datasets/w/train_B'

# List the images in the folder
images1 = os.listdir(folder1)
images2 = os.listdir(folder2)

# Compare the images in the folder
for image in images1:
    if image not in images2:
        os.remove(os.path.join(folder1, image))

for image in images2:
    if image not in images1:
        os.remove(os.path.join(folder2, image))

print('Common images are retained in both the folders')

# End of code

# Output:
# Common images are retained in both the folders