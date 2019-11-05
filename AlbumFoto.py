class AlbumFoto:
    def __init__(self):
        self.id = 0
        self.album_id = 0
        self.foto_id = 0

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def album_id(self):
        return self.__album_id
    @album_id.setter
    def album_id(self, album_id):
        self.__album_id = album_id

    @property
    def foto_id(self):
        return self.__foto_id
    @foto_id.setter
    def foto_id(self, foto_id):
        self.__foto_id = foto_id