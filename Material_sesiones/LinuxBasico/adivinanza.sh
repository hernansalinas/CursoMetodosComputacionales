#!/bin/bash

# Generar un número aleatorio entre 1 y 100
numero_secreto=$((RANDOM % 100 + 1))

echo "¡Bienvenido al juego de Adivina el Número!"
echo "He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?"

intentos=0
adivinado=0

# Bucle del juego
while [ $adivinado -eq 0 ]; do
    echo "Introduce tu suposición:"
    read suposicion

    # Incrementar el contador de intentos
    intentos=$((intentos + 1))

    # Verificar la suposición del jugador
    if [ $suposicion -lt $numero_secreto ]; then
        echo "Demasiado bajo. ¡Intenta de nuevo!"
    elif [ $suposicion -gt $numero_secreto ]; then
        echo "Demasiado alto. ¡Intenta de nuevo!"
    else
        echo "¡Felicidades! Has adivinado el número en $intentos intentos."
        adivinado=1
    fi
done

echo "Gracias por jugar. ¡Hasta la próxima!"

