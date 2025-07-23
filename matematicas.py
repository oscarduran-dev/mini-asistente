def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Ingresa solo numeros. "
    

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Ingresa solo numeros. "
    
    

def multiplicacion(a , b):
    try:
        return a * b
    except TypeError:
        return "Ingresa solo numeros. "
    
    

def division(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "Error. No se puede dividir por cero."
    except TypeError:
        return "Ingresa solo numeros. "

def potencia(a, b):
    try:
        return a ** b
    except TypeError:
        return "Ingresa solo numeros. "
    
    
def es_primo(numero):
    for i in range(2, numero):
        if numero%i == 0:
            return False
    
    return True

def es_par(numero):
    return numero % 2 == 0
        
        