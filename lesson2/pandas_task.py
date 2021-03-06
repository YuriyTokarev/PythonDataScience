import numpy as np
import pandas as pd

print("Задание 1:")
authors = pd.DataFrame({
            'author_id': [1, 2, 3], 
            'author_name': ['Тургенев', 'Чехов', 'Островский']
          }, columns=['author_id', 'author_name'])
book = pd.DataFrame({
            'author_id': [1, 1, 1, 2, 2, 3, 3], 
            'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
            'price': [450, 300, 350, 500, 450, 370, 290]
          }, columns=['author_id', 'book_title', 'price'])
print(authors)
print(book)

print("Задание 2:")
authors_price = pd.merge(authors, book, on = 'author_id', how = 'inner')
print(authors_price)

print("Задание 3:")
top5 = authors_price.nlargest(5,['price'])
print(top5)

print("Задание 4:")
authors_stat = authors_price.groupby('author_name').price.agg(min_price = 'min', max_price = 'max', mean_price = 'mean')
print(authors_stat)

print("Задание 5:")
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
book_info  = pd.pivot_table(authors_price, values='price',index=['author_name'], columns=['cover'], aggfunc=np.sum, fill_value=0)
print(book_info)
book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
print(book_info2)