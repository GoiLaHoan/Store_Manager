from MVC.Controller.ReadnWriteF_Commodity import ReadnWriteF
import numpy as np
import matplotlib.pyplot as plt

class Graph_Commodity(object):

    def __init__(self):
        self.listIDCom = []
        self.listNameCom=[]


        '''
        Processing file Commodity
        '''
        fileC = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        for lineCom in fileC:
            lineCom = lineCom.split()
            self.listIDCom.append(lineCom[0])
            self.listNameCom.append(lineCom[1])
        self.sumDataSale = [0 for i in range(len(self.listIDCom))]
        fileC.close()


        '''
        Processing file Sales
        '''
        fileS = ReadnWriteF.ReadnWrite_File_Sales(self, 'rt')
        for line in fileS:
            lineSal=line.replace('\n','').strip()
            lineSal = lineSal.split()
            for i in range(len(self.listIDCom)):
                if len(lineSal) >0 :
                    if self.listIDCom[i] == lineSal[0]:
                        self.sumDataSale[i] = self.sumDataSale[i] + int(lineSal[2])
        fileS.close()

        '''
        Create Column Chart
        '''
        plt.figure(figsize=(10, 7))
        plt.gcf().canvas.set_window_title('window title')
        x=np.arange(len(self.sumDataSale))
        y1=[10,20,40,30,23,10,20,40,30,23]
        plt.bar(x,y1,width=0.3,color='green',label='Import Commodity')
        plt.bar(x+0.3,self.sumDataSale,width=0.3,color='blue',label='Sale Commodity')
        plt.title('Bán hàng để cứu anh Bảnh')
        plt.ylabel('QuantilySales of Commodity',color='red')
        plt.xlabel('Name of Commodity',color='red')
        plt.xticks(x+0.3/2,self.listNameCom)
        plt.legend(loc='best')
        plt.show()

def main5():
    Graph_Commodity()

if __name__ == "__main__":
    main5()
