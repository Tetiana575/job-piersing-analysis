import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import ast
import folium
from geopy.geocoders import Nominatim
import time
import seaborn as sns

# Загрузка CSV файла с помощью pandas (если файл является CSV, а не JSON)
df = pd.read_csv('personalsachbearbeiter.csv', encoding='utf-8')

def parse_list_column(x):
    if x is None:
        return []
    elif isinstance(x, list):
        return x
    elif isinstance(x, str):
        try:
            return ast.literal_eval(x)
        except:
            return []
    elif isinstance(x, (pd.Series, pd.DataFrame, np.ndarray)):
        return []
    else:
        return []

# Обработка столбца 'verantwortlichkeiten'   
df['verantwortlichkeiten'] = df['verantwortlichkeiten'].apply(parse_list_column)
# Объединяем все списки из выбранного столбца
all_words = []

for words_list in df['verantwortlichkeiten']:
    all_words.extend(words_list)

word_counts = Counter(all_words)

# Сортируем слова по количеству встречаемости
sorted_words = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:15])

# Выводим результат
print('\n Verantwortlichkeiten')
for word, count in sorted_words.items():
    print(f"{word}: {count}")


# # Построение гистограммы
plt.barh(list(sorted_words.keys()),list(sorted_words.values()), color='#2a3990',)
#plt.ylabel('Verantwortlichkeiten')
#plt.xlabel('Count')
#plt.axis('off')
#plt.gca().spines['bottom'].set_visible(False)
plt.box(False)
plt.xticks([])
plt.title('Top 15 Verantwortlichkeiten')
#plt.xticks(rotation=45)
for i, (skill, count) in enumerate(sorted_words.items()):
    plt.text(count + 0.1, i, str(count), va='center')  # +0.1 для отступа справа от столбца
plt.tight_layout()
plt.gca().invert_yaxis()  # чтобы самый большой столбец был сверху
plt.show() 


# Преобразование строки в список
df['sprache'] = df['sprache'].apply(parse_list_column)

all_sprache = []
# Объединяем все списки из выбранного столбца
for words_list in df['sprache']:
    all_sprache.extend(words_list)

word_counts1 = Counter(all_sprache)

# Сортируем слова по количеству встречаемости
sorted_words1 = dict(sorted(word_counts1.items(), key=lambda x: x[1], reverse=True)[:20])

# Выводим результат
print('\n Sprachen')
for word, count in sorted_words1.items():
    print(f"{word}: {count}")


# Построение круговой диаграммы
plt.pie(list(sorted_words1.values()), labels=list(sorted_words1.keys()), colors=['#2a3990',  '#7890cd', 'grey','green', 'orange', 'red','yellow','violet'],autopct='%1.1f%%')
plt.axis('equal')
plt.legend([f'{word}: {count}' for word, count in sorted_words1.items()], title='Sprachen', bbox_to_anchor=(0.7, 0.45, 0.5, 1), loc='center')
plt.title('Sprachen')
plt.show()

df['home_work'] = df['home_work'].apply(parse_list_column)

all_sprache = []
# Объединяем все списки из выбранного столбца
for words_list in df['home_work']:
    all_sprache.extend(words_list)

word_counts1 = Counter(all_sprache)

# Сортируем слова по количеству встречаемости
sorted_words1 = dict(sorted(word_counts1.items(), key=lambda x: x[1], reverse=True)[:20])

# Выводим результат
print('\n Home  oder Office Work')
for word, count in sorted_words1.items():
    print(f"{word}: {count}")


# Построение круговой диаграммы
plt.pie(list(sorted_words1.values()), labels=list(sorted_words1.keys()), colors=['#2a3990',  '#7890cd', 'grey','green', 'yellow','violet'],autopct='%1.1f%%')
plt.axis('equal')
plt.legend([f'{word}: {count}' for word, count in sorted_words1.items()], title='Sprachen', bbox_to_anchor=(0.7, 0.45, 0.5, 1), loc='center')
plt.title('Home  oder Office Work')
plt.show()

# Преобразование строки в список
df['Arbetszeit'] = df['Arbetszeit'].apply(parse_list_column)

all_arbetszeit = []
# Объединяем все списки из выбранного столбца
for words_list in df['Arbetszeit']:
    all_arbetszeit.extend(words_list)

word_counts1 = Counter(all_arbetszeit)

# Сортируем слова по количеству встречаемости
sorted_words1 = dict(sorted(word_counts1.items(), key=lambda x: x[1], reverse=True))

# Выводим результат
print('\n Arbetszeit')
for word, count in sorted_words1.items():
    print(f"{word}: {count}")

# Построение круговой диаграммы
plt.barh(list(sorted_words1.keys()),list(sorted_words1.values()), color='#2a3990',)
plt.box(False)
plt.xticks([])
plt.title('Arbetszeit')
#plt.xticks(rotation=45)
for i, (skill, count) in enumerate(sorted_words1.items()):
    plt.text(count + 0.1, i, str(count), va='center')  # +0.1 для отступа справа от столбца
plt.tight_layout()
plt.gca().invert_yaxis()  # чтобы самый большой столбец был сверху
plt.show() 


# Преобразование строки в список
df['Arbeitsbedingungen'] = df['Arbeitsbedingungen'].apply(parse_list_column)

all_arbetsbedingungen = []
# Объединяем все списки из выбранного столбца
for words_list in df['Arbeitsbedingungen']:
    all_arbetsbedingungen.extend(words_list)

word_counts1 = Counter(all_arbetsbedingungen)

# Сортируем слова по количеству встречаемости
sorted_words1 = dict(sorted(word_counts1.items(), key=lambda x: x[1], reverse=True)[:20])

# Выводим результат
print('\n Arbeitsbedingungen')
for word, count in sorted_words1.items():
    print(f"{word}: {count}")

# Построение круговой диаграммы
plt.pie(list(sorted_words1.values()), labels=list(sorted_words1.keys()), colors=['#2a3990',  '#7890cd', 'green','yellow','violet'], autopct='%1.1f%%')
plt.axis('equal')
plt.legend( title='Arbeitsbedingungen', bbox_to_anchor=(0.5, -0.5, 0.6, 1), loc='center')
plt.title('Arbeitsbedingungen')
plt.show()

df['Softskils'] = df['Softskils'].apply(parse_list_column)
# Объединяем все списки из выбранного столбца
all_words = []

for words_list in df['Softskils']:
    all_words.extend(words_list)

word_counts = Counter(all_words)

# Сортируем слова по количеству встречаемости
sorted_words = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:15])

# Выводим результат
print('\n Softskils')
for word, count in sorted_words.items():
    print(f"{word}: {count}")

plt.barh(list(sorted_words.keys()),list(sorted_words.values()), color='#2a3990',)
plt.box(False)
plt.xticks([])
plt.title('Top 15 Software Skills')
#plt.xticks(rotation=45)
for i, (skill, count) in enumerate(sorted_words.items()):
    plt.text(count + 0.1, i, str(count), va='center')  # +0.1 для отступа справа от столбца
plt.tight_layout()
plt.gca().invert_yaxis()  # чтобы самый большой столбец был сверху
plt.show() 



df['Hardskils'] = df['Hardskils'].apply(parse_list_column)
# Объединяем все списки из выбранного столбца
all_words = []

for words_list in df['Hardskils']:
    all_words.extend(words_list)

word_counts = Counter(all_words)

# Сортируем слова по количеству встречаемости
sorted_words = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10])

# Выводим результат
print('\n Hardskils')
for word, count in sorted_words.items():
    print(f"{word}: {count}")

plt.barh(list(sorted_words.keys()),list(sorted_words.values()), color='#2a3990',)
plt.box(False)
plt.xticks([])
plt.title('Top 10 Hardskils')
#plt.xticks(rotation=45)
for i, (skill, count) in enumerate(sorted_words.items()):
    plt.text(count + 0.1, i, str(count), va='center')  # +0.1 для отступа справа от столбца
plt.tight_layout()
plt.gca().invert_yaxis()  # чтобы самый большой столбец был сверху
plt.show() 

df['branche'] = df['branche'].apply(parse_list_column)
# Объединяем все списки из выбранного столбца
all_words = []

for words_list in df['branche']:
    all_words.extend(words_list)

word_counts = Counter(all_words)

# Сортируем слова по количеству встречаемости
sorted_words = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20])

# Выводим результат
print('\n Branches')
for word, count in sorted_words.items():
    print(f"{word}: {count}")

plt.barh(list(sorted_words.keys()),list(sorted_words.values()), color='#2a3990',)
plt.box(False)
plt.xticks([])
plt.title('Top 20 Branches')
#plt.xticks(rotation=45)
for i, (skill, count) in enumerate(sorted_words.items()):
    plt.text(count + 0.1, i, str(count), va='center')  # +0.1 для отступа справа от столбца
plt.tight_layout()
plt.gca().invert_yaxis()  # чтобы самый большой столбец был сверху
plt.show() 

df['Greed'] = df['Greed'].apply(parse_list_column)
# Объединяем все списки из выбранного столбца
all_words = []

for words_list in df['Greed']:
    all_words.extend(words_list)

word_counts = Counter(all_words)

# Сортируем слова по количеству встречаемости
sorted_words = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))

# Выводим результат
print('\n Greeds')
for word, count in sorted_words.items():
    print(f"{word}: {count}")

plt.barh(list(sorted_words.keys()),list(sorted_words.values()), color='#2a3990',)
plt.box(False)
plt.xticks([])
plt.title('Greeds')
#plt.xticks(rotation=45)
for i, (skill, count) in enumerate(sorted_words.items()):
    plt.text(count + 0.1, i, str(count), va='center')  # +0.1 для отступа справа от столбца
plt.tight_layout()
plt.gca().invert_yaxis()  # чтобы самый большой столбец был сверху
plt.show() 

#визуализируем на карте города
# Подсчитываем количество объявлений по каждому городу
city_counts = df['location'].value_counts()
sorted_words = dict(sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:20])

# Выводим результат
print('\n Cyties')
for word, count in sorted_words.items():
    print(f"{word}: {count}")

cities = list(sorted_words.keys())
counts = list(sorted_words.values())

# Строим бар-чарт
plt.figure(figsize=(10, 6))


sns.barplot(x=counts, y=cities, color='#2a3990',  legend=False)

plt.box(False)
plt.xticks([])
for i, (skill, count) in enumerate(sorted_words.items()):
    plt.text(count + 0.1, i, str(count), va='center') 
plt.title('Geographical Distribution of Jobs')
plt.show()

# Создадим словарь дней недели на немецком
german_days = {
    'Monday': 'Montag',
    'Tuesday': 'Dienstag',
    'Wednesday': 'Mittwoch',
    'Thursday': 'Donnerstag',
    'Friday': 'Freitag',
    'Saturday': 'Samstag',
    'Sunday': 'Sonntag'
}

# Подсчитываем количество объявлений по каждому дню недели
df['datePosted'] = pd.to_datetime(df['datePosted'])
df['weekday'] = df['datePosted'].dt.day_name()
day_counts = df['weekday'].value_counts()

# Создаем список дней недели по порядку
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Создаем список с количеством объявлений по дням недели в правильном порядке
counts_in_order = [day_counts.get(day, 0) for day in days_order]

# Создаем список названий дней на немецком в порядке days_order
days_in_german = [german_days[day] for day in days_order]

print('\n Wochentage')
for word, count in zip(days_in_german, counts_in_order):
    print(f"{word}: {count}")

# Визуализация
plt.figure(figsize=(10,6))
sns.barplot(x=days_in_german, y=counts_in_order, color='#2a3990',  legend=False)
for i, count in enumerate(counts_in_order):
    plt.text(i, count + 0.2, str(count), ha='center') 

# Определение самого популярного дня и его отображение
most_common_day = day_counts.idxmax()
plt.box(False)
plt.yticks([])
plt.title(f'Der beliebteste Wochentag ist {german_days[most_common_day]}')
plt.show()

# Выводим самый популярный день
print(f"Der beliebteste Wochentag ist: {german_days[most_common_day]}")


