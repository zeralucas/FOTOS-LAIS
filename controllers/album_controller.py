from flask_restful import Resource, reqparse
import MySQLdb
from models.album import Album
from dao.album_dao import AlbumDao


class AlbumController(Resource):
    def __init__(self):
        self.dao = AlbumDao()
        self.req = reqparse.RequestParser()
        self.req.add_argument("id")
        self.req.add_argument("titulo")
        self.req.add_argument("descricao")
        self.req.add_argument("pessoa_id")

    def get(self,pessoa_id:int, id=None):
        if id is not None:
            self.dao.album_by_id(id)
        return self.dao.list_all()

    def post(self,pessoa_id:int):
        args = self.req.parse_args()
        descricao = args['descricao']
        titulo = args['titulo']
        pessoa_id = args['pessoa_id']
        album = Album(descricao, titulo, pessoa_id)
        return self.dao.create(album), 201