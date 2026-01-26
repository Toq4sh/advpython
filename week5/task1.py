import string  # Модуль для работы со строками и пунктуацией

def analyze_text():
    # Открываем файл text.txt для чтения в кодировке UTF-8
    with open("text.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()  # Читаем все строки файла в список

    line_count = len(lines)  # Количество строк в файле
    word_count = 0           # Общее количество слов
    freq = {}                # Словарь для подсчета частоты слов

    # Проходим по каждой строке текста
    for line in lines:
        # Переводим строку в нижний регистр и удаляем знаки пунктуации
        line = line.lower().translate(
            str.maketrans("", "", string.punctuation)
        )

        words = line.split()        # Разбиваем строку на слова
        word_count += len(words)    # Увеличиваем общее количество слов

        # Подсчитываем частоту каждого слова
        for w in words:
            freq[w] = freq.get(w, 0) + 1

    # Открываем файл analysis.txt для записи результата
    with open("analysis.txt", "w", encoding="utf-8") as f:
        f.write(f"Lines: {line_count}\n")   # Записываем количество строк
        f.write(f"Words: {word_count}\n")  # Записываем количество слов
        f.write("Word frequency:\n")        # Заголовок

        # Записываем частоту каждого слова
        for k, v in freq.items():
            f.write(f"{k}: {v}\n")

# Запуск функции анализа текста
analyze_text()



