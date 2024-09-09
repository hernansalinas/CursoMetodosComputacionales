
# Laboratorio de Comandos en Bash: Nivel Básico e Intermedio

## Objetivos
- Familiarizarse con comandos básicos de Bash.
- Practicar la manipulación de archivos y directorios.
- Realizar búsquedas y procesamiento de texto.
- Gestionar permisos y recursos del sistema.

---

## Sección 1: Ejercicios Básicos de Linux

### Ejercicio 1: Creación y Navegación de Directorios

1. **Crea un directorio llamado `MetodosComputacionales` dentro de `Document/`.**
   - Comando: `mkdir ~/Document/MetodosComputacionales`
   
2. **Dentro de `MetodosComputacionales`, crea un directorio llamado `student`, el cual debería llevar tu nombre.**
   - Comando: `mkdir ~/Document/MetodosComputacionales/tu_nombre`

3. **Navega al directorio `/home` y luego vuelve al directorio `student` utilizando el comando `cd -`.**
   - Comandos: 
     ```bash
     cd /home
     cd -
     ```

4. **Lista los archivos y directorios del directorio `student`. Luego, lista los archivos y directorios de `/home`.**
   - Comandos:
     ```bash
     ls ~/Document/MetodosComputacionales/tu_nombre
     ls /home
     ```

5. **Muestra el directorio actual usando `pwd`. Luego, cambia al directorio `/usr/bin` y muestra el directorio actual nuevamente.**
   - Comandos:
     ```bash
     pwd
     cd /usr/bin
     pwd
     ```

---

### Ejercicio 2: Manipulación de Archivos y Directorios

1. **Crea un nuevo directorio llamado `prueba` dentro del directorio `student`. Luego, crea un subdirectorio llamado `subprueba` dentro de `prueba`.**
   - Comandos:
     ```bash
     mkdir ~/Document/MetodosComputacionales/tu_nombre/prueba
     mkdir ~/Document/MetodosComputacionales/tu_nombre/prueba/subprueba
     ```

2. **Elimina el subdirectorio `subprueba` que creaste en el paso anterior. Luego, intenta eliminar el directorio `prueba`.**
   - Comandos:
     ```bash
     rmdir ~/Document/MetodosComputacionales/tu_nombre/prueba/subprueba
     rmdir ~/Document/MetodosComputacionales/tu_nombre/prueba
     ```

3. **Crea un nuevo archivo llamado `saludo.txt` con el contenido "Hola mundo". Luego, copia `saludo.txt` al mismo directorio con el nombre `saludo2.txt`.**
   - Comandos:
     ```bash
     echo "Hola mundo" > ~/Document/MetodosComputacionales/tu_nombre/saludo.txt
     cp ~/Document/MetodosComputacionales/tu_nombre/saludo.txt ~/Document/MetodosComputacionales/tu_nombre/saludo2.txt
     ```

4. **Mueve el archivo `saludo2.txt` al directorio `prueba` y luego renómbralo a `saludo3.txt` dentro de `prueba`.**
   - Comandos:
     ```bash
     mv ~/Document/MetodosComputacionales/tu_nombre/saludo2.txt ~/Document/MetodosComputacionales/tu_nombre/prueba/
     mv ~/Document/MetodosComputacionales/tu_nombre/prueba/saludo2.txt ~/Document/MetodosComputacionales/tu_nombre/prueba/saludo3.txt
     ```

5. **Elimina el archivo `saludo.txt` en el directorio `student` y luego elimina `saludo3.txt` en el directorio `prueba`.**
   - Comandos:
     ```bash
     rm ~/Document/MetodosComputacionales/tu_nombre/saludo.txt
     rm ~/Document/MetodosComputacionales/tu_nombre/prueba/saludo3.txt
     ```

---

### Ejercicio 3: Procesamiento de Texto y Búsquedas

1. **Crea un archivo llamado `datos.txt` con los nombres y edades de tres personas, separados por comas. Luego, muestra su contenido.**
   - Comandos:
     ```bash
     echo -e "Ana,25
Pedro,30
Luisa,28" > ~/Document/MetodosComputacionales/tu_nombre/datos.txt
     cat ~/Document/MetodosComputacionales/tu_nombre/datos.txt
     ```

2. **Busca archivos con la extensión `.txt` en el directorio `student` y sus subdirectorios. Luego, busca archivos con un tamaño menor a 1 KB en el mismo directorio.**
   - Comandos:
     ```bash
     find ~/Document/MetodosComputacionales/tu_nombre -name "*.txt"
     find ~/Document/MetodosComputacionales/tu_nombre -size -1k
     ```

3. **Busca la palabra "Pedro" en el archivo `datos.txt` y muestra las líneas que la contienen. Luego, busca la palabra "Pedro" en todos los archivos del directorio `student`.**
   - Comandos:
     ```bash
     grep "Pedro" ~/Document/MetodosComputacionales/tu_nombre/datos.txt
     grep -r "Pedro" ~/Document/MetodosComputacionales/tu_nombre
     ```

---

## Sección 2: Ejercicios Intermedios de Linux

### Ejercicio 4: Verificación del Uso de Recursos

1. **Muestra la cantidad de espacio libre y usado en el disco duro en un formato legible.**
   - Comando: `df -h`

2. **Muestra la memoria usada y disponible en el sistema.**
   - Comando: `free -h`

3. **Lista todos los procesos que están utilizando más del 10% de la CPU.**
   - Comando:
     ```bash
     ps aux --sort=-%cpu | awk '$3>10'
     ```

---

### Ejercicio 5: Gestión de Permisos

1. **Cambia los permisos de `datos.txt` para que solo el propietario pueda leer y escribir, mientras que el grupo y otros solo puedan leer.**
   - Comando: `chmod 644 ~/Document/MetodosComputacionales/tu_nombre/datos.txt`

2. **Cambia el propietario de `datos.txt` a `root`.**
   - Comando: `sudo chown root:root ~/Document/MetodosComputacionales/tu_nombre/datos.txt`

