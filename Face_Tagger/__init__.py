from Excel_Data.Excel_Data import Excel_Data
from UI.Tagger_Viewer import Tagger_Viewer_UI
from UI.Url_Viewer import Url_Viewer_UI

EXCEL_URL = 'Resources/TabInfo.xls'
CSV_URL = 'Resources/Person_Data.csv'
def main():
    Excel_Data_Object = Excel_Data()
    Excel_Data_Object.excel_url = EXCEL_URL
    Excel_Data_Object.csv_url = CSV_URL
    Url_Viewer_object = Url_Viewer_UI()
    Tagger_Viewer_Object = Tagger_Viewer_UI()
    Tagger_Viewer_Object.excel_data = Excel_Data_Object
    Tagger_Viewer_Object.Url_Viewer_Object = Url_Viewer_object
    Tagger_Viewer_Object.show_interface()

if __name__ == '__main__':
    main()
    

