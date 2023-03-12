import random

# Generar número aleatorio
numero_secreto = random.randint(1, 100)

# Configuración del juego
intentos = 0
limite_intentos = 7

# Juego
print("¡Bienvenido al juego de adivinanza de números!")
print("Tienes que adivinar un número del 1 al 100 en", limite_intentos, "intentos.")
print("¡Buena suerte!")

while intentos < limite_intentos:
    intentos += 1
    print("Intento", intentos, ":")
    # Pedir al usuario que ingrese un número
    try:
        numero_ingresado = int(input())
    except:
        print("Entrada no válida. Por favor ingrese un número.")
        continue
    
    # Verificar si el número ingresado es correcto
    if numero_ingresado == numero_secreto:
        print("¡Felicitaciones! Adivinaste el número en", intentos, "intentos.")
        break
    elif numero_ingresado < numero_secreto:
        print("El número ingresado es demasiado bajo. Intenta nuevamente.")
    elif numero_ingresado > numero_secreto:
        print("El número ingresado es demasiado alto. Intenta nuevamente.")
        
    # Verificar si el jugador ha agotado todos los intentos
    if intentos == limite_intentos:
        print("Lo siento, has agotado todos tus intentos. El número secreto era", numero_secreto)
