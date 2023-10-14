from typing import Union, Optional


def value_to_float(value: Union[str, int, float]) -> Optional[float]:
    try:
        return float(value)
    except ValueError:
        return


if __name__ == '__main__':
    print(value_to_float(5.6))
    print(value_to_float(5))
    print(value_to_float('5.6'))
    print(value_to_float('5'))
    print(value_to_float('sfjhk'))