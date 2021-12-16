import json

NSBP_LIST = [7528, 9146, 9457, 11186, 12723, 12789, 14791, 18507, 19299, 20189, 20234, 20312, 20867, 21239, 23228, 23443, 23774, 23783, 23890, 24046, 24090, 24603, 24857, 25302, 25384, 27341, 27518, 27564, 27593, 27651, 27825, 27985, 28184, 28193, 28193, 28943, 29009, 29011, 29924, 30037, 30541, 30703, 31996, 33897, 33996, 34384, 39103, 39572, 41045, 48347, 48632, 48693, 48921, 48943, 48971, 49912, 50560, 52752, 56295, 56868, 58218]


def get_objects():
    with open(f'films_info_10_lower_title.json', 'r') as file:
        OBJECTS = json.loads(file.read())
    return OBJECTS


def load_objects(obj):
    with open('films_info_11_harry_potter.json', 'w') as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)
        print("Json успешно записан")


def change_NBSP(): # \xa0
    objects = get_objects()
    for film in objects:
        for country in film['countries']:
            country.replace('\xa0', ' ')
    load_objects(objects)


def create_genres_list():
    genres_list = []
    objects = get_objects()
    for film in objects:
        for genre in film['genres']:
            genres_list.append(genre)
    return set(genres_list)


def sort_countries():
    objects = get_objects()
    for film in objects:
        film['countries'] = sorted(film['countries'])
    print(objects[:10])
    load_objects(objects)


def change_duration():
    objects = get_objects()
    for film in objects:
        film_duration = film['duration'].split()
        minutes = 0
        if 'ч.' in film_duration and 'мин.' in film_duration:
            minutes += 60 * int(film_duration[0]) + int(film_duration[2])
        elif 'ч.' in film_duration:
            minutes += 60 * int(film_duration[0])
        elif 'мин.' in film_duration:
            minutes += int(film_duration[0])
        film['duration'] = minutes
    load_objects(objects)


def change_null_duration():
    objects = get_objects()
    for film in objects:
        if film['duration'] == 0:
            film['duration'] = 105
    load_objects(objects)


def rename_id_field():
    objects = get_objects()
    count = 1
    for film in objects:
        film['id'] = count
        count += 1
    load_objects(objects)


def split_nsbp():
    objects = get_objects()
    for ob in objects:
        if ob['id'] in NSBP_LIST:
            new_country_list = []
            for country in ob['countries']:
                splitted = country.split()
                joined = ' '.join(splitted)
                new_country_list.append(joined)
            ob['countries'] = new_country_list
    load_objects(objects)


def rename_vatican():
    objects = get_objects()
    for film in objects:
        new_country_list = []
        for country in film['countries']:
            if country == 'Папский Престол (Государство-город Ватикан)':
                country = 'Ватикан'
            new_country_list.append(country)
        film['countries'] = new_country_list
    load_objects(objects)


def lower_case_film_title_ru():
    objects = get_objects()
    for film in objects:
        new_title = film['title_ru'].lower()
        film['title_ru'] = new_title
    load_objects(objects)

def change_harry_pooter():
    objects = get_objects()
    for film in objects:
        if film['id'] == 28:
            film['title_ru'] = film['title_ru'].replace('ii', '2')
        if film['id'] == 30:
            film['title_ru'] = film['title_ru'].replace('i', '1')
    load_objects(objects)

# print(create_genres_list())
# change_NBSP()
# sort_countries()
# change_duration()
# change_null_duration()
# rename_id_field()
# split_nsbp()
# rename_vatican()
# lower_case_film_title_ru()
change_harry_pooter()