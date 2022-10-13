from email import message
from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# handling post form data
careers_post_args = reqparse.RequestParser()
careers_post_args.add_argument('career_id', type=int, help="You need to specify the career id", required=True)
careers_post_args.add_argument('name', type=str, help='Name of career is required', required=True)

careers_put = reqparse.RequestParser()
careers_put.add_argument('career_id', type=int, help="You need to specify the career id", required=True)
careers_put.add_argument('name', type=str, help='Name of career is required', required=True)

people = {2: {'name': 'Elizabeth Holmes', 'gender': 'Female', 'age': 35}}
careers = {}

# an api that manages people and careers

# search By name
class GetPerson(Resource):
    def get(self, person_id):
        return people[person_id]

api.add_resource(GetPerson, "/person/<int:person_id>")

# add new person
class AddPerson(Resource):
    def post(self):
        person = {}
        person_id = request.form['p_id']
        person['name'] = request.form['name']
        person['gender'] = request.form['gender']
        person['age'] = request.form['age']
        people[person_id] = person
        return people

api.add_resource(AddPerson, "/add-person")

# add new career
class AddCareer(Resource):
    def post(self):
        args = careers_post_args.parse_args()
        careers[args['career_id']] = {'name': args['name']}
        return careers

api.add_resource(AddCareer, '/add-career')

class ChangerCareer(Resource):
    def put(self):
        args = careers_put.parse_args()
        career = careers[args['career_id']]
        career['name'] = args['name']
        return careers

api.add_resource(ChangerCareer, '/update-career')

def abort_if_not_found(p_id):
    if p_id not in people:
        abort(409, message='Person not found')

class DeletePerson(Resource):
    def delete(self, p_id):
        abort_if_not_found(p_id)
        del people[p_id]
        return people

api.add_resource(DeletePerson, '/delete-person/<int:p_id>')

if __name__ == "__main__":
    app.run(debug=True)