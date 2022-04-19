
import pandas as pd
import ast
from openpyxl import load_workbook

class Excel_Data:
    
    def __init__(self):
        self._tab_menu_atrib_values = []
        self._tab_menu_atrib_names = [] 
        self._tab_menu_atrib_layout = []
        self._tab_menu_index = []
        self._phrases_data_names = {}
        self._phrases_data = {}
        self._sheet_names = None
        self._excel_url = None
        

    @property
    def excel_url(self):
        return self._excel_url
    
    @excel_url.setter
    def excel_url(self,excel_url_v):
        self._excel_url = excel_url_v
    @property
    def sheet_names(self):
        return self._sheet_names

    @sheet_names.setter
    def sheet_names(self, sheet_names_v):
        self._sheet_names = sheet_names_v

    @property
    def tab_menu_index(self):
        return self._tab_menu_index
    @tab_menu_index.setter
    def tab_menu_index(self,tab_menu_index_v):
        self._tab_menu_index = tab_menu_index_v

    @property
    def phrases_data(self):
        return self._phrases_data
    @phrases_data.setter
    def phrases_data(self, phrases_data_v):
        self._phrases_data = phrases_data_v

    @property
    def phrases_data_names(self):
        return self._phrases_data_names
    @phrases_data_names.setter
    def phrases_data_names(self, phrases_data_names_v):
        self._phrases_data_names = phrases_data_names_v
    @property
    def tab_menu_atrib_values(self):
        if(self.excel_url == None):
            return print("NO hay ruta del excel")
        else:
            xls = pd.ExcelFile(self.excel_url)
            self.sheet_names = xls.sheet_names
            for n in range(0,len(self.sheet_names)):
                df = pd.read_excel(xls,self.sheet_names[n])
                df_index = df.index.stop
                self.tab_menu_index.append(df.index.stop)
                data = pd.DataFrame(df, columns=['Value'])
                for n in range(0,df_index):
                    data_clean = self.data_cleanner(str(data.values[n]))
                    self._tab_menu_atrib_values.append(data_clean)
        
        return self._tab_menu_atrib_values
    @property
    def tab_menu_atrib_names(self):
       if(self.excel_url == None):
            return print("NO hay ruta del excel")
       else:
            xls = pd.ExcelFile(self.excel_url)
            for n in range(0,len(self.sheet_names)):
                df = pd.read_excel(xls,self.sheet_names[n])
                df_index = df.index.stop
                data = pd.DataFrame(df, columns=['Name'])
                for n in range(0, df_index):
                    data_clean = self.data_cleanner(str(data.values[n]))
                    self._tab_menu_atrib_names.append(data_clean)

       return self._tab_menu_atrib_names
    
    @property
    def tab_menu_atrib_layout(self):
       if(self.excel_url == None):
            return print("NO hay ruta del excel")
       else:
            xls = pd.ExcelFile(self.excel_url)
            for n in range(0,len(self.sheet_names)):
                df = pd.read_excel(xls,self.sheet_names[n])
                df_index = df.index.stop
                data = pd.DataFrame(df, columns=['Layout'])
                for n in range(0, df_index):
                    data_clean = self.data_cleanner(str(data.values[n]))
                    self._tab_menu_atrib_layout.append(data_clean)
       return self._tab_menu_atrib_layout
        
    def read_layout_phrases(self,index):
        xls = pd.ExcelFile(self.excel_url)
        df = pd.read_excel(xls,self.sheet_names[len(self.sheet_names)-1])
        phrase = pd.DataFrame(df, columns=['Phrase'])
        system = pd.DataFrame(df, columns=['System'])
        print(self.to_dic_from_string(str(system.values[index])[2:-2:]))
        return (str(phrase.values[index])[2:-2:],self.to_dic_from_string(str(system.values[index])[2:-2:]))

    def write_phrase_data(self):
        PHRASE_EXAMPLE = f'Se seleccionaron los checkbox siguientes: {self.phrases_data[1]}, el radio buttoom siguiente: {self.phrases_data[2]} , el combobox siguiente: {self.phrases_data[3]}, el radio buttom siguiente: {self.phrases_data[4]}'
        xls = pd.ExcelFile(self.excel_url)
        df = pd.read_excel(xls,self.sheet_names[len(self.sheet_names)-1])
        df_index = df.index.stop
        wb = load_workbook(filename = self.excel_url)
        ws = wb.get_sheet_by_name(self.sheet_names[len(self.sheet_names)-1])
        ws.cell(df_index+2,1).value = self.phrases_data[0]
        ws.cell(df_index+2,2).value = PHRASE_EXAMPLE
        ws.cell(df_index+2,3).value = str(self.phrases_data_names)
        wb.save(self.excel_url)

    def modify_phrase_data(self,index):
        PHRASE_EXAMPLE = f'Se seleccionaron los checkbox siguientes: {self.phrases_data[1]}, el radio buttoom siguiente: {self.phrases_data[2]} , el combobox siguiente: {self.phrases_data[3]}, el radio buttom siguiente: {self.phrases_data[4]}'
        xls = pd.ExcelFile(self.excel_url)
        df = pd.read_excel(xls,self.sheet_names[len(self.sheet_names)-1])
        df_index = df.index.stop
        wb = load_workbook(filename = self.excel_url)
        ws = wb.get_sheet_by_name(self.sheet_names[len(self.sheet_names)-1])
        ws.cell(index+2,1).value = self.phrases_data[0]
        ws.cell(index+2,2).value = PHRASE_EXAMPLE
        ws.cell(index+2,3).value = str(self.phrases_data_names)
        wb.save(self.excel_url)
        
    def search_id(self,id_person):
        xls = pd.ExcelFile(self.excel_url)
        df = pd.read_excel(xls,self.sheet_names[len(self.sheet_names)-1])
        df_index = df.index.stop
        data = pd.DataFrame(df, columns=['ID'])
        for n in range(0, df_index):
            data_clean = str(data.values[n])
            if(data_clean[2:-2:]==id_person):
                print('entro')
                return (True,n)
            
                
        return (False,None)

    def to_dic_from_string(self,string):
        for i in string.splitlines():
            dic=ast.literal_eval(i)
        return dic
            
        

    def data_cleanner(self,data):
        data_clean = data[2:-2:].split(',')
        return data_clean
        
    
            
    
