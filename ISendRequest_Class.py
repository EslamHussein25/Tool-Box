'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- interface class for all the AI agent to abstract the agent method implementation to avoid futures bugs
'''

from abc import ABC, abstractmethod




class Request(ABC):

    @abstractmethod
    def SendRequest(text, agent):
        pass 