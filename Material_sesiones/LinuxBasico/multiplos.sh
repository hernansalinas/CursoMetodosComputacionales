#!/bin/bash

echo "Ingrese un número:"
read numero

echo "Ingrese un límite:"
read limite

a=1
while [ $((numero * a)) -le $limite ]; do
    echo "$((numero * a))"
    a=$((a + 1))  # Incrementar la variable a
done
