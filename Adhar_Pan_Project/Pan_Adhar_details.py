import pytesseract
import os
import re
import pandas as pd

##############################################################################################

#for extract date of birth and pan number with help of regular expression
class PanDetails:
    def __init__(self,folder_path):
        self.folder_path=folder_path
        
    def __date_of_birth(self):
        dob=re.findall('[012][1-9][-/][01][0-9][-/][0-9]{4}',self.text)
        self.dob=dob
        return self.dob
    
    def __pan_number(self):
        pan=re.findall('[A-Z]{5}[0-9]{4}[A-Z]',self.text)
        self.pan=pan
        return self.pan
    
    def callpandetails(self):
        dob=self.__date_of_birth()
        if dob:
            self.date_of_birth.append(dob[0])
        else:
            self.date_of_birth.append('')
        pan_num=self.__pan_number()
        if pan_num:
            self.pan_number.append(pan_num[0])
        else:
            self.pan_number.append('')
            

###############################################################################################            
            
#for extract date of birth and Adhar number with help of regular expression
class AdharCard():
    def __Adate_of_birth(self):
        adhar_dob=re.findall('[012][1-9][-/][01][0-9][-/][0-9]{4}',self.text)
        self.adhar_dob=adhar_dob
        return self.adhar_dob
    def __adhar_card_number(self):
        adhar_num=re.findall('\d{4}\s\d{4}\s\d{4}',self.text)
        self.adhar_num=adhar_num
        return self.adhar_num
    
    def calladhardetails(self):
        dob=self.__Adate_of_birth()
        if dob:
            self.date_of_birth.append(dob[0])
        else:
            self.date_of_birth.append('')
            
        adhar_num=self.__adhar_card_number()
        if adhar_num:
            self.pan_number.append(adhar_num[0])
        else:
            self.pan_number.append('')
            
################################################################################################
            
 #initially rename all file std. order format               
class FileProcessing():
    def __rename_file(self):
        if self.TypeFile=='Adhar':   #if pass file type as Adhar the rename all file name adhar0.jpg if any go to else block
            try:
                for i,file in enumerate(self.pan_data):
                    if file in self.pan_data:
                        os.rename(self.folder_path +'\\'+file,self.folder_path+'\\'+'adhar_card'+ f'{i}'+'.jpg')
                    else:
                        continue
            except:
                pass
        else:
            try:
                for i,file in enumerate(self.pan_data):
                    if file in self.pan_data:
                        os.rename(self.folder_path +'\\'+file,self.folder_path+'\\'+'Pan_card'+ f'{i}'+'.jpg')
                    else:
                        continue
            except:
                pass
                
    def callfileprocessing(self):
        self.__rename_file()
        
################################################################################################
        
# after image to string convert and then read that file and clean the data (remove of null vaue rows)
#and store data in file of csv.        
class DataProcessing():
    def __csv_clean(self):
        dfn=pd.read_csv(self.Fs)
        new_clean=dfn.dropna(subset=['Date of Birth'])
        del new_clean['Unnamed: 0']
        new_clean.reset_index(inplace=True)
        del new_clean['index']
        print(new_clean)
        while True:
            clean_file_name=input('enter the clean file name= ')
            if clean_file_name not in os.listdir(storage_path) and clean_file_name.endswith('.csv'):
                CF=storage_path+'\\' + clean_file_name
                new_clean.to_csv(CF)
                print(f'Update into excel {clean_file_name} succesefully')
                break
            else:
                print(f'{clean_file_name} is Present in Current Dir')
            
    def call_csv_clean(self):
        self.__csv_clean()
        
##################################################################################################
        
 #Final Proccessing class happenend of processing related to image to text  and store all text sequencally in list.
class FinalProcessing(FileProcessing,PanDetails,AdharCard):
    def __pan_details(self):
        self.pan_data=os.listdir(self.folder_path)
        self.TypeFile=data
        self.callfileprocessing()
        self.pan_data=os.listdir(self.folder_path)
        self.pan_data.sort()
#         print(self.pan_data)
        self.date_of_birth=[]
        self.pan_number=[]
        self.file_name=[]
        for file in self.pan_data:
            image_file=self.folder_path+'\\'+file
            pytesseract.pytesseract.tesseract_cmd=r'C:\Users\91703\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
            self.text=pytesseract.image_to_string(image_file)
            self.file_name.append(file)
            if self.TypeFile=='Adhar':
                self.calladhardetails()    #call and apend the pan card date into the file
            else:
                self.callpandetails() 
            
    def callfinalprocessing(self):
            self.__pan_details()
            
 ####################################################################################################
 
 #create here dict and then convert into dataframe using pandas module and use df.to_csv() store into into csv file.
#last call the DataProcessing class function to clean the data frame have empty rows and again store into new csv file       
class DataUpdate(FinalProcessing,DataProcessing):
    def data_update_csv(self):
        self.callfinalprocessing()
        if self.TypeFile =='Adhar':
            Pan_Dict={'File Name':self.file_name,
                     'Date of Birth':self.date_of_birth,
                     'Adhar Number':self.pan_number}
        else:
             Pan_Dict={'File Name':self.file_name,
                     'Date of Birth':self.date_of_birth,
                     'Pan Number':self.pan_number}
        df=pd.DataFrame(Pan_Dict)
        while True:
            self.file_name=input('Enter the File Name=')
            if self.file_name not in os.listdir(storage_path) and self.file_name.endswith('.csv') :
                self.Fs=storage_path+'\\'+self.file_name
                df.to_csv(self.Fs)
                print(f'{self.file_name} Updated Successfully')
                break
            else:
                print(f'{self.file_name} File is Present')

        self.call_csv_clean()
        

######################################################################################################
#'Final Output File Path Location Give Here'
storage_path=r'E:\10.python\03\03.03.2022'

######################################################################################################
print("""Adhar: Adhar card file format enter 'Adhar'
Pan : Pan Card format enter 'Pan'""")

data=input('Enter the Type of document= ')
print('\033[2;31;47m Please Wait.... \033[0;0m')
#####################################################################################################
if data=='Pan':
    #here give the path of image Pan card folder location
    path=r'E:\10.python\03\02.03.2022\pan card'
else:
    #here give the path image of  adhar card folder location
    path=r"E:\10.python\03\01.03.2022\adhar_card"

######################################################################################################
panobj=DataUpdate(path)
panobj.data_update_csv()