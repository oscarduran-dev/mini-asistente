def contar_palabras (texto):
    return texto.count(" ")+1


def contar_vocales(texto):
    texto = texto.lower()
    vocales = 'aeiou'
    resultado = ""
    for vocal in vocales:
        cantidad = texto.count(vocal)
        resultado += f"{vocal}: {cantidad}  | "
    return resultado.strip(" | ")

def invertir_texto(texto):
    return texto[::-1]

def texto_mayusculas(texto):
    return texto.upper()

def texto_minusculas(texto):
    return texto.lower()

def contar_letra(texto, letra):
    cantidad = texto.count(letra)
    return f"La letra {letra} aparece {cantidad} veces."

def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    return texto == texto[::-1]
    

def reemplazar_palabra(texto, palabra_vieja, palabra_nueva):
    return texto.replace(palabra_vieja, palabra_nueva)


    
    