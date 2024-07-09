from sqlalchemy import Column,String,Integer,ForeignKey,DATETIME,Float,DateTime
from database import Base
from datetime import datetime

class Users(Base):
    __tablename__="users"
    user_id=Column("user_id",Integer,primary_key=True,index=True,autoincrement=True)
    firstname=Column("firstname",String(50),nullable=False)
    lastname=Column("lastname",String(50),nullable=False)
    username=Column("username",String(50),unique=True,nullable=False)
    email=Column("email",String(50),unique=True,nullable=False)
    password=Column("password",String(255),nullable=False)

    def __init__(self,firstname,lastname,username,email,password):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.email=email
        self.password=password

class Messages(Base):
    __tablename__="massages"
    message_id=Column("message_id",Integer,primary_key=True,index=True,autoincrement=True)
    sender_id=Column("sender_id",Integer,ForeignKey("users.user_id"))
    recipent_id=Column("recipent_id",Integer,ForeignKey("users.user_id"))
    content=Column("content",String(50),nullable=False)
    sent_date=Column("sent_date",DateTime,default=datetime.utcnow())

    def __init__(self,sender_id,recipent_id,content):
        self.sender_id=sender_id
        self.recipent_id=recipent_id
        self.content=content

class Posts(Base):
    __tablename__="posts"
    post_id=Column("post_id",Integer,primary_key=True,index=True,autoincrement=True)
    user_id=Column("user_id",Integer,ForeignKey("users.user_id"))
    content=Column("content",String(50),nullable=False)
    likes=Column("likes",Integer)
    dislike=Column("dislike",Integer)
    created=Column("created",DateTime,default=datetime.utcnow())

    def __init__(self,user_id,content):
        self.user_id=user_id
        self.content=content
class Comments(Base):
    __tablename__="comments"
    id=Column("id",Integer,primary_key=True,index=True,autoincrement=True)
    post_id=Column("post_id",Integer,ForeignKey("posts.post_id"))
    user_id=Column("user_id",Integer,ForeignKey("users.user_id"))
    comments=Column("comments",String(50))
    created=Column("created",DateTime,default=datetime.utcnow())

    def __init__(self,post_id,user_id,comments):
        self.post_id=post_id
        self.user_id=user_id
        self.comments=comments



class Account(Base):
    __tablename__="account"
    account_id=Column("account_id",Integer,primary_key=True,autoincrement=True)
    account_num=Column("account_num",String(50),unique=True,nullable=False,index=True)
    user_id=Column("user_id",Integer,ForeignKey("users.user_id"))
    amount=Column("amount",Float)

    def __init__(self,user_id,amount,account_num):
        self.user_id=user_id
        self.amount=amount
        self.account_num=account_num

class Transactions(Base):
    __tablename__="transactions"
    id=Column("id",Integer,primary_key=True,index=True,autoincrement=True)
    user_id=Column("user_id",Integer,ForeignKey("users.user_id"))
    sender_account=Column("sender",String(50),ForeignKey("account.account_num"))
    rec_account=Column("reciver",String(50),ForeignKey("account.account_num"))
    date=Column("date",DateTime,default=datetime.utcnow())
    amount = Column("amount", Float)

    def __init__(self,user_id,sender_account,rec_account,amount):
        self.user_id=user_id
        self.sender_account=sender_account
        self.rec_account=rec_account
        self.amount=amount



