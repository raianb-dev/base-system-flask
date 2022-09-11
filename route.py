from flask import Flask, request, jsonify
from serializer.to_json import serial
from models.userModel import User, db
from models.connection.mysql import connection_mysql

db, api = connection_mysql()

@api.route('/')
def init():
    msg = "Api v1 Connection Success"
    return serial(200, msg)

@api.route('/v1/account/user', methods=['POST'])
def account():
    data = request.get_json()
    user = User(
        fullname = data["fullname"],
        age = data["age"]
    )
    db.session.add(user)
    db.session.commit()
    msg = {"ok":"ok"}
    return jsonify(msg)