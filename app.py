from typing import Dict, List

import json
import os
import datetime

DATA_PATH = "data.json"


def load_data(json_path: str) -> Dict:
    with open(json_path) as f:
        return json.loads(f.read())


def check_weekend(datepoint: str) -> List[bool]:
    """Check if weekend.

    datepoint: yyyy-mm-dd, `2019-01-01`
    """
    year, month, day = (int(x) for x in datepoint.split("-"))
    _day = datetime.date(year, month, day)
    return _day.weekday() in [5, 6]


def cnholiday(datepoint: str) -> bool:
    data = load_data(os.path.join(os.path.dirname(__file__), DATA_PATH))
    if data[datepoint] or check_weekend(datepoint):
        return True
    else:
        return False


if __name__ == "__main__":
    print(cnholiday("2019-10-01"))
