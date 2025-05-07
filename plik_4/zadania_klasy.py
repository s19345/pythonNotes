# 1.1.Prosta klasa z init Napisz klasę Samochod, która ma atrybuty marka, model i
# rok_produkcji. Utwórz kilka obiektów tej klasy i wyświetl ich informacje.

class Samochod:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.__przebieg = 0

    def information(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}")

    def opis(self):
        return f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}"

    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}, Przebieg: {self.__przebieg} km"

    @staticmethod
    def info():
        return "Ta klasa reprezentuje samochody."

    def zmien_rok_produkcji(self, nowy_rok):
        self.rok_produkcji = nowy_rok

    def dodaj_kilometry(self, km):
        if km > 0:
            self.__przebieg += km
        else:
            print("Nie można dodać ujemnej liczby kilometrów.")

    def __repr__(self):
        return (
            f"Samochod(marka='{self.marka}', model='{self.model}', "
            f"rok_produkcji={self.rok_produkcji}, przebieg={self.__przebieg})"
        )


car1 = Samochod("Toyota", "Corolla", 2020)
car2 = Samochod("BMW", "X5", 2018)
car3 = Samochod("Ford", "Focus", 2015)

car1.information()
car2.information()
car3.information()



# 1.2.Użycie self Dodaj do klasy Samochod metodę opis, która zwróci łańcuch znaków
# opisujący samochód.


print(car1.opis())
print(car2.opis())
print(car3.opis())


# 1.3.Słownik (dict) Utwórz obiekt klasy Samochod i wyświetl jego atrybuty w formie
# słownika, używając .dict.

car4 = Samochod("Mazda", "CX-5", 2022)

print(car4.__dict__)


# 1.4.Metoda str Dodaj do klasy Samochod metodę str, aby zwracała czytelną reprezentację
# obiektu.

print(car4.__str__())


# 1.5.Klasa z metodą statyczną (@staticmethod) Napisz metodę statyczną info(), która
# zwróci informację, że klasa reprezentuje samochody.

print(car4.info())

# 1.6.Dziedziczenie klas Utwórz klasę ElektrycznySamochod, która dziedziczy po
# Samochod i dodaje nowy atrybut bateria. Dodaj metodę zasieg, która oblicza zasięg na
# podstawie pojemności baterii.

class ElektrycznySamochod(Samochod):
    def __init__(self, marka, model, rok_produkcji, bateria):
        super().__init__(marka, model, rok_produkcji)
        self.bateria = bateria

    def zasieg(self):
        # przyjmijmy, że 1 kWh to 5 km zasięgu
        return f"Szacowany zasięg: {self.bateria * 5}"

tesla = ElektrycznySamochod("Tesla", "Model 3", 2023, 75)
print(tesla.zasieg())


# 1.7.Modyfikacja atrybutów za pomocą metod Dodaj do klasy Samochod metodę
# zmien_rok_produkcji(nowy_rok), która zmienia rok produkcji samochodu

car5 = Samochod("Opel", "Astra", 2010)
print("Przed zmianą:", car5)

car5.zmien_rok_produkcji(2015)
print("Po zmianie:", car5)


# 1.8.Ukrywanie atrybutów (__private_attr) Dodaj do klasy Samochod prywatny atrybut
# _przebieg i metodę dodaj_kilometry, która pozwala go zmieniać.

car6 = Samochod("Skoda", "Octavia", 2019)
print(car6)

car6.dodaj_kilometry(150)
car6.dodaj_kilometry(200)
print(car6)

car6.dodaj_kilometry(-50)


# 1.9.Metoda repr Dodaj do klasy Samochod metodę repr, aby zwracała techniczną
# reprezentację obiektu.

car = Samochod("Renault", "Megane", 2017)
car.dodaj_kilometry(123000)
print(repr(car))

# 1.10. Klasa jako kontener (iter) Utwórz klasę Flota, która przechowuje listę
# obiektów Samochod i implementuje iter, aby można było iterować po jej zawartości.

class Flota:
    def __init__(self):
        self.samochody = []

    def dodaj_samochod(self, samochod):
        self.samochody.append(samochod)

    def __iter__(self):
        return iter(self.samochody)


car7 = Samochod("Toyota", "Yaris", 2018)
car8 = Samochod("Hyundai", "i30", 2020)
car9 = Samochod("Peugeot", "208", 2019)

flota = Flota()
flota.dodaj_samochod(car7)
flota.dodaj_samochod(car8)
flota.dodaj_samochod(car9)

print("Samochody we flocie:")
for auto in flota:
    print(auto)



