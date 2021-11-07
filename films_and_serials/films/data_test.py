import json
from db_countries import pars_csv_countries

ALL_COUNTRIES = pars_csv_countries()
ALL_GENRES = ['драма', 'эротика', 'боевик', 'мюзикл', 'исторический', 'аниме', 'триллер', 'приключения', 'криминал', 'вестерн', 'мелодрама', 'фэнтези', 'документальный', 'спорт', 'детский', 'музыкальный', 'мультфильмы', 'фантастика', 'военный', 'ужасы', 'комедия', 'биография', 'детектив', 'семейный', 'короткометражный']


def get_ojects():
    with open(f'../serials/serials_info1.json', 'r') as file:
        OBJECTS = json.loads(file.read())
    return OBJECTS


def test_countries():
    incorrect_films_country = []
    for film in get_ojects():
        for country in film['countries']:
            if country not in ALL_COUNTRIES:
                incorrect_films_country.append(film['id'])
    print(f'Films with incorrect country name: {incorrect_films_country} \n Count of mistakes: {len(incorrect_films_country)}')


def test_year():
    incorrect_years = []
    for film in get_ojects():
        try:
            year = int(film['year'][:4])
            if year < 1800 or year > 2021 or len(film['year']) > 4:
                raise Exception
        except Exception as e:
            incorrect_years.append(film['id'])
    print(f'Films with incorrect years: {incorrect_years}')


def test_year_in_serials():
    incorrect_years = []
    for film in get_ojects():
        try:
            if film['year']:
                if len(film['year']) == 1:
                    year = int(film['year'][0])
                    if year < 1800 or year > 2021:
                        raise Exception
                elif len(film['year']) == 2:
                    start_year = int(film['year'][0])
                    end_year = int(film['year'][1])
                    if start_year < 1800 or start_year > 2021 or end_year < 1800 or end_year > 2021:
                        raise Exception
                elif len(film['year']) > 2:
                    incorrect_years.append(film['id'])
        except Exception:
            incorrect_years.append(film['id'])

    print(f'Films with incorrect years: {incorrect_years}')


def test_duration():
    incorrect_films = []
    for film in get_ojects():
        try:
            if film['duration']:
                film['duration'] += 1
        except Exception:
            incorrect_films.append(film['id'])
    print(f'Films with incorrect duration time ({len(incorrect_films)} errors): {incorrect_films}')


def test_genre():
    films_with_error = []
    for film in get_ojects():
        for genre in film['genres']:
            if genre not in ALL_GENRES:
                films_with_error.append(film['id'])
    print(f'Films with incorrect years: {films_with_error}')


def test_directors():
    films = get_ojects()
    id = []
    for film in films:
        if len(film['directors']) > 1:
            id.append(film['id'])
    print(id)
    print(len(id))


def test_length_directors():
    films = get_ojects()
    l1 = 0
    l2 = 0
    l3 = 0
    l4 = 0
    l5 = 0
    for film in films:
        if len(film['directors']) == 1:
            l1 += 1
        elif len(film['directors']) == 2:
            l2 += 1
        elif len(film['directors']) == 3:
            l3 += 1
        elif len(film['directors']) == 4:
            l4 += 1
        elif len(film['directors']) == 5:
            l5 += 1
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


if __name__ == '__main__':
    # test_countries() # Не получается убрать [BSCP]
    # test_year() # Три фильма с поздним годом (нужно проверить 21758, 48006, 48190)
    # test_duration() # Прошел
    # test_genre() # Прошел
    # test_directors()
    # test_length_directors()
    test_year_in_serials()
    # print('Нет тестов')
