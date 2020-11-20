class Commodity:
    def __init__(self, CID, CName, CQuantily, CUnit, CPrice):
        self.CID = CID
        self.CName = CName
        self.CQuantily = CQuantily
        self.CPrice = CPrice
        self.CUnit = CUnit

    def getCUnit(self):
        return self.CUnit

    def getCID(self):
        return self.CID

    def setCID(self, CID):
        self.CID = CID

    def getCName(self):
        return self.CName

    def setCName(self, CName):
        self.CName = CName

    def getCQuantily(self):
        return self.CQuantily

    def setCQuantily(self, CQuantily):
        self.CQuantily = CQuantily

    def getCPrice(self):
        return self.CPrice

    def setCPrice(self, CPrice):
        self.CPrice = CPrice
