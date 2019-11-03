"""If the day is China holiday?
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict

DATA_PATH = "data.json"


def load_data(json_path: str) -> Dict:
    with open(json_path) as f:
        return json.loads(f.read())


class CNHoliday:
    data = load_data(os.path.join(os.path.dirname(__file__), DATA_PATH))

    def _check_data(self, datepoint: datetime) -> bool:
        """Lookup JSON.
        """
        _year = str(datepoint.year)
        if _year in self.data:
            _year_dict = self.data[_year]
            if datepoint.__format__("%Y-%m-%d") in _year_dict:
                return _year_dict[datepoint.__format__("%Y-%m-%d")]["holiday"]

    def _check_cal(self, datepoint: datetime) -> bool:
        """Lookup Calendar.
        """
        if datepoint.weekday() in [5, 6]:
            return True
        else:
            return False

    def check(self, datepoint: datetime) -> bool:
        """Call self.func and return True/False.
        """
        _data_resp = self._check_data(datepoint)
        if _data_resp is not None:
            return _data_resp
        else:
            return self._check_cal(datepoint)

    def check_shift(self, datepoint: datetime, shift: int = 1) -> bool:
        """Shift input date's `day`.
        """
        datepoint = datepoint + timedelta(days=shift)
        return self.check(datepoint)


if __name__ == "__main__":
    cnholiday = CNHoliday()
    _day = datetime(2019, 10, 1)
    print(cnholiday.check(_day))
    print(cnholiday.check_shift(_day))
    print(cnholiday.check_shift(_day, shift=2))
    print(cnholiday.check_shift(_day, shift=3))
