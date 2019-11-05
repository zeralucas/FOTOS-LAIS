import MySQLdb
from models.album import Album

#========== Classe para acesso ao banco de dados 
#========== para a classe/tabela Picture/Foto


class AlbumDao:
    #----- construtor da class para iniciar conexao com o banco
    def __init__(self):
        pass
    #----- Lista todos os dados da tabela foto
    def list_all(self):
        connection = MySQLdb.connect(
                                        host="mysql.zuplae.com"
                                        ,user="zuplae15"
                                        ,passwd="lend4s"
                                        ,database="zuplae15"
                                    )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ALBUM")
        list_album = []
        for p in cursor.fetchall():
            album = Album( p[1] ,p[2], p[3], p[0] )
            list_album.append(album.__dict__)
        connection.close()
        return list_album

    def create(self, album:Album):
        connection = MySQLdb.connect(
                                        host="mysql.zuplae.com"
                                        ,user="zuplae15"
                                        ,passwd="lend4s"
                                        ,database="zuplae15"
                                    )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO ALBUM (TITULO, DESCRICAO, PESSOA_ID) VALUES('{album.titulo}','{ album.descricao}',{ album.pessoa_id})")
        album.id = cursor.lastrowid
        connection.commit()
        connection.close()

        return album.__dict__


    #----- Lista uma unica pessoa, filtrando pela coluna ID 
    def album_by_id(self, id):
        connection = MySQLdb.connect(
                                        host="mysql.zuplae.com"
                                        ,user="zuplae15"
                                        ,passwd="lend4s"
                                        ,database="zuplae15"
                                    )
        cursor = connection.cursor()
        cursor.execute(f"SELECT ID, TITULO, DESCRICAO, PESSOA_ID FROM ALBUM WHERE ID = {id}")
        p = cursor.fetchone()
        album = Album( p[1] ,p[2], p[3], p[0] )
        connection.close()
        return album.__dict__