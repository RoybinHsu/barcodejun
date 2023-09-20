import unittest

from barcodejun import BarcodeType, BarcodeData, Barcode, BarcodeVers


class TestBarcodeData(unittest.TestCase):
    barcode_data: BarcodeData
    barcode: Barcode
    input_data = "[420]77030[94]00136105440331666909"
    filepath = "/tmp/data_matrix.png"

    @classmethod
    def setUpClass(cls) -> None:
        cls.barcode_data = BarcodeData(
            data=cls.input_data,
            barcode=BarcodeType.CODE128,
            gs1=True,
            output=cls.filepath,
            vers=BarcodeVers.SIZE_20_20,
        )
        cls.barcode = Barcode()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.barcode_data
        pass

    def test_data(self):
        cmd_params = self.barcode.build(self.barcode_data).cmd_params
        self.assertIn("--data=%s" % self.input_data, cmd_params)
        self.assertIn("--barcode=%d" % BarcodeType.CODE128, cmd_params)
        self.assertIn("--gs1", cmd_params)
        self.assertIn("--output=%s" % self.filepath, cmd_params)
        self.assertIn("--vers=%d" % BarcodeVers.SIZE_20_20, cmd_params)

