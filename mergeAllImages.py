'''
/**
* @author Karine Mendes Tavares
*/
'''

import shutil
import os
from PIL import Image
from PIL import ImageOps

# Configuration.
os.chdir('K:')
path = os.getcwd()

# Funciton to copy and rename images to another fold.
def copyAndRenameImages(original_img_folder, copy_img_folder):
    # Iteract in the files directory.
    for dir in os.listdir(original_img_folder):
        print(f"Class {dir}")

        for file in os.listdir(os.path.join(original_img_folder, dir)):
            image_path = os.path.join(original_img_folder, dir, file)#{img_folder}{dir=4a|4b|4c}{file}
            # Copy image to new directory (original, target)
            shutil.copy(image_path,os.path.join(copy_img_folder, dir + "_class_" + file))

# Funciton to rotate images.
# Param img_folder - contains the image folder path.
# Param rotation angle - angle which you want to be rotated.
def rotate_augmentation(img_folder, rotation_angle):
    # Iteract in the files directory.
    for file in os.listdir(img_folder):
        image_path = os.path.join(img_folder, file)
        image = Image.open(image_path)

        # Rotate according to rotation_angle and save the image in a new directory.
        angle = int(360/rotation_angle)
        for i in range(1,angle):
            rotated_image = image.rotate(i*rotation_angle)
            rotated_image.save(f"{img_folder}\\r_{i}_{file}", quality=100) #{img_folder}-rotate_augmentation

# Function to mirror images.
# Param img_folder - contains the image folder path.
def mirroring_augmentation(img_folder):
    # Iteract in the files directory.
    for file in os.listdir(img_folder):
        image_path = os.path.join(img_folder,  file)
        image = Image.open(image_path)
        
        # Mirror and save image in a new directory.
        mirror_image = ImageOps.mirror(image)
        mirror_image.save(f"{img_folder}\\m_{file}", quality=100) #{img_folder}-mirroring_augmentation

# Function to augmentate data. Execute roation and mirroring in the images.
# Param img_folder - contains the image folder path.
# Param rotation angle - angle which you want to be rotated.
def data_augmentation(img_folder, rotation_angle):
    rotate_augmentation(img_folder, rotation_angle)
    mirroring_augmentation(img_folder)

original_img_folder = os.path.dirname(path)+'\Datasets\Colombiam\\split\\360x360-dataset-category-4-split\\full-dataset'
copy_img_folder = os.path.dirname(path)+'\Datasets\Colombiam\\split\\360x360-dataset-category-4-split\\full-dataset-all'
backgroun_w = 360
backgroun_h = 360

# copyAndRenameImages(original_img_folder, copy_img_folder)
data_augmentation(copy_img_folder, 45)