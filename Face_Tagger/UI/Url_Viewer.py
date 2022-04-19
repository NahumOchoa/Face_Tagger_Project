import PySimpleGUI as sg
import os

IMG_TYPES = (".png", ".jpg", "jpeg", ".tiff", ".bmp")



class Url_Viewer_UI:
    def __init__(self):
        self.Url_Viewer_Logic_Object = Url_Viewer_Logic()
        

    def show_interface(self):
        self.Url_Viewer_Logic_Object.folder = sg.popup_get_folder('Image folder to open', default_path='')
       
        if not self.Url_Viewer_Logic_Object.folder:
            sg.popup_cancel('Cancelling')
            raise SystemExit()
        self.Url_Viewer_Logic_Object.fnames

        self.Url_Viewer_Logic_Object.num_files = len(self.Url_Viewer_Logic_Object.fnames)
        if self.Url_Viewer_Logic_Object.num_files == 0:
            sg.popup('No files in folder')
            raise SystemExit()

        return (self.Url_Viewer_Logic_Object.folder,self.Url_Viewer_Logic_Object.fnames,self.Url_Viewer_Logic_Object.num_files)
        

class Url_Viewer_Logic:

    def __init__(self):
        self._folder = None
        self._fnames = []
        self._num_files = None
    
    @property
    def folder(self):
        return self._folder
    
    @folder.setter
    def folder(self, folder_v):
        self._folder = folder_v

    @property
    def fnames(self):
        flist0 = os.listdir(self.folder)
        self._fnames = [f for f in flist0 if os.path.isfile(os.path.join(self.folder, f)) and f.lower().endswith(IMG_TYPES)]
        del flist0
        return self._fnames

    @property
    def num_files(self):
        return self._num_files

    @num_files.setter
    def num_files(self,num_files_v):
        self._num_files = num_files_v
    

    

