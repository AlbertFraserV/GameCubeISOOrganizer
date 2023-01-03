#!/usr/bin/env python

from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
path = askdirectory(title='Select Folder') # shows dialog box and return the path

for filename in os.listdir(path):
    f = os.path.join(path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if ".DS_Store" in f:
            continue
        folder_name = ''.join(filename.rpartition('.')[:-1])[:-1]
        file_name = ''.join(f.rpartition('/')[-1])
        new_folder_path = path + "/" + folder_name
        os.mkdir(new_folder_path)
        os.popen(f'cp {f} {new_folder_path}/{file_name}') 
