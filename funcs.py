from flask import jsonify, request
from flask_restful import Resource
from database import init_db


class List(Resource):

    def get(self):
        motivations = list(init_db().motivations.find({'is_visible': True}))
        return jsonify({'Motivations': [motivation for motivation in motivations]})

    def post(self):
        data = request.get_json()
        motivation = {
            "_id": list(init_db().motivations.find().sort('_id', -1).limit(1))[0]['_id'] + 1,
            "nickname": data["nickname"],
            "motivation": data["motivation"],
            "is_visible": data["is_visible"]
        }
        try:
            init_db().motivations.insert_one(motivation)
        except:
            raise Exception
        return {"message": "created"}, 201


class ListDetail(Resource):

    def get(self, id):
        motivation = init_db().motivations.find_one({'_id': id})
        if motivation:
            return jsonify(motivation)
        return {"message": f"Motivation with id:{id} not found"}, 404

    def put(self, id):
        query = init_db().motivations.find_one({'_id': id})
        if query:
            data = request.get_json()
            updated_motivation = {
                "_id": id,
                "nickname": data['nickname'],
                "motivation": data['motivation'],
                "is_visible": data['is_visible']
            }
            init_db().motivations.update_one({'_id': id}, {'$set': updated_motivation})
            return {"message": "updated"}, 200
        return {"message": f"Motivation with id:{id} not found"}, 404

    def delete(self, id):
        init_db().motivations.delete_one({'_id': id})
        return {"message": "deleted"}, 200


class ListRandom(Resource):

    def get(self):
        motivation = init_db().motivations.aggregate([{'$sample': {'size': 1}}])
        if motivation:
            return jsonify({'Motivation': [element for element in motivation]})
        return {"message": "No entries!"}, 404



