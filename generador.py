import random
import  math
def leer_numero(ini, fin, mensaje):
    while True:

        try:
            valor = int(input(mensaje))

        except:
            print("error")

        else:
            if ini <= valor <= fin:
                break
    return valor

def generador():
    numeros = leer_numero(1, 20, "cuantos numeros quires generar?")
    modo = leer_numero(1,3, "Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    lista_numeros = []
    for n in range(numeros):
        aleatorio = random.uniform(0,101)
        print(aleatorio)

        if(modo==1):
            lista_numeros.append(math.ceil(aleatorio))
        elif modo==2:
            lista_numeros.append(math.floor(aleatorio))
        else:
            lista_numeros.append(round(aleatorio))
    return lista_numeros

print(generador())






