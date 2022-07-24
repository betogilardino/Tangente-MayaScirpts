# Script by Alberto Martinez Arce - 2022

# Este Script crea un locator, lo coloca en la posicion de los objetos seleccionados
# y los nombra usando el mismo nombre del objeto original
# Si no hay objetos seleccionados, solo se crea un locator normal
# Create LOCATORS in place if nothing selected, and on the same position of any selected object/s

'''
Para agregar este script a un shelf button o a un hotkey, agrega el siguiente codigo Python:

import createLocator
createLocator.create()

'''

import maya.cmds as cmds


def create():

    objList = cmds.ls(sl=True)

    if len(objList) == 0:
        cmds.spaceLocator()

    else:
        for obj in objList:
            transforms = cmds.xform(obj, ws=True,q=True,matrix=1)
            rotOrder = cmds.xform(obj,q=True,rotateOrder=1)

            print(transforms)
            locName = "{}_Loc".format(obj)
            cmds.spaceLocator(name=locName)
            cmds.xform(locName,rotateOrder=rotOrder)
            cmds.xform(locName, ws=1, matrix=transforms)


