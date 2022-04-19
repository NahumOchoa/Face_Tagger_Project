#!/usr/bin/env python
from tracemalloc import start
import PySimpleGUI as sg
import os
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import io
import ast
import Url_Viewer
from sys import path
path.append("../Excel_Data")
import Excel_Data 

"""
Simple Image Browser based on PySimpleGUI
--------------------------------------------
There are some improvements compared to the PNG browser of the repository:
1. Paging is cyclic, i.e. automatically wraps around if file index is outside
2. Supports all file types that are valid PIL images
3. Limits the maximum form size to the physical screen
4. When selecting an image from the listbox, subsequent paging uses its index
5. Paging performance improved significantly because of using PIL
Dependecies
------------
Python3
PIL
"""
TAB_MENU_NAME = ['test1','test2','test3']
EXCEL_URL = '../Excel_Data/TabInfo.xlsx'
# Get the folder containin:g the images from the user
"""
folder = sg.popup_get_folder('Image folder to open', default_path='')
if not folder:
    sg.popup_cancel('Cancelling')
    raise SystemExit()

# PIL supported image types
img_types = (".png", ".jpg", "jpeg", ".tiff", ".bmp")

# get list of files in folder
flist0 = os.listdir(folder)

# create sub list of image files (no sub folders, no wrong file types)
fnames = [f for f in flist0 if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith(img_types)]

num_files = len(fnames)                # number of iamges found
if num_files == 0:
    sg.popup('No files in folder')
    raise SystemExit()

del flist0                             # no longer needed
"""
# ------------------------------------------------------------------------------
# use PIL to read data of one image
# ------------------------------------------------------------------------------


def get_img_data(f, maxsize=(1200, 850), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Create a tab section with excel data
# ------------------------------------------------------------------------------
def tab_create(tab_menu_attrib):
    i = 0
    temp = 0
    tab_group_temp = []
    tab_group_final = []
    print(tab_menu_attrib.tab_menu_atrib_names)
    for n in range(0,len(tab_menu_attrib.sheet_names)):
        
        layoutTab = []
        ranges = tab_menu_attrib.tab_menu_index[i]
        for n2 in range(0,ranges):
            tab_menu_attrib_temp =  tab_menu_attrib.tab_menu_atrib_values[temp]
            tab_menu_attrib_temp_titles =str(tab_menu_attrib.tab_menu_atrib_names[temp])
           

            print('entro')
            if(len(tab_menu_attrib.tab_menu_atrib_values[temp]) <=2 ):
                layoutTab.append([sg.Text(f'{tab_menu_attrib_temp_titles[2:-2:]}',size=(15, 1))])
                layoutTab.append([sg.Radio(tab_menu_attrib_temp[0], f'{tab_menu_attrib.tab_menu_atrib_names[temp]}{i}',default = False)])
                layoutTab.append([sg.Radio(tab_menu_attrib_temp[1], f'{tab_menu_attrib.tab_menu_atrib_names[temp]}{i}',default = True)])
            else:
                layoutTab.append([sg.Text(f'{tab_menu_attrib_temp_titles[2:-2:]}')])
                layoutTab.append([sg.Combo(tab_menu_attrib_temp)])
            temp = temp+1
            
        
        tab_group_temp.append([sg.Tab(f'{tab_menu_attrib.sheet_names[i]}', layoutTab, title_color='Red',border_width =10, background_color='Green')])
        
        i = i+1
                            
    tab_group_final = [[sg.TabGroup(tab_group_temp)]]  
    return tab_group_final  
    
# make these 2 elements outside the layout as we want to "update" them later
# initialize to the first file in the list
Url_Viewer_object = Url_Viewer.Url_Viewer_UI()
start_viewer = Url_Viewer_object.show_interface()
fnames = start_viewer[1]
filename = os.path.join(start_viewer[0], fnames[0])  # name of first file in list
image_elem = sg.Image(data=get_img_data(filename, first=True))
filename_display_elem = sg.Text(filename, size=(80, 3))
file_num_display_elem = sg.Text('File 1 of {}'.format(start_viewer[2]), size=(15, 1))
tab_menu_attrib_object = Excel_Data.Excel_Data()
tab_menu_attrib_object.excel_url = EXCEL_URL
tab_menu_attrib_object.tab_menu_atrib_values
tab_menu_attrib_object.tab_menu_atrib_names
tab_group = tab_create(tab_menu_attrib_object)

    
    
# define layout, show and read the form
col = [[filename_display_elem],
       [image_elem]]

col_files = [[sg.Listbox(values=fnames, change_submits=True, size=(60, 30), key='listbox')],
             [sg.Button('Next', size=(8, 2)), sg.Button('Prev', size=(8, 2)), file_num_display_elem]]

layout = [[sg.Column(col_files), sg.Column(col),sg.Column(tab_group)]]

window = sg.Window('Image Browser', layout, return_keyboard_events=True,
                   location=(0, 0), use_default_focus=False)

# loop reading the user input and displaying image, filename
def update_img():
    i = 0
    while True:
        # read the form
        event, values = window.read()
        print(event, values)
        # perform button and keyboard operations
        if event == sg.WIN_CLOSED:
            break
        elif event in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34'):
            i += 1
            if i >= start_viewer[2]:
                i -= start_viewer[2]
            filename = os.path.join(start_viewer[0], fnames[i])
        elif event in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33'):
            i -= 1
            if i < 0:
                i = start_viewer[2] + i
            filename = os.path.join(start_viewer[0], fnames[i])
        elif event == 'listbox':            # something from the listbox
            f = values["listbox"][0]            # selected filename
            filename = os.path.join(start_viewer[0], f)  # read this file
            i = fnames.index(f)                 # update running index
        else:
            filename = os.path.join(start_viewer[0], fnames[i])

        # update window with new image
        image_elem.update(data=get_img_data(filename, first=True))
        # update window with filename
        filename_display_elem.update(filename)
        # update page display
        file_num_display_elem.update('File {} of {}'.format(i+1, start_viewer[2]))
        
update_img()
window.close()