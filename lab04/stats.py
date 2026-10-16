def parse_record(line: str):
    parse_list = line.split(';')

    if len(parse_list) != 3:
        raise ValueError('Полей не ровно 3')

    if not parse_list[0]:
        raise ValueError('Поле города пустое')

    if not parse_list[-1]:
        raise ValueError('Поле даты пустое')

    try:
        parse_list[1] = float(parse_list[1].replace(',','.'))
    except ValueError:
        raise ValueError('Температура не является числом')

    return {"city": parse_list[0], "temperature": parse_list[1], "date": parse_list[2]}


def read_valid(line_list: list):
    parsed_list = []
    for line in line_list:
        if not line.strip():
            continue
        try:
            parsed_dictionary = parse_record(line)
            parsed_list.append(parsed_dictionary)
        except ValueError:
            pass
    return parsed_list


def average_by_city(records: list):
    city_stats = {}
    for record in records:
        city = record.get('Город')
        temp = record.get('Температура')
        if city is None or temp is None:
            continue
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
    if not averages:
        pass
    else:
        max_temp = max(averages.values())
        candidates = [city for city, temp in averages.items() if temp == max_temp]
        return min(candidates)
