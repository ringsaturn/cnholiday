# CNHoliday: 查询某天是否放假

数据来源:

| 年份 | 出处                                                                                                             |
| :--: | ---------------------------------------------------------------------------------------------------------------- |
| 2019 | [国务院办公厅关于 2019 年部分节假日安排的通知](http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm) |
| 2020 | [国务院办公厅关于 2020 年部分节假日安排的通知](http://www.gov.cn/zhengce/content/2019-11/21/content_5454164.htm) |

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

---

相关项目：

- GitHub 上有另一个同名项目 <https://github.com/valaxy/cnholiday>
