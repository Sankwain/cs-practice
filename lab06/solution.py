from pathlib import PurePosixPath


def count_by_extension(paths: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for p in paths:
        ext = PurePosixPath(p).suffix[1:].lower() 
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return max(paths, key=lambda p: (p.count("/"), [-ord(c) for c in p]))


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