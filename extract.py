import pydicom as dicom
import os
import PIL # optional
import pandas as pd
import csv
# list of attributes available in dicom image
# download this file from the given github link
dicom_image_description = pd.read_csv("dicom_image_description.csv")
# Specify the .dcm folder path
folder_path = "stage_1_test_images"
images_path = os.listdir(folder_path)
# Patient's information will be stored in working directory #'Patient_Detail.csv'
with open('Patient_Detail.csv', 'w', newline ='') as csvfile:
    fieldnames = list(dicom_image_description["Description"])
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(fieldnames)
    for n, image in enumerate(images_path):
        ds = dicom.dcmread(os.path.join(folder_path, image))
        rows = []
        for field in fieldnames:
            if ds.data_element(field) is None:
                rows.append('')
            else:
                x = str(ds.data_element(field)).replace("'", "")
                y = x.find(":")
                x = x[y+2:]
                rows.append(x)
        writer.writerow(rows)