# Задача "Функциональное разнообразие":
from random import choice, random
# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)
# Замыкание:
def  get_advanced_writer(file_name): # принимающая название файла для записи
    def  write_everything(*data_set): # функция c параметром принимающим неограниченное количество данных любого типа
        with open(file_name, 'a', encoding='utf8') as file:
            for element in data_set:
                file.write(str(element) + '\n') # добавление  всех данных из data_set в том же виде
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Метод __call__:
class  MysticBall:
    def __init__(self, *words):  # коллекция строк
        self.words = words
    def __call__(self):
        word = choice(self.words) # выбирает случайным образом слово из words и возвращает его
        return word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
