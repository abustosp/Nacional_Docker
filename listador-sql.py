#from tkinter.filedialog import askdirectory
import os
import re

#directorio = askdirectory()
directorio = "master"
archivos = os.listdir(directorio)
archivos = [archivo for archivo in archivos if archivo.endswith('.sql')]
# Eliminar el archivo creardatabases.sql si existe
if 'creardatabases.sql' in archivos:
    archivos.remove('creardatabases.sql')
archivos = [os.path.join(directorio, archivo) for archivo in archivos]
crear = []
importar = []
for i in archivos:
    # imprimir la database (es lo que precede a "Database: ") (está dentro de las primeras 5 línes)
    i = i.replace('\\', '/')
    with open(i, 'r') as f:
        for j in range(5):
            linea = f.readline()
            if 'Database: ' in linea:
                database = re.search(r'Database: (.+)', linea).group(1)
                break

    # agregar a importar la línea f'docker exec -ti mysql bash -c "mysql -uroot -proot {database.replace(" ", "_")} < master/{i.split("/")[-1]}"'
    importar.append(f'docker exec -ti mysql bash -c "mysql -uroot -proot {database.replace(" ", "_")} < master/{i.split("/")[-1]}"')
    # agregar a crear la line f'CREATE DATABASE IF NOT EXISTS {database.replace(" ", "_")}'
    crear.append(f'CREATE DATABASE IF NOT EXISTS {database.replace(" ", "_")};')

# Exportar crear a sql
with open('master/creardatabases.sql', 'w') as f:
    f.write("\n".join(crear))
    
# Exportar importar a sh
with open('importar.sh', 'w') as f:
    f.write("\n".join(importar))
