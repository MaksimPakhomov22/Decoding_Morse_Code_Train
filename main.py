import random


code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

words = ["code", "bit", "list", "soul", "next"]

answers = []


def morse_encode(word):
    morse_code = ""
    for i in word:
        morse_code += code[i] + " "
    return morse_code


def get_word():
    word_random = random.choice(words)
    return word_random


def print_statistics(answers):
    total_tasks = len(answers)
    right_answer = answers.count(True)
    wrong_answer = answers.count(False)
    print(f"""Всего задачек: {total_tasks} \nОтвечено верно: {right_answer} \nОтвечено неверно: {wrong_answer}""")


print("""Сегодня мы потренируемся расшифровывать морзянку. \nНажмите Enter и начнем""")


for question_number in range(1, 6):
    word_random = get_word()
    encode_question_word = morse_encode(word_random)

    print(f"Слово {question_number}: {encode_question_word}\n")

    user_answer = input('Введите перевод слова: ')

    if user_answer.lower() == word_random.lower():
        print(f"Верно, {word_random}!")
        answers.append(True)
    else:
        print(f"Неверно. Верный ответ: {word_random}!")
        answers.append(False)

print(print_statistics(answers))
