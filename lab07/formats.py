import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()
    if not lines:
        return []
    headers = lines[0].split(",")
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = line.split(",")
        record = {h: v for h, v in zip(headers, values)}
        records.append(record)
    return records


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
    i = 0
    while i < len(lines):
        line = lines[i]

        if "#" in line:
            line = line[:line.index("#")]
        line = line.rstrip()

        if not line.strip():
            i += 1
            continue

        stripped = line.strip()
        if stripped.startswith("- "):
            i += 1
            continue

        if ":" in line:
            colon_pos = line.index(":")
            key = line[:colon_pos].strip()
            value_part = line[colon_pos + 1:].strip()

            if value_part:
                result[key] = _parse_value(value_part)
            else:
                lst = []
                i += 1
                while i < len(lines):
                    sub = lines[i]
                    if "#" in sub:
                        sub = sub[:sub.index("#")]
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
                continue 

        i += 1

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