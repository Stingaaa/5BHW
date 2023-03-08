from classes.gender import Gender
from classes.typ import Typ

class Firma:
    
    def __init__(self, name):
        self.name = name
        self.personen = []
        self.personenProTyp = {Typ.Mitarbeiter: 0, Typ.Leiter: 0}
        self.abteilungen = []
        self.mitarbeiterProAbteilung = {}
        
    def getName(self):
        return self.name
    
    def addPerson(self, p):
        self.personen.append(p)
        self.personenProTyp[p.getType()] += 1
        if p.getAbteilung() in self.mitarbeiterProAbteilung:
            self.mitarbeiterProAbteilung[p.getAbteilung()] += 1
        else:
            self.mitarbeiterProAbteilung[p.getAbteilung()] = 1
            self.abteilungen.append(p.getAbteilung())
        
    def getPersonen(self):
        return self.personenProTyp
    
    def getAbteilungszahl(self):
        return len(self.abteilungen)
    
    def getStaerksteAbteilung(self):
        count = 0
        abt = ""
        for i in range(len(self.mitarbeiterProAbteilung)):
            if count < self.mitarbeiterProAbteilung[self.abteilungen[i]]:
                count = self.mitarbeiterProAbteilung[self.abteilungen[i]]
                abt = self.abteilungen[i]
        return abt
    
    def getAnteil(self):
        male = 0
        female = 0
        for i in self.personen:
            g = i.getGender()
            match g:
                case Gender.male:
                    male += 1
                case Gender.female:
                    female += 1
        return "Anteil Männer: " + str(male) + " - " + str(round(male/(male+female)*100,2)) + "%\nAnteil Frauen: " + str(female) + " - " + str(round(female/(male + female)*100,2)) + "%"