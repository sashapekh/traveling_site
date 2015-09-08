
# coding=utf-8

# формат записи в файл "21.12.12 / 12:00 / событие"


def date_arr_create():
    try:
        file = open('text.txt', 'r')
        date_arr = []
        with file as f:
            for line in f:
                date_arr.append(str(line[0:8]))
        del date_arr[-1]
        file.close()
        return date_arr
    except IOError as e:
        not_exist_file = 'Файл не найдено , нельзя считать дату'
        return not_exist_file


def time_arr_create():
    try:
        file = open('text.txt', 'r')
        time_arr = []
        with file as f:
            for line in f:
                time_arr.append(str(line[12:16]))
        del time_arr[-1]
        file.close()
        return time_arr
    except IOError as e:
        not_exist_file = 'файл не найдено , нельзя считать время'
        return not_exist_file


def string_arr_create():
    try:
        file = open('text.txt', 'r')
        string_arr = []
        with file as f:
            for line in f:
                string_arr.append(line[19:])
        del string_arr[-1]
        file.close()
        return string_arr
    except IOError as e:
        not_exist_file = 'файл не найдено , нельзя считать информацию'
        return not_exist_file


# print(date_arr_create())
# print(time_arr_create())
# print(string_arr_create())

