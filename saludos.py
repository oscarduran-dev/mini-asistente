def saludo(nombre):
    return f"Hola, {nombre}. Bienvenido a mi primer mini-proyecto independiente. Como te encuentras? "

def saludo_informal(apodo):
    return f"Que onda {apodo}, todo bien o que? Un saludo amigazo, aqui andamos al 100"

def despedida(nombre):
    return f"Muchas gracias por haber usado mi programa. Espero sigas teniendo un maravilloso dia, cuidate, {nombre}."

def despedida_informal(apodo):
    return f"Adios {apodo}, te la lavas jajaja, no te creas. Cuidate."

def saludo_en_mayusculas(nombre):
    return f"HOLA, {nombre.upper()}, COMO TE ENCUENTRAS?"

def saludo_internacional(nombre, idioma="es"):
    saludos = {
        "es": f"¡Hola {nombre}!",
        "en": f"Hello {nombre}!",
        "fr": f"Bonjour {nombre}!",
        "it": f"Ciao {nombre}!",
        "de": f"Hallo {nombre}!"
    }
    return saludos.get(idioma, f"¡Hola {nombre}!")

