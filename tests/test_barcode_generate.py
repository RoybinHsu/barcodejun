import os
import tempfile
import unittest
from PIL import Image, PngImagePlugin

from barcodejun import BarcodeData, BarcodeType, BarcodeVers, Barcode


class TestBarcodeGenerate(unittest.TestCase):
    barcode: Barcode
    output = os.path.join(tempfile.mkdtemp(), "test.png")

    @classmethod
    def setUpClass(cls) -> None:
        cls.barcode = Barcode()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove(cls.output)
        pass

    def test_generate(self):
        barcode_data = BarcodeData(
            data="[420]77030[94]00136105440331666909",
            barcode=BarcodeType.DATAMATRIX,
            gs1=True,
            scale=4,
            square=True,
            vers=BarcodeVers.SIZE_20_20,
            notext=True,
            direct=True
        )
        barcode_data = barcode_data
        ok, img = self.barcode.generate(data=barcode_data)
        self.assertTrue(ok)
        self.assertTrue(isinstance(img, Image.Image))
        pass

    def test_output(self):
        barcode_data = BarcodeData(
            data="[420]77030[94]00136105440331666909",
            barcode=BarcodeType.DATAMATRIX,
            gs1=True,
            scale=4,
            square=True,
            vers=BarcodeVers.SIZE_20_20,
            notext=True,
            direct=False,
            output=self.output
        )
        self.barcode.generate(data=barcode_data)
        self.assertTrue(os.path.exists(self.output))

    def test(self):
        barcode_data = BarcodeData(
            data="[420]77030[94]00136105440331666909",
            barcode=BarcodeType.DATAMATRIX,
            gs1=True,
            scale=4,
            square=True,
            vers=BarcodeVers.SIZE_20_20,
            notext=True,
            direct=True
        )
        barcode_creator = Barcode()
        barcode_creator.generate(data=barcode_data)
