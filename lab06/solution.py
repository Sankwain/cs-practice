from pathlib import PurePosixPath


def count_by_extension(paths: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for p in paths:
        name = PurePosixPath(p).name
        if "." in name:
            ext = name.rsplit(".", 1)[1].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    value = float(n_bytes)
    for unit in units:
        if value < 1024 or unit == "ТБ":
            if unit == "Б":
                return f"{int(value)} Б"
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} ТБ"