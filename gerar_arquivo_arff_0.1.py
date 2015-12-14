# -*- encoding:utf-8 -*-

####################
#         .　　.   #
#▼▁▁▁▁▁▁◣▁◢     #
# LAB_AM◕⃝ ◔⃝　     #
#▔▔▔▔▔▔▔▔▔▔     #
#    Laboratório   #
#       de         # 
#   Aprendizagem   #
#       de         # 
#     Máquina      #
#                  #
####################

import csv
import sys
import glob
import re

nome_arquivo = []
nome_arquivo += nome_arquivo + glob.glob('*.names')
radical = nome_arquivo[0].split(".")

aux = open(sys.argv[1],"r")
ultima_linha = aux.readlines()[-1]
aux.close()


with open(sys.argv[1],"rb") as fonte_name:
    with open(radical[0] + ".arff", "w") as saida:
        for i, linha in enumerate(fonte_name.readlines()):
            if i == 0:
                del linha
                saida.write("@RELATION " + re.findall(r"[\w']+", ultima_linha)[2] + "\n") 
            elif i == 1:
                del linha  
                saida.write("\n")
            else:
                atributo = re.findall(r"[\w']+", linha)
                if "att_class" not in  atributo[0]:
                    saida.write("@ATTRIBUTE " + atributo[0] + " " + atributo[1] + "\n")
                else:
                    del linha
                    ultima_linha = ultima_linha.replace('(', '{')
                    ultima_linha = ultima_linha.replace(').', '}') 
                    ultima_linha = ultima_linha.replace(':nominal', ' ')
                    saida.write("@ATTRIBUTE " + ultima_linha + "\n")       
        saida.write("@DATA" + "\n")
        
        with open(sys.argv[2],"rb") as fonte_data:
            leitura = csv.reader(fonte_data)
            escrita = csv.writer(saida)
            for linha in leitura:
                del linha[0]
                escrita.writerow(linha)

    print("Aquivo " + radical[0] + ".arff" + " gerado com sucesso!!!")
