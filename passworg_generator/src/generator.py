from src.get_data import get_data
import random

def gen_password() -> str:
    s = get_data()
    variants = []

    for j in range(len(s)):
        variants.append(s[j])

    resulter = []

    for _ in range(7):
        index = random.randint(0, len(variants)-1)
        resulter.append(variants[index])

    char = " ".join(str(c) for c in resulter)

    return char