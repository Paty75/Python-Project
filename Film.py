class Film:

    def __init__(self, titlu, durata):
        if durata > 180:
            raise Exception("Durata filmelor trebuie sa fie de cel mult 180 de minute.")

        self.titlu = titlu
        self.durata = durata

    def __str__(self): 
        return f'Film( {self.titlu} ) - [ {self.durata}] minute'