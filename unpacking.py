import json
import pandas as pd
import csv

# Читаем содержимое файла .txt
with open('parsing_personalsacbearbeiter270925.txt', 'r', encoding='utf-8') as file:
    json_str = file.read()

# Проверка содержимого файла вручную: убедитесь, что файл содержит валидный JSON
print(json_str[:200])  # Выведет первые 200 символов файла для проверки

# Преобразование строки JSON в объект Python
data = json.loads(json_str)

# Создание DataFrame из списка словарей
df = pd.DataFrame(data) 

counter = df.shape[0]
print(counter)
# Вывод DataFrame
print(df.head(10))

# Сохранение DataFrame в CSV-файл
df.to_csv('parsing_personalsachbearbeiter.csv', index=False, encoding='utf-8')


