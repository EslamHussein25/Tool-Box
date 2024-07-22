'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- conver the string which pssed to this method to be single line 
2- Check the end of the chapter using some key words 
'''

class TextWork :

    def __init__(self) -> None:
        self.char_list = ['\n', '(' , ')' , '\t' , '  ' , ':' , '.' , ',']
        self.Chapter_Keywords = ["CH" , "Hotel Riyadh, KSA" , "Hotel" , "Riyadh, KSA" , "chapter" , "End  of the chapter"]    

    def String_Control(self , strings)->str:
        for i in self.char_list :
            words = strings.split(i)
            strings = ''.join(words)
        return strings 

    def CheckEndChapter(self , Text:str)->bool:
        depend = 0 
        max_eff = len(self.Chapter_Keywords)
        for count in self.Chapter_Keywords:
            if count in Text:
                depend+=1
        decision = (depend / max_eff)
        decision *= 100
        if decision >= 50:
            return True 
        else:
            return False 