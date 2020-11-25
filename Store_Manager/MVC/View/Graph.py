
from MVC.Controller.ReadnWriteF_Commodity import ReadnWriteF
import numpy as np
import matplotlib.pyplot as plt

class Graph_Commodity(object):


    def __init__(self):
        self.listIDCom = []
        self.listNameCom=[]
        fC = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        fS = ReadnWriteF.ReadnWrite_File_Sales(self, 'rt')
        fI = ReadnWriteF.ReadnWrite_File_Import_Commodity(self,'rt')
        for lineCom in fC:
            lineCom = lineCom.split()
            self.listIDCom.append(lineCom[0])
            self.listNameCom.append(lineCom[1])
        fC.close()
        self.sumDataSale =[0 for i in range(len(self.listIDCom))]
        self.sumDataImport = [0 for i in range(len(self.listIDCom))]

        for line in fS:
            lineSal=line.replace('\n','').strip()
            lineSal = lineSal.split()
            for i in range(len(self.listIDCom)):
                if len(lineSal) >0 :
                    if self.listIDCom[i] == lineSal[0]:
                        self.sumDataSale[i] = self.sumDataSale[i] + int(lineSal[2])
        fS.close()
        for line in fI:
            lineImp=line.replace('\n','').strip()
            lineImp = lineImp.split()
            for i in range(len(self.listIDCom)):
                if len(lineImp) >0 :
                    if self.listIDCom[i] == lineImp[0]:
                        self.sumDataImport[i] = self.sumDataImport[i] + int(lineImp[2])
        fS.close()
        plt.gcf().canvas.set_window_title('window title')
        x=np.arange(len(self.sumDataSale))
        plt.bar(x,self.sumDataImport,width=0.3,color='green',label='Import Commodity')
        plt.bar(x+0.3,self.sumDataSale,width=0.3,color='blue',label='Sale Commodity')
        plt.title('Chào học trò thầy Huấn')
        plt.ylabel('QuantilySales of Commodity',color='red')
        plt.xlabel('Name of Commodity',color='red')
        plt.xticks(x+0.3/2,self.listNameCom)
        plt.legend(loc='best')
        plt.show()

def main5():
    Graph_Commodity()

if __name__ == "__main__":
    main5()
