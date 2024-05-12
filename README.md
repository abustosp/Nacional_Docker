# Instalación del Sistema nacional en Servidores

Para poder instalar el  Nacional en un servidor VPS, vamos a tener que seguir una serie de pasos que los iré explicando en distintas secciones, algunas pueden realizarse en distinto orden.

Recomiendo utilizar Ubuntu como SO para el servidor, igualmente en teoría el instalador está dockerizado y debería funcionar sin problemas en otros SO.

Se puede utilizar tanto la IP Fija de los servicios de servidores (importante tenerla en cuenta para la conexión) como un dominio y la utilización de un Reverse Proxy para no "Acordarnos de esta dirección de IP"

## Descarga de este repositorio de github

Si tenemos git lo descargamos con `git clone https://github.com/abustosp/Nacional_Docker.git`, sinó podemos hacer click en code y `Download ZIP`.

## Descarga de los archivos necesarios de Nacional

1. Desde la página oficial de [Nacional](https://nacionalsoft.com/) vamos a Descargas y después bajamos el [[Nacional Sistema versión de 64 bits](https://nacionalsoft.com/file/Nacional_Sistema_1.7.0_64bit_install.exe).

2. Extraemos los binarios, esto lo hacemos con click derecho en el archivo descargado y dependiendo del archivador de ficheros que usemos podemos tener disitntas opciones (recomiendo usar [7Zip](https://www.7-zip.org/) que es gratis y de código abierto).

3. Copiamos/movemos la Carpeta de `server`  a la descargada del repositorio.

4. Copiamos nuestra licencia en la `carpeta server/cfg` 

5. Modificamos el archivo `server/cfg/nacional.cfg` con el editor de texto que prefiramos cambiamos los siguientes valores:
   - `net.host=localhost` por `net.host=0.0.0.0`
   - `web.host=`por `web.host=0.0.0.0`
   - `web.port=` por `web.port=8080`


## Preparación del servidor

1. Instalamos docker, podemos hacerlo con `apt install docker.io docker-compose-v2 -y` (en otros SO puede cambiar ligeramente el comando y puede no existir la dependencia de docker-compose-v2)

2. Copiamos toda la carpeta preparada anteriormente (la que posee los archivos extraídos con la licencia) al servidor, para esto hay muchas formas, la mas "sencilla" para los no programadores es usar [WinSCP](https://winscp.net/eng/index.php).

3. Una vez copiada la carpeta abrimos con conectamos por SSH al servidor y hacemos lo siguiente:
   
   1. Vamos a la carpeta con los archivos `cd NombreDeTuCarpeta`
   
   2. Instalamos el nacional, tenemos 2 opciones:
      
      1. Corremos `bash installation.sh`, para hacer una instalación un poco mas automatizada
      
      2. Corremos `docker compose -d` y luego que se creen los contenedores `bash import-master.sh`

## Preparación de las maquinas cliente (las que se conectan al servidor)

1. Instalamos nacional con el instalador previamente descargado.

2. Copiamos nuestra licencia en la `carpeta server/cfg`.

3. para conectar ponemos la `IP del Servidor contratado` o el `Dominio` ( ejemplo.com.ar si realizamos el Reverse Proxy) en `Opciones` y `Servidor`.

# Tips

- Modificar los puertos del `docker-compose.yml` (recordar usar el mismo en el cliente), el puerto 3306 es el más común para el uso de MySQL, si dejamos el puerto “normal” por defecto es más probable que algún atacante pueda encontrar una vulnerabilidad y copiarlas/borrarlas

- modificar las claves por defecto (`root`), si dejamos la original estamos dejando las bases de manera muy insegura y cualquiera podría acceder.

- Agregar el ingreso a IPs autorizadas (para esto se requiere tener un poco más de conocimientos de Administración de Bases de Datos de MySQL, hay muchos tutoriales en internet)
