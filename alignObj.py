#Script by Alberto Martinez Arce - 2022
#Este Script toma la posicion y rotacion en en coordenadas globales
#del ultimo objeto seleccionado y lo aplica al resto de los objetos seleccionados

'''
Para agregar este script a un shelf button o a un hotkey, agrega el siguiente codigo Python:

Para copiar la pose al siguiente Frame:

import alignObj
alignObj.doAlign()

'''

import maya.cmds as cmds

def doAlign():

    objList = cmds.ls(sl=True)

    if len(objList) < 2:
        cmds.warning('Select at least two objects/Selecciona al menos dos objetos')

    else:
        masterObj = objList[-1]
        slaveObjs = objList[0:-1]

        trans = cmds.xform(masterObj, ws=True, q=True, translation=True)
        rot = cmds.xform(masterObj, ws=True, q=True, rotation=True)

        for obj in slaveObjs:

            cmds.xform(obj, ws=True, rotation=rot, translation=trans)
