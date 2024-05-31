#from tkinter.filedialog import askdirectory
import os
import re

#directorio = askdirectory()
directorio = "master"
archivos = os.listdir(directorio)
archivos = [archivo for archivo in archivos if archivo.endswith('.sql')]
archivos = [os.path.join(directorio, archivo) for archivo in archivos]
for i in archivos:
    # imprimir la database (es lo que precede a "Database: ") (está dentro de las primeras 5 línes)
    i = i.replace('\\', '/')
    with open(i, 'r') as f:
        for j in range(5):
            linea = f.readline()
            if 'Database: ' in linea:
                database = re.search(r'Database: (.+)', linea).group(1)
                break
    # print(f"{i.split('/')[-1]}:{database}")
    print(f'docker exec -ti mysql bash -c "mysql -uroot -proot {database} < master/{i.split("/")[-1]}"')