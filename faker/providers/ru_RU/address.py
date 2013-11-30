# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..address import Provider as AddressProvider


class Provider(AddressProvider):
    cities = (
        'Москва', 'Санкт-Перербург', 'Красногорск', 'Пенза', 'Владивосток',
        'Уфа', 'Новороссийск', 'Мурманск', 'Брянск', 'Пермь'
    )
    # City name can be either existing or fake (50/50%).
    city_formats = cities + (
        '{{last_name_m}}ск',
        '{{last_name_f}}горск',
    ) * int(len(cities) / 2)
