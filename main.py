 #fundacion de adopcion de mascotas
    #MIS PERRIS
 
from Mascota import Mascota

#se crea un OBJETO  a partir de l clase
m1 = Mascota()
#se modifican sus atributos
m1.nombre='doki'
m1.edad=10
m1.raza='Terrier chileno'
m1.genero='Macho'
m1.chip='1010101'
#mostrar atributos
print(f"el nombre de la mascota es: {m1.nombre}")
print(f"la raza de la mascota es: {m1.raza}")
#llamaremos el metodo imprimir
print(f"los datos de la mascota son : {m1.imprimir()}")
print(f"Categoria: {m1.categoria()}")