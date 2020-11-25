class ReadnWriteF:

    def ReadnWrite_File_Commodity(self, mode):
        ReadnWrite = open('./../../Data/Data_Commodity.txt', mode, encoding='utf-8')
        return ReadnWrite

    def ReadnWrite_File_Sales(self, mode):
        ReadnWrite = open('../../Data/Data_Sale_Commodity.txt', mode, encoding='utf-8')
        return ReadnWrite

    def ReadnWrite_File_Import_Commodity(self, mode):
        ReadnWrite = open('./../../Data/Data_Import Compodity.txt', mode, encoding='utf-8')
        return ReadnWrite

