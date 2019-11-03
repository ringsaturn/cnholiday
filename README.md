# CNHoliday: 查询某天是否放假

数据来源: <http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm>

安装：

```sh
pip install cnholiday
```

用法：

```python
>>> from datetime import datetime
>>>
>>> from cnholiday import CNHoliday
>>>
>>>
>>> cnholiday = CNHoliday()
>>> _day = datetime(2019, 10, 1)
>>> print(cnholiday.check(_day))
True
>>> print(cnholiday.check_shift(_day))
True
>>> print(cnholiday.check_shift(_day, shift=2))
True
>>> print(cnholiday.check_shift(_day, shift=3))
True
```
