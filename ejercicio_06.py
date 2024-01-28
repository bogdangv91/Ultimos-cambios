"""
def sumar_dos_numeros(numero1, numero2):
    return numero1 + numero2

resultado = sumar_dos_numeros(10, 20)
print("El resultado de la suma es:", resultado)

def suma_tres_numero(numero1, numero2, numero3):
    return numero1 + numero2 + numero3
total = suma_tres_numero(10, 20, 30)
print("El resultado es",total)
"""

def multiplica_dos_numeros(numero1, numero2):
    return numero1 * numero2
resultado = multiplica_dos_numeros(2, 3)
print("El resultado es",resultado)

def multiplica_estos_numeros(numero1, numero2, numero3):
    return numero1 * numero2 * numero3 
resultado = multiplica_estos_numeros(2, 3, 4)
print("El resultado es",resultado)



def divide_estos_numero(numero1, numero2,):
    return numero1 / numero2
resultado = divide_estos_numero(20, 2)
print("El resultado es",resultado)


def realiza_estas_operaciones(numero1, numero2, numero3, numero4):
    return numero1 + numero2 * numero3 / numero4
resultado = realiza_estas_operaciones(10, 10, 2, 2)
print("El resultado es",resultado)

def realiza_estas_operaciones_combinadas(numero1, numero2, numero3, numero4, numero5, numero6):
    return numero1 * numero2 / numero3 +numero4 * numero5 + numero6
resultado = realiza_estas_operaciones_combinadas(2, 7, 9, 10, 21, 5)
print("El resultado total es", resultado)



def es_verdadero_o_falso(numero):
    if numero:
        return(True)
    else:
        return(False)
print(es_verdadero_o_falso(10>20))







def pares_impares():
    pares = []
    impares = []
    for a in range(1, 100):
        if a % 2 == 0:pares.append(a)
        else:impares.append(a)
    return pares, impares

pares, impares = pares_impares()

pares,impares = pares_impares()
print("Numeros pares del 1 a 100:",pares)
print("Numeros impares del 1 al 100:",impares)






def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"
num = 3
resultado = es_par_o_impar(num)
print(resultado)

   
    
      



