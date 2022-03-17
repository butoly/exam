class Database:
    def __init__(self):
        self._data: DataFrame

    def setData(self, data: DataFrame):
        self._data = data

    def getData(self):
        return self._data
