import re
from pyuca import Collator

def read_and_process_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Помилка: Файл не знайдено")
        return

    # Розділення тексту на речення (за крапками, знаками оклику, питання)
    sentences = re.split(r'[.!?]', text)
    first_sentence = sentences[0].strip() if sentences else ""

    # Виведення першого речення
    print("Перше речення:", first_sentence)

    # Знайти всі слова та відсортувати їх за алфавітом
    words = re.findall(r'\b\w+\b', first_sentence)
    collator = Collator()
    words = sorted(words, key=collator.sort_key)  # Сортування з використанням UCA
    word_count = len(words)

    # Розділення на українські та англійські слова
    ukrainian_words = [word for word in words if re.match(r'[а-яА-ЯїЇєЄґҐ]', word)]
    english_words = [word for word in words if re.match(r'[a-zA-Z]', word)]

    if ukrainian_words:
        print("Українські слова:", ", ".join(ukrainian_words))
    if english_words:
        print("Англійські слова:", ", ".join(english_words))
    print("Загальна кількість слів:", word_count)


if __name__ == "__main__":
    file_path = "sort.txt"
    read_and_process_text(file_path)
