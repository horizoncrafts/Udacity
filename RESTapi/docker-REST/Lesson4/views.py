
from models import Base, User, Bagel
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
# deprecated
#from flask.ext.httpauth import HTTPBasicAuth
from flask_httpauth import HTTPBasicAuth



engine = create_engine('sqlite:///bagelShop.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

auth = HTTPBasicAuth() 

@auth.verify_password
def verify_password(username, password):
    print('Verify:', username, password)
    q = session.query(User).filter_by( name = username )
    #print(str(q))
    user = q.first()
    return user.passwordHash == password

#ADD a /users route here
@app.route('/users', methods = ['POST'])
def addUser():
    name = request.json.get('username')
    password = request.json.get('password')


    print( 'addUser:', name, password)

    newUser = User(name, password)
    session.add(newUser)
    session.commit()

    return jsonify(newUser.serialize)


@app.route('/bagels', methods = ['POST'])
#@auth.login_required
def post_showAllBagels():

    print( 'POST:', request.authorization )

    if request.method == 'GET':
        bagels = session.query(Bagel).all()
        return jsonify(bagels = [bagel.serialize for bagel in bagels])
    elif request.method == 'POST':

        name = request.json.get('name')
        description = request.json.get('description')
        picture = request.json.get('picture')
        price = request.json.get('price')
        newBagel = Bagel(name = name, description = description, picture = picture, price = price)
        session.add(newBagel)
        session.commit()
        return jsonify(newBagel.serialize)



@app.route('/bagels', methods = ['GET'])
@auth.login_required
def showAllBagels():

    print( 'GETh:', request.headers )
    print( 'GETa:', request.authorization )

    if request.method == 'GET':
        bagels = session.query(Bagel).all()
        return jsonify(bagels = [bagel.serialize for bagel in bagels])
    elif request.method == 'POST':

        name = request.json.get('name')
        description = request.json.get('description')
        picture = request.json.get('picture')
        price = request.json.get('price')
        newBagel = Bagel(name = name, description = description, picture = picture, price = price)
        session.add(newBagel)
        session.commit()
        return jsonify(newBagel.serialize)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)