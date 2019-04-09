import unittest
import foo_lib

class Test_foo_lib(unittest.TestCase):

    def test_foo1_general1(selfself):
        self.assertEqual(3, foo_lib.fool(9))

    def test_fool_general2(self):
        self.assertEqual(4, foo_libfool(16))

    def test_foo1_unusual_negative(self):
        self.assertRaises(ValueError, foo_lib.fool, -16)

    def test_foo1_unusual_negative_specific_msg(self):
        with self.assertRaises(ValueError) as err:
            foo_lib.foo1(-16)

        self.assertEqual("cannot square a negative number", str(err.exception))