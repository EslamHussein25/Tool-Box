'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- calculate the tokens of the words count for any file to decide if this token is the max or not
'''
from PDF_Class import *

maxToken = 4096

class TokensControl:

    __Path:str 
    __Chapters:str 

    def __init__(self ) -> None:
        #self.__Path = Path
        #self.__PDF = PDFTool(self.__Path)  
        self.SendChapters = ""

    def __TokenCalculation(self , words)-> int:
        return (words / 0.75)

    def TokensCalculation(self , ChaptersToGet:str)->str: 
        self.__Chapters = ChaptersToGet
        AllTokens = 0
        TokensCount = 0
        for Chapter in self.__Chapters:
            WordsCount = len(Chapter)  # lenght of single chapter 
            TokensCount = self.__TokenCalculation(WordsCount)# add the sum of tokens for every chapter 
            AllTokens += TokensCount
            TokensCount = 0
            if AllTokens < maxToken : 
                self.SendChapters += Chapter # if less than max tokens add this chapter to the chapters to send     
            else :
                break
        return self.SendChapters # if max tokens stop and send request 
               


