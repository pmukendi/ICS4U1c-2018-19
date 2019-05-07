import unittest
import stringLib

class Test_stringlib(unittest.TestCase):
    def test_strLength_general(self):
        self.assertEquals(4, stringLib.strLength("yeye"))

    def test_strLength_specific(self):
        se;f.assertEquals(9, stringLib.strLength("minecraft"))