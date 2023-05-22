# Ejercicio Basico de linux 

- Crea un directorio llamado MetodosComputacionales dentro de Document/

- Crea un directorio llamado student dentro MetodossComputacionales, el directorio student deberia ser su nombre 

- cd: Cambia al directorio /home usando el comando cd /home. Luego, vuelve al directorio student usando el comando cd -.

- ls: Lista los archivos y directorios del directorio student usando el comando ls. Luego, lista los archivos y directorios del directorio /home usando el argumento /home. Finalmente, lista los archivos y directorios del directorio student con detalles usando la flag -l.

- pwd: Muestra el directorio actual usando el comando pwd. Luego, cambia al directorio /usr/bin usando el comando cd /usr/bin. Finalmente, muestra el directorio actual de nuevo usando el comando pwd.


- mkdir: Crea un nuevo directorio llamado prueba dentro del directorio student usando el comando mkdir prueba. Luego, crea un nuevo directorio llamado subprueba dentro del directorio prueba usando el comando mkdir prueba/subprueba. Finalmente, lista los archivos y directorios del directorio prueba usando el comando ls prueba.

- rmdir: Elimina el directorio subprueba que creaste en el paso anterior usando el comando rmdir prueba/subprueba. Luego, intenta eliminar el directorio prueba usando el mismo comando. Finalmente, verifica que el comando te dé un error porque el directorio prueba no está vacío.

- cp: Crea un nuevo archivo llamado saludo.txt con el contenido “Hola mundo” usando el comando echo “Hola mundo” > saludo.txt. Luego, copia el archivo saludo.txt al mismo directorio con el nombre saludo2.txt usando el comando cp saludo.txt saludo2.txt. Finalmente, lista los archivos y directorios del directorio student usando el comando ls.

- mv: Mueve el archivo saludo2.txt al directorio prueba que creaste anteriormente usando el comando mv saludo2.txt prueba/. Luego, renombra el archivo saludo2.txt a saludo3.txt dentro del directorio prueba usando el comando mv prueba/saludo2.txt prueba/saludo3.txt. Finalmente, lista los archivos y directorios del directorio prueba usando el comando ls prueba.

- rm: Elimina el archivo saludo.txt que creaste en el directorio student usando el comando rm saludo.txt. Luego, elimina el archivo saludo3.txt que moviste al directorio prueba usando el comando rm prueba/saludo3.txt. Finalmente, lista los archivos y directorios del directorio prueba usando el comando ls prueba.

- cat: Crea un nuevo archivo llamado datos.txt con los nombres y edades de tres personas separados por comas usando el comando echo “Ana,25\nPedro,30\nLuisa,28” > datos.txt. Luego, muestra el contenido del archivo datos.txt usando el comando cat datos.txt.
find: Busca archivos con la extensión .txt en el directorio student y sus subdirectorios usando el comando find . -name “*.txt”. Luego, busca archivos con un tamaño menor a 1 KB en el mismo directorio y sus subdirectorios usando el comando find . -size -1k. Finalmente, busca archivos que contengan la palabra “hola” en su nombre en el mismo directorio y sus subdirectorios usando el comando find . -name “hola”.

- grep: Busca la palabra “Pedro” en el archivo datos.txt y muestra las líneas que la contienen usando el comando grep “Pedro” datos.txt. Luego, busca la palabra “Pedro” en todos los archivos del directorio student y sus subdirectorios y muestra los nombres de los archivos y las líneas que la contienen usando el comando grep -r “Pedro” . Finalmente, busca la palabra “Pedro” en todos los archivos del mismo directorio y sus subdirectorios y muestra solo los nombres de los archivos que la contienen usando el comando grep -rl “Pedro” .