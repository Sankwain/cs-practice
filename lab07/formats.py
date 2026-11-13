import json


def csv_to_records(text: str) -> list[dict[str, str]]:
    lines = text.strip().split("\n")
    headers = [h.strip() for h in lines[0].split(",")]
    result = []
    for line in lines[1:]:
        if not line.strip():  # пропускаем пустые строки
            continue
        values = [v.strip() for v in line.split(",")]
        result.append(dict(zip(headers, values)))
    return result


def _parse_value(raw: str):
    raw = raw.strip()
    if raw.lower() in ("true", "yes"):
        return True
    if raw.lower() in ("false", "no"):
        return False
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        pass
    return raw


def parse_settings(lines: list[str]) -> dict:
    result = {}
    for line in lines:
        # Отбрасываем комментарий
        if "#" in line:
            line = line[:line.index("#")]
        line = line.strip()
        if not line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        # Пробуем превратить в число
        try:
            num_str = value.replace(",", ".")
            if "." in num_str:
                result[key] = float(num_str)
            else:
                result[key] = int(num_str)
        except ValueError:
            result[key] = value
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
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