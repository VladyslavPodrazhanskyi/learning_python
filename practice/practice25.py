from unittest.mock import Mock

def side_effect_func(v):
    if v < 0:
        return 1
    return 2

def funct(a):
    return a + 1


funct = Mock(side_effect = side_effect_func)


print(funct(-6))