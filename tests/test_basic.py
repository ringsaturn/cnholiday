import unittest
from datetime import datetime

from cnholiday import CNHoliday


class testBasicCase(unittest.TestCase):
    def test_one(self):
        cnholiday = CNHoliday()
        _day = datetime(2019, 10, 31)
        self.assertEqual(cnholiday.check(_day), False)

    def test_two(self):
        cnholiday = CNHoliday()
        _day = datetime(2019, 10, 31)
        self.assertEqual(cnholiday.check_shift(_day), False)

    def test_three(self):
        cnholiday = CNHoliday()
        _day = datetime(2019, 10, 31)
        self.assertEqual(cnholiday.check_shift(_day, 2), True)
