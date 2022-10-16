
import uuid
from serializer.to_json import serial
from models.userModel import Account , db, api
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify



@api.get('/')
@jwt_required()
def init():
    msg = "Api v1 Connection Success"
    return serial(200, msg)

@api.route("/login", methods=["POST"])
def login():
    
    data = request.get_json()
    query = Account.query.filter_by(username=data["username"]).first()
    

    if(query):
        
        user = query.userGetby()
        pwd = user["pwd"]
        chek_pass = check_password_hash(pwd, data["password"])
        
        if chek_pass is False:
            msg = 'pwd incorrect or urser incorrect'
            return serial(401, msg )
        else:
            user = Account.query.filter_by(username=data["username"]).first()
            user.online = True
            db.session.merge(user)
            db.session.commit()
            access_token = create_access_token(identity=pwd)
            msg ='ok'
        return serial(200, msg, access_token)
    
    else:
        msg = 'pwd incorrect or urser not exist'
        return serial(401, msg )
        
    

@api.route('/v1/account/users', methods=['POST'])
def account():
    data = request.get_json()
    gen_pass = str(generate_password_hash(data["password"]))
    uuidone = str(uuid.uuid4())
    user = Account(
        id = uuidone,
        fullname = data["fullname"],
        username = data["username"],
        password = gen_pass,
        age = data["age"],
        uf = data["uf"]
    )
    db.session.add(user)
    db.session.commit()
    msg = "User created success"
    return serial(200,msg)

@api.route('/v1/account/users', methods=['GET'])
@jwt_required()
def selectAccount():
    cursor = Account.query.all()
    user_json = [Account.selectUser() for Account in cursor]
    return serial(200, user_json)

@api.route('/v1/account/user/<id>', methods=['GET'])
@jwt_required()
def getByIdAccount(id):
    query = Account.query.filter_by(id=id).first()
    query = query.userGetby()
    return serial(200, query)

@api.route('/v1/account/user/<id>', methods=['PUT'])
@jwt_required()
def putByAccount(id):
    data = request.get_json()
    user = Account.query.filter_by(id=id).first()
    
    user.fullname = data["fullname"]
    user.age = data["age"]
    
    db.session.merge(user)
    db.session.commit()

    msg= 'Update succesful'
    return serial(200, msg)
    
@api.route('/v1/account/user/<id>', methods=['DELETE'])
@jwt_required()
def deleteAccount(id):

    user = Account.query.filter_by(id=id).first()

    db.session.delete(user)
    db.session.commit()
    msg = 'Deleted succesful'
    return serial(200, msg)

@api.route('/logout/<id>', methods=["GET"])
def logout(id):
    
    user = Account.query.filter_by(id=id).first()
    user.online = False

    db.session.expunge(user)
    db.session.merge(user)
    db.session.commit()
    user = user.userGetby()
    msg = "logout success"
    return serial(200, msg )

if __name__ == "__main__":
    api.run(port=8000)

