#Primero importamos el modulo "random"
import random

#Creamos el constructor de la clase secuenciador
class secuenciador:
    def __init__(self):
        self.hebra = self.random_hebra()
        self.hebra2 = self.hebra_complementaria()
        self.nucleotidos = self.contar_nucleotidos()
        self.patrones = self.encontrar_patron("AG")
        self.peso = self.peso_molecular()
#Definimos sus atributos y le asignamos como "valor", los metodos utilizados.
        
#Se genera una hebra random, con 15 nucleotidos.        
    def random_hebra(self):
        self.secuencia = ''.join(random.choices(['A', 'T', 'C', 'G'], k = 15))
        print("Secuencia principal:", self.secuencia)
        
#De la hebra anterior, se crea su complementaria    
    def hebra_complementaria(self):
        complementaria = ""
        for base in self.secuencia:
            if base == 'A':
                complementaria += 'T'
            elif base == 'T':
                complementaria += 'A'
            elif base == 'C':
                complementaria += 'G'
            elif base == 'G':
                complementaria += 'C'
        print("Secuencia paralela: ", complementaria)
        
#Función/metodo para contar los nucleotidos de la hebra principal   
    def contar_nucleotidos(self):
        conteo = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for i in self.secuencia:
            if i in conteo:
                conteo[i] += 1
        return conteo
#Función/metodo para buscar patrones, este patrón se debe definir en "self.patrones = self.encontrar_patron("INSERTE PATRÓN")    
    def encontrar_patron(self, patron):
        posiciones = []
        len_patron = len(patron)
        for i in range(len(self.secuencia)-len_patron+1):
            if self.secuencia[i:i+len_patron] == patron:
                posiciones.append(i)
        return posiciones
#Función/metodo para calcular el peso molecular, por cada nucleotido    
    def peso_molecular(self):
        peso_molecular = 0
        pesos = {'A': 313.21, 'T': 304.2, 'C': 289.18, 'G': 329.21}
        for i in self.secuencia:
            if i in pesos:
                peso_molecular += pesos[i]
        return peso_molecular
#Se crea un objeto x que es un secuenciador y recibe los atributos de esta clase.          
x = secuenciador()
print(x.hebra)
print(x.hebra2)
print("La cantidad de cada nucleotido de la secuencia principal es: ", x.nucleotidos)
print("El peso molecular de la secuencia principal es: ", x.peso)
print("En la posición", x.patrones, "de la secuencia principal existe un patrón 'AG'")
print("*En caso de que '[]' este vacío, quiere decir que no hay patrones 'AG'*")


quit()

        
        
        