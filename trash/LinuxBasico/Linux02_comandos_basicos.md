# Comandos basicos de linux 
Los archivos en Linux están ordenados según una estructura jerárquica de directorios y subdirectorios que se conoce como árbol de archivos. El árbol de archivos comienza en la raíz o /, que es el directorio principal que contiene todos los demás directorios y archivos. Cada directorio puede contener otros directorios o archivos, formando así ramas del árbol. Por ejemplo, el directorio /home contiene los directorios personales de los usuarios, y el directorio /etc contiene los archivos de configuración del sistema.




| Nombre del comando | Ejemplo | Descripción |
| ------------------ | ------- | ----------- |
| cd | cd /home | Cambia el directorio actual al que se especifica como argumento. |
| ls | ls -l | Lista los archivos y directorios del directorio actual con detalles. |
| pwd | pwd | Muestra el directorio actual. |
| mkdir | mkdir nuevo | Crea un nuevo directorio llamado nuevo. |
| rmdir | rmdir viejo | Elimina el directorio llamado viejo si está vacío. |
| cp | cp archivo1 archivo2 | Copia el archivo1 al archivo2. |
| mv | mv archivo1 archivo2 | Mueve o renombra el archivo1 al archivo2. |
| rm | rm archivo1 | Elimina el archivo1. |
| cat | cat archivo1 | Muestra el contenido del archivo1. |
| find | find . -name "*.txt" | Busca archivos con la extensión .txt en el directorio actual y sus subdirectorios. |
| grep | grep "hola" archivo1 | Busca la palabra "hola" en el archivo1 y muestra las líneas que la contienen. |
| sudo | sudo apt-get update | Ejecuta el comando apt-get update como superusuario o administrador. |
| man | man ls | Muestra el manual o la ayuda del comando ls. |
| top | top | Muestra los procesos que se están ejecutando en el sistema y su consumo de recursos. |
| ping | ping www.google.com | Envía paquetes de prueba a una dirección de red o web y muestra el tiempo de respuesta. |
| wget | wget https://www.ionos.es/digitalguide/servidores/configuracion/comandos-de-linux-la-lista-fundamental/ | Descarga un archivo o una página web desde una URL. |
| uname | uname -a | Muestra información sobre el sistema operativo y el hardware. |
| tar | tar -czvf archivo.tar.gz carpeta | Crea un archivo comprimido llamado archivo.tar.gz con el contenido de la carpeta. |
| chmod | chmod 755 archivo1 | Cambia los permisos de acceso al archivo1 a 755 (lectura, escritura y ejecución para el propietario, lectura y ejecución para el grupo y los demás). |
| chown | chown usuario:grupo archivo1 | Cambia el propietario y el grupo del archivo1 al usuario y grupo especificados. |
| ps | ps -aux | Muestra información sobre los procesos que se están ejecutando en el sistema. |
| kill | kill -9 1234 | Termina el proceso con el identificador 1234. |
| echo | echo "Hola mundo" | Imprime un mensaje en la pantalla o en un archivo. |
| zip | zip archivo.zip archivo1 archivo2 | Crea un archivo comprimido llamado archivo.zip con los archivos archivo1 y archivo2. |
| unzip | unzip archivo.zip | Extrae los archivos de un archivo comprimido. |