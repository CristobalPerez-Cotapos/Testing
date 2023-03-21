from ast import *
import os
from rewriter import *

# Accede al folder donde estan los archivos python a ser transformados
path = "input-code/"
dir_list = os.listdir(path)
 
print("Transforming files in '", path, "' :")

# Se transforma cada archivo en el folder input-code
for file in dir_list:
    print(" ==== " + file + " ==== ")

    # Se genera el AST (tree) segun el codigo del archivo
    fileContent = open(path+file).read()
    tree = parse(fileContent)

    # Se analiza el AST (tree) segun las los comandos definidos en rewriter/__init__.py
    for commandClass in RewriterCommand.__subclasses__():    
        command = commandClass()
        tree = command.apply(tree)

    # Se exporta el AST transformado a un archivo en el folder transformed-code
    f = open("transformed-code/" + file , "w")
    f.write(unparse(tree))
    f.close()
