import unittest

from src.barcodejun.barcode_data import BarcodeData
from src.barcodejun.barcode_type import BarcodeType


class TestBarcodeData(unittest.TestCase):
    def test_params(self):
        data = BarcodeData(
            data="[420]77030[94]00136105440331666909",
            type=BarcodeType.DATAMATRIX,
            mode_gs1=True,
            scale=2
        )
        self.assertEqual(data.data, "[420]77030[94]00136105440331666909")
        self.assertEqual(data.type, BarcodeType.DATAMATRIX)
        self.assertTrue(data.mode_gs1)
        self.assertEqual(data.scale, 2)
    pass


if __name__ == "__main__":
    unittest.main()
