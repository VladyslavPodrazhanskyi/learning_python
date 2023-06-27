ranges = [
              {
                "minTerm": None,
                "maxTerm": None,
                "minEFA": None,
                "maxEFA": None,
                "rate": 0.05,
                "flatProfit": None
              },
              {
                "minTerm": None,
                "maxTerm": None,
                "minEFA": None,
                "maxEFA": None,
                "rate": 0.04,
                "flatProfit": None
              },
              {
                "minTerm": None,
                "maxTerm": None,
                "minEFA": None,
                "maxEFA": None,
                "rate": 0.03,
                "flatProfit": None
              },
              {
                "minTerm": None,
                "maxTerm": None,
                "minEFA": None,
                "maxEFA": None,
                "rate": 0.02,
                "flatProfit": None
              },
              {
                "minTerm": None,
                "maxTerm": None,
                "minEFA": None,
                "maxEFA": None,
                "rate": 0.02,
                "flatProfit": None
              }
            ]

tier_in_flat_program: bool = any(r for r in ranges if 'tier' in r)

print([r for r in ranges if 'tier' in r])

tier = ''

if tier is None:
    print(True)
else:
    print(False)