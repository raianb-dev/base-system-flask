import uuid
from serializer.to_json import serial
from models.userModel import Account , db, api
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify
from flask import Flask
from flasgger import Swagger

# Configuração do Swagger para JWT Bearer Auth
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Base System API",
        "description": "Base System Flask",
        "version": "1.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Insira o token JWT com o prefixo 'Bearer '. Exemplo: Bearer seu_token_aqui"
        }
    }
}
swagger = Swagger(api, template=swagger_template)

@api.get('/')
@jwt_required()
def init():
    """
    Teste de conexão com a API.
    ---
    tags:
      - Ordens de Serviço
    security:
      - Bearer: []
    responses:
      200:
        description: Conexão bem-sucedida
    """
    msg = "Api v1 Connection Success"
    return serial(200, msg)

@api.route("/login", methods=["POST"])
def login():
    """
    Login do usuário.
    ---
    tags:
      - Acesso
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login realizado com sucesso
      401:
        description: Usuário ou senha incorretos
    """
    
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
            access_token = "Bearer"+" "+create_access_token(identity=pwd)
            
            msg ='ok'
        return serial(200, msg, access_token)
    
    else:
        msg = 'pwd incorrect or urser not exist'
        return serial(401, msg )
        
    

@api.route('/v1/account/users', methods=['POST'])
def account():
    """
    Criação de novo usuário.
    ---
    tags:
      - Acesso
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - fullname
            - username
            - password
            - age
            - uf
          properties:
            fullname:
              type: string
            username:
              type: string
            password:
              type: string
            age:
              type: integer
            uf:
              type: string
    responses:
      200:
        description: Usuário criado com sucesso
    """
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
    """
    Lista todos os usuários.
    ---
    tags:
      - Acesso
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de usuários
    """
    cursor = Account.query.all()
    user_json = [Account.selectUser() for Account in cursor]
    return serial(200, user_json)

@api.route('/v1/account/user/<id>', methods=['GET'])
@jwt_required()
def getByIdAccount(id):
    """
    Busca usuário por ID.
    ---
    tags:
      - Acesso
    security:
      - Bearer: []
    parameters:
      - in: path
        name: id
        type: string
        required: true
    responses:
      200:
        description: Usuário encontrado
    """
    query = Account.query.filter_by(id=id).first()
    query = query.userGetby()
    return serial(200, query)

@api.route('/v1/account/user/<id>', methods=['PUT'])
@jwt_required()
def putByAccount(id):
    """
    Atualiza dados do usuário.
    ---
    tags:
      - Acesso
    security:
      - Bearer: []
    parameters:
      - in: path
        name: id
        type: string
        required: true
      - in: body
        name: body
        schema:
          type: object
          required:
            - fullname
            - age
          properties:
            fullname:
              type: string
            age:
              type: integer
    responses:
      200:
        description: Atualização realizada com sucesso
    """
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
    """
    Remove usuário por ID.
    ---
    tags:
      - Ordens de Serviço
    security:
      - Bearer: []
    parameters:
      - in: path
        name: id
        type: string
        required: true
    responses:
      200:
        description: Usuário removido com sucesso
    """
    user = Account.query.filter_by(id=id).first()

    db.session.delete(user)
    db.session.commit()
    msg = 'Deleted succesful'
    return serial(200, msg)

@api.route('/logout/<id>', methods=["GET"])
def logout(id):
    """
    Logout do usuário.
    ---
    tags:
      - Ordens de Serviço
    parameters:
      - in: path
        name: id
        type: string
        required: true
    responses:
      200:
        description: Logout realizado com sucesso
    """
    
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

