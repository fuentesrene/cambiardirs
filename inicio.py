

# Programa de Python program
# 1. Lee todas combinaciones historicas de un archivo, una combinacion un linea
# 2. De cada linea se obtiene 6C2 = 15 combs 
# 3. Se almacenan las combs de 2. en mydic{} sin repeticion para saber que cuanto ha caido
# 4. Creamos un umbral para escoger 80% del centro de todas las combs
# 5. combinations of given length

import os
from pathlib import Path


dir1 = "G:\Eventos"
dir2 = "E:\Eventos"
i1 = dir1[:1]
i2 = dir2[:1]



#   2do método: extrae las tuplas necesarias con numeros no repetidos para llegar a 49 numeros
#   Llena las cur_tuplas dict con las tuplas actuales ya sean 2, 3, 4, 5
def iniciar(dir1, dir2):
    folders_dir1 = set()
    folders_dir2 = set()
    # os.walk regresa 3-tuple (dirpath, dirnames, filenames), x[0] es la primera tuple.
    # folders_dir2 = set([x[0] for x in os.walk(dir2)])
    for x in os.walk(dir1):
        x1 = x[0][1:]
        folders_dir1.add(x1)
    for y in os.walk(dir2):
        y1 = y[0][1:]
        folders_dir2.add(y1)
    folders_in_dir1_but_not_dir2 = folders_dir1 - folders_dir2 
    folders_in_dir2_but_not_dir1 = folders_dir2 - folders_dir1

    print("\n\n")
    print ("     ==================================================================")
    print ("      Hay " + str(len(folders_in_dir1_but_not_dir2)) + " directorios en " + dir1 + " que no estan en " + dir2 + " :")
    print ("     ==================================================================")
    print("\n\n")
    print ("     =======================================================")
    print ("      Directorios en " + dir1 + " que no estan en " + dir2 + " :")
    print ("     ========================================================")
    print(" ")
    for f1 in folders_in_dir1_but_not_dir2:
        print ("     " + i1 + f1)
  
    print("\n\n")
    print ("     ==================================================================")
    print ("      Hay " + str(len(folders_in_dir2_but_not_dir1)) + " diclsrectorios en " + dir2 + " que no estan en " + dir1 + " :")
    print ("     ==================================================================")
    print(" ")
    print("\n\n")
    print ("     =======================================================")
    print ("      Directorios en " + dir2 + " que no estan en " + dir1 + " :")
    print ("     =======================================================")
    print(" ")
    for f2 in folders_in_dir2_but_not_dir1:
        print ("     " + i2 + f2)
    print ("")

    dir1_filenames = set(f.name for f in Path(dir1).rglob('*'))
    dir2_filenames = set(f.name for f in Path(dir2).rglob('*'))
    files_in_dir1_but_not_dir2 = dir1_filenames - dir2_filenames 
    files_in_dir2_but_not_dir1 = dir2_filenames - dir1_filenames

    print("\n\n")
    print ("     =======================================================")
    print ("      Archivos en " + dir1 + " que no estan en " + dir2 + " :")
    print ("     =======================================================")
    print(" ")
    for el in files_in_dir1_but_not_dir2:
        print ("     " + el)
    print ("")
    print("\n\n")
    print ("     =======================================================")
    print ("      Archivos en " + dir2 + " que no estan en " + dir1 + " :")
    print ("     =======================================================")
    print(" ")
    for un in files_in_dir2_but_not_dir1:
        print ("     " + un)
    print ("")
    return dir1_filenames, dir2_filenames


if __name__ == '__main__':
    #iniciar49()
    iniciar(dir1, dir2)
    