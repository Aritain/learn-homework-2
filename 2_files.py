"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    symbol_count = len(file_content)
    word_count = len(file_content.split())
    
    print(f"Файл состоит из {symbol_count} символов")
    print(f"Файл состоит из {word_count} слов")
    
    with open('referat2.txt', 'w', encoding='utf-8') as file:
        file.write(file_content.replace('.','!'))

if __name__ == "__main__":
    main()
