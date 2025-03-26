# Napisz program, który zapisuje do pliku listę imion.

names = ['Marlena', 'Cezary', 'Maria']

with open('names.txt', 'w') as names_file:
    for name in names:
        names_file.write(name + '\n')

print("Imiona zostały zapisane do pliku")


# Otwórz plik tekstowy i wypisz jego zawartość na ekranie.
try:
    with open('names.txt', 'r') as names_file:
        content = names_file.read()
        print(content)
except FileNotFoundError:
    print("File not found")



# Napisz funkcję, która odczytuje plik i liczy wystąpienia danego słowa.

def count_words(filename, word):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        word_counter = content.lower().split().count(word.lower())

        return word_counter

    except FileNotFoundError:
        print(f'File {filename} not found')

#  Użycie:
file_name = 'names.txt'
word = 'Marlena'
count = count_words(file_name, word)
print(f"Słowo '{word}' występuje {count} razy w pliku.")
