import time
import numpy as np
from multiprocessing import Pool
from itertools import repeat

"""
Complete aqui la funcion que multiplica 2 vectores
Entradas: los 2 vectores
Salidas: El producto de la multiplicacion(numero entero)
"""
#inciso a
def multiplicacion_serial(matriz,vector):
    resultado=[]
    for fila in matriz:
        resultado.append(multiplica_vectorxvector(vector,fila))
    return resultado

#inciso b
def multiplica_vectorxvector(vector1, vector2):
    total=0
    for (a,b) in zip(vector1,vector2):
        total += a*b
    return total


if __name__ == '__main__':
    # Llenamos la matriz y el vector con valores aleatorios
    tam = 5000
    matrix_M = np.random.randint(1,10, size=(tam, tam))
    vector_A = np.random.randint(1,10, size=(tam))

    t1 = time.perf_counter()
    #inciso a (ejecucion serial)
    resultado_serial=multiplicacion_serial(matrix_M,vector_A)
    t2 = time.perf_counter()
    tiempo_serial = t2 - t1
    print("Tiempo de ejecucion en serial: ",tiempo_serial)
# Hacemos multiplicacion en paralelo y medimos el tiempo de ejecucion
    #inciso b (ejecucion paralela)
    joined_vector = zip(matrix_M, repeat(vector_A))  # joined_vector va a ser la entrada a starmap(ver guia teorica)
    t1 = time.perf_counter()
    p = Pool()
    resultado_paralelo=p.starmap(multiplica_vectorxvector,joined_vector)
    p.close()
    p.join()
    t2 = time.perf_counter()
    tiempo_paralelo = t2 -t1
    print("Tiempo de ejecucion en paralelo: ",tiempo_paralelo)
    assert(resultado_serial == resultado_paralelo)
    #adicional
    print("El SpeedUp es ",tiempo_serial/tiempo_paralelo)