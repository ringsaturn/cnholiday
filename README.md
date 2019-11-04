# CNHoliday: 查询某天是否放假

数据来源: 2019: <http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm>


安装：

```sh
# 不依赖第三方包库
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

*****

相关项目：

- GitHub 上有另一个同名项目 <https://github.com/valaxy/cnholiday>
