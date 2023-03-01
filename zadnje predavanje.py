class Oseba:


    def __init__(self, ime_osebe, spol):
        self.ime = ime_osebe
        self.spol = spol
        self.sovrazniki = []
        self.svezi_sovraznike = None

    def pozdravi(self):
        print(f"Pozdravljeni, moje ime je, {self.ime} in sem {self.kaj_sem()}")
    def zasovrazi(self, koga: "Oseba"):
        self.sovrazniki.append(koga)
        self.svezi_sovraznik = koga

    def ali_sovrazis(self, ime: str):
        for oseba in self.sovrazniki:
            if oseba.ime == ime:
                return True
        return False
    def izrazi_sovrastvo(self):
        print(f"Sovrazim te, {self.svezi_sovraznik.ime}")
    def jej(self):
        print("Cmook, cmok , cmok")

    def spi(self):
        print("zzzzzzzzz")

class Student(Oseba):
    def __init__(self, ime, spol):
        super().__init__(ime, spol)

        self.ocena = {}
    def kaj_sem(self):
        super().pozdravi()
        if self.spol == "z":
            return "studentka"
        else:
            return "student"

    def prejmi_oceno(self,predmet, ocena):
        self.ocena[predmet] = ocena



    def povej_oceno(self,predmet):
        return self.ocene[predmet]


class Ucitelj(Oseba):
    def __init__(self,ime, spol, naziv):
        super().__init__(ime, spol)
        self.naziv = naziv
    def kaj_sem(self):
        return self.naziv




berta = Oseba("Berta", "z")

cilka = Oseba("Cilka", "z")
ana = Student("Ana", "z")

cilka = Ucitelj("Cilka", "z","docent")
cilka.pozdravi()
ana.pozdravi()