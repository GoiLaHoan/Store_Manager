from MVC.Controller.ReadnWriteF_Commodity import ReadnWriteF
import numpy as np
import matplotlib.pyplot as plt


class Graph_Commodity(object):

    def __init__(self):
        self.listIDCom = []
        self.listNameCom = []

        fileData_Commodity = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        file_Export = ReadnWriteF.ReadnWrite_File_Export_Commodity(self, 'rt')
        file_Import = ReadnWriteF.ReadnWrite_File_Import_Commodity(self, 'rt')

        for lineCom in fileData_Commodity:
            lineCom = lineCom.split()
            self.listIDCom.append(lineCom[0])
            self.listNameCom.append(lineCom[1])
        fileData_Commodity.close()

        self.sumDataExport = [0 for i in range(len(self.listIDCom))]
        self.sumDataImport = [0 for i in range(len(self.listIDCom))]

        for line in file_Export:
            lineExport = line.replace('\n', '').strip()
            lineExport = lineExport.split()
            for i in range(len(self.listIDCom)):
                if len(lineExport) > 0:
                    if self.listIDCom[i] == lineExport[0]:
                        self.sumDataExport[i] = self.sumDataExport[i] + int(lineExport[2])
        file_Export.close()

        for line in file_Import:
            lineImport = line.replace('\n', '').strip()
            lineImport = lineImport.split()
            for i in range(len(self.listIDCom)):
                if len(lineImport) > 0:
                    if self.listIDCom[i] == lineImport[0]:
                        self.sumDataImport[i] = self.sumDataImport[i] + int(lineImport[2])
        file_Import.close()

        '''
        Design Graph
        '''
        plt.figure(figsize=(13, 8))
        plt.gcf().canvas.set_window_title('Statistics On The Amount Of Import - Export')
        x = np.arange(len(self.sumDataExport))
        plt.bar(x, self.sumDataImport, width=0.3, color='green', label='Import Commodity')
        plt.bar(x + 0.3, self.sumDataExport, width=0.3, color='blue', label='Export Commodity')
        plt.title('Statistical Tables')
        plt.ylabel('Quantily Export of Commodity', color='red')
        plt.xlabel('Name of Commodity', color='red')
        plt.xticks(x + 0.3 / 2, self.listNameCom)
        plt.legend(loc='best')
        plt.show()


def main5():
    Graph_Commodity()


if __name__ == "__main__":
    main5()
