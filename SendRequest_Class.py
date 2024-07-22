'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- concrete class to handle the request to the AI agent by implementation of ISendRequest interface class
'''

from ISendRequest_Class import *
import os 
from enum import Enum
from openai import OpenAI
from TokensCalcluation_Class import TokensControl

Agent_3_prompot = "act as senior HR to review this cv file but send me the response or your answer as string"


Agent_4_prompot = "act as senior for this topic which i will send it to you "


api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    print("No API is Set!\n")


class AIAgent(Enum):
    GPT3 = 1
    GPT4 = 2
    Gemini = 3
    GPT4MIN = 4 

class Request_AI(Request):

    AIModel:int
    __openai_client = OpenAI(api_key=api_key)
    __conversation_history = []
    
    def __init__(self) -> None:
        super().__init__()

    def UploadFile(self , ChaptersToSend:str)->str:
        FileData = ChaptersToSend
        return self.SendRequest(FileData)

    def SendRequest(self , Text_ASK:str)->str:
        if self.AIModel == AIAgent.GPT3.value:
            print("Send the Qustion to GPT3: \n")
            return self.__SendRequest3(Text_ASK , Agent_3_prompot)
        elif self.AIModel == AIAgent.GPT4.value:
            print("Send the Qustion to GPT4: \n")
            return self.__SendRequest4(Text_ASK , Agent_4_prompot)






    def __SendRequest3(self , Text , agent)->str:
        self.__conversation_history.append({"role": "user", "content": Text})
        response = self.__openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=
            [
                {"role": "system", "content": agent},
                {"role": "user", "content": Text},
            ] + self.__conversation_history,
            
            temperature=0.5,
            n=1,
            stop=None,
        )
        try:
            completion_text = response.choices[0].message.content
            self.__conversation_history.append({"role": "assistant", "content": completion_text})
        except KeyError:
            completion_text = "Error processing completion."
        return completion_text

    def __SendRequest4(self , Text , agent)->str:
        self.__conversation_history.append({"role": "user", "content": Text})
        response = self.__openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=
            [
                {"role": "system", "content": agent},
                {"role": "user", "content": Text},
            ] + self.__conversation_history,
            
            temperature=0.5,
            n=1,
            stop=None,
        )
        try:
            completion_text = response.choices[0].message.content
            self.__conversation_history.append({"role": "assistant", "content": completion_text})
        except KeyError:
            completion_text = "Error processing completion."
        return completion_text