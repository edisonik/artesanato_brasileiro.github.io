from Person import Person
from Biography import Biography
from datetime import date

class Artisan(Person):

    def __init__(self,name,birthday,location): 
        self._biography = Biography()
        Person.__init__(self,name,birthday,location,"Brasileiro")
    
    def __str__(self):
        return Person.__str__(self)

    @property 
    def MetaData(self):
        return str(self) + '\n' + str(self._biography)
    
    def setBiography(self,author,title,content):
        self._biography._author = author
        self._biography._title = title
        self._biography._content = content
        