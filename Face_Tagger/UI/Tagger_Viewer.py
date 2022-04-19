import PySimpleGUI as sg
import os
from PIL import Image, ImageTk
import io

class Tagger_Viewer_UI:
    def __init__(self):
        self.Tagger_Viewer_Logic_Object = Tagger_Viewer_Logic()
        self._Url_Viewer_Object = None
        self._excel_data = None
    @property
    def excel_Data(self):
        return self._excel_data
    @excel_Data.setter
    def excel_Data(self,Excel_Data_v):
        self._excel_data = Excel_Data_v
    @property
    def Url_Viewer_Object(self):
        return self._Url_Viewer_Object

    @Url_Viewer_Object.setter
    def Url_Viewer_Object(self,Url_Viewer_Object_v):
        self._Url_Viewer_Object = Url_Viewer_Object_v

    def show_interface(self):
   
        start_viewer = self.Url_Viewer_Object.show_interface()
        
        fnames = start_viewer[1]
        filename = os.path.join(start_viewer[0], fnames[0])  # name of first file in list
       
        self.Tagger_Viewer_Logic_Object.file_name = filename
        image_elem = sg.Image(data=self.Tagger_Viewer_Logic_Object.img_data( first=True),size=(400, 400))
        filename_display_elem = sg.Text(filename, size=(47,3 ))
        file_num_display_elem = sg.Text('File 1 of {}'.format(start_viewer[2]), size=(15, 1))
        tab_menu_attrib_object = self.excel_data
        tab_menu_attrib_object.tab_menu_atrib_values
        tab_menu_attrib_object.tab_menu_atrib_names
        tab_menu_attrib_object.tab_menu_atrib_layout
        
        tab_group = self.Tagger_Viewer_Logic_Object.tab_create(tab_menu_attrib_object)            
        # define layout, show and read the form
        col = [[filename_display_elem],
            [image_elem]]

        col_files = [[sg.Listbox(values=fnames, change_submits=True, size=(30, 20), key='listbox')],
                    [sg.Button('Next', size=(8, 2)), sg.Button('Prev', size=(6, 2)), file_num_display_elem]]

        layout = [[sg.Column(col_files, vertical_alignment='center'), sg.Column(col,element_justification="center"),sg.Column(tab_group)]]

        window = sg.Window('Image Browser', layout, return_keyboard_events=True,
                        location=(0,0), use_default_focus=False, size=(820,580),margins=(0,0),element_justification="center")
    
        self.Tagger_Viewer_Logic_Object.update_img(window,start_viewer,fnames,image_elem,filename_display_elem,file_num_display_elem,tab_menu_attrib_object)
        window.close()

class Tagger_Viewer_Logic:
    def __init__(self):
        self._file_name = None
        self._group_size = []
        self._group_type =[]
        self._group_data_dict = {}
        self._group_data_dict_default = {}
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self,file_name_v):
        self._file_name = file_name_v
    @property
    def group_size(self):
        return self._group_size
    @group_size.setter
    def group_size(self,group_size_v):
        self._group_size = group_size_v
    @property
    def group_type(self):
        return self._group_type
    @group_type.setter
    def group_type(self,group_type_v):
        self._group_type = group_type_v
    @property
    def group_data_dict(self):
        return self._group_data_dict
    @group_data_dict.setter
    def group_data_dict(self,group_data_dict_v):
        self._group_data_dict = group_data_dict_v
    @property
    def group_data_dict_default(self):
        return self._group_data_dict_default
    @group_data_dict_default.setter
    def group_data_dict_default(self,group_data_dict_default_v):
        self._group_data_dict_default = group_data_dict_default_v
    
    def img_data(self, maxsize=(400, 400), first=False):
        """
        Generate image data using PIL
        """
        img = Image.open(self.file_name)
        img.thumbnail(maxsize)
        
        new_image = img.resize(maxsize)
        if first:                     # tkinter is inactive the first time
            bio = io.BytesIO()
            new_image.save(bio, format="PNG")
            del new_image
            return bio.getvalue()
        return ImageTk.PhotoImage(new_image)

    def tab_create(self, tab_menu_attrib):
        i = 0
        temp = 0
        group =[]
        tab_group_temp = []
        tab_group_final = []
        print(tab_menu_attrib.tab_menu_atrib_names)
        for n in range(0,len(tab_menu_attrib.sheet_names)-1):
            
            layoutTab = []
            ranges = tab_menu_attrib.tab_menu_index[i]
            for n2 in range(0,ranges):
                
                j = 0
                tab_menu_attrib_temp =  tab_menu_attrib.tab_menu_atrib_values[temp]
                tab_menu_attrib_temp_titles =str(tab_menu_attrib.tab_menu_atrib_names[temp])
                tab_menu_attrib_temp_layout = str(tab_menu_attrib.tab_menu_atrib_layout[temp])
                if(len(tab_menu_attrib.tab_menu_atrib_values[temp])>0):
                    print('entro')
                    if(tab_menu_attrib_temp_layout[2:-2:] == 'Radio' ):
                        layoutTab.append([sg.Text(f'{tab_menu_attrib_temp_titles[2:-2:]}',size=(15, 1))])
                        layoutTab.append([sg.Radio(tab_menu_attrib_temp[0], f'{tab_menu_attrib.tab_menu_atrib_names[temp]}{i}',default = False,key=f'{tab_menu_attrib_temp[0]}')])
                        layoutTab.append([sg.Radio(tab_menu_attrib_temp[1], f'{tab_menu_attrib.tab_menu_atrib_names[temp]}{i}',default = True,key=f'{tab_menu_attrib_temp[1]}')])
                        j = j+2
                        self.group_type.append('Radio')
                    elif(tab_menu_attrib_temp_layout[2:-2:] == 'Combo'):
                        layoutTab.append([sg.Text(f'{tab_menu_attrib_temp_titles[2:-2:]}')])
                        layoutTab.append([sg.Combo(tab_menu_attrib_temp, default_value= tab_menu_attrib_temp[0],)])
                        j = j+1
                        self.group_type.append('Combo')

                    elif(tab_menu_attrib_temp_layout[2:-2:]=='Check'):
                        layoutTab.append([sg.Text(f'{tab_menu_attrib_temp_titles[2:-2:]}',size=(15, 1))])
                        for n in range(0, len(tab_menu_attrib_temp)):
                          
                            tab_menu_attrib_temp_values_independet = str(tab_menu_attrib_temp[n])
                            layoutTab.append([sg.Checkbox(tab_menu_attrib_temp_values_independet,key=f'{tab_menu_attrib_temp_values_independet}')])
                            j = j+1
                        self.group_type.append('Check')
                    temp = temp+1
                else:
                    print('no hay nada')
                group.append(j)
            
            tab_group_temp.append([sg.Tab(f'{tab_menu_attrib.sheet_names[i]}', layoutTab, title_color='Red',border_width =10, background_color='Green')])
            
            
            i = i+1
        self.group_size = group
        print(self.group_size)   
        print(self.group_type)                   
        tab_group_final = [[sg.TabGroup(tab_group_temp)],[sg.Button('Save', size=(10, 2))]] 
        return tab_group_final 

    def group_data(self,value_temp):
        
        group_data_dict_temp = {}
        value_index = list(value_temp.keys())
        i = 1
        temp = 0
        flag = 0
        
        for n in range(0,len(self.group_size)):
            
            if self.group_type[n] == 'Combo':
                print('entro combo')
                group_data_dict_temp[i] = value_temp[value_index[temp]]
                temp = temp+1
                #print(group_data_dict_temp)
            elif self.group_type[n]=='Radio':
                print('entro radio')
                if(value_temp[value_index[temp]]== True):
                    group_data_dict_temp[i] = 'Si tiene'
                        
                else:
                    group_data_dict_temp[i] = 'No tiene'
                #print(group_data_dict_temp)
                temp = temp+2
                    
            elif self.group_type[n]=='Check':
                #print('entro check')
                for n2 in range(0,self.group_size[n]):
                    print('entro check')
                    if value_temp[value_index[temp]] == True and flag == 0:
                        group_data_dict_temp[i] = value_index[temp]
                        flag = 1
                        
                    elif value_temp[value_index[temp]] == True:
                        group_data_dict_temp[i] = f'{group_data_dict_temp[i]}, {value_index[temp]}'
                        
                    temp = temp+1
                    
                    #print(group_data_dict_temp)
                if flag == 0:
                        group_data_dict_temp[i] = 'no tiene algun'
                    
        
            i= i+1 
        self.group_data_dict = group_data_dict_temp  
        print(self.group_data_dict) 
    def update_img(self,window,start_viewer,fnames,image_elem,filename_display_elem,file_num_display_elem,tab_menu_attrib_object):
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
                fnames_temp = fnames[i].split('.')
                
                if(tab_menu_attrib_object.search_id(fnames_temp[0])[0] == True):
                    
                    self.update_layout(tab_menu_attrib_object.search_id(fnames_temp[0])[1],tab_menu_attrib_object,window)
                    
                else:
                    self.update_layout(0,tab_menu_attrib_object,window)

                filename = os.path.join(start_viewer[0], fnames[i])
            elif event in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33'):
                i -= 1
                if i < 0:
                    i = start_viewer[2] + i
                fnames_temp = fnames[i].split('.')    
                if(tab_menu_attrib_object.search_id(fnames_temp[0])[0] == True):
                    
                    self.update_layout(tab_menu_attrib_object.search_id(fnames_temp[0])[1],tab_menu_attrib_object,window)
                else:
                    self.update_layout(0,tab_menu_attrib_object,window)
                filename = os.path.join(start_viewer[0], fnames[i])
            elif event in('Save', 'MouseWheel:Up', 'Up:38', 'Prior:33'):
                value_temp = self.clean_data(values)

                self.group_data(value_temp)
                fnames_temp = fnames[i].split('.')
                self.group_data_dict[0] = fnames_temp[0]
                tab_menu_attrib_object.phrases_data = self.group_data_dict
                tab_menu_attrib_object.phrases_data_names = value_temp
                if(tab_menu_attrib_object.search_id(fnames_temp[0])[0] == True):
                    tab_menu_attrib_object.modify_phrase_data(tab_menu_attrib_object.search_id(fnames_temp[0])[1])
                else:
                    
                    tab_menu_attrib_object.write_phrase_data()
                
                filename = os.path.join(start_viewer[0], fnames[i])
                
            elif event == 'listbox':            # something from the listbox
                f = values["listbox"][0]            # selected filename
                
                filename = os.path.join(start_viewer[0], f)  # read this file
                i = fnames.index(f)                 # update running index
            else:
                filename = os.path.join(start_viewer[0], fnames[i])

            # update window with new image
            self.file_name = filename
            image_elem.update(data=self.img_data(first=True))
            # update window with filename
            filename_display_elem.update(filename)
            # update page display
            file_num_display_elem.update('File {} of {}'.format(i+1, start_viewer[2]))
    
    def update_layout(self,index,tab_menu_attrib_object,window):
        update_data = tab_menu_attrib_object.read_layout_phrases(index)
        update_data_dic = update_data[1]
        for i in update_data_dic:
            window[i].update(update_data_dic[i])
         
    def clean_data(self, value):
        value_temp = value
        value_temp.popitem()
        del value_temp['listbox']
        return value_temp