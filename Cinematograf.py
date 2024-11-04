import random

from Drama import Drama
from Animatie import Animatie

class Cinematograf:
    def __init__(self, info):
        self.info = info
        self.lista_filme = []

    def afisare_info(self):
        print(f"Informatii generale pentru cinematograful: {self.info}")

    def adauga_drama(self, titlu, durata, varsta):
        drama_noua = Drama(titlu, durata, varsta)
        self.lista_filme.append( drama_noua )

    def adauga_animatie(self, titlu, durata, limba_dublare):
        animatie_noua = Animatie(titlu, durata, limba_dublare)
        self.lista_filme.append( animatie_noua )

    def afisare_animatii(self):
        print('Lista animatii existente:')

        for film in self.lista_filme:
            if(isinstance(film, Animatie)):
                print(film)

    def alege_film_aleatoriu(self):
        if len(self.lista_filme) == 0:
            print('Nu exista filme adaugate')
        else:
            print('Film aleatoriu:')
            nr_film_aleatoriu = random.randint(0, len(self.lista_filme) - 1)
            print(self.lista_filme[nr_film_aleatoriu])

    def salveaza_filme(self, nume_fisier):
        print(f'salveaza filme int {nume_fisier}')
        fisier = open(nume_fisier, 'w')

        for film in self.lista_filme:
            continut = film.__str__()
            fisier.write(continut)
            fisier.write('\n')

        fisier.close()

    def afisare_lista_filme(self):
        print(f"Lista completa a filmelor din cinematograful {self.info}")
        for film in self.lista_filme:
            continut = film.__str__()
            print(continut) 

