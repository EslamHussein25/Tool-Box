'''
Author: Eslam Hussein - Juba 
Date: 11/7/2024
Version: 04
'''
#this class is responsible for:
'''
1- fast api controller - back end side for the user request and AI agent response (main app)
'''

from fastapi import FastAPI , APIRouter , Body , File, UploadFile , Form
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel, Field
from PDF_Class import *
from TokensCalcluation_Class import *
from SendRequest_Class import * 
from DataTransfer_Class import *
from JsonWork_Class import *  

UserContoller = APIRouter(
    prefix="/user",
    tags=["user"]
)

busdata = RequestData()
makeRequest = Request_AI()
jsonWork = JsonConvert()

#this method 
'''
1- Get the pdf file (row data) from user request(post)
2- use pdftool to get the chapters from pd file (row chapters)
3- send this row chapters to to the Tokens Calculation to get the real chapters must send 
4- send this chapters to GPT  and get response 
'''

@UserContoller.post("/upload-files/")
async def UploadFiles(Rowfile: UploadFile = File(...) , Agent:int = Form()):
    pdfTool = PDFTool()
    TokensCtrl = TokensControl()
    RowChapters: List[str] = []

    file_contents = await Rowfile.read()
    RowChapters = pdfTool.GetChapters(Rowfile.file)
    ChaptersMustSend = TokensCtrl.TokensCalculation(RowChapters)
    busdata.SetAgent(Agent)
    busdata.SetChaptersMustSend(ChaptersMustSend)
    makeRequest.AIModel = busdata.GetAgent() 
    JsonResult = makeRequest.UploadFile(busdata.GetChaptersMustSend())
    #strResult = jsonWork.ReadJson(JsonResult)
    return JsonResult
    #return JSONResponse(content={"message": "Successfully Uploaded, Kick Start to start new conversion with your file"})



@UserContoller.post("/ask/")
async def StartChat(Query:str = Form()):

    JsonResult = makeRequest.SendRequest(Query)
    #strResult = jsonWork.ReadJson(JsonResult)
    return JsonResult
    #return JSONResponse(content={"message": strData})
 





