from multiprocessing import Pool

def hallar_total(lista):
    kwh_total = 0
    kvarh_total = 0
    for datos in lista:
        kwh_total += float(datos[1])*0.25
        kvarh_total += float(datos[2])*0.25
    return [kwh_total,kvarh_total]

def hallar_maximo(lista):
    horas_puntas=["18","19","20","21","22","23"]
    horas_fp=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17"]
    r_puntas_kw = []
    r_fp_kw = []
    for fila in lista:
        tiempo = fila[0].split(" ")[1].split(":")
        hora = tiempo[0]
        if hora in horas_puntas:
            r_puntas_kw.append(float(fila[1]))
        if hora in horas_fp:
            r_fp_kw.append(float(fila[1]))
    max_puntas_kw = max(r_puntas_kw)
    max_fp_kw = max(r_fp_kw)
    return [max_puntas_kw,max_fp_kw]

def principal(archivo):
    data=[]
    archivo_interno = open(archivo)
    archivo_leido=archivo_interno.read()
    archivo_interno.close()
    filas = archivo_leido.split("\n")
    for fila in filas:
        datos = fila.split(";")
        data.append(datos)
    data.pop(0)
    inciso_a = hallar_total(data)
    inciso_b = hallar_maximo(data)
    return [inciso_a,inciso_b]

if __name__ == '__main__':

    archivos=["torre_A.csv","torre_B.csv"]
    p = Pool()
    resultado = p.map(principal,archivos)
    p.close()
    p.join()
    data_A = resultado[0]
    data_B = resultado[1]
    #inciso(a):
    print("La torre A consumió ",data_A[0][0],"Kw/h en total y ",data_A[0][1]," Kvar/h en total")
    print("La torre B consumió ",data_B[0][0],"Kw/h en total y ",data_B[0][1]," Kvar/h en total")
    #inciso(b):
    print("La potencia maxima en hora punta para la torre A fue ",data_A[1][0],"kw y la potencia maxima en hora fuera de punta",data_A[1][1],"kw")
    print("La potencia maxima en hora punta para la torre B fue ",data_B[1][0],"kw y la potencia maxima en hora fuera de punta",data_B[1][1],"kw")
