class Person():
    
    def __init__(self, name, abteilung, gender):
        self.name = name
        self.abteilung = abteilung
        self.gender = gender
    
    def getName(self):
        return self.name
    
    def getAbteilung(self):
        return self.abteilung
    
    def getGender(self):
        return self.gender