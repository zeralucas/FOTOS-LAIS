class Album:
    def __init__(self):
        self.__id = 0
        self.__descricao = ''
        self.__pessoa_id = 0

    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def pessoa_id(self):
        return self.__pessoa_id
    @pessoa_id.setter
    def pessoa_id(self, pessoa_id):
        self.__pessoa_id = pessoa_id
    