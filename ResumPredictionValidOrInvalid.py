#import numpy as np
import pandas as pd
import os
from docx import Document
import re
#import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
class read_files_and_get_text():
    
    def readfiles(self,path):
        textfile=[]
        for root, dirs ,files in os.walk(path):
            for f1 in files:
                filepath = os.path.join(root, f1)
                textfile.append(filepath)
        return textfile
                
    def gettext(self,path):#It is taking list as an argument
        textfinal=[]
        #for a in lst_arg:
        document = Document(path)
        for para in document.paragraphs:
            textfinal.append(para.text)
        return '\n'.join (textfinal)
    
    def getfinaltext(self,list_files):
        lst_data=[]
        for a in range(len(list_files)):
           textfinal=get_data.gettext(list_files[a])
           lst_data.append(textfinal)
        return lst_data


    def createDataFrame(self,lst):
        d={'Resume details': lst}
    
        datasetOfResumeDetails=pd.DataFrame(data=d)
        return datasetOfResumeDetails


    def createCorpus(self,dataframe):
        corpus=[]
        for i in range(len(dataframe)):
            CleanDataset2 = re.sub('[^a-zA-Zc#C#]', ' ', dataframe['Resume details'][i])
            CleanDataset2 = CleanDataset2.lower()
            CleanDataset2 = CleanDataset2.split()
            ps = PorterStemmer()
            CleanDataset2 = [ps.stem(word2) for word2 in CleanDataset2 if not word2 in set(stopwords.words('english'))]
            CleanDataset2 = ' '.join(CleanDataset2)
            corpus.append(CleanDataset2)
        return corpus
            
class searchresumeViatechnology():
    def checkvalid(self,corpus, wordtosearch):
           #d={}
            totalCount=[]
            for a in corpus:
                if len(a)>=500:
                    count=0
                    for s in a.split():
                        if s in [wordtosearch]:
                            count+=1
                    totalCount.append(count)
                else:
                    totalCount.append(0)
            return totalCount
        
    def valid_invalid(self,val):
        if int(val)>=8:
            return 'Valid'
        else:
            return 'Invalid'


get_data =read_files_and_get_text()
doc_files_list=get_data.readfiles(r"C:\Users\kpanwar\Desktop\Importent Folder-Dont delete\pythonProject\Monster_.Net Developer_1832019_141650\Resumes")
final_lst=get_data.getfinaltext(doc_files_list)
dataframe_resume_details=get_data.createDataFrame(final_lst)
corpus=get_data.createCorpus(dataframe_resume_details)



    
obj= searchresumeViatechnology()      
lstofSearchwords=obj.checkvalid(corpus,'java')
dicti = { 'Resume Files':doc_files_list,
          'WordCount': lstofSearchwords  }



finalDataFrame = pd.DataFrame(data= dicti)

finalDataFrame['ValidOrInvalid']=finalDataFrame['WordCount'].apply(obj.valid_invalid)

