#saludos.py
#módulo que contiene funciones para saludar y despedirse en diferentes estilos

#saludo formal que da la bienvenida al usuario
def saludo(nombre):
    return f"Hola, {nombre}. Bienvenido a mi primer mini-proyecto independiente. Como te encuentras? "

#saludo con un tono informal para usar con amigos
def saludo_informal(apodo):
    return f"Que onda {apodo}, todo bien o que? Un abrazo amigo, que estés al 100"

#despedida formal y positiva
def despedida(nombre):
    return f"Muchas gracias por haber usado mi programa. Espero sigas teniendo un maravilloso dia, cuidate, {nombre}."

#despedida con un tono informal y casual
def despedida_informal(apodo):
    return f"Adios {apodo}, estamos pendientes."

#saludo formal completamente en mayusculas
def saludo_en_mayusculas(nombre):
    return f"HOLA, {nombre.upper()}, COMO TE ENCUENTRAS?"

#saludo formal que permite saludar en varios idiomas
#idiomas soportados: español (es), inglés (en), francés (fr), italiano (it), alemán (de)
def saludo_internacional(nombre, idioma="es"):
    saludos = {
        "es": f"¡Hola {nombre}!",
        "en": f"Hello {nombre}!",
        "fr": f"Bonjour {nombre}!",
        "it": f"Ciao {nombre}!",
        "de": f"Hallo {nombre}!"
    }
    #si el idioma no está en el diccionario, se usa español por defecto
    return saludos.get(idioma, f"¡Hola {nombre}!")

