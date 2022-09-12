from flask import request
from serializer.to_json import serial
from models.userModel import User
from models.connection.mysql import connection_mysql
db, api = connection_mysql()

@api.route('/')
def init():
    msg = "Api v1 Connection Success"
    return serial(200, msg)

@api.route('/v1/account/users', methods=['POST'])
def account():
    data = request.get_json()
    user = User(
        fullname = data["fullname"],
        age = data["age"]
    )
    db.session.add(user)
    db.session.commit()

    return serial(200,None,"User created success")

@api.route('/v1/account/users', methods=['GET'])
def selectAccount():
    cursor = User.query.all()
    user_json = [User.selectUser() for User in cursor]
    return serial(200, user_json)

@api.route('/v1/account/user/<id>', methods=['GET'])
def getByIdAccount(id):
    query = User.query.filter_by(id=id).first()
    query = query.selectUser()
    return serial(200, query)

@api.route('/v1/account/user/<id>', methods=['PUT'])
def putByAccount(id):
    data = request.get_json()
    user = User.query.filter_by(id=id).first()
    
    user.fullname = data["fullname"]
    user.age = data["age"]
    
    db.session.merge(user)
    db.session.commit()

    msg= 'Update succesful'
    return serial(200, msg)
    
@api.route('/v1/account/user/<id>', methods=['DELETE'])
def deleteAccount(id):

    user = User.query.filter_by(id=id).first()
    db.session.expunge(user)
    db.session.delete(user)
    db.session.commit()
    msg = 'Deleted succesful'
    return serial(200, msg)