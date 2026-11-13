import json


def csv_to_records(text: str) -> list[dict]:
    """Разбирает CSV с заголовком в список словарей. Значения остаются строками."""
    lines = text.strip().splitlines()
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = line.split(",")
        record = {}
        for h, v in zip(headers, values):
            record[h] = v.strip()
        records.append(record)
    return records


def _parse_value(raw: str):
    """Приводит строку к нужному типу: bool, int, float или оставляет строкой."""
    s = raw.strip()
    low = s.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(s)
    except ValueError:
        pass
    # Поддержка запятой как десятичного разделителя (3,5 → 3.5)
    try:
        return float(s.replace(",", "."))
    except ValueError:
        pass
    return s


def parse_settings(lines: list[str]) -> dict:
    """Простой YAML: «ключ: значение», списки через «- », комментарии после #."""
    result = {}
    i = 0
    while i < len(lines):
        line = lines[i]

        # Убираем комментарий (всё после первого #)
        comment_pos = line.find("#")
        if comment_pos != -1:
            line = line[:comment_pos]
        line = line.rstrip()

        # Пропускаем пустые строки
        if not line.strip():
            i += 1
            continue

        # Ищем первое двоеточие
        colon_pos = line.find(":")
        if colon_pos == -1:
            i += 1
            continue

        key = line[:colon_pos].strip()
        value_part = line[colon_pos + 1:].strip()

        if value_part:
            result[key] = _parse_value(value_part)
            i += 1
        else:
            # Ключ без значения — открывает список
            lst = []
            i += 1
            while i < len(lines):
                sub = lines[i]
                comment_pos = sub.find("#")
                if comment_pos != -1:
                    sub = sub[:comment_pos]
                sub = sub.rstrip()
                sub_stripped = sub.strip()

                if sub_stripped.startswith("- "):
                    lst.append(_parse_value(sub_stripped[2:]))
                    i += 1
                elif sub_stripped == "":
                    i += 1
                else:
                    break
            result[key] = lst

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из словаря по значению ключа key.
    Поля самой записи важнее: при конфликте остаётся значение из записи."""
    result = []
    for row in rows:
        lookup = row.get(key)
        if lookup in extra:
            merged = {**extra[lookup], **row}
            result.append(merged)
        else:
            result.append(dict(row))
    return result


def records_to_json(records: list[dict]) -> str:
    """Список словарей в JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)