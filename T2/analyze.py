from ast import *
import os
from rules import *

# Accede al folder donde estan los archivos python a ser analizados

path = "input-code/"
dir_list = os.listdir(path)
 
print("Analyzing files in '", path, "' :")

# Se analiza cada archivo en el folder input-code
for file in dir_list:
    print(" ==== " + file + " ==== ")
    
    # Se genera el AST (tree) segun el codigo del archivo
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    warnings = []

    # Se analiza el AST (tree) segun las reglas definidas en rules/__init__.py
    for ruleClass in Rule.__subclasses__():
        newRule = ruleClass()
        result = newRule.analyze(tree)
        warnings.extend(result)
        warnings.sort()

    # Se imprimen los warnings en consola
    for warning in warnings:
        print(warning)
