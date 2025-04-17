class Mascota:
    chip=''
    nombre=''
    raza=''
    genero=''
    peso=0
    edad=0
    # constuctor de la clase
    def __init__(self):
        self.chip='0000000000'
        self.nombre='NN'
        self.raza='SR'
        self.peso=0
        self.edad=0
        self.genero='SG'
    #metodo imprimir
    def imprimir(self):
        return self.nombre+" "+self.raza+" "+self.categoria()
    def categoria(self):
        if self.edad<=1:
            return "cachorro"
        if self.edad>1 and self.edad<5:
            return "adulto"
        if self.edad>5:
            return "senior"