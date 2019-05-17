class Biography:
    
    def __init__(self, author = "", title = "", content = ""):
        self._author = author
        self._title = title
        self._content = content
    
    def __str__(self):
        return "Autor: " + self.Author + '\n' + "Título: " + self.Title + '\n' + "Conteúdo: " + self.Content
            
    @property
    def Author(self):
        return self._author
    
    @property
    def Title(self):
        return self._title

    @property
    def Content(self):
        return self._content
