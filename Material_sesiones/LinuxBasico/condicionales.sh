#!/bin/bash

echo "¡Bienvenido al Laberinto de Condicionales!"
echo "Tu objetivo es salir del laberinto tomando las decisiones correctas."
echo "En cada paso, tendrás que elegir una opción."

# Posición inicial en el laberinto
posicion=0

# Función que presenta una situación y pide una decisión
hacer_decision() {
    local mensaje="$1"
    local opcion1="$2"
    local opcion2="$3"
    local respuesta_correcta="$4"

    echo "$mensaje"
    echo "1) $opcion1"
    echo "2) $opcion2"
    read -p "Elige 1 o 2: " eleccion

    if [ "$eleccion" -eq "$respuesta_correcta" ]; then
        echo "¡Correcto! Avanzas un paso."
        posicion=$((posicion + 1))
    else
        echo "Incorrecto. Debes intentar de nuevo."
    fi
}

# Laberinto con tres decisiones
while [ $posicion -lt 3 ]; do
    if [ $posicion -eq 0 ]; then
        hacer_decision "Estás en la entrada del laberinto. Un cartel dice 'Elige el camino más corto'." \
                      "Camino a la izquierda (parece fácil)" \
                      "Camino a la derecha (parece complicado)" \
                      2
    elif [ $posicion -eq 1 ]; then
        hacer_decision "Llegas a una bifurcación. Un cartel dice 'Elige el número más grande'." \
                      "Camino con el número 5" \
                      "Camino con el número 9" \
                      2
    elif [ $posicion -eq 2 ]; then
        hacer_decision "Llegas a una puerta cerrada con dos llaves. Un cartel dice 'Elige la llave correcta'." \
                      "Llave de oro" \
                      "Llave de plata" \
                      1
    fi
done

echo "¡Felicidades! Has salido del laberinto de condicionales."
