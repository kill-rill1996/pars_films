import csv


def pars_csv_countries():
    with open('_countries.csv', 'r') as file:
        file_reader = csv.reader(file, delimiter=';')
        all_countries = []
        for row in file_reader:
            all_countries.append(row)
        country_ru = []
        for country in all_countries:
            country_ru.append(country[1])
        return country_ru


