"""
pytest Testing/study_pytest/ -v
py.test Testing/study_pytest/ -v
py.test Testing/study_pytest/ -k method1 -v
-k <expression> is used to represent the substring to match

"""
import pytest


@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert not x == y, "test failed"


@pytest.mark.set1
def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
