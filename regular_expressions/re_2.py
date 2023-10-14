"""
https://realpython.com/regex-python/
"""

import re
from typing import Optional


def extract_tier(programId: str) -> Optional[str]:
    pattern = r'tier\s*(\d+)'
    match = re.search(pattern, programId.lower())
    if match:
        number = match.group(1)
        return number
    else:
        return None


# Example usage:
string = " t 1243  sds239837 This is a Tier  4 tier 555 6 example"
number = extract_tier(string)
if number is not None:
    print(number)
else:
    print("Number not found")
