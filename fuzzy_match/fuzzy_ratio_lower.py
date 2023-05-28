from typing import List, Tuple
from fuzzywuzzy.fuzz import ratio, partial_ratio, token_sort_ratio, token_set_ratio
from fuzzywuzzy.process import extractBests, extractOne


def best_match(dt_trim: str, st_trims: List[str]) -> Tuple[str, List[Tuple[str, int]]]:
    return (dt_trim, sorted(
        [
            (st_trim, token_set_ratio(dt_trim.lower(), st_trim.lower()))
            for st_trim in st_trims
        ],
        key=lambda a: a[1],
        reverse=True
    ))


if __name__ == '__main__':

    # vin_num=2T3WFREV8JW513611
    print(best_match(
        "Adventure FWD (Natl)",
        ["Adventure", "XLE"]
    ))  # ('Adventure FWD (Natl)', [('Adventure', 100), ('XLE', 33)])

    print(best_match(
        "XLE FWD (GS)",
        ["Adventure", "XLE"]
    ))  # ('XLE FWD (GS)', [('XLE', 100), ('Adventure', 11)])

    # vin_num=4T1B11HK0JU582088
    print(best_match(
        "L Auto (Natl)",
        ["XLE", 'L', 'LE']
    ))  # ('L Auto (Natl)', [('L', 100), ('LE', 50), ('XLE', 33)])

    # !!!  vin_num = ML32AUHJ8MH002762
    print(best_match(
        "FWD 4dr Limited",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # ('FWD 4dr Limited', [('Carbonite Edition', 31), ('LE', 24), ('ES', 12)])

    # vin_num = ML32AUHJ8MH002762
    print(best_match(
        "ES 2.0 CVT",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # ('ES 2.0 CVT', [('ES', 100), ('Carbonite Edition', 30), ('LE', 17)])

    # vin_num = ML32AUHJ8MH002762
    print(best_match(
        "Carbonite Edition CVT",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # ('Carbonite Edition CVT', [('Carbonite Edition', 100), ('LE', 9), ('ES', 9)])

    # !!!! vin_num = 1C6RR7LT3ES144771
    print(best_match(
        '4WD Crew Cab 140.5" Big Horn',
        [
            '"4WD Crew Cab 140.5" Big Horn',
            "Lone Star", "Big Horn", "Outdoorsman"
        ]
    ))  # ('4WD Crew Cab 140.5" Big Horn', [('"4WD Crew Cab 140.5" Big Horn', 100), ('Big Horn', 100), ('Outdoorsman', 21), ('Lone Star', 17)])

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
    ))  # ('Venture 4WD (Natl)', [('Venture', 100), ('TRD Off-Road', 36), ('TRD Off-Road Premium', 28), ('Limited', 26), ('TRD Pro', 26), ('Nightshade', 23), ('SR5 Premium', 22), ('SR5', 11)])


    # ML32AUHJ8MH008674
    print(best_match(
        '+ Auto, AWD 4dr, LE CVT',
        ['ES', 'LE', 'Carbonite Edition']
    ))  # ('+ Auto, AWD 4dr, LE CVT', [('LE', 100), ('Carbonite Edition', 28), ('ES', 10)])

    print(best_match(
        'Carbonite Edition CVT, 1.4T SE Auto',
        ['ES', 'LE', 'Carbonite Edition']
    ))  # ('Carbonite Edition CVT, 1.4T SE Auto', [('Carbonite Edition', 100), ('ES', 11), ('LE', 6)])

    print(best_match(
        'ES CVT',
        ['ES', 'LE', 'Carbonite Edition']
    ))  # ('ES CVT', [('ES', 100), ('Carbonite Edition', 35), ('LE', 25)])

    # JA4AD3A36KZ028834
    print(best_match(
        'SEL FWD',
        ['SE', 'LE', 'SEL']
    ))  # ('SEL FWD', [('SEL', 100), ('SE', 44), ('LE', 22)])

    # ML32A5HJ9LH009773
    print(best_match(
        'GT CVT',
        ['GT', 'LE']
    ))  # ('GT CVT', [('GT', 100), ('LE', 0)])

    ################################################
    # special matching cases

    # ML32A5HJ9LH009773
    print(best_match(
        '5dr Wgn CVT S FWD',
        ['GT', 'LE']
    ))  # ('5dr Wgn CVT S FWD', [('GT', 11), ('LE', 0)])

    # !!!  vin_num = ML32AUHJ8MH002762
    print(best_match(
        "FWD 4dr Limited",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # ('FWD 4dr Limited', [('Carbonite Edition', 31), ('LE', 24), ('ES', 12)])

    # !!!! vin_num = JTEBU5JR7L5806847
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
    ))  # ('UTILITY 4D TRD ', [('TRD Pro', 60), ('TRD Off-Road', 40), ('TRD Off-Road Premium', 35), ('Limited', 29), ('Venture', 19), ('Nightshade', 17), ('SR5 Premium', 16), ('SR5', 12)])

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
    ))  # ('OFF-ROAD 4WD V6', [('TRD Off-Road', 80), ('TRD Off-Road Premium', 70), ('TRD Pro', 36), ('Nightshade', 16), ('SR5 Premium', 15), ('SR5', 11), ('Limited', 9), ('Venture', 9)])

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
    ))  # ('OFF-ROAD 4WD V6', [('TRD Off-Road', 80), ('TRD Off-Road Premium', 70), ('TRD Pro', 36), ('Nightshade', 16), ('SR5 Premium', 15), ('SR5', 11), ('Limited', 9), ('Venture', 9)])

    # !!!! vin_num = 1C4AJWAG9JL816494
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
    ))  # ('Utility 2D Sport 4WD 3.6L V6', [('Sport', 100), ('Sport S', 83), ('Sport Willys Wheeler W Edition', 52), ('Sport Willys Wheeler Edition', 50), ('Sport Golden Eagle Edition', 41), ('Sport Freedom Edition', 41)])

    # !!!!!
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
    ))  # ('Sport 4x4', [('Sport', 100), ('Sport S', 83), ('Sport Willys Wheeler W Edition', 71), ('Sport Golden Eagle Edition', 71), ('Sport Willys Wheeler Edition', 71), ('Sport Freedom Edition', 71)])