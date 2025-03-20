import random


class Order:

    def __init__(self):
        self.name = self.generate_order_data()
        self.surname = self.generate_order_data()
        self.address = 'г. Москва, ' + random.choice(
            ['ул. Тверская, 44, кв. 100', 'ул. Арбат, 100, кв. 44', 'ул. Варварка, 200, кв. 144'])
        self.station = random.choice(['Лужники', 'Митино', 'ВДНХ', 'Лихоборы', 'Театральная'])
        self.telephone = int('89' + ''.join([random.choice(list('1234567890')) for num in range(9)]))
        self.date = random.choice(range(7))
        self.rental_period = random.choice(
            ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток'])
        self.color = random.choice(['black', 'grey'])
        self.comment = random.choice(['Код домофона: 123', 'Домофон не работает', 'Просьба доставить после 18:00'])

    def generate_order_data(self):
        result = random.choice(list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ'))
        for i in range(5):
            result += random.choice(list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'))

        return result