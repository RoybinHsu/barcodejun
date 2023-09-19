import unittest

from barcodejun import BarcodeType, BarcodeData, Barcode


class TestBarcodeData(unittest.TestCase):
    def test_params(self):
        input_data = "[420]77030[94]00136105440331666909"
        input_data = 123
        barcode_data = BarcodeData(
            data=input_data,
        )
        print(dir(barcode_data), "asfasfdasdfasdfasf")
        # data = barcode_data.build_params()
        # print(data)
        # self.assertIn("--data=" + str(input_data), data)

        # self.assertEqual(data.data, "[420]77030[94]00136105440331666909")
        # self.assertEqual(data.barcode, BarcodeType.DATAMATRIX)
        # self.assertTrue(data.mode_gs1)
        # self.assertEqual(data.scale, 2)

    pass


# class TestBarcodeGenerate(unittest.TestCase):
#     def test_cmd(self):
#         data = BarcodeData(
#             b=BarcodeType.DATAMATRIX,
#             scale=2
#         )
#         barcode = Barcode(data=data)
#         barcode.generate()


if __name__ == "__main__":
    unittest.main()
