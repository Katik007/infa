import os
import re
import argparse

def select_files(directory, start_letter, min_name_length):
    selected_files = []
    for filename in os.listdir(directory):
        if filename.startswith(start_letter):
            name_without_extension = os.path.splitext(filename)[0]
            if len(name_without_extension) >= min_name_length and filename[-2].isdigit() and filename.endswith('.txt'):
                selected_files.append(os.path.join(directory, filename))
    return selected_files

def search_data_in_files(files):
    results = {}
    for file in files:
        with open(file, 'r') as f:
            file_data = f.read()
            # Паттерны для поиска различных типов данных
            time_pattern = r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?\b'
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            url_pattern = r'(http|ftp|https)://[\w_-]+(\.[\w_-]+)+([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
            python_variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
            date_pattern = r'\b(?:\d{4}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4})\b'
            float_pattern = r'\b\d+\.\d+\b'
            license_plate_pattern = r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'

            patterns = {
                "Time": time_pattern,
                "Email": email_pattern,
                "URL": url_pattern,
                "Python Variable": python_variable_pattern,
                "Date": date_pattern,
                "Float": float_pattern,
                "Russian License Plate": license_plate_pattern
            }

            file_results = {}
            for data_type, pattern in patterns.items():
                matches = re.findall(pattern, file_data)
                if matches:
                    file_results[data_type] = matches
            results[file] = file_results
    return results

def generate_files(directory, num_files, prefix):
    for i in range(num_files):
        filename = f"{prefix}_{i}.txt"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            # В данном примере генерируем пустые файлы
            f.write("")

def main():
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Анализ папки с файлами")
    parser.add_argument("directory", type=str, help="Путь к папке с файлами")
    parser.add_argument("start_letter", type=str, help="Начальная буква имени файла")
    parser.add_argument("min_name_length", type=int, help="Минимальная длина имени файла (без учета расширения)")
    parser.add_argument("--generate", action="store_true", help="Генерация файлов с данными")
    parser.add_argument("--num_files", type=int, default=5, help="Количество файлов для генерации (по умолчанию 5)")
    parser.add_argument("--prefix", type=str, default="data", help="Префикс для названий файлов при генерации (по умолчанию 'data')")
    args = parser.parse_args()

    # Проверка наличия и обработка аргумента --generate
    if args.generate:
        generate_files(args.directory, args.num_files, args.prefix)
        print(f"Создано {args.num_files} файлов с префиксом '{args.prefix}' в папке '{args.directory}'")
        return

    # Выбор файлов по критериям имени
    selected_files = select_files(args.directory, args.start_letter, args.min_name_length)
    print("Выбранные файлы:")
    for file in selected_files:
        print(file)

    # Поиск данных в выбранных файлах
    data_results = search_data_in_files(selected_files)
    print("\nРезультаты анализа данных в файлах:")
    for file, results in data_results.items():
        print(f"\nФайл: {file}")
        for data_type, data in results.items():
            print(f"{data_type}: {data}")

main()