from Film import Film

class Drama(Film):
    def __init__(self, titlu, durata, varsta_minima):
        super().__init__(titlu, durata) 
        self.varsta_minima = varsta_minima

    def __str__(self):
        return f'Drama( {self.titlu} ) - ({self.durata}) minute - cu varsta minima de ({self.varsta_minima}) ani'