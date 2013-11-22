# -*- coding: utf-8 -*-
from ..person import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{last_name_m}} {{first_name_m}} {{middle_name_m}}',
        '{{last_name_m}} {{first_name_m}}',
        '{{first_name_m}} {{middle_name_m}} {{last_name_m}}',
        '{{last_name_f}} {{first_name_f}} {{middle_name_f}}',
        '{{last_name_f}} {{first_name_f}}',
        '{{first_name_f}} {{middle_name_f}} {{last_name_f}}',
    )

    last_names_m = (
        u'Сидоров', u'Иванов', u'Кузнецов', u'Петухов', u'Марков', u'Галкин', u'Суворов', u'Логинов',
    )

    last_names_f = (
        u'Иванова', u'Смирнова', u'Попова', u'Лебедева', u'Соколова', u'Новикова', u'Волкова', u'Павлова', u'Белова',
    )

    first_names_m = (
        u'Андрей', u'Антон', u'Виктор', u'Егор', u'Никита', u'Олег', u'Сергей', u'Иннокентий', u'Яков'
    )

    first_names_f = (
        u'Анна', u'Алена', u'Варвара', u'Вера', u'Дарья', u'Елена', u'Зоя', u'Ирина', u'Кристина', u'Лариса',
    )

    middle_names_m = (
        u'Артурович', u'Борисович', u'Васильевич', u'Дмитриевич', u'Игоревич', u'Михайлович', u'Яковлевич', u'Вадимович', u'Геннадьевич'
    )

    middle_names_f = (
        u'Александровна', u'Андреевна', u'Владимировна', u'Викторовна', u'Ивановна', u'Егоровна', u'Михайловна', u'Сергеевна', u'Николаевна',
    )

    @classmethod
    def last_name(cls):
        return cls.random_element(cls.last_names_m + cls.last_names_f)

    @classmethod
    def last_name_m(cls):
        return cls.random_element(cls.last_names_m)

    @classmethod
    def last_name_f(cls):
        return cls.random_element(cls.last_names_f)

    @classmethod
    def first_name(cls):
        return cls.random_element(cls.first_names_m + cls.first_names_f)

    @classmethod
    def first_name_m(cls):
        return cls.random_element(cls.first_names_m)

    @classmethod
    def first_name_f(cls):
        return cls.random_element(cls.first_names_f)

    @classmethod
    def middle_name(cls):
        return cls.random_element(cls.middle_names_m + cls.middle_names_f)

    @classmethod
    def middle_name_m(cls):
        return cls.random_element(cls.middle_names_m)

    @classmethod
    def middle_name_f(cls):
        return cls.random_element(cls.middle_names_f)
