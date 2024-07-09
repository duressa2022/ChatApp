from pydantic import BaseModel
from datetime import datetime

class userCreated(BaseModel):
    username:str
    firstname:str
    lastname:str
    password:str
    email:str
class userLogin(BaseModel):
    username:str
    password:str
class userResponse(BaseModel):
    user_id:int
    username:str
    class config:
        orm_mode=True

class messageCreated(BaseModel):
    sender_id:int
    recipent_id:int
    content:str

class messageResponse(BaseModel):
    message_id:int

    class config:
        orm_mode=True
class postCreated(BaseModel):
    content:str

class postResponse(BaseModel):
    user_id:int
    post_id:int
    content:str
    class config:
        orm_mode=True


class accountCreated(BaseModel):
    user_id:int
    account_num:str
    amount:float

class accountResponse(BaseModel):
    user_id:int
    class config:
        orm_mode=True

class transactionCreated(BaseModel):
    user_id:int
    sender_account:str
    rec_account:str

class tranactionResponse(BaseModel):
    id:int
    class config:
        orm_mode=True
class updateFirst(BaseModel):
    firstname:str
class updatelast(BaseModel):
    lastname:str
class updateuser(BaseModel):
    username:str
class updatepass(BaseModel):
    password:str
class updateemail(BaseModel):
    email:str
class createComment(BaseModel):
    user_id:int
    comments:str
class createLike(BaseModel):
    user_id:int
class loadMessage(BaseModel):
    sender_id:int
    recipent_id:int



