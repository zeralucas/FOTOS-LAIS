class Foto:
    def __init__(self):
        self.id = 0
        self.descricao = ''
        self.data_criacao = ''

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
    def data_criacao(self):
        return self.__data_criacao
    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self.__data_criacao = data_criacao