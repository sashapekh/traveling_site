# coding=utf-8
__author__ = 'sashapekh'


dict = {
    'date' : [],
    'time' : [],
    'text' : []
}


def result():
    dict = {
        'date':[],
        'time':[],
        'text':[],
        'error':'Файл не найдено'
    }
    res_dict = None
    try:
        file = open('text.txt','rb')
        with file as f:
            for line in f:
                dict['date'].append(line[0:8])
                dict['time'].append(line[10 :16])
                dict['text'].append(line[19:])
            # не забудь удалить последние елементы массива
        res_dict = dict
        file.close()
        return res_dict
    except IOError as e:
        return dict['error']
