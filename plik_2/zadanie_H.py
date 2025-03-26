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