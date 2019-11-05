from flask_restful import Resource, reqparse
import MySQLdb
from models.picture import Picture
from dao.picture_dao import PictureDao


class PictureController(Resource):
    def __init__(self):
        self.dao = PictureDao()
        self.req = reqparse.RequestParser()
        self.req.add_argument("id")
        self.req.add_argument("descri")
        self.req.add_argument("date_create")
        self.req.add_argument("conteudo")


    def get(self,pessoa_id:int, album_id:int, id=None):
        if id is not None:
            return self.dao.picture_by_id(id)
        return self.dao.list_all()

    def post(self,pessoa_id:int, album_id:int):
        args = self.req.parse_args()
        descri = args['descri']
        date_create = args['date_create']
        conteudo = args['conteudo']
        picture = Picture(conteudo, descri, date_create)
        return self.dao.create(picture), 201


    def put(self,pessoa_id:int, album_id:int, id:int):
        args = self.req.parse_args()
        descri = args['descri']
        date_create = args['date_create']
        conteudo = args['conteudo']
        picture = Picture(descri, date_create, conteudo, id)
        return self.dao.update(picture)

    def delete(self,pessoa_id:int, album_id:int, id:int):
        self.dao = PictureDao()
        self.dao.delete(id)
        return "DELETADO MONXTRAO", 204
      