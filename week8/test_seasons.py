from datetime import date
from seasons import get_minutes
import pytest

def test_get_minutes_one_year():
    # 测试相隔一年的平年，天数为 365 天
    # 365 * 24 * 60 = 525,600 分钟
    birth = date(1999, 1, 1)
    today = date(2000, 1, 1)
    assert get_minutes(birth, today) == "Five hundred twenty-five thousand, six hundred minutes"

def test_get_minutes_two_years_leap():
    # 测试相隔两年并包含一个闰年 (2000年是闰年)，天数为 365 + 366 = 731 天
    # 731 * 24 * 60 = 1,052,640 分钟
    birth = date(1999, 1, 1)
    today = date(2001, 1, 1)
    assert get_minutes(birth, today) == "One million, fifty-two thousand, six hundred forty minutes"