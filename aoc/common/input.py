import os


def load_lines(day: str, name: str, mapper=None, strip: bool = True) -> list:
    data_dir: str = os.getenv("DATA_DIR")
    input_file: str = f"{data_dir}/{day}/{name}.in"
    with open(input_file, "r") as inf:
        if strip:
            iterable = map(lambda l: l.strip(), inf.readlines())
        else:
            iterable = inf.readlines()
        if mapper is None:
            return list(iterable)
        return list(map(mapper, iterable))


def load_single_csv(day: str, name: str, mapper=None) -> list:
    lines: list[str] = load_lines(day, name)
    csv: list[str] = lines[0].split(",")
    if mapper is None:
        return csv
    return list(map(mapper, csv))
