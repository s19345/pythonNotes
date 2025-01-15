# . Bazując na poniższym słowniku, stwórz słownik gdzie klucze staną się wartościami
# a wartości kluczami. source: {“Key1”:”League”,”Key2”:”Of”,”Key3”:”Legends”}

source = {"Key1": "League", "Key2": "Of", "Key3": "Legends"}

result = {value: key for key, value in source.items()}

print(result)