import MySQLdb
from models.picture import Picture



#========== Classe para acesso ao banco de dados 
#========== para a classe/tabela Picture/Foto


class PictureDao:
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
        cursor.execute("SELECT * FROM FOTO")
        list_picture = []
        for p in cursor.fetchall():
            picture = Picture( p[1] ,p[2], p[3], p[0] )
            list_picture.append(picture.__dict__)
        connection.close()
        return list_picture



    #----- Lista uma unica pessoa, filtrando pela coluna ID 
    def picture_by_id(self, id):
        connection = MySQLdb.connect(
                                        host="mysql.zuplae.com"
                                        ,user="zuplae15"
                                        ,passwd="lend4s"
                                        ,database="zuplae15"
                                    )
        cursor = connection.cursor()
        cursor.execute(f"SELECT ID, CONTEUDO, DESCRICAO, DATA_CRIACAO FROM PESSOA WHERE ID = {id}")
        p = cursor.fetchone()
        picture = Picture( p[1] ,p[2], p[3], p[0] )
        connection.close()
        return picture.__dict__
    #----- Insere um novo registro na tabela FOTO
    def create(self, picture:Picture):
        connection = MySQLdb.connect(
                                        host="mysql.zuplae.com"
                                        ,user="zuplae15"
                                        ,passwd="lend4s"
                                        ,database="zuplae15"
                                    )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO FOTO (CONTEUDO, DESCRICAO, DATA_CRIACAO) VALUES('{picture.conteudo}','{ picture.descri}','{ picture.date_create}')")
        picture.id = cursor.lastrowid
        connection.commit()
        connection.close()

        return picture.__dict__

    #----- Altera um registro na tabela ALBUM
    def update(self, picture:Picture):
        connection = MySQLdb.connect(
                                        host="mysql.zuplae.com"
                                        ,user="zuplae15"
                                        ,passwd="lend4s"
                                        ,database="zuplae15"
                                    )
        cursor = connection.cursor()
        cursor.execute( f"UPDATE FOTO SET CONTEUDO = '{picture.conteudo}', DESCRICAO ='{ picture.descri}', DATA_CRIACAO = '{ picture.date_create}' WHERE ID = {picture.id}")
        connection.commit()
        connection.close()
        return picture.__dict__

    #----- Exclui um registro na tabela FOTO
    def delete(self, id:int):
        connection = MySQLdb.connect(
                                        host="mysql.zuplae.com"
                                        ,user="zuplae15"
                                        ,passwd="lend4s"
                                        ,database="zuplae15"
                                    )
        cursor = connection.cursor()
        cursor.execute(
                        f"DELETE FROM FOTO WHERE ID = '{id}'"
                      )
        connection.commit()
        connection.close()