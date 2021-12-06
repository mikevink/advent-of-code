import os

def load_lines(day: str, name: str) -> list[str]:
    data_dir: str = os.getenv("DATA_DIR")
    input_file: str = f"{data_dir}/{day}/{name}.in"
    with open(input_file, "r") as inf:
        return list(map(lambda l: l.strip(), inf.readlines()))
