LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"Негодная строка: {line!r}")

    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"Неизвестный уровень {level!r} в строке: {line!r}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines: list[str]) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            key = parse_event(line)["level"]
        except ValueError:
            key = "BROKEN"
        counts[key] = counts.get(key, 0) + 1
    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    freq = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            freq[msg] = freq.get(msg, 0) + 1

    ranked = sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))
    return [[msg, count] for msg, count in ranked[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    out = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        out.append(f"{level}: {counts[level]}")
    out.append("")
    out.append("Частые ошибки:")
    for message, count in errors:
        out.append(f"- {message} — {count}")
    return "\n".join(out) + "\n"