from database import engine,Base
from models import Users,Messages,Posts,Account,Transactions

Base.metadata.create_all(bind=engine)