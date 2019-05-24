from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs


engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


def add_restaurant(location, mealType):
    resto_info = findARestaurant(mealType, location)
    print( resto_info )

    resto = Restaurant( restaurant_name=resto_info['name'], restaurant_address=resto_info['address'], restaurant_image=resto_info['image'] )

    session.add(resto)
    session.commit()
    return jsonify(resto = resto.serialize)


def get_all_restaurants():
    restos = session.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restos])


def get_restaurant(id):
    resto = session.query(Restaurant).filter_by(id = id).first()
    print(resto)
    return jsonify(resto)


def update_restaurant(id, name, address, image):
    resto = session.query(Restaurant).filter_by(id = id).one()

    print(resto)

    resto.restaurant_name = name
    resto.restaurant_address = address
    resto.restaurant_image = image

    session.commit()


    return jsonify(resto.serialize)


def delete_restaurant(id):
    print('ID:', id)
    resto = session.query(Restaurant).filter_by(id = id).one()
    resto = session.delete(resto)
    print(resto)

    session.commit()
    return jsonify(resto)



@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
    #YOUR CODE HERE
    if request.method == 'POST':

        restaurant = add_restaurant(
            request.args.get('location', ''), 
            request.args.get('mealType', '')
        )

        return restaurant
    elif request.method == 'GET':
        return get_all_restaurants()

    
@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
    #YOUR CODE HERE
    if request.method == 'GET':
        return get_restaurant(request.args.get('id'))

    if request.method == 'PUT':
        return update_restaurant( 
            id,
            request.args.get('name'),
            request.args.get('address'),
            request.args.get('image')                        
        )

    if request.method == 'DELETE':
        return delete_restaurant(id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

