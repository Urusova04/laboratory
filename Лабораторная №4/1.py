# TODO решите задачу
import json
def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    result = sum(item ['weight'] * item ['score'] for item in data)
    return round (result, 3)

print(task())
