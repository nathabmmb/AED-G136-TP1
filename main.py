"""
Este codigo ha sido desarrollado por el grupo 136
"""
import random

# Título, mensaje de bienvenida y reglas
titulo = """
+++++++++++++++++
+  El Juego de  +
+  Dos o Tres   +
+++++++++++++++++
"""

print(titulo)
# Redactar Reglas de Juego

reglamento = "Estas algún día van a ser las reglas del juego\n"

reglas = input("Bienvenido! ¿Desea leer las reglas del juego antes de empezar? (S/N)\n")
if reglas == "s" or reglas == "S":
    print(reglamento)

# Carga de nombre de jugadores y comienzo del juego
jugador1 = input("Jugador 1, ingrese su nombre: ")
jugador2 = input("Jugador 2, ingrese su nombre: ")
input("\nEl juego está listo. Presione Enter para comenzar")
puntaje1, puntaje2 = 0, 0

# Mensaje 1ra ronda, Jugador 1
print("-"*60)
print("INICIO RONDA 1")
print("-"*60)
input("Turno de {}: presione enter para lanzar los dados...".format(jugador1))
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))



# Proceso: Cálculo de puntaje jugador 1 primera ronda
relanzar = False
if dado1 == dado2 and dado1 == dado3:
    puntaje1 += 6
    print(jugador1, "obtiene 6 puntos")
elif dado1 == dado2:
    puntaje1 += 3
    relanzar = True
    comparar = dado1
elif dado1 == dado3:
    puntaje1 += 3
    relanzar = True
    comparar = dado1
elif dado2 == dado3:
    puntaje1 += 3
    relanzar = True
    comparar = dado2

if relanzar:
    print("Tienes dos dados iguales, obtienes 3 puntos.")
    input("Presiona enter para volver a tirar el dado distinto: ")
    dado4 = random.randint(1, 6)
    print("Tu dado salió: [{}]".format(dado4))
    if dado4 == comparar:
        print("Sumas 3 puntos más!")
        puntaje1 += 3

print("\nFin de la jugada. En esta ronda", jugador1, "obtuvo", puntaje1, "puntos.")

# Jugador 2
print("-"*60)
input("Turno {}: presione enter para lanzar los dados...".format(jugador2))
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))

# Proceso: Cálculo de puntaje jugador 2 primera ronda
relanzar = False
if dado1 == dado2 and dado1 == dado3:
    puntaje2 += 6
    print(jugador2, "obtiene 6 puntos")
elif dado1 == dado2:
    puntaje2 += 3
    relanzar = True
    comparar = dado1
elif dado1 == dado3:
    puntaje2 += 3
    relanzar = True
    comparar = dado1
elif dado2 == dado3:
    puntaje2 += 3
    relanzar = True
    comparar = dado2

if relanzar:
    print("Tienes dos dados iguales, obtienes 3 puntos.")
    input("\nPresiona enter para volver a tirar el dado distinto: ")
    dado4 = random.randint(1, 6)
    print("Tu dado salió: [{}]".format(dado4))
    if dado4 == comparar:
        print("Sumas 3 puntos más!")
        puntaje2 += 3


print("\nFin de la jugada. En esta ronda", jugador2, "obtuvo", puntaje2, "puntos.")

print("-"*60)
print("Puntajes Parciales: ", jugador1, "tiene", puntaje1, "puntos y", jugador2, "tiene", puntaje2, "puntos")
input("Presione enter para pasar a la Segunda Ronda")

# Segunda Ronda
# Turno de Jugador1
print("\n"+"-"*60)
print("INICIO SEGUNDA RONDA")
print("-"*60)
print("Turno de {}".format(jugador1))

# Apuesta jugador 1
print("Debe apostar por resultado par o impar.")
apuesta1 = input("¿Desea apostar por par? (s/n)\n")
if apuesta1 == "s" or apuesta1 == "S":
    apuesta1 = 0
    print(jugador1, "apuesta por par...")
else:
    apuesta1 = 1
    print(jugador1, "apuesta por impar...")

print("-"*60)
input("Presione enter para lanzar los dados...")
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))

# Proceso: Cálculo de puntaje jugador 1 Segunda Ronda
mayor1 = max(dado1, dado2, dado3)
menor1 = min(dado1, dado2, dado3)
suma1 = dado1 + dado2 + dado3
if suma1 % 2 == 0:
    print("\nLa suma de los dados es par!")
else:
    print("\nLa suma de los dados es impar!")
if suma1 % 2 == apuesta1:
    puntaje1 += mayor1
    print(jugador1, "obtiene", mayor1, "puntos")
    if dado1 % 2 == apuesta1 and dado2 % 2 == apuesta1 and dado3 % 2 == apuesta1:
        print("Todos los dados coinciden con la apuesta!", jugador1, "duplica su puntaje!!!")
        puntaje1 *= 2
        print(jugador1, "ahora tiene", puntaje1, "puntos")
else:
    puntaje1 -= menor1
    print(jugador1, "pierde", menor1, "puntos")

# Turno de Jugador2
print("-"*60)
print("Turno de {}".format(jugador2))

# Apuesta jugador 2
print("Debe apostar por resultado par o impar.")
apuesta2 = input("¿Desea apostar por par? (s/n)\n")
if apuesta2 == "s" or apuesta2 == "S":
    apuesta2 = 0
    print(jugador2, "apuesta por par...")
else:
    apuesta2 = 1
    print(jugador2, "apuesta por impar...")

print("-"*60)
input("Presione enter para lanzar los dados...")
print("...\n*Ruido de dados...* [USE SU IMAGINACIÓN >:| ]\n...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
input("Tus dados son: [{}] [{}] [{}]".format(dado1, dado2, dado3))

# Proceso: Cálculo de puntaje jugador 1 Segunda Ronda
mayor2 = max(dado1, dado2, dado3)
menor2 = min(dado1, dado2, dado3)
suma2 = dado1 + dado2 + dado3
if suma2 % 2 == 0:
    print("\nLa suma de los dados es par!")
else:
    print("\nLa suma de los dados es impar!")
if suma2 % 2 == apuesta2:
    puntaje2 += mayor2
    print(jugador2, "obtiene", mayor2, "puntos")
    if dado1 % 2 == apuesta2 and dado2 % 2 == apuesta2 and dado3 % 2 == apuesta2:
        print("Todos los dados coinciden con la apuesta!", jugador2, "duplica su puntaje!!!")
        puntaje2 *= 2
        print(jugador2, "ahora tiene", puntaje2, "puntos")
else:
    puntaje2 -= menor2
    print(jugador2, "pierde", menor2, "puntos")

# Resultado
print("="*60)
print("FIN DE LA PARTIDA")
print("="*60)
input("\nVeamos quien gano... Presione enter para continuar...\n")
print("*"*60)
print("*", jugador1, "obtuvo", puntaje1, "puntos y", jugador2, "obtuvo", puntaje2, "puntos")
if puntaje1 == puntaje2:
    print("* El resultado es empate! :/")
else:
    if puntaje1 > puntaje2:
        print("* El ganador es", jugador1, "!!!")
    else:
        print("* El ganador es", jugador2, "!!!")
print("*"*60)
print("\nGracias por jugar!\nEsperamos que lo hayan disfrutado :D")

# Créditos
creditos = """
(lease con voz en off...)

Diseño: Equipo docente
    -ing. Romina Teicher
    -ing. Marcela Tartabini
    -ing. Jorge Harach

Ejecución: Grupo 136 
    -Matías Avila (93599)
    -Nathaniel Balderramas (92334)
    -Gabriela Silva (92708)
"""
input("Presione enter para ver los créditos del juego...")
print(creditos)
