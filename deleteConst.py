#Script by Alberto Martinez Arce - 2022
#Este Script borra cualquier constraints de los objetos seleccionados


'''
Para agregar este script a un shelf button o a un hotkey, agrega el siguiente codigo Python:

import deleteConst
deleteConst.doDelete()

'''
import maya.cmds as cmds

def doDelete():
    deleteList = []

    itemList = cmds.ls(sl=1)

    if len(itemList) is 0:
        cmds.warning("No hay objetos seleccionados/ There's no selected Objects")

    else:

        for item in itemList:

            constraintList = cmds.listRelatives(item,fullPath=True,type='constraint')
            if constraintList:
                for const in constraintList:
                    deleteList.append(const)
        

        if len(deleteList) is 0:
            cmds.warning("Los objetos seleccionados no tienen Constraints/The selected objects have no Constraints")

        else:
            print("Lista de Constraints a borrar: / Constraint delete list:")
            for const in deleteList:
                print(const.split('|')[-1])

            cmds.delete(deleteList)
