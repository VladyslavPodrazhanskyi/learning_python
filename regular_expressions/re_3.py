import re
from typing import Optional


def extract_tier(text: str) -> Optional[str]:
    pattern = r'tier\s*(\w+|\d+)'  # Pattern to match word or number after "tier"
    match = re.search(pattern, text.lower())
    if match:
        tier = match.group(1)
        return tier
    return


if __name__ == '__main__':
    string = "This is a Tier o0j"
    tier = extract_tier(string)
    print(tier)
