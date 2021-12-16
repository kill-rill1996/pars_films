import json


def connect_serials():
    all_serials = []
    for i in range(1, 14):
        with open(f'serials/serials_info_{i}.json', 'r') as file:
            objects = json.loads(file.read())
        for serial in objects:
            all_serials.append(serial)

    with open('old_jsons/serials_info.json', 'w') as file:
        json.dump(all_serials, file, indent=4, ensure_ascii=False)


def len_test():
    with open('old_jsons/serials_info.json', 'r') as file:
        objects = json.loads(file.read())
    print(len(objects))


# connect_serials()
# len_test()