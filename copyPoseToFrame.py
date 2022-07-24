# Script by Alberto Martinez Arce - 2022
# Este Script toma la pose de tu objeto(s) seleccionados y la coloca 
# en el mismo objeto en el frame adelante o atras


'''
Para agregar este script a un shelf button o a un hotkey, agrega el siguiente codigo Python:

Para copiar la pose al siguiente Frame:

import copyPoseToFrame
copyPoseToFrame.forward()

Para copiar la pose al frame anterior

import copyPoseToFrame
copyPoseToFrame.backwards()

'''


#Importa dentro de Python la libreria de comandos de Maya
import maya.cmds as cmds


def copyPoseTo(direction=1):
    #Genera una lista de objetos seleccionados y los asigna a la variable ObjList
    objList = cmds.ls(sl=1)

    #Use el comando current time con el flag q (query) para saber en que frame estamos,
    #y lo almacena en curTime
    curTime = cmds.currentTime(q=1)


    #Para saber que frame sera donde se copie la pose, sumamos el curTime y la direccion,
    #lo guardamos en la variable pasteTime
    pasteTime = curTime + direction


    #Creamos un FOR loop, para que las siguientes acciones se apliquen a cada elemento de 
    #la lista objList
    for obj in objList:
        #Con el comando Xform y el flag q (query), obtenemos la matrix (m) de transformacion 
        #de nuestro objeto en cuestion
        #Usando el flag: WorldSpace, nos aseguramos que los valores sean absolutos
        #Almacenando la informacion en la variable transforms
        transforms = cmds.xform(obj,q=1,m=1,worldSpace=1)
        
        #Con el comando currentTime hacemos que el frame actual sea el frame donde pegaremos la pose
        cmds.currentTime(pasteTime)
        
        #Con Xform movemos el objeto a la matrix de transformacion
        #que obtuvimos de nuestra pose original
        cmds.xform(obj,m=transforms,worldSpace=1)
        
        #Con el comando currentTime regresamos a nuestro frame original 
        #para copiar la pose del siguiente objeto seleccionado
        cmds.currentTime(curTime)
        

    #Una vez que acabamos de pegar todas las poses, avanzamos al frame 
    #donde se pegaron las poses de todos los controles u objetos
    cmds.currentTime(pasteTime)

def forward():
    copyPoseTo(direction=1)

def backwards():
    copyPoseTo(direction=-1)