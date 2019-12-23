from flask import request, json, Response, Blueprint, jsonify, current_app
from src.Models import  Users, UserSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity

user_api = Blueprint('users', __name__)
user_schema = UserSchema()

@user_api.route('/test', methods=['GET'])
def test():
    message = {'message': 'Connected fine'}
    return custom_response(message, 200)

@user_api.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    if not request.is_json:
        return custom_response({"msg": "Missing JSON in request"}, 400)

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not (username) or not (password):
        return custom_response({"Error": "Missing username or password parameter"}, 400)

    if username != current_app.config['ADMIN_USER'] or password != current_app.config['ADMIN_PASS']:
        return custom_response({"Error": "Incorrect username or password"}, 401)
    access_token = create_access_token(identity=req_data)
    msg = {'Authorization': 'Bearer ' + access_token}
    return custom_response(msg, 200)

@user_api.route('/checkjwt', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(jwt_logged_in_user=current_user), 200

@user_api.route('/create', methods=['POST'])
@jwt_required
def create():
    req_data = request.get_json()
    data={}
    try:
        data = user_schema.load(req_data)
    except ValidationError as errr:
        print(errr.messages)
        return custom_response(errr.messages, 400)
    user_in_db = Users.get_user_by_email(data.get('email'))
    if user_in_db:
        message = {'error': 'Duplicate email user exists, please provide another email'}
        return custom_response(message, 400)
    else:
        user = Users(data)
        user.save()
        resp = user_schema.dump(user)
        return custom_response(resp, 201)

@user_api.route('/getusers', methods=['GET'])
@jwt_required
def get_all():
    users = Users.get_all_users()
    resp = user_schema.dump(users, many=True)
    return custom_response(resp, 200)

@user_api.route('/<int:user_id>', methods=['GET'])
@jwt_required
def get_a_user(user_id):
    user = Users.get_one_user(user_id)
    if not user:
        return custom_response({'Error': 'user not found with the given ID'}, 404)
    else:
        resp = user_schema.dump(user)
        return custom_response(resp, 200)  

@user_api.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required
def delete(user_id):
    user = Users.get_one_user(user_id)
    if not user:
        return custom_response({'Error': 'user not found with the given ID'}, 404)
    else:
        user.delete()
        return custom_response({'message': 'user deleted'}, 200)

@user_api.route('/delete', methods=['DELETE'])
@jwt_required
def delete_with_email():
    json_data = request.get_json()
    #print (json_data['email'])
    email = ''
    if not json_data:
        return custom_response({"error": "Input data not proper format"}, 400)
    try:
        email = json_data['email']
    except ValidationError as errr:
        return custom_response(errr.messages, 400)
    user = Users.get_user_by_email(email)
    if not user:
        return custom_response({'Error': 'user not found with the given EmailID'}, 404)
    else:
        user.delete()
        return custom_response({'message': 'User deleted success'}, 200)

@user_api.route('/update', methods=['PUT'])
@jwt_required
def update():
    json_data = request.get_json()
    data = {}
    if not json_data:
        return custom_response({"error": "Input data not proper format"}, 400)
    try:
        data = user_schema.load(json_data)
    except ValidationError as errr:
        return custom_response(errr.messages, 400)
    #print ( data.get('email'))
    user_in_db = Users.get_user_by_email(data.get('email'))
    #print (user_in_db)
    if not user_in_db:
        return custom_response({'Error': 'user not found with the given Email'}, 404)
    else:
        user_in_db.update(data)
        resp = user_schema.dump(user_in_db)
        return custom_response(resp, 200)
  
def custom_response(resp, stat_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(resp),
        status=stat_code
  )