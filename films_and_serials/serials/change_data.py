import json


def get_objects():
    with open('serials_info.json', 'r') as file:
        objects = json.loads(file.read())
    return objects


def load_objects(obj):
    with open('serials_info.json', 'w') as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)


# def change_NBSP(): # \xa0
#     objects = get_objects()
#     for film in objects:
#         for country in film['countries']:
#             country.replace('\xa0', ' ')
#     load_objects(objects)


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


def union_serials():
    union_list = []
    for i in range(1, 14):
        objects = get_objects()
        for serial in objects:
            union_list.append(serial)
    load_objects(union_list)


def change_year_and_ended_serials():
    serials = get_objects()
    for serial in serials:
        if serial['year']:
            new_year = []
            status = 0
            if '(Сериал закончился)' in serial['year']:
                status += 1
                split_year = serial['year'].split()
                years = split_year[:-2]
                print(years)





# print(create_genres_list())
# change_NBSP()
# sort_countries()
# change_duration()
# union_serials()
# change_year_and_ended_serials()