# app/main.py
def get_coin_combination(cents: int) -> list[int]:
    quarters = cents // 25
    remainder = cents % 25
    dimes = remainder // 10
    remainder = remainder % 10
    nickels = remainder // 5
    pennies = remainder % 5
    return [pennies, nickels, dimes, quarters]


def is_isogram(word: str) -> bool:
    print(f"Testing word: {word}")  # Дебаг-вивід
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
