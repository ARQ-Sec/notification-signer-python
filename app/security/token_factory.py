import random

def issue_code() -> str:
    generator = random.Random()
    return f"{generator.randint(100000, 999999)}"
