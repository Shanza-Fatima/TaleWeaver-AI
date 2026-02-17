from sqlalchemy import create_engine #autually coonecting with the db
from sqlalchemy.orm import sessionmaker #create a session everytime when talking to db
from sqlalchemy.ext.declarative import declarative_base #the foundation for models every table u create will inherit from this

from core.config import settings
#the url to connect with the databse
engine = create_engine(
    settings.DATABASE_URL

)
                            #make sure not to commit everything unless told, # prevents alcmy to send every small detai to db
SessionLocal = sessionmaker(autocomit = False, autoflush=False, bind=engine)# connects the seeion factory to the enginer
#a templete or a class that is inherited in a class sqlalcmy auto knows that the user class is database table
Base = declarative_base() #the d_b : the factory

def get_db():
    db = SessionLocal() # create fresh session for a single request
    try:
        yield db #provide the session to API route
    finally:
        db.close() #always clos the connec when its done

def create_tables():
    Base.metadata.create_all(bind = engine)
    #Base : the special variable i.e the main registration office
    #metadata : A catalog of Base which store all the tables, coloumns etc i.e the register
    #engine : where the implementation will happen i.e the construction site
    #create_all : will implement all the tables