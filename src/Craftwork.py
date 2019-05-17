class Craftwork:

    def __init__(self,type,descryption):
        self._type = type
        self._descryption = descryption
        self._questions = []

    def __str__(self):
        return "Tipo: " + self.Type + '\n' + "Descrição: " + self.Descryption

    @property
    def Type(self):
        return self._type
    
    @property
    def Descryption(self):
        return self._descryption

a = Craftwork("Feio","mais feio")
print(a)