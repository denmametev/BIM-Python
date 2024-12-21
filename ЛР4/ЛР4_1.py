import json

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    total = sum(item["score"] * item["weight"] for item in data)

    return round(total, 3)


print(task())
