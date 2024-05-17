from fastapi import FastAPI,Body, Cookie, Header
from pydantic import BaseModel, HttpUrl, Field
from typing import List
from uuid import UUID
from datetime import datetime,time,timedelta

myapp = FastAPI(title="My fAPI")

@myapp.get("/")
async def test():
    return {"msg":"this is myapi"}

# class Image(BaseModel):
#     name : str
#     url : HttpUrl

# class Item(BaseModel):
#     name : str = Field(...,example="Hello")
#     desc : str = Field(None,example="new desc")
#     price : float = Field(...,example=123)
#     # tax : float = None
#     # tag : List[str] = []
#     # img : Image

# @myapp.post("/item")
# # async def post_itme(item_id : int, item : Item = Body(...,embed=True)):
# # async def post_itme(item_id : int, item : Item = Body(...,example={"name":"test","desc":"desc","price":123})):
# async def post_itme(item_id : int, item : Item):
#     return item

# for 11 video--

# @myapp.post("/item")
# async def pst(item_id : UUID):
#     cur_time = datetime.now()
#     time_d = timedelta(days=2,hours=6)
#     future_time = cur_time + time_d
#     print(cur_time)
#     print(time_d)
#     print(future_time)
#     return {"item_id" : item_id, "current_time" : cur_time, "time_delta": time_d, "future_time": future_time}


#for 12 video-Cookies and Header Parameter-
@myapp.post("/items")
async def test(cokkie_id : str = Cookie(None),
               except_encoding: str = Header(None),
               sec_ch_us : str = Header(None),
               user_agent : str = Header(None)
               ):
    return {"COOKIES_ID":cokkie_id,"except_encoding":except_encoding,"sec_ch_us":sec_ch_us,"user_agent":user_agent}