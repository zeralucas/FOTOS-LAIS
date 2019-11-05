class Picture:
    def __init__(self, conteudo, descri, date_create, id=None):
        self.id = id
        self.descri = descri
        self.date_create = str(date_create)
        self.conteudo = conteudo