"""
Equipo 3 - Biomecánica - Jueves 
Jorge  Fuentes
Adán  Briones
Arely Cabrera
Reyna  Fernández
Romano Villareal
"""
#Bibliotecas
from multiprocessing import Pool
from random import randint
import statistics
import matplotlib.pyplot as plt

#Configuraciones
width = 800
heigth = width
radio = width

npuntos = 0
ndentro = 0
radio2 = radio*radio
replicas = 1000
promediopi = []


#Simulación
if __name__ == '__main__':
        with Pool(6) as p:
            for j in range(replicas):
                    for i in range(1,100000):
                        x = randint(0,width)
                        y = randint(0,width)
                        npuntos += 1
                        if x*x + y*y <= radio2:
                            ndentro += 1
                        pi = ndentro * 4 /npuntos
                        promediopi.append(pi)   

#Gráfica
v=[0,1000,3,3.5]
plt.plot(promediopi,"b--")
plt.xlabel('Replicas')
plt.ylabel('Valores de pi')
plt.title('Tarea #3 Equipo #3 Biomecánica Jueves N3 - N6')
plt.axis(v)
plt.grid()
plt.show()  
