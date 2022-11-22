import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

"""
Función: calcular_histograma
Entrada: El archivo de la imagen en formato .npy
Salida: El arreglo del histograma
"""
def calcular_histograma(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load(filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro
    resultado = []
    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas

    """
    Escriba aquí su algoritmo para calcular el histograma
    """
    resultado=[0]*256
    for i in range(M):
        for j in range(N):
            resultado[imagen[i][j]] += 1
    return resultado

"""
Función: graficar_histograma
Entradas:
- histograma_list: Su histograma que quiere graficar
- filename: Cadena de texto con el nombre del archivo para su gráfico que va a generar. Debe terminar en .png
- color: Cadena de texto con el color en inglés para su gráfico, 
Salida: Genera un gráfico de su histograma en formato .png
"""
def graficar_histograma(histograma_list, filename, color):
    plt.plot(range(0, len(histograma_list)), histograma_list, color=color)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':

    #imagenes=["goldhill_x2.npy","hong kong_x2.npy","lena_x2.npy","stonehenge_x2.npy"] descomentar esta linea para el inciso b
    imagenes = ["goldhill.npy","hong kong.npy","lena.npy","stonehenge.npy"]#linea para el inciso c
    resultado_serial = []
    # Parte a: Calculo del histograma en serial
    t1 = time.perf_counter()
    for imagen in imagenes:
        resultado_serial.append(calcular_histograma(imagen))
    t2 = time.perf_counter()
    tiempo_serial = t2-t1
    print("Tiempo total en serie: ",tiempo_serial)
    nombres=[]
    for imagen in imagenes:
        aux = imagen.split(".")
        nombres.append(aux[0]+"_serial"+".png")
    comb_serial = []
    i=0
    for nombre in nombres:
        comb_serial.append([nombre,resultado_serial[i]])
        i += 1
    for parametros in comb_serial:
        graficar_histograma(parametros[1],parametros[0],"blue")
    # Parte b: Calculo del histograma en paralelo
    t1 = time.perf_counter()
    p = Pool()
    resultado_paralelo = p.map(calcular_histograma,imagenes)
    p.close()
    p.join()
    t2 = time.perf_counter()
    tiempo_paralelo = t2 -t1
    print('Tiempo de ejecucion en paralelo:',tiempo_paralelo)
    nombres_paralelo=[]
    for imagen in imagenes:
        aux = imagen.split(".")
        nombres_paralelo.append(aux[0]+"_paralelo"+".png")
    comb_paralelo=[]
    j=0
    for nombre in nombres_paralelo:
        comb_paralelo.append([nombre,resultado_paralelo[j]])
        j += 1
    for parametros in comb_paralelo:
        graficar_histograma(parametros[1],parametros[0],"red")

    print("El SpeedUp hallado fue ",tiempo_serial/tiempo_paralelo)

    # Nota: Las gráficas del cálculo de los histogramas en serie y en paralelo deben salir iguales.
