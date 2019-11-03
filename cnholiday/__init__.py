"""If CN holiday?
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

    def check(self, datepoint: datetime) -> bool:
        if str(datepoint) in self.data and self.data[str(datepoint)]:
            # if in json file and true
            return True
        elif str(datepoint) in self.data and not self.data[str(datepoint)]:
            # if in json file and false
            return False
        elif datepoint.weekday() in [5, 6]:
            return True
        else:
            return False

    def check_shift(self, datepoint: datetime, shift: int = 1) -> bool:
        datepoint = datepoint + timedelta(days=shift)
        return self.check(datepoint)


if __name__ == "__main__":
    cnholiday = CNHoliday()
    _day = datetime(2019, 10, 31)
    print(cnholiday.check(_day))
    print(cnholiday.check_shift(_day))
    print(cnholiday.check_shift(_day, shift=2))
    print(cnholiday.check_shift(_day, shift=3))
