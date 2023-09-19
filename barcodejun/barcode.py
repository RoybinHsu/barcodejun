from barcodejun.data import BarcodeData


class Barcode:
    __data: BarcodeData = None

    def __init__(self, data: BarcodeData = None):
        self.__data = data
        pass

    def generate(self):
        binary = "zint"
        params = self.__data.build_params()
        # print(params)
        cmd = [binary] + params
        # print(cmd, "++++++++++")
        pass

    pass
