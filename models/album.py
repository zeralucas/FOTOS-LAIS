class Album:
    def __init__(self, titulo, descricao, pessoa_id, id=None):
        self.id = id
        self.descricao = descricao
        self.pessoa_id = pessoa_id
        self.titulo = titulo