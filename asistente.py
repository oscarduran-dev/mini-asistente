import sys   #print(sys.builtin_module_names)
sys.path.append("c:\\Proyectos_python\\VSC\\PythonCurso\\modulos_mini_asistente")
#importando los modulos saludos, matemáticas y texto
from saludos import saludo, saludo_informal, despedida
from matematicas import suma, resta, multiplicacion, division, es_primo
from texto import contar_vocales, texto_mayusculas, invertir_texto

print("""Hola, bienvenido al mini asistente de Oscar.
      ¿Qué deseas hacer?
      1. Usar herramientas de saludo
      2. Realizar una operación matemática
      3. Usar herramientas de textos
      4. Salir
      """)
nombre = input("Ingresa tu nombre: ")
try:
    modulo = int(input("Selecciona una opción:"))
except ValueError:
    print("Ingrese solo números")
else:
    if modulo == 1:
        print("""Eligiste usar herramientas de saludo.
              
              1. Saludar
              2. Saludar informalmente
              3. Despedirse
              """)
        try:
            accion = int(input("¿Qué acción quieres realizar?"))
        except ValueError:
            print("Ingrese solo valores numéricos.")
        else:
            if accion ==1:
                print(saludo(nombre))
            elif accion ==2:
                print(saludo_informal(nombre))
            elif accion == 3:
                print(despedida(nombre))
            else:
                print("Selecciona números en el rango.")
        finally:
            print("Fin del programa. Hasta luego. ")
    elif modulo == 2:
        print("""Elegiste realizar una operación matemática.
              
              1. Suma
              2. Resta
              3. Multiplicación
              4. División
              5. Saber si n es primo
              """)
        try:
            
            accion = int(input("¿Qué operación quieres realizar?"))
        except ValueError:
            print("Ingrese solo valores numéricos. ")
        else:
            if accion == 1:
                a = int(input("Ingresa el primer número: "))
                b = int(input("Ingresa el segundo número: "))
                print(suma(a, b))
            elif accion == 2:
                a = int(input("Ingresa el primer número: "))
                b = int(input("Ingresa el segundo número: "))
                print(resta(a, b))
            elif accion == 3:
                a = int(input("Ingresa el primer número: "))
                b = int(input("Ingresa el segundo número: "))
                print(multiplicacion(a, b))
            elif accion == 4:
                a = int(input("Ingresa el primer número: "))
                b = int(input("Ingresa el segundo número: "))
                print(division(a, b))
            elif accion == 5:
                numero = int(input("Ingresa el número a evaluar: "))
                print(es_primo(numero))
            else:
                print("Seleccione un número dentro del rango.")
        finally:
            print("Fin del programa. Hasta luego. ")
    elif modulo == 3:
        print("""Elegiste usar herramientas de texto.
              
              1. Contar las vocales de un texto
              2. Mostrar el texto en mayúsculas
              3. Mostrar el texto invertido
              """)
        try:
            accion = int(input("¿Qué acción quieres realizar?"))
        except ValueError:
            print("Ingrese solo valores numéricos. ")
        else:
            if accion == 1:
                texto_a_evaluar = input("Ingresa el texto a evaluar: ")
                print(contar_vocales(texto_a_evaluar))
            elif accion == 2:
                texto_a_evaluar = input("Ingresa el texto a evaluar: ")
                print(texto_mayusculas(texto_a_evaluar))
            elif accion == 3:
                texto_a_evaluar = input("Ingresa el texto a evaluar: ")
                print(invertir_texto(texto_a_evaluar))
            else:
                print("Selecciona números dentro del rango. ")
        finally:
            print("Fin del programa. Hasta luego. ")
    elif modulo == 4:
        print("Has seleccionado la opción (Salir). Hasta pronto.")
    else:
        print("Seleccione una opción dentro del rango. ")