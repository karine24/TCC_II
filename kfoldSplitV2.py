'''
/**
* @author Karine Mendes Tavares
*/
'''

import splitfolders
import os
from sklearn.model_selection import KFold, StratifiedGroupKFold
from random import sample
import pandas as pd
import shutil
import numpy as np

# Configuration.
os.chdir('K:')
path = os.getcwd()

group_id = 0

def getGroupsList(files_dir):
    global group_id
    map = {}
    groups = []
    for file_name in os.listdir(files_dir):
        patient_id = file_name.split('_')[0]
        map_result = map.get(patient_id)
        if map_result is None:
            group_id += 1
            map[patient_id] = group_id
            groups.append(group_id)
        else:
            groups.append(map_result)
    return groups        
            
def stratifiedGroupKFoldSplit(original_img_folder, copy_img_folder):
    all_labels = []
    all_groups = []
    all_files = []

    # Iteract in the files directory.
    for dir in os.listdir(original_img_folder):
        print(f"Class {dir}")

        class_dir_path = os.path.join(original_img_folder, dir) #{img_folder}{dir=4a|4b|4c}
        images = os.listdir(class_dir_path)

        #Files array - x
        all_files = np.concatenate((all_files, images))

        #Labels array - y
        all_labels = np.concatenate((all_labels, np.full(len(images), dir)))

        #Groups array - group
        all_groups = np.concatenate((all_groups, getGroupsList(class_dir_path)))
        
        # Get images
        pandasImages = pd.DataFrame(images)

    # Split on KFolds
    kf = StratifiedGroupKFold(n_splits=10, shuffle = True, random_state = 2)  
    folds = kf.split(all_files, all_labels, all_groups)

    for i, (train_index, test_index) in enumerate(folds):
        print(f"Fold {i}")
        fold_dir = f"fold-{i}"

        # Check if fold directory exists.
        Exist = os.path.exists(f"{copy_img_folder}\\{fold_dir}")
        if not Exist:
            os.mkdir(f"{copy_img_folder}\\{fold_dir}")

        sub_dir = "train"
        for idx in train_index:
            file = all_files[idx]
            dir = all_labels[idx]
            image_path = os.path.join(original_img_folder, dir, file)
            copy_image_path = os.path.join(copy_img_folder, fold_dir, sub_dir)

            # Check if type directory exists.
            Exist = os.path.exists(f"{copy_img_folder}\\{fold_dir}\\{sub_dir}") 
            if not Exist:
                os.mkdir(f"{copy_img_folder}\\{fold_dir}\\{sub_dir}") 

            # Copy image to new directory (original, target)
            shutil.copy(image_path,os.path.join(copy_image_path, dir + "_class_" + file))

        sub_dir = "test"
        for idx in test_index:
            file = all_files[idx]      
            dir = all_labels[idx]  
            image_path = os.path.join(original_img_folder, dir, file)
            copy_image_path = os.path.join(copy_img_folder, fold_dir, sub_dir)

            # Check if type directory exists.
            Exist = os.path.exists(f"{copy_img_folder}\\{fold_dir}\\{sub_dir}") 
            if not Exist:
                os.mkdir(f"{copy_img_folder}\\{fold_dir}\\{sub_dir}") 

            # Copy image to new directory (original, target)
            shutil.copy(image_path,os.path.join(copy_image_path, dir + "_class_" + file))

    # for index, group in enumerate(all_groups):
    #     print(f"  Image: {all_files[index]} | label: {all_labels[index]} | group: {group}")

    
original_img_folder = os.path.dirname(path)+'\Datasets\Colombiam\\split\\360x360-dataset-category-4-split\\full-dataset'
copy_img_folder = os.path.dirname(path)+'\Datasets\Colombiam\\split\\360x360-dataset-category-4-split\\test-fold'
stratifiedGroupKFoldSplit(original_img_folder, copy_img_folder)