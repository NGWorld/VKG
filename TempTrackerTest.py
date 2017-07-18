__author__ = 'VK Gupta'

import unittest
from TempTracker import TempTracker

class TestTempTracker(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.tracker = TempTracker([15,55,60,77])
    def test_insert(self):
        self.tracker.insert(99)
        self.assertIn(99,self.tracker.data)
    def test_get_min(self):
        self.assertEqual(15,self.tracker.get_min())
    def test_get_max(self):
        self.assertEqual(77,self.tracker.get_max())
    def test_get_mean(self):
        self.assertEqual(type(0.1),type(self.tracker.get_mean()))
    def test_formatValue(self):
        self.assertTrue(self.tracker.formatValue(10).endswith('F'))

if __name__ == '__main__':
    unittest.main()