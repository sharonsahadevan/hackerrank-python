def unique_country(N, countries):
    count = 0
    unique_country = set()
    for country in countries:
        if country not in unique_country:
            unique_country.add(country)
            count += 1
    print(count)


N = int(input())
countries = list(input() for i in range(N))

unique_country(N, countries)
