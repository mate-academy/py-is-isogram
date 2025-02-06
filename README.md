# Is isogram

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start.

An isogram is a word that has no repeating letters, consecutive or non-consecutive.

Inside `app/test_main.py`, write tests for a function `is_isogram` that takes a string word, that contains only letters, 
and checks whether this word is an isogram.

Notes:

- for this task, the empty string is an isogram;
- function should be case-insensitive (M and m are considered the same letter).

**Please note:** you have to use `pytest` for writing tests.

Examples:
```python
is_isogram('playgrounds') is True
is_isogram('look') is False
is_isogram('Adam') is False
is_isogram('') is True
```

Ізограма - це слово, яке не має повторюваних літер, послідовних або непослідовних.

Усередині `app/test_main.py` напишіть тести для функції `is_isogram`, яка приймає рядкове слово, яке містить лише літери,
і перевіряє, чи це слово є ізограмою.

Примітки:

- для цього завдання порожній рядок є ізограмою;
- функція має бути нечутливою до регістру (M і m вважаються однією буквою).

**Зверніть увагу:** для написання тестів потрібно використовувати `pytest`.
Run `pytest app/` to check if function pass your tests.

Run `pytest --numprocesses=auto tests/` to check if your tests cover all boundary conditions
and pass task tests.
