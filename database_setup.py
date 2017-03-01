import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///RestaurantApp/data/restaurantapp.db')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/RestaurantApp/models')
import Restaurant
from Menu import Menu
from User import User
Base.metadata.create_all(engine)



