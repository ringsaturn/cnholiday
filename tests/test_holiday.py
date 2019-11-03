import unittest
from datetime import datetime

from cnholiday import CNHoliday


class testHolidayCase(unittest.TestCase):
    def test_one(self):
        cnholiday = CNHoliday()
        _day = datetime(2019, 10, 1)
        print(cnholiday.check(_day))
        self.assertEqual(cnholiday.check(_day), True)

    def test_two(self):
        cnholiday = CNHoliday()
        _day = datetime(2019, 10, 1)
        self.assertEqual(cnholiday.check_shift(_day, -1), False)
