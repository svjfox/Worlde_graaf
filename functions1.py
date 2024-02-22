import random
import tkinter as tk
from tkinter import messagebox

# Загрузка слов из файла
def load_words(file_name):
    with open(file_name, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words if len(word.strip()) == 5]

# Выбор случайного слова из списка
def choose_word(words):
    return random.choice(words)

# Проверка угаданных букв
def check_guess(word, guess):
    result = []
    for i in range(len(word)):
        if word[i] == guess[i]:
            result.append('green')  # Правильная буква на правильном месте
        elif guess[i] in word:
            result.append('yellow')  # Правильная буква, но не на своем месте
        else:
            result.append('black')  # Буква не в слове
    return result

# Обработчик события при нажатии на кнопку "Проверить"
def guess_word():
    global attempts_left
    global secret_word
    global current_row

    guess = [entry_boxes[current_row][i].get() for i in range(5)]

    if ''.join(guess) == secret_word:
        messagebox.showinfo("Поздравляем!", "Вы угадали слово!")
        reset_game()
        return

    feedback = check_guess(secret_word, guess)

    for i in range(5):
        entry_boxes[current_row][i].config(bg=feedback[i])

    attempts_left -= 1
    attempts_label.config(text=f"Попыток осталось: {attempts_left}")

    current_row += 1
    if attempts_left == 0:
        messagebox.showinfo("Игра окончена", f"Жаль, Вы не угадали слово. Загаданное слово: {secret_word}")
        reset_game()

# Сброс игры
def reset_game():
    global secret_word
    global attempts_left
    global current_row

    secret_word = choose_word(words)
    attempts_left = 6
    attempts_label.config(text=f"Попыток осталось: {attempts_left}")
    for row in entry_boxes:
        for box in row:
            box.delete(0, 'end')
            box.config(bg='white')
    current_row = 0

# Основная часть программы
root = tk.Tk()
root.title("Game")

# Загрузка слов
words = load_words('words1.txt')
secret_word = choose_word(words)
attempts_left = 6
current_row = 0﻿
