from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs

def add_restaurant:
    

engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
    #YOUR CODE HERE
    if request.method == 'POST':
        restarant = add_restaurant()
    elif requent.method == 'GET':
        restaurant = get_restaurant()
    
    
@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
    #YOUR CODE HERE

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


