import json


def get_objects():
    with open('serials_info_4_lower.json', 'r') as file:
        objects = json.loads(file.read())
    return objects[:50]


def change_year_and_ended_serials():
    serials = get_objects()
    clean_years = []
    for serial in serials:
        if serial['year']:
            if '(Сериал закончился)' in serial['year']:
                serial['year'] = serial['year'].replace(' (Сериал закончился)', '')
                serial_years_splited = serial['year'].split(' — ')
                print(serial_years_splited)
                if len(serial_years_splited) == 1:
                    year_start = serial_years_splited[0]
                    year_end = serial_years_splited[0]
                else:
                    year_start = serial_years_splited[0]
                    year_end = serial_years_splited[1]
                clean_years.append((year_start, year_end))

            if 'по н.в.' in serial['year']:
                serial['year'] = serial['year'].replace('по н.в.', '')
                serial_years_splited = serial['year'].split(' — ')
                year_start = serial_years_splited[0]
                clean_years.append((year_start, ))
    return clean_years
