# Uruchom pierwszy plik, a później drugi. Co się stało?

# Uruchomienie my_lib.py:
# Program wykona się w pełni, ponieważ my_lib.py jest uruchamiany bezpośrednio. Wypisze:
# Hello python outside main
# Hello python inside main

# Uruchomienie my_lib2.py:
# wykona się kod tylko poza blokiem if __name__ == "__main__".Wypisze:
# Hello python outside main
# W momencie importu pliku my_lib.py w my_lib2.py, wartość zmiennej __name__ w pliku my_lib.py będzie równa "my_lib" (nazwa pliku),
# a nie "__main__". Wtedy warunek if __name__ == "__main__": będzie fałszywy, bo __name__ nie jest równe "__main__".
# W rezultacie kod wewnątrz tego bloku się nie wykona.



# Do czego można użyć “if __name__ == "__main__"”
# Instrukcja if __name__ == "__main__" pozwala nam kontrolować, które fragmenty kodu uruchamiają się w zależności od tego,
# czy plik jest uruchamiany bezpośrednio, czy importowany do innego skryptu. Dzięki temu możemy oddzielić kod
# przeznaczony do uruchamiania jako samodzielny skrypt od kodu, który ma być używany jako moduł w innych programach.
# Pozwala to uniknąć niechcianego wykonywania kodu podczas importu