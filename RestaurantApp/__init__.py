import sys
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask

Base = declarative_base()

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/models')
import User
import Restaurant
import Menu

engine = create_engine('sqlite:///RestaurantApp/data/restaurantapp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

# Circular Imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/views')
import Login
import DeleteMenu
import Disconnect
import EditMenu
import NewMenu
import ShowMenu
import DeleteRestaurant
import ShowRestaurant
import EditRestaurant
import NewRestaurant
import ConnectWithGoogle
import ConnectWithFacebook
import DisconnectFromGoogle
import DisconnectFromFacebook
import DownloadJSON
