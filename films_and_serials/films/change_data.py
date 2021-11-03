import json


def get_objects():
    with open(f'films_info.json', 'r') as file:
        OBJECTS = json.loads(file.read())
    return OBJECTS


def load_objects(obj):
    with open('films_info_5.json', 'w') as file:
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

# print(create_genres_list())
# change_NBSP()
# sort_countries()
# change_duration()