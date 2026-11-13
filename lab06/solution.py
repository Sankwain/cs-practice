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


    