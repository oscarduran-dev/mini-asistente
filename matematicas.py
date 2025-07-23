#matemáticas.py
#módulo con funciones matemáticas

#función que suma 2 números
def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Ingresa solo numeros. "
    
    
#función que resta 2 números
def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Ingresa solo numeros. "
    
    
#función que multiplica 2 números
def multiplicacion(a , b):
    try:
        return a * b
    except TypeError:
        return "Ingresa solo numeros. "
    
    
#función que divide 2 números y redonde a 2 decimales
def division(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "Error. No se puede dividir por cero."
    except TypeError:
        return "Ingresa solo numeros. "



#función que calcula la potencia de a elevado a b
def potencia(a, b):
    try:
        return a ** b
    except TypeError:
        return "Ingresa solo numeros. "
    
    
#función que verifica si un número es primo   
def es_primo(numero):
    #un número menor que 2 no se considera primo
    for i in range(2, numero):
        if numero%i == 0:
            return False
    return True


#función que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0
        
        