from classes.typ import Typ
from classes.person import Person

class Mitarbeiter(Person):
    
    def __init__(self, name, abtelung, gender):
        super().__init__(name, abtelung, gender)
        self.typ = Typ.Mitarbeiter
        
    def getName(self):
        return super().getName()
    
    def getAbteilung(self):
        return super().getAbteilung()
    
    def getGender(self):
        return super().getGender()
    
    def getType(self):
        return self.typ