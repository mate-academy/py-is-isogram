def is_isogram(word: str) -> bool:
    # Convert the word to lowercase to make it case-insensitive
    word = word.lower()

    # Check if there are any repeating letters
    return len(word) == len(set(word))
