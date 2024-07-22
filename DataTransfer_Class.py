'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- to transefer the main data between the api inside the controller of the fast api 
'''

class RequestData():

    def __init__(self):
        self.__Agent = ""
        self.__ChaptersMustSend = ""

    def GetAgent(self)->str:
        return self.__Agent

    def SetAgent(self , Agent):
        self.__Agent = Agent
    
    def GetChaptersMustSend(self)->str:
        return self.__ChaptersMustSend

    def SetChaptersMustSend(self ,ChaptersMustSend):
        self.__ChaptersMustSend = ChaptersMustSend 
