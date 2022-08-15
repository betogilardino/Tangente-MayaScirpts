#Script by Alberto Martinez Arce - 2022
#Cuando tienes un objeto que esta siendo modificado por un constraint y quieres saber
# cual es o son los objetos que lo controlan puedes usar este script

#Selecciona un objeto a la vez que esta siendo controlado por cualquier constraint, y ejecuta el script, 
# el resultado te dejara seleccionado los objetos que tiene como maestros en los Constraints y
# en el script editor, creara una lista de esos objetos

'''
Para agregar este script a un shelf button o a un hotkey, agrega el siguiente codigo Python:

import selectParent
selectParent.doSelectParent()

'''
import maya.cmds as cmds

def doSelectParent():
    #Crea una lista vacia de los objetos que controlan a nuestro objeto seleccionado
    parentList = []

    #Listamos los objetos que estan actualmente seleccionados
    itemList = cmds.ls(sl=1)

    #Verificamos que el numero de objetos seleccionados sea exactamente 1
    if len(itemList) is 0:
        cmds.warning("Selecciona un objeto/ Select one object")
    elif len(itemList) > 1:
        cmds.warning("Selecciona 1 objeto a la vez/ Select one object at the time")

    else:
        #Creamos una lista vacia, para agregar ahi todos los constraintes que pueden
        #estar modificando a nuestro objeto seleccionado, a veces pueden ser varios constriants a la vez
        constraintList = []
        
        #Verificamos si el objeto seleccionado es un constraint, si lo es, lo agregamos a la lista
        if cmds.objectType(itemList, isAType='constraint'):
            constraintList = cmds.ls(itemList,l=True)

        # De no ser un constraint, hacemos una busqueda de relativos que solo nos regrese los enlistados al 
        # que son constraints de cualquier tipo
        else:
            constraintList = cmds.listRelatives(itemList,fullPath=True,type='constraint')
        # si la lista de Constraints tiene al menos un integrante, avanzamos a la siguiente parte
        if constraintList:
            # For loop, para analizar cada constraint involucrado
            for const in constraintList:
                # Enlistamos las conecciones del constraint que tengan un target
                connections = cmds.listConnections('{}.target'.format(const))
                # Revisando que si se hayan detectado targets como conecciones
                if connections:
                    #Para cada uno de los targets indicados:
                    for item in connections:
                        #Primero conseguimos el nombre absoluto de ese item, y tomamos el primer elmento
                        #para convertirlo de lista a un string normal
                        itemFull = cmds.ls(item,l=True)[0]
                        #Checar que el target no esta ya incluido en nuestra lista de objetos que son los maestros
                        if itemFull not in parentList:
                            # Por ultimo checamos que el target no sea el mismo nombre del constraint que estamos usando
                            #Ya que Maya regresa el nombre del constraint en la lista de conecciones

                            if itemFull != const:
                                #Lo aniadimos a la lista de padres
                                parentList.append(itemFull)
                       
            #Mostrar en el Script Editor una lista de los objetos maestros
            print("Lista de maestros de los objetos seleccionados: / Target list on selected objects:")
            for target in parentList:
               print(target.split('|')[-1])
            print('**********************')

            #Por ultimo, seleccionamos los objetos que estan en la lista de parentList
            cmds.select(parentList,r=True)

        # Si los objetos seleccionados originalmente no estan influenciados por un constraint, mandar un aviso
        else:
             cmds.warning("Los objetos seleccionados no tienen Constraints/The selected objects have no Constraints")