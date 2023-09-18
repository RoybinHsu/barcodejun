from src.barcodejun.barcode import BarcodeFileType, BarcodeSymbolSize


class BarcodeData:
    # 编码的数据
    data: str = ""
    # BarcodeType属性
    type: int = 0
    # 是否使用gs1mode 如果使用gs1mode data 格式为： [420]12345[94]001234489798778
    mode_gs1: bool = False
    # barcode大小
    scale: int = 2
    # 正方形
    square: bool = False
    # symbol size
    symbol_size: int = BarcodeSymbolSize.SIZE_20_20
    # no text 是否展示编码字符
    no_text: bool = True
    # filetype
    file_type: str = BarcodeFileType.TYPE_PNG

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def build_params(self):
        params = []
        if self.data != "":
            params.append(["-d", self.data])
        if self.type > 0:
            params.append(["-b", "%d" % self.type])
        if self.mode_gs1:
            params.append("--gs1")
        if self.scale > 0:
            params.append(["--scale", "%d" % self.scale])
        if self.square:
            params.append("--square")
        if self.symbol_size > 0:
            params.append(["--vers", "%d" % self.symbol_size])
        if self.no_text:
            params.append(["--notext"])
        if self.file_type != "":
            params.append(["--filetype", self.file_type])
        return params

    pass
