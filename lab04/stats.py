def parse_record(line:str):
    parse_list = line.split(';')

    if len(parse_list) != 3:
        raise ValueError('Полей не ровно 3')

    if not parse_list[0]:
        raise ValueError('Поле города пустое')

    if not parse_list[-1]:
        raise ValueError('Поле даты пустое')

    try:
        parse_list[1] = float(parse_list[1])
    except ValueError:
        raise ValueError('Температура не является числом')

    return {"City":parse_list[0],"Temperature":parse_list[1],"Date":parse_list[2]}


def read_valid(line_list:list):
    parsed_List = []
    for line in line_list:
        try:
            parsed_dictionary = parse_record(line)
            parsed_List.append(parsed_dictionary)
        except ValueError:
            pass
    return parsed_List


def average_by_city(records: list):
    city_stats = {}

    for record in records:
        city = record.get('City')
        temp = record.get('Temperature')

        if city not in city_stats:
            city_stats[city] = [0.0, 0]

        city_stats[city][0] += temp
        city_stats[city][1] += 1

    average_dct = {}
    for city in city_stats:
        total_temp = city_stats[city][0]
        count = city_stats[city][1]
        average_dct[city] = total_temp / count

    return average_dct


def warmest_city(records: list):
    averages = average_by_city(records)

    max_temp = max(averages.values())

    candidates = [city for city, temp in averages.items() if temp == max_temp]

    return min(candidates)
