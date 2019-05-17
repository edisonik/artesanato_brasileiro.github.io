from datetime import date,datetime

class Person:

    def __init__(self,name,birthday,location,nationality):
        self._name = name
        self._birthday = birthday
        self._location = location
        self._nationality = nationality
    
    def __str__(self):
        return "Nome: " + self.Name + '\n' + "Data de nascimento: " + str(self.Birthday) + '\n' + "Natural de: " + self.Location + '\n' + "Nacionalidade: " + self.Nationality
        
    @property
    def Name(self):
        return self._name
    
    @property
    def Birthday(self):
        return self._birthday
    
    @property
    def Location(self):
        return self._location
    
    @property
    def Nationality(self):
        return self._nationality
