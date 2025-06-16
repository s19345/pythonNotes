import json
import requests

# 3.1.Konwersja obiektu do JSON - Utwórz obiekt klasy Samochod, przekonwertuj go na
# JSON i zapisz do pliku.

class Samochod:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

    def to_dict(self):
        return {
            "marka": self.marka,
            "model": self.model,
            "rok_produkcji": self.rok_produkcji
        }

    def __str__(self):
        return f"{self.marka} {self.model}, Rok: {self.rok_produkcji}"

samochod = Samochod("Toyota", "Corolla", 2020)

samochod_json = json.dumps(samochod.to_dict(), indent=4)

with open("samochod.json", "w") as plik:
    plik.write(samochod_json)

print("Obiekt zapisany do pliku samochod.json")

# 3.2.Odczyt danych z pliku JSON - Odczytaj dane z pliku JSON i przekształć je z powrotem
# w obiekt klasy Samochod.

with open("samochod.json", "r") as plik:
    dane = json.load(plik)

samochod = Samochod(**dane)

print("Odczytano obiekt z JSON:")
print(samochod)


# 3.3.Lista obiektów do JSON - Utwórz kilka obiektów klasy Samochod, zapisz je jako listę
# w formacie JSON.


auta = [
    Samochod("Toyota", "Corolla", 2020),
    Samochod("BMW", "X5", 2018),
    Samochod("Ford", "Focus", 2015)
]

auta_dict = [auto.to_dict() for auto in auta]

with open("lista_samochodow.json", "w") as plik:
    json.dump(auta_dict, plik, indent=4)

print("Lista samochodów zapisana do pliku lista_samochodow.json")


# 3.4.Ładowanie JSON z Internetu (Dodatkowe) - Pobierz dane w formacie JSON (np.
# informacje o pogodzie z API), przekształć je w słownik i wyświetl wybrane wartości.

# prognoza pogody w Warszawie
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.23,
    "longitude": 21.01,
    "current_weather": True
}

response = requests.get(url, params=params)

if response.status_code == 200:
    dane = response.json()
    print(type(dane))
    print("Aktualna pogoda:")
    current = dane["current_weather"]
    print(f"Temperatura: {current['temperature']}°C")
    print(f"Prędkość wiatru: {current['windspeed']} km/h")
    print(f"Kierunek wiatru: {current['winddirection']}°")
else:
    print("Błąd pobierania danych:", response.status_code)
