from classes import firma, mitarbeiter, abteilungsleiter, gender, typ

def createCompany(name):
    return firma.Firma(name)

def createEmployee(type, name, abt, gender, f):
    e = None
    match type:
        case typ.Typ.Mitarbeiter:
            e = mitarbeiter.Mitarbeiter(name, abt, gender)
        case typ.Typ.Leiter:
            e = abteilungsleiter.Abteilungsleiter(name, abt, gender)
    f.addPerson(e)
    return e

def getPeople(f, t):
    p = f.getPersonen()
    return p[t]

if __name__ == "__main__":
    f = createCompany("Firma oda so")
    m1 = createEmployee(typ.Typ.Mitarbeiter, "Franz", "IT", gender.Gender.male, f)
    m2 = createEmployee(typ.Typ.Mitarbeiter, "Pepi", "Marketing", gender.Gender.male, f)
    m3 = createEmployee(typ.Typ.Mitarbeiter, "Josie", "IT", gender.Gender.female, f)
    m4 = createEmployee(typ.Typ.Mitarbeiter, "Sylvi", "Produktion", gender.Gender.female, f)
    a1 = createEmployee(typ.Typ.Leiter, "Rainer", "Marketing", gender.Gender.male, f)
    a2 = createEmployee(typ.Typ.Leiter, "Moni", "IT", gender.Gender.female, f)
    a3 = createEmployee(typ.Typ.Leiter, "Stoani", "Produktion", gender.Gender.male, f)
    print("Es sind " + str(getPeople(f, typ.Typ.Mitarbeiter)) + " Mitarbeiter im Unternehmen!")
    print("Es sind " + str(getPeople(f, typ.Typ.Leiter)) + " Abteilungsleiter im Unternehmen!")
    print("Es gibt " + str(f.getAbteilungszahl()) + " Abteilungen im Unternehmen!")
    print("Die Abteilung " + str(f.getStaerksteAbteilung()) + " hat die meisten Mitarbeiter!")
    print(f.getAnteil())