from Film import Film

class Animatie(Film):
    def __init__(self, titlu, durata, limba_dublata):
        super().__init__(titlu, durata)
        self.limba_dublata = limba_dublata

    def get_limba_dublare(self):
        return self.limba_dublata
    def __str__(self):
        return f'Animatie( {self.titlu} ) - ({self.durata}) minute - dublat in ({self.limba_dublata})'

