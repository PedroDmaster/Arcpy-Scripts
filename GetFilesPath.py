# Obter uma lista de todas as FeatureClasses numa directoria de trabalho, e o nome das respectivas fileGeoDB onde estão inseridas


import arcpy
import os

x = 0
fcPaths = []
# wspace = input(r"Workspace to search: ")
wspace = r"C:\GISData"
arcpy.env.workspace = wspace
for dirpath, dirname, dirfiles in os.walk(wspace, topdown=True):
    print(dirpath)
    # definir directoria de trabalho -> workspace
    arcpy.env.workspace = dirpath
    # obter uma lista de todos os workspaces dentro da directoria
    gdbList = arcpy.ListWorkspaces('*', 'FileGDB')
    for gdb in gdbList:
        # definir cada gdb como workspace
        arcpy.env.workspace = gdb
        # listar todos os datasets da gdb actual
        datasetList = arcpy.ListDatasets('*', 'Feature')
        # listar todas as feature classes da gdb actual
        fcList = arcpy.ListFeatureClasses()
        # separador de paths usado pelo OS
        sep = "\\"
        for fc in fcList:
            # print da directoria e do nome da fc
            print(arcpy.env.workspace, fc)
            # adicionar o path da fc à lista
            fcPaths.append(
                f"Feature Class:\t{fc}\nGeoDB:\t{gdb}\nLocalização(Path):\t{arcpy.env.workspace}{sep}{fc}")
            x += 1
        for dataset in datasetList:
            # mudar o workspace para cada dataset da lista
            arcpy.env.workspace = dataset
            # listar as fc do dataset
            fcList = arcpy.ListFeatureClasses()
            for fc in fcList:
                # print da directoria e do nome da fc
                print(arcpy.env.workspace, fc)
                # adicionar o path da fc à lista
                fcPaths.append(
                    f"Feature Class:\t{fc}\nDataset:\t{dataset}\nGeoDB:\t{gdb}\nLocalização(Path):\t{arcpy.env.workspace}{sep}{fc}")
                x += 1

print('Fez a lista: ', "\n\n".join(fcPaths), "Nr de FC: " + str(x))

open("C:\\Users\\pedro\\Feature_Classes_existentes.txt", "w").write(
    "Nr de FC: " + str(x) + "\n\n" + "\n\n".join(fcPaths))

print('Fez o txt')
