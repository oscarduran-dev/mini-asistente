#texto.py
#módulo con funciones para analizar y manipular textos:

#función que cuenta cuántas palanbras hay en un texto, asumiendo que están separadas por espacios
def contar_palabras (texto):
    return texto.count(" ")+1

#función que cuenta cuántas veces aparece cada vocal (aeiou) en el texto
def contar_vocales(texto):
    texto = texto.lower()
    vocales = 'aeiou'
    resultado = ""
    for vocal in vocales:
        cantidad = texto.count(vocal)
        resultado += f"{vocal}: {cantidad}  | "
    return resultado.strip(" | ")

#función que devuelve el texto invertido, de atrás hacia adcelante
def invertir_texto(texto):
    return texto[::-1]


#función que devuelve el texto completamente en mayusculas
def texto_mayusculas(texto):
    return texto.upper()

#función que devuelve el texto completamente en minusculas
def texto_minusculas(texto):
    return texto.lower()

#función que cuenta cuántas veces aparece una letra especifica en el texto
def contar_letra(texto, letra):
    cantidad = texto.count(letra)
    return f"La letra {letra} aparece {cantidad} veces."

#función que verifica si el texto es un palíndromo (se lee igual de atrás hacia adelante) ignorando mayusculas y espacios
def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    return texto == texto[::-1]
    
#función que reemplaza todas las ocurrencias de una palabra por una nueva palabra
def reemplazar_palabra(texto, palabra_vieja, palabra_nueva):
    return texto.replace(palabra_vieja, palabra_nueva)


    
    