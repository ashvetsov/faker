# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..merchandise import Provider as MerchandiseProvider


class Provider(MerchandiseProvider):
    merchandise_types = (
        'Компьютер', 'Ноутбук', 'Монитор', 'Принтер', 'Холодильник', 'СВЧ', 'Плита',
        'Будильник', 'Часы', 'Наручные часы', 'Украшение', 'Коробка', 'Планшет', 'Кровать', 'Радио', 'Телефон',
        'Ботинки', 'Туфли', 'Шорты', 'Сапоги', 'Брюки', 'Джинсы', 'Комбинезон', 'Пальто',
        'Одеяло', 'Полотенце', 'Подушка', 'Трико', 'Конструктор', 'Паззл', 'Развивающая игра',
        'Велосипед', 'Мяч', 'Кондиционер', 'Чехол', 'Накопитель', 'Зеркало',
        'Стул', 'Стол', 'Ящик', 'Комод', 'Пакет', 'Подарочный набор', 'Рама'
    )
    merchandise_formats = (
        '{{merchandise_type}} {{merchandise_brand}}',
        '{{merchandise_type}} {{merchandise_consumer}}',
        '{{merchandise_type}} {{merchandise_consumer}} {{merchandise_brand}}',
        '{{merchandise_type}} {{merchandise_consumer}} ({{merchandise_brand}})',
        '{{merchandise_type}} {{merchandise_consumer}} {{merchandise_brand}}',
        '{{merchandise_brand}} {{merchandise_type}} ({{merchandise_consumer}})',
    )
    modifications_formats = (
        '## размер', 'тип ?', '##см', '##/##'
    )
    merchandise_consumers = ('дет.', 'жен.', 'муж.', 'уни.', 'для детей')

    @classmethod
    def merchandise_consumer(cls):
        """
        Get a possible merchandise consumer.
        example: 'для детей'
        """
        return cls.random_element(cls.merchandise_consumers)
