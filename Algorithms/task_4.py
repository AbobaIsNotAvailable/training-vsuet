import json


def write_to_file():

    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]

    with open("GrebenshikovPavel_ZIT-2022_vvod.json", "utf-8", "w") as fw:
        json.dump(matrix, fw)



def read_from_file():

    with open("GrebenshikovPavel_ZIT-2022_vivod.json", "utf-8", "r") as rf:
        data = json.load(rf)
        print(data)