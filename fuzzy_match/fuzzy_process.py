from typing import List, Tuple
from fuzzywuzzy import fuzz, process


if __name__ == '__main__':

    # vin_num=2T3WFREV8JW513611
    print(process.extractBests(
        "Adventure FWD (Natl)",
        ["Adventure", "XLE"]
    ))  # [('Adventure', 90), ('XLE', 30)]

    print(process.extractBests(
        "XLE FWD (GS)",
        ["Adventure", "XLE"]
    ))  # [('XLE', 90), ('Adventure', 20)]

    # vin_num=4T1B11HK0JU582088
    print(process.extractBests(
        "L Auto (Natl)",
        ["XLE", 'L', 'LE']
    ))  # [('L', 60), ('LE', 45), ('XLE', 36)]

    # vin_num = ML32AUHJ8MH002762
    print(process.extractBests(
        "FWD 4dr Limited",
        ["LE", 'ES', 'Carbonite Edition']
    ))  # [('LE', 45), ('ES', 45), ('Carbonite Edition', 31)]



    # print(process.extractBests(
    #     "XLE FWD (GS)",
    #     ["Adventure", "XLE"]
    # ))  # XLE
    #
    # print(process.extractBests(
    #     "L Auto (Natl)",
    #     ["XLE", 'L', 'LE']
    # ))  # XLE
    #
    # print(process.extractBests(
    #     "FWD 4dr Limited",
    #     ["LE", 'ES', 'Carbonite Edition']
    # ))  # Carbonite Edition
    #
    # print(process.extractBests(
    #     "ES 2.0 CVT",
    #     ["LE", 'ES', 'Carbonite Edition']
    # ))  # ES
    #
    # print(process.extractBests(
    #     "Carbonite Edition CVT",
    #     ["LE", 'ES', 'Carbonite Edition']
    # ))  # Carbonite Edition
    #
    # print(process.extractBests(
    #     '"4WD Crew Cab 140.5" Big Horn',
    #     [
    #         '"4WD Crew Cab 140.5" Big Horn',
    #         "Lone Star", "Big Horn", "Outdoorsman"
    #     ]
    # ))  # "4WD Crew Cab 140.5" Big Horn
    #
    # print(process.extractBests(
    #     'UTILITY 4D TRD ',
    #     [
    #         'Nightshade',
    #         "TRD Off-Road",
    #         "Limited",
    #         "SR5",
    #         "SR5 Premium",
    #         "Venture",
    #         "TRD Pro",
    #         'TRD Off-Road Premium'
    #     ]
    # ))  # TRD Pro
    #
    # print(process.extractBests(
    #     'OFF-ROAD 4WD V6',
    #     [
    #         'Nightshade',
    #         "TRD Off-Road",
    #         "Limited",
    #         "SR5",
    #         "SR5 Premium",
    #         "Venture",
    #         "TRD Pro",
    #         'TRD Off-Road Premium'
    #     ]
    # ))  # TRD Pro
    #
    # print(process.extractBests(
    #     'Venture 4WD (Natl)',
    #     [
    #         'Nightshade',
    #         "TRD Off-Road",
    #         "Limited",
    #         "SR5",
    #         "SR5 Premium",
    #         "Venture",
    #         "TRD Pro",
    #         'TRD Off-Road Premium'
    #     ]
    # ))   # Venture
    #
    # print(process.extractBests(
    #     'Utility 2D Sport 4WD 3.6L V6',
    #     [
    #         'Sport Willys Wheeler W Edition',
    #         "Sport Golden Eagle Edition",
    #         "Sport",
    #         "Sport Willys Wheeler Edition",
    #         "Sport S",
    #         "Sport Freedom Edition",
    #     ]
    # ))  # Sport S
    #
    # print(process.extractBests(
    #     'Sport 4x4',
    #     [
    #         'Sport Willys Wheeler W Edition',
    #         "Sport Golden Eagle Edition",
    #         "Sport",
    #         "Sport Willys Wheeler Edition",
    #         "Sport S",
    #         "Sport Freedom Edition",
    #     ]
    # ))  # Sport S


