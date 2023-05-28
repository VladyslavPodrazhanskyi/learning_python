from typing import List, Tuple

from fuzzywuzzy import fuzz, process


def best_match(dt_trim: str, st_trims: List[str]) -> Tuple[str, List[Tuple[str, int]]]:
    return (dt_trim,  sorted(
        [
            (st_trim, fuzz.partial_ratio(dt_trim.lower(), st_trim.lower()))
            for st_trim in st_trims
        ],
        key=lambda a: a[1],
        reverse=True
    ))




if __name__ == '__main__':
    print(best_match(
        "Adventure FWD (Natl)",
        ["Adventure", "XLE"]
    ))  # Adventure

    print(best_match(
        "XLE FWD (GS)",
        ["Adventure", "XLE"]
    ))  # XLE

    print(best_match(
        "L Auto (Natl)",
        ["XLE", 'L', 'LE']
    ))  # XLE

    print(best_match(
        "FWD 4dr Limited",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # Carbonite Edition

    print(best_match(
        "ES 2.0 CVT",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # ES

    print(best_match(
        "Carbonite Edition CVT",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # Carbonite Edition

    print(best_match(
        '"4WD Crew Cab 140.5" Big Horn',
        [
            '"4WD Crew Cab 140.5" Big Horn',
            "Lone Star", "Big Horn", "Outdoorsman"
        ]
    ))  # "4WD Crew Cab 140.5" Big Horn

    print(best_match(
        'UTILITY 4D TRD ',
        [
            'Nightshade',
            "TRD Off-Road",
            "Limited",
            "SR5",
            "SR5 Premium",
            "Venture",
            "TRD Pro",
            'TRD Off-Road Premium'
        ]
    ))  # TRD Pro

    print(best_match(
        'OFF-ROAD 4WD V6',
        [
            'Nightshade',
            "TRD Off-Road",
            "Limited",
            "SR5",
            "SR5 Premium",
            "Venture",
            "TRD Pro",
            'TRD Off-Road Premium'
        ]
    ))  # TRD Pro

    print(best_match(
        'Venture 4WD (Natl)',
        [
            'Nightshade',
            "TRD Off-Road",
            "Limited",
            "SR5",
            "SR5 Premium",
            "Venture",
            "TRD Pro",
            'TRD Off-Road Premium'
        ]
    ))   # Venture

    print(best_match(
        'Utility 2D Sport 4WD 3.6L V6',
        [
            'Sport Willys Wheeler W Edition',
            "Sport Golden Eagle Edition",
            "Sport",
            "Sport Willys Wheeler Edition",
            "Sport S",
            "Sport Freedom Edition",
        ]
    ))  # Sport S

    print(best_match(
        'Sport 4x4',
        [
            'Sport Willys Wheeler W Edition',
            "Sport Golden Eagle Edition",
            "Sport",
            "Sport Willys Wheeler Edition",
            "Sport S",
            "Sport Freedom Edition",
        ]
    ))  # Sport S


