import math


class Sudoku():
    def __init__(self, elementos):
        self.__elementos = elementos

    def getVerificarFila(self):
        array = [0,0,0,0,0,0,0,0,0,0]
        for i in range(len(self.__elementos)):
            num = int(self.__elementos[i])
            # print (num)
            if((i)%9 == 0):
                # print(array)
                array = [0,0,0,0,0,0,0,0,0,0]
            if(array[num]==0):
                array[num]=1
            else:
                return False
        return True
    
    def getVerificarColumna(self):
        for i in range(9):
           
            array = [0,0,0,0,0,0,0,0,0,0]
            for j in range(i,len(self.__elementos),9):
                num = int(self.__elementos[j])
                if(array[num]==0):
                    array[num]=1
                else:
                    return False

        return True

