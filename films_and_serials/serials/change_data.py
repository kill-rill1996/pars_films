import json


def get_objects():
    with open('old_jsons/serials_info_3.json', 'r') as file:
        objects = json.loads(file.read())
    return objects


def load_objects(obj):
    with open('serials_info_4_lower.json', 'w') as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)
    print('Все обекты успешно записаны в базу данных')


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


# def change_duration():
#     objects = get_objects()
#     for film in objects:
#         film_duration = film['duration'].split()
#         minutes = 0
#         if 'ч.' in film_duration and 'мин.' in film_duration:
#             minutes += 60 * int(film_duration[0]) + int(film_duration[2])
#         elif 'ч.' in film_duration:
#             minutes += 60 * int(film_duration[0])
#         elif 'мин.' in film_duration:
#             minutes += int(film_duration[0])
#         film['duration'] = minutes
#     load_objects(objects)


def union_serials():
    union_list = []
    for i in range(1, 14):
        objects = get_objects()
        for serial in objects:
            union_list.append(serial)
    load_objects(union_list)


def change_year_and_ended_serials():
    serials = get_objects()
    serials_with_cleaned_year = []
    for serial in serials:
        if serial['year']:
            status = 0
            if '(Сериал закончился)' in serial['year']:
                status += 1
                clean_year = serial['year'].replace(' (Сериал закончился)', '')
                serial['year'] = clean_year
            serial['end_status'] = status
            split_years = serial['year'].split(' — ')
            if len(split_years) == 1:
                year = split_years[0].split()[0]
                serial['year'] = [year]
            else:
                start_year = split_years[0]
                serial['year'] = [start_year]
                if 'по н.в.' not in split_years[1]:
                    end_year = split_years[1].strip()
                    if end_year != '0000':
                        serial['year'].append(end_year)
        serials_with_cleaned_year.append(serial)
    load_objects(serials_with_cleaned_year)


def add_end_status():
    objects = get_objects('serials_info_2.json')
    objects_with_status = get_objects('serials_info1.json')
    new_serials = []

    for new, old in zip(objects, objects_with_status):
        new['end_status'] = old['end_status']
        new_serials.append(new)
    load_objects(new_serials)

def lower_case_film_title_ru():
    objects = get_objects()
    for film in objects:
        new_title = film['title_ru'].lower()
        film['title_ru'] = new_title
    load_objects(objects)




# print(create_genres_list())
# change_NBSP()
# sort_countries()
# change_duration()
# union_serials()
# change_year_and_ended_serials()
# add_end_status()
lower_case_film_title_ru()