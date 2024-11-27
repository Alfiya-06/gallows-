import random

# Список слов для игры
words = ['студент', 'программирование', 'игра', 'компьютер', 'алгоритм']
word = random.choice(words)  # Случайное слово
guessed_letters = []  # Хранит угаданные буквы
attempts = 6  # Количество попыток


# Функция для отображения состояния загаданного слова
def display_word():
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()


# Функция для отображения состояния повешенного
def display_hangman(attempts):
    stages = [
        """ 
           -----
           |   |
           |   o
           |  /|\\
           |  /|\\
           | 
        """,
        """ 
           -----
           |   |
           |   o
           |  /|\\
           |  /
           |  
        """,
        """ 
           -----
           |   |
           |   o
           |  /|\\
           |  
           |  
        """,
        """ 
           -----
           |   |
           |   o
           |  /|
           |  
           |  
        """,
        """ 
           -----
           |   |
           |   o
           |   |
           |  
           |  
        """,
        """ 
            -----
            |   |
            |   o
            |   
            |  
            |  
        """,
        """ 
           -----
           |   |
           |   
           |  
           |  
           |  
        """
    ]
    return stages[attempts]


# Главная функция игры
def hangman():
    global attempts
    while attempts > 0:
        print(display_hangman(attempts))
        print(display_word())
        guess = input("Введите букву: ").lower()

        # Проверка на ввод
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, вводите только одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
            continue

        guessed_letters.append(guess)  # Добавляем букву в список угаданных

        if guess not in word:
            attempts -= 1
            print(f"Неправильно! Осталось попыток: {attempts}")
        else:
            print("Правильно!")

        if all(letter in guessed_letters for letter in word):  # Проверка на выигрыш
            print(f"Поздравляем! Вы угадали слово: {word}")
            break
    else:
        print(display_hangman(attempts))
        print(f"Вы проиграли! Загаданное слово было: {word}")


# Запуск игры
hangman()