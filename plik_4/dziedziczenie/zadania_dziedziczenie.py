from abc import ABC, abstractmethod

# 2.1.Utwórz klasę Osoba z atrybutami imie i nazwisko. Następnie utwórz klasę Pracownik,
# która dziedziczy po Osoba i dodaje atrybut stanowisko. Przetestuj działanie klas.


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"Osoba: {self.imie} {self.nazwisko}"

    def __repr__(self):
        return f"Osoba(imie='{self.imie}', nazwisko='{self.nazwisko}')"

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}"

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, stanowisko):
        super().__init__(imie, nazwisko)
        self.stanowisko = stanowisko

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}, Stanowisko: {self.stanowisko}"

    def __repr__(self):
        return f"Pracownik(imie='{self.imie}', nazwisko='{self.nazwisko}', stanowisko='{self.stanowisko}')"

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}, pracuję jako {self.stanowisko}"

osoba = Osoba("Marlena", "Czurak")
pracownik = Pracownik("Marlena", "Czurak", "Programistka")

print("Osoba:", osoba)
print("Pracownik:", pracownik)


# 2.2.Nadpisywanie metod (method overriding) Dodaj metodę przedstaw_sie() w klasie
# Osoba, która zwraca "Jestem imię nazwisko". Nadpisz tę metodę w klasie Pracownik,
# aby dodatkowo podawała stanowisko.

print(osoba.przedstaw_sie())
print(pracownik.przedstaw_sie())


# 2.3.Dziedziczenie wielopoziomowe - Dodaj klasę Kierownik, która dziedziczy po
# Pracownik i dodaje atrybut dzial. Przetestuj jej działanie.

class Kierownik(Pracownik):
    def __init__(self, imie, nazwisko, stanowisko, dzial):
        super().__init__(imie, nazwisko, stanowisko)
        self.dzial = dzial

    def przedstaw_sie(self):
        return f"{super().przedstaw_sie()}, kieruję działem {self.dzial}"

    def __str__(self):
        return f"Kierownik: {self.imie} {self.nazwisko}, Stanowisko: {self.stanowisko}, Dział: {self.dzial}"

    def __repr__(self):
        return f"Kierownik(imie='{self.imie}', nazwisko='{self.nazwisko}', stanowisko='{self.stanowisko}', dzial='{self.dzial}')"

kierownik = Kierownik("Cezary", "Szukiel", "Kierownik Projektu", "IT")
print(kierownik.przedstaw_sie())


# 2.4.Dziedziczenie wielokrotne - Utwórz klasy Sportowiec i Student, a następnie stwórz
# klasę StudentSportowiec, która dziedziczy po obu. Dodaj metody unikalne dla każdej
# klasy i sprawdź, jak działa ich wywoływanie.


class Sportowiec:
    def __init__(self, dyscyplina):
        self.dyscyplina = dyscyplina

    def trenuj(self):
        return f"Trenuję {self.dyscyplina}"

class Student:
    def __init__(self, kierunek):
        self.kierunek = kierunek

    def ucz_sie(self):
        return f"Uczę się na kierunku: {self.kierunek}"

class StudentSportowiec(Student, Sportowiec):
    def __init__(self, imie, nazwisko, kierunek, dyscyplina):
        Student.__init__(self, kierunek)
        Sportowiec.__init__(self, dyscyplina)
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}, student i sportowiec."


student_sportowiec = StudentSportowiec("Marlena", "Czurak", "Informatyka", "bieganie")

print(student_sportowiec.przedstaw_sie())
print(student_sportowiec.ucz_sie())
print(student_sportowiec.trenuj())


# 2.5.Sprawdzenie typu obiektu (isinstance(), issubclass()) - Stwórz obiekty różnych klas i
# sprawdź, czy należą do klasy Pracownik lub Osoba za pomocą isinstance(). Sprawdź,
# czy Kierownik jest podklasą Osoba używając issubclass().


print(isinstance(osoba, Osoba))
print(isinstance(pracownik, Osoba))
print(isinstance(kierownik, Osoba))
print(isinstance(kierownik, Pracownik))
print(isinstance(kierownik, Kierownik))

print(issubclass(Kierownik, Osoba))


# 2.6.Użycie super() do wywołania metody klasy bazowej - W klasie Kierownik użyj super()
# w metodzie przedstaw_sie(), aby najpierw wywołać metodę z Pracownik, a potem
# dodać informację o dziale.

kierownik = Kierownik("Marlena", "Czurak", "Kierownik Projektu", "IT")
print(kierownik.przedstaw_sie())

# 2.7.Tworzenie abstrakcyjnej klasy bazowej (ABC) Zaimplementuj abstrakcyjną klasę
# Zwierze z metodą daj_glos(), która będzie wymagana w klasach Kot i Pies.

class Zwierze(ABC):
    @abstractmethod
    def daj_glos(self):
        pass

class Kot(Zwierze):
    def daj_glos(self):
        return "miau"

class Pies(Zwierze):
    def daj_glos(self):
        return "hau"

kot = Kot()
pies = Pies()

print(f"Kot: {kot.daj_glos()}")
print(f"Pies: {pies.daj_glos()}")



# 2.8.Operator str i repr w dziedziczeniu Dodaj do klas Osoba, Pracownik i Kierownik
# metodę str, która będzie zwracać czytelne informacje o obiekcie.

print(osoba)
print(pracownik)
print(kierownik)

print(repr(osoba))
print(repr(pracownik))
print(repr(kierownik))
