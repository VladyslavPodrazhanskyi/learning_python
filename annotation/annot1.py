from typing import List, Optional

result: List[int] = []
value: Optional[float] = None

Number = int
Numbers = List[int]


def total(data: Numbers) -> Number:
    return sum(data)
