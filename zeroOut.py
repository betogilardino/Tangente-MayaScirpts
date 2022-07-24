# Script by Alberto Martinez Arce - 2022
# Este script regresa los valores de rotacion, translacion a 0, o escala a 1
# Dependiendo que valor este marcado como True al llamar la funcion applyZeroOut
# This script will set rotation, translation and scale attributes to 0 depending 
# depending which value is set to True when the funciton applyZeroOut is called

'''
Para usarlo como un hotkey o como boton en el shelf, copia el siguiente codigo Python dependiendo
que atributos quieres modificar:

Para hacer que la translacion se vuelva 0:

import zeroOut
zeroOut.applyZeroOut(rot=True,trans=False,scale=False)
_________________________________________________________________

Para hacer que la translacion se vuelva 0:

import zeroOut
zeroOut.applyZeroOut(rot=False,trans=True,scale=False)
_________________________________________________________________
Para hacer que la escala se vuelva 1:

import zeroOut
zeroOut.applyZeroOut(rot=False,trans=False,scale=True)

'''



import maya.cmds as cmds

#Funcion para asignar los valores a cada atributo
def zeroOut(list,attrs,newValue=0):
    for obj in list:
        for at in attrs:
            if cmds.getAttr('{}.{}'.format(obj,at), se=True):
                cmds.setAttr("%s.%s"%(obj,at),newValue)

#Funcion para applicar los nuevos valores
def applyZeroOut(rot=True,trans=True,scale=False):
    rotList = ["ry","rx","rz"]
    transList = ["ty","tx","tz"]
    scaleList = ["sy","sx","sz"]

    objSelected = cmds.ls(sl=1)

    if len(objSelected) == 0:
        cmds.warning("No objects Selected/No hay objetos seleccionados")

    else:
        if rot:
            zeroOut(objSelected,rotList)
        elif trans:
            zeroOut(objSelected,transList)
        elif scale:
            zeroOut(objSelected,scaleList,newValue=1)

