import unittest
import importlib as il

mod = getattr(il.import_module('WordsToHex.WordsToHex'), 'HexGenerator')

class TestWordsToHex(unittest.TestCase):

    def test_PreProcess(self):
        actual = mod.preProcess(self,["fhsduaifhsdaiu"])
        expected = False
        self.assertEqual(actual, expected)

    def test_FormatHex(self):
        actual = mod.formatHex(self,"HeLlO")
        expected = "#HELLO"
        self.assertEqual(actual, expected)

    def test_CreateBinaryRepresentation(self):
        actual = mod.createBinaryRepresentation(self,'cassia')
        expected = ['0', '1', '0', '0', '0', '1']
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)