
from fastapi import FastAPI,Depends,HTTPException
from models import Users,Messages,Posts,Transactions,Account
from schemas import userCreated,userLogin,userResponse
from schemas import messageCreated,messageResponse
from schemas import postResponse,postCreated
from schemas import accountCreated,accountResponse
from schemas import transactionCreated,tranactionResponse
from schemas import updateemail,updatelast,updateuser,updateFirst,updatepass,createLike
from schemas import createComment,loadMessage
from models import Comments
from database import get_db
from typing import List
from sqlalchemy.orm import Session
import bcrypt

app=FastAPI()

@app.post("/register",response_model=userResponse)
def register_user(user:userCreated,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.email==user.email).first()
    if db_user:
        raise HTTPException(status_code=400,detail="User already exist")
    password=bcrypt.hashpw(user.password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    new_user=Users(firstname=user.firstname,lastname=user.lastname,username=user.username,email=user.email,password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@app.post("/login",response_model=userResponse)
def login_user(user:userLogin,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.username==user.username).first()
    if not db_user or not bcrypt.checkpw(user.password.encode("utf-8"),db_user.password.encode("utf-8")):
        raise HTTPException(status_code=400,detail="Invalid username or password")
    return db_user
@app.get("/getprofile/{user_id}")
def get_profile(user_id:int,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.user_id==user_id).first()
    return db_user
@app.put("/updatefirst/{user_id}")
def update_first(user_id:int,user:updateFirst,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.user_id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=400,detail="User not found")
    db_user.firstname=user.firstname
    db.commit()
    db.refresh(db_user)
    return {
        "message":"first name is updated"
    }
@app.put("/updatelast/{user_id}")
def update_last(user_id:int,user:updatelast,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.user_id==user_id).first()
    db_user.lastname=user.lastname
    db.commit()
    db.refresh(db_user)
    return {
        "message":"lastname is updated"
    }
@app.put("/updatepass/{user_id}")
def update_pass(user_id:int,user:updatepass,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.user_id==user_id).first()
    db_user.password=bcrypt.hashpw(user.password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    db.commit()
    db.refresh(db_user)
    return {
        "message":"password is updated"
    }
@app.put("/updateemail/{user_id}")
def update_email(user_id:int,user:updateemail,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.user_id==user_id).first()
    db_user.email=user.email
    db.commit()
    db.refresh(db_user)
    return {
        "message":"email is updated"
    }
@app.put("/updateuser/{user_id}")
def update_user(user_id:int,user:updateuser,db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.user_id==user_id).first()
    db_user.username=user.username
    db.commit()
    db.refresh(db_user)
    return {
        "message":"user name updated"
    }
@app.post("/createpost/{user_id}")
def create_post(user_id:int,post:postCreated,db:Session=Depends(get_db)):
    user_post=Posts(user_id=user_id,content=post.content)
    db.add(user_post)
    db.commit()
    db.refresh(user_post)
    return {
        "message":"you successfully created a post!"
    }
@app.put("/updatepost/{post_id}")
def update_post(post_id:int,post:postCreated,db:Session=Depends(get_db)):
    user_post=db.query(Posts).filter(Posts.post_id==post_id).first()
    if not user_post:
        raise HTTPException(status_code=404,detail="post is not found")
    user_post.content=post.content
    db.commit()
    db.refresh(user_post)
    return {
        "message":"your post succesfully updated!!!"
    }
@app.delete("/deletepost/{post_id}")
def delete_post(post_id:int,db:Session=Depends(get_db)):
    user_post=db.query(Posts).filter(Posts.post_id==post_id).first()
    if not user_post:
        raise HTTPException(status_code=404,detail="post is not found!!!")
    db.delete(user_post)
    db.commit()
    return {
        "message":"your post is succesfully deleted"
    }
@app.get("/viewpost/{user_id}")
def view_post(user_id:int,db:Session=Depends(get_db)):
    user_post=db.query(Posts).filter(Posts.user_id==user_id).all()
    if not user_post:
        raise HTTPException(status_code=404,detail="You haven't posted yet.")
    return user_post
@app.get("/searchuser/{username}")
def search_user(username:str,db:Session=Depends(get_db)):
    user=db.query(Users).filter(Users.username==username).first()
    if user:
        return {
            "message":"True",
            "user_id":user.user_id
        }
    else:
        return {
            "message":"False"
        }
@app.get("/verfiy/{post_id}")
def verfiy(post_id:int,db:Session=Depends(get_db)):
    post=db.query(Posts).filter(Posts.post_id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="post not found")
    return {
        "message":"found"
    }
@app.post("/createcomment/{post_id}")
def create_comment(post_id:int,comment:createComment,db:Session=Depends(get_db)):
    post_comment=Comments(post_id=post_id,user_id=comment.user_id,comments=comment.comments)
    db.add(post_comment)
    db.commit()
    db.refresh(post_comment)
    return {
        "message":"commented"
    }
@app.put("/like/{post_id}")
def like_post(post_id:int,db:Session=Depends(get_db)):
    post=db.query(Posts).filter(Posts.post_id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="post not found")
    if post.likes is None:
        post.likes=0
    post.likes=post.likes+1
    db.commit()
    db.refresh(post)
    return {
        "message":"you liked the post"
    }
@app.put("/dislike/{post_id}")
def dislike_post(post_id:int,db:Session=Depends(get_db)):
    post=db.query(Posts).filter(Posts.post_id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="post not found")

    if post.dislike is None:
        post.dislike=0
    post.dislike = post.dislike + 1
    db.commit()
    db.refresh(post)
    return {
        "message":"you disliked the post"
    }
@app.post("/messages")
def send_message(message:messageCreated,db:Session=Depends(get_db)):
    sent=Messages(message.sender_id,message.recipent_id,message.content)
    db.add(sent)
    db.commit()
    db.refresh(sent)
    return {
        "message":"message sent!"
    }
@app.get("/username/{user_id}")
def get_username(user_id: int,db:Session=Depends(get_db)):
    users=db.query(Users).filter(Users.user_id==user_id).first()
    if not users:
        raise HTTPException(status_code=404,detail="not found")
    return {
        "message":users.username
    }
@app.get("/message_data")
def load_message(message:loadMessage,db:Session=Depends(get_db)):
    messages=db.query(Messages).filter(
        or_(Messages.sender_id==message.sender_id & Messages.recipent_id==message.recipent_id )
         (Messages.recipent_id==message.sender_id & Messages.sender_id==message.recipent_id)).all()
    if not messages:
        raise HTTPException(status_code=400,detail="not message yet")
    return messages


