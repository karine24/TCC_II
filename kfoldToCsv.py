'''
/**
* @author Karine Mendes Tavares
*/
'''

import csv
import os

csv_path = "K:\\Faculdade\\TCC\\Datasets\\Colombiam\\split\\360x360-dataset-category-4-split\\10fold-group\\csv"
folds_path = "K:\\Faculdade\\TCC\\Datasets\\Colombiam\\split\\360x360-dataset-category-4-split\\10fold-group"

header = ['img_dir', 'label']
# Iteract in the files directory.
for dir in os.listdir(folds_path):
    if not "csv" in dir:
        for split in os.listdir(os.path.join(folds_path, dir)):
            # open the file in the write mode
            f = open(f"{csv_path}\\{split}-{dir}.csv", 'w')

            # create the csv writer
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)
            for file in os.listdir(os.path.join(folds_path, dir, split)):
                data = []
                image_dir = f"/content/gdrive/MyDrive/puc/tcc/Datasets/360x360-10fold/{file}"
                data.append(image_dir)

                label = file.split('_class_')[0].split('_')
                label = label[len(label)-1]
                data.append(label)
                # write the data
                writer.writerow(data)
            f.close()
                