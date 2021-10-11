companies = ['Epam', 'Amazon', 'Google']
comp_iter = iter(companies)

while True:
    try:
        company = next(comp_iter)
    except StopIteration:
        break
    else:
        print(company)