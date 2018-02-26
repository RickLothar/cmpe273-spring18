from flask import Flask, request, jsonify

# this file for test and others, please use hello.py to run the program

app = Flask(__name__)

user_id = 0
user_list = []

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/users', methods=['POST', 'GET'])
def add_user():
    user_id = len(user_list)
    name = request.form["name"]
    new_user = {"id": user_id+1, "name": name}
    user_list.append(new_user)
    if request.method == 'POST':
        print(user_list[user_id])
        return jsonify(new_user), 201
    elif request.method == 'GET':
        return jsonify(new_user)
    else:
        return 404


@app.route('/users/<int:user_id>', methods=['GET', 'DELETE'])
def show_user(user_id):
    if request.method == 'GET':
        if user_id <= len(user_list):
            print(user_list[user_id-1])
            return jsonify(user_list[user_id-1])
        else:
            print("No user with this ID")
            return "User Not Found",404
    elif request.method == 'DELETE':
        if user_id <= len(user_list):
            del user_list[user_id-1]
            return "user deleted",204
        else:
            return "No such user",400
    else:
        return "Method not supported"
