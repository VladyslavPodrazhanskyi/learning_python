def city_function(city, country, population=""):
    if population:
        return city + ", " + country + " - population " + str(population) + "."
    else:
        return city + ", " + country


print(city_function('Kharkiv', 'Ukraine', 1500000))