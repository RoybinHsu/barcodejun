from __future__ import annotations

import io
import subprocess
from typing import Any
from PIL import Image

from barcodejun.data import BarcodeData


class Barcode(object):
    __cmd_params: list[Any]
    __cmd_binary = "zint"
    __field_short_map = {
        "d": "data",
        "o": "output",
        "i": "input",
        "b": "barcode",
        "w": "whitesp",
        "e": "ecinos",
        "r": "reverse",
        "t": "types",
    }

    @classmethod
    def __filter_fields(cls, input_params: dict):
        """
        参数缩写和飞缩写同时存在优先取缩写
        :param input_params:
        :return:
        """
        input_fields = input_params.keys()
        for k, v in input_params.items():
            if k in input_fields and v in input_fields:
                input_params.pop(v)
        return input_params

    def build(self, data: BarcodeData) -> Barcode:
        """
        :returns:  `barcodejun.Barcode`
        """
        kwargs = data.__dict__
        input_fields = self.__filter_fields(kwargs)
        params = []
        for attr in kwargs.keys():
            value = kwargs.get(attr)
            if type(value) in (bool,) and input_fields.get(attr):
                params += ["--%s" % attr]
                pass
            elif type(value) in (str, int, float) and input_fields.get(attr) is not None:
                if type(value) in (str,):
                    params += ["--%s=%s" % (attr, str(input_fields.get(attr)))]
                else:
                    params += ["--%s=%s" % (attr, str(input_fields.get(attr)))]
        self.__cmd_params = params
        return self

    @property
    def cmd_params(self):
        return self.__cmd_params

    def set_cmd_binary(self, binary_path="zint"):
        self.__cmd_binary = binary_path
        return self

    def get_cmd_binary(self):
        return self.__cmd_binary

    def generate(self, data: BarcodeData) -> Any:
        """
        :exception Exception
        :returns: An :py:class:`~PIL.Image.Image` object.
        """
        self.build(data=data)
        binary = self.get_cmd_binary()
        cmd = [binary] + self.__cmd_params
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            raise Exception(stderr)
        else:
            if type(stdout) is bytes and len(stdout) > 0:
                buff = io.BytesIO(stdout)
                img = Image.open(buff)
                return True, img
            else:
                return True, stdout
