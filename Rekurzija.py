rodbina = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}
def velikost_rodbine(oseba):
    velikost = 0
    for otrok in rodbina[oseba]:
        velikost += velikost_rodbine(otrok)

    return velikost + 1
    #return  1 + sum(velikost_rodbine(otrok) for otrok in oseba)
print(velikost_rodbine("Elizabeta"))



def obstaja(oseba, ime):
    if oseba == ime:
        return True
    for otrok in rodbina[oseba]:
        if obstaja(otrok, ime):
            return True
    return False

print(obstaja('Elizabeta', "Jožef"))


def globina(oseba):
    if not rodbina[oseba]:
        return 0
    naj_globina = 0
    for otrok in rodbina[oseba]:
        g = globina(otrok)
        if g > naj_globina:
            naj_globina = g
    return naj_globina + 1
    #return 1 + max((globina(otrok) for otrok in rodbina[oseba]), default=0)
print(globina("Elizabeta"))


def vsa_imena(oseba):
    vsi = [oseba]
    for otrok in rodbina[oseba]:
        vsi += vsa_imena(otrok)
    return vsi
    #return [oseba] + sum((vsa_imena(otrok) for otrok in rodbina[oseba]), start=[])
print(vsa_imena("Jurij"))

def vsota(s):
    if s == []:
        return 0
    return s[0] + vsota(s[1:])

def max(s):
    if len(s) == 1:
        return s[0]
    if s[0] > max(s[1:]):
        return s[0]
    else:
        return ma



















