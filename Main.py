'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- Main App to manage the server and port number for this server and our app 
'''

from fastapi import FastAPI
from User_Controller import UserContoller


app = FastAPI()

# Include routers for different controllers
app.include_router(UserContoller)





def __main__():
    if __name__ == "__main__":
        #to run the server using this command 
        #uvicorn Request_Controller:app  --reload
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8002)


__main__()