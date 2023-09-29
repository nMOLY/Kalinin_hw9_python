# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

# Загрузка файла в DataFrame
df = pd.read_csv('sample_data/california_housing_train.csv')

# Нахождение минимального значения столбца population
min_population = df['population'].min()

# Фильтрация строк по минимальному значению столбца population
filtered_df = df[df['population'] == min_population]

# Нахождение максимального значения столбца households для отфильтрованных строк
max_households = filtered_df['households'].max()

print(f'Максимальное количество households в зоне с минимальным значением population: {max_households}')