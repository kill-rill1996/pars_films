import json


def get_points_by_year(film_1, film_2, current_film) -> None:
    """Начисляет фильмам очки за года"""
    if film_1['year'] == film_2['year']:
        if current_film['year'] == film_1['year']:
            points = 10
        elif abs(int(current_film['year']) - int(film_1['year'])) == 1:
            points = 15
        elif abs(int(current_film['year']) - int(film_1['year'])) == 2:
            points = 13
        elif abs(int(current_film['year']) - int(film_1['year'])) == 3:
            points = 11
        else:
            points = 0
        FILMS_POINTS[f'{current_film["id"]}'] += points
    else:
        if int(current_film['year']) in [int(film_1['year']), int(film_2['year'])]:
            points = 12
        elif abs(int(current_film['year']) - int(film_1['year'])) == 1 or \
                abs(int(current_film['year']) - int(film_2['year'])) == 1:
            points = 10
        elif abs(int(current_film['year']) - int(film_1['year'])) == 2 or \
                abs(int(current_film['year']) - int(film_2['year'])) == 2:
            points = 8
        else:
            points = 0
        FILMS_POINTS[f'{current_film["id"]}'] += points


# max 10
def get_points_by_duration(film_1, film_2, current_film) -> None:
    """Начисляет фильмам очки за продолжительность"""

    if film_1['duration'] and film_2['duration']:
        time_1 = film_1['duration']
        time_2 = film_2['duration']
    elif film_1['duration'] or film_2['duration']:
        for time in (film_1['duration'], film_2['duration']):
            if time:
                time_1 = time
        time_2 = 105
    else:
        time_1 = 105
        time_2 = 105

    average_duration = (time_1 + time_2) / 2
    points = 10 - abs(current_film['duration'] - average_duration) * 0.2

    if points < 0:
        points = 0
    FILMS_POINTS[f'{current_film["id"]}'] += points


# max 170
def get_points_by_genres(film_1, film_2, current_film) -> None:
    """Начисляет очки в соответствии с жанрами"""

    coinciding = list(set(film_1['genres']) & set(film_2['genres']))
    film1_genres = list(set(film_1['genres']) - set(film_2['genres']))
    film2_genres = list(set(film_2['genres']) - set(film_1['genres']))

    coinciding_count = 0
    film1_count = 0
    film2_count = 0

    if current_film['genres']:
        for genre in current_film['genres']:
            if genre in coinciding:
                coinciding_count += 1
            elif genre in film1_genres:
                film1_count += 1
            elif genre in film2_genres:
                film2_count += 1

        if film2_count and film1_count:
            points = (15 * coinciding_count * 1.5 ** coinciding_count) + \
                                             (7 * film1_count * 1.3 ** film1_count) + \
                                             (7 * film2_count * 1.3 ** film2_count)
        else:
            points = (12 * coinciding_count * 1.5 ** coinciding_count) + \
                                             (5 * film1_count * 1.2 ** film1_count) + \
                                             (5 * film2_count * 1.2 ** film2_count)
        if points > 170:
            points = 170
        FILMS_POINTS[f'{current_film["id"]}'] += points


# max 50
def get_points_by_country(film_1, film_2, current_film) -> None:
    """Начисляет фильмам очки за страну"""
    coinciding_countries = list(set(film_1['countries']) & set(film_2['countries']))
    film1_countries = list(set(film_1['countries']) - set(film_2['countries']))
    film2_countries = list(set(film_2['countries']) - set(film_1['countries']))

    coinciding_count = 0
    film1_count = 0
    film2_count = 0

    if current_film['countries']:
        for country in current_film['countries']:
            if country in coinciding_countries:
                coinciding_count += 1
            elif country in film1_countries:
                film1_count += 1
            elif country in film2_countries:
                film2_count += 1

        if film2_count and film1_count:
            points = (12 * coinciding_count * 1.5 ** coinciding_count) + \
                                             (7 * film1_count * 1.3 ** film1_count) + \
                                             (7 * film2_count * 1.3 ** film2_count)
        else:
            points = (12 * coinciding_count * 1.5 ** coinciding_count) + \
                                         (5 * film1_count * 1.2 ** film1_count) + \
                                         (5 * film2_count * 1.2 ** film2_count)
        if points > 50:
            points = 50
        FILMS_POINTS[f'{current_film["id"]}'] += points


# max 100
def get_points_by_directors(film_1, film_2, current_film) -> None:
    """Начисляет очки в соответствии с режиссером"""
    coinciding_directors = list(set(film_1['directors']) & set(film_2['directors']))
    film1_directors = list(set(film_1['directors']) - set(film_2['directors']))
    film2_directors = list(set(film_2['directors']) - set(film_1['directors']))

    coinciding_count = 0
    film1_count = 0
    film2_count = 0

    if current_film['directors']:
        for director in current_film['directors']:
            if director in coinciding_directors:
                coinciding_count += 1
            elif director in film1_directors:
                film1_count += 1
            elif director in film2_directors:
                film2_count += 1

    if film2_count and film1_count:
        points = (25 * coinciding_count * 1.5 ** coinciding_count) + \
                                         (12 * film1_count * 1.3 ** film1_count) + \
                                         (12 * film2_count * 1.3 ** film2_count)
    else:
        points = (25 * coinciding_count * 1.5 ** coinciding_count) + \
                                         (10 * film1_count * 1.2 ** film1_count) + \
                                         (10 * film2_count * 1.2 ** film2_count)
    if points > 150:
        points = 150
    FILMS_POINTS[f'{current_film["id"]}'] += points


# max 100
def get_points_by_actors(film_1, film_2, current_film) -> None:
    """Начисляет очки в соответствии с актерами"""
    coinciding_directors = list(set(film_1['actors']) & set(film_2['actors']))
    film1_directors = list(set(film_1['actors']) - set(film_2['actors']))
    film2_directors = list(set(film_2['actors']) - set(film_1['actors']))

    coinciding_count = 0
    film1_count = 0
    film2_count = 0

    if current_film['actors']:
        for actor in current_film['actors']:
            if actor in coinciding_directors:
                coinciding_count += 1
            elif actor in film1_directors:
                film1_count += 1
            elif actor in film2_directors:
                film2_count += 1

    if film2_count and film1_count:
        points = (10 * coinciding_count * 1.5 ** coinciding_count) + \
                                         (7 * film1_count * 1.3 ** film1_count) + \
                                         (7 * film2_count * 1.3 ** film2_count)

    else:
        points = (10 * coinciding_count * 1.5 ** coinciding_count) + \
                                         (5 * film1_count * 1.2 ** film1_count) + \
                                         (5 * film2_count * 1.2 ** film2_count)
    if points > 100:
        points = 100 + points / 100
    FILMS_POINTS[f'{current_film["id"]}'] += points


def get_objects() -> list:
    """Получает все фильмы"""
    with open('films_info.json', 'r') as file:
        films = json.loads(file.read())
    return films


def create_points_dict(films) -> dict:
    """Создает словарь (key - id фильма, value - кол-во очков)"""
    films_point_dict = {}
    for film in films:
        films_point_dict[f"{film['id']}"] = 0
    return films_point_dict


def get_film_by_id(id) -> dict:
    """Получает фильм по id и удаляет его из списка всех фильмов"""
    for film in FILMS:
        if film['id'] == id:
            return FILMS.pop(FILMS.index(film))
        

def get_top_ten_films(films) -> list:
    """Возвращает лист из 10 кортежей (id: points)"""
    top_ten_list = []
    count = 0
    for k in sorted(films, key=films.get, reverse=True):
        if count == 10:
            break
        top_ten_list.append((k, films[f'{k}']))
        count += 1
    return top_ten_list


def show_top_films(films):
    top_ten = get_top_ten_films(FILMS_POINTS)
    top_films_list = []
    for film in films:
        for film_id, _ in top_ten:
            if film['id'] == int(film_id):
                top_films_list.append(film)
    return top_films_list


def main(id_1, id_2):

    # get searched films
    film_1 = get_film_by_id(id_1)
    film_2 = get_film_by_id(id_2)

    # get points
    for current_film in FILMS:
        get_points_by_year(film_1, film_2, current_film)
        get_points_by_duration(film_1, film_2, current_film)
        get_points_by_genres(film_1, film_2, current_film)
        get_points_by_country(film_1, film_2, current_film)
        get_points_by_directors(film_1, film_2, current_film)
        get_points_by_actors(film_1, film_2, current_film)

    # get top films
    top_films = show_top_films(FILMS)
    print(get_top_ten_films(FILMS_POINTS))
    print('_____________________________________')
    for film in top_films:
        print(film['id'], film['title_ru'], film['year'], film['genres'], film['countries'],
              film['directors'], film['actors'])


if __name__ == '__main__':
    FILMS = get_objects()
    FILMS_POINTS = create_points_dict(FILMS)

    main(28, 51)
