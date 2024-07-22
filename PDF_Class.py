'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- get the pdf from user 
2- Get pdf chapters for  any other classes may need it  
'''
import PyPDF4
from BuildString_Class import *
from typing import List



class PDFTool :

    def __init__(self)->None :
        self.__PDFText = ""
        self.__Chapter = ""
        self.__textWork = TextWork()
        self.__PDFFile = None
        self.Chapters: List[str] = []
    
    def GetChapters(self , file)->str:
            FilePDF = PyPDF4.PdfFileReader(file)
            for PageNum in range(FilePDF.numPages):
                Page = FilePDF.getPage(PageNum) #1
                self.__PDFText = Page.extractText() # Text of page 1
                PageInSingleLine = self.__textWork.String_Control(self.__PDFText) # single line for page 1*************
                if self.__textWork.CheckEndChapter(PageInSingleLine):#*****************
                    self.Chapters.append(self.__Chapter) # every single chapter in index 
                    self.__Chapter = ""
                else:
                    self.__Chapter += PageInSingleLine 
            if len(self.Chapters) == 0:# in case single chapter 
                self.Chapters.append(self.__Chapter)
            return self.Chapters

























    def ShowChapters(self)->None:
        count = 0
        for i in self.__Chapter:
            print("Chapter " , count , ":\n" , i , "\n")
            count +=1

    def ShowChapter(self , ChapterNumber:int)->None:
        print("Chapter " , ChapterNumber , ":\n" , self.Chapters[ChapterNumber] , "\n")