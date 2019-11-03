# CNHoliday: 查询某天是否放假

数据来源: <http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm>

用法：

```python
from cnholiday import CNHoliday


cnholiday = CNHoliday()
_day = datetime(2019, 10, 1)
print(cnholiday.check(_day))
print(cnholiday.check_shift(_day))
print(cnholiday.check_shift(_day, shift=2))
print(cnholiday.check_shift(_day, shift=3))
```
