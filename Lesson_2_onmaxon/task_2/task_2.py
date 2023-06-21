"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json

def writer_order_to_json(item, quantity, price, buyer, date):
    with open('orders_1.json') as f:
        obj = json.load(f)

    with open('orders_1.json', 'w', encoding='utf-8') as f:
        add_order = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
            }
        obj['orders'].append(add_order)
        json.dump(obj,f, indent=4, ensure_ascii=False)

writer_order_to_json('printer', '10', '777777', 'Ivanov I.P.', '5.04.2023')
writer_order_to_json('Роутер', '555', '6750', 'Petrova I.I.', '10.02.2023')
writer_order_to_json('iphone', '1', '72500', 'Sidorov P.P.', '13.03.2023')
