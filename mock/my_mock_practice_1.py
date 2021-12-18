import time
from unittest.mock import Mock

def sleep_calc(*args):
    time.sleep(4)
    return sum(args)


if __name__ == '__main__':
    time = Mock()
    time.sleep.return_value = None
    print(sleep_calc(1, 2, 3))