class Ave:
    def __init__(self):
        self.volador = "VOLADOR"
    def vuela(self):
        print("Vuela ave")
        
class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = "NADADOR"
    def vuela(self):
        super().vuela()
        print("vuela pato")
        
pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)