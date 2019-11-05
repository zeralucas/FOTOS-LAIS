from flask import Flask, render_template, redirect, request, session,flash,url_for
import MySQLdb 
from flask_restful import Api, Resource
from controllers.picture_controller import PictureController
from controllers.album_controller import AlbumController
# from foto import Foto
# from albumFoto import AlbumFoto
# from album import Album
from flask_cors import CORS

# album = 'Padawan Album'


# #################### INSERIR A FOTO DO PERFIL ###################################################################
# def inserir_foto_perfil():
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae15", passwd="lend4s", database="zuplae15")
#     cursor = conexao.cursor()
#     #chamando_classe= Foto()

#     cursor.execute("INSERT INTO  ()VALUES(NULL,'{}','{}','{}')")
#     conexao.commit()
#     conexao.commit()
#     conexao.close()

app = Flask(__name__)
CORS(app)
api = Api(app)

##segura lais

#### Albuns
api.add_resource(AlbumController, '/api/pessoa/<int:pessoa_id>/album/', endpoint="albuns")
api.add_resource(AlbumController, '/api/pessoa/<int:pessoa_id>/album/<int:id_album>', endpoint="album")
#### Fotos
api.add_resource(PictureController, '/api/pessoa/<int:pessoa_id>/album/<int:album_id>/foto', endpoint="fotos")
api.add_resource(PictureController, '/api/pessoa/<int:pessoa_id>/album/<int:album_id>/foto/<int:id>', endpoint="foto")


######
#api.add_resource(AlbumController, '/api/adicionar/', endpoint="adicionar")


app.run(debug=True, host="192.168.0.151", port="80")