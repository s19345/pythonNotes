# Pobierz liczbę (1-7) i zwróć odpowiadający jej dzień tygodnia, używając match.

day_number = int(input("Podaj liczbę od 1 do 7: "))

match day_number:
    case 1:
        print ("Poniedziałek")
    case 2:
        print("Wtorek")
    case 3:
        print("Środa")
    case 4:
        print("Czwartek")
    case 5:
        print("Piątek")
    case 6:
        print("Sobota")
    case 7:
        print("Niedziela")


