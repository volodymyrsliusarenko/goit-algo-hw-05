import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r'\s\d+\.\d+\s'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "20.12 or 12.28 . 333.1  and 2.9  or 0.2 and 2 or4.4 end 5.5."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
