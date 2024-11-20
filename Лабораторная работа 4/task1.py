# TODO решите задачу

import json

def task() -> float:
    with open("input.json", 'r') as file:
        findings = json.load(file)
        sum_multips = 0
        for found in findings:
            sum_multips += found["score"] * found["weight"]
    return sum_multips


print(round(task(), 3))
