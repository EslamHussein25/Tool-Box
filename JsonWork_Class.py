'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- to convert the json to string and vise versa with possibility to add some modifications and edit on the json or string data
'''

import json
from json import *

class JsonConvert:
    def __init__(self) -> None:
        pass

    #Convert data to json 
    def WriteJson(self , Data , JsonData):
        json.dumps(Data, JsonData) 

    # Convert json to data 
    def ReadJson(self , JsonData)->str:
        Data:str 
        Data = json.loads(JsonData)
        return Data 
 

