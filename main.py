# Proiect Practic - Python Fundamentals
# Se va scrie o aplicatie pentru un cinematograf, ce va fi folosita pentru gestionarea filmelor ce ruleaza in cadrul acestuia.
# Cinematograful ofera o lista de filme.
# Un film are precizate titlul si durata exprimata in minute.
# Filmele se impart in 2 categorii: drame si animatii. Dramele au specificata varsta minima a telespectatorilor.
# Cinematograful poate dubla filmele sale. Orice film care este dublat trebuie sa respecte o regula generala: trebuie sa specifice limba in care este dublat.
# In cazul nostru, doar animatiile sunt dublate. Ele au o metoda care returneaza limba in care se face dublarea.
# Aplicatia lucreaza cu un singur cinematograf si are urmatoarele functionalitati:
# - adaugare film
# - afisare filme
# - afisare animatii
# - alegere film aleator
# - salvare filme
# In cazul in care durata filmelor adaugate este de peste 180 de minute se va genera o exceptie (ex: ValueEror("Durata filmelor trebuie sa fie de cel mult 180 de minute.")).
# Tratati exceptia in cazul in care aceasta apare in timpul rularii.
# Aplicatia poate primi urmatoarele comenzi:
# - adauga_drama <titlu> <durata> <varsta>
# - adauga_animatie <titlu> <durata> <limba_dublare>
# - afisare - afiseaza toate filmele
# - afisare_animatii
# - alege_film
# - salveaza_filme <nume_fisier>
# - exit : iesirea din aplicatie
# HINT: Citirea comenzilor se va face in cadrul unei bucle infinite (ex: while True).
# Folosindu-va de clasele si metodele definite anterior, in cadrul unei executii a aplicatiei, rezolvati urmatoarele cerinte:
# 1. Adaugati o serie de filme si salvati informatiile despre ele (titlu, durata etc.) intr-un fisier cu nume specificat.
# 2. Alegeti un film aleator si afisati toate datele despre acesta
# Punctaj:
#  definirea clasei Cinematograf - 15p
#  definirea structurii de clase: Film - Drama - Animatie - 45p (15p per clasa)
# (In cadrul definirii de clasa se puncteaza adaugarea de atribute si comportamente conform cerintelor)
#  structurarea aplicatiei pentru citirea comenzilor - 20p
#  cerinta 1 - 15p
#  cerinta 2 - 15p
# TOTAL - 110p
from Cinematograf import Cinematograf

def executa_program():
    c = Cinematograf("Cinematograful unirea");

    while True:
        try:
            print("Introduceti comanda: ")
            linie = str(input())
            argumente = linie.split()

            if argumente[0] == 'adauga_drama':
                titlu = argumente[1]
                durata = int(argumente[2])
                varsta = int(argumente[3])
                c.adauga_drama(titlu, durata, varsta)

            elif argumente[0] == 'adauga_animatie':
                titlu = argumente[1]
                durata = int(argumente[2])
                limba_dublare = argumente[3]
                c.adauga_animatie(titlu, durata, limba_dublare)

            elif argumente[0] == 'afisare':
                c.afisare_lista_filme()

            elif argumente[0] == 'afisare_animatii':
                c.afisare_animatii()

            elif argumente[0] == 'alege_film':
                c.alege_film_aleatoriu()

            elif argumente[0] == 'salveaza_filme':
                nume_fisier = argumente[1]
                c.salveaza_filme(nume_fisier)
            elif argumente[0] == 'exit':
                break

            else:
                print('Comanda introdusa nu este corecta');


        except Exception as e:
            print('Exceptie aparuta:')
            print(e)

    print('Terminare program.')

if __name__ == "__main__":
    executa_program()
