# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..company import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{company_prefix}} "{{last_name}} и Партнеры"',
        'ИП {{last_name}} {{initials}}',
        '{{company_prefix}} "{{first_name}}-{{company_suffix}}"',
        '{{company_prefix}} "{{city}} {{company_suffix}}"',
    )

    company_prefixes = ('ООО', 'ЗАО') * 5 + ('ОАО', 'ТД', 'ГУП', 'ФГУП')
    company_suffixes = ('Трейд', 'Стиль', 'Траст', 'Строй',
                        'Кредит', 'Банк', 'Медиа', 'Финанс')

    @classmethod
    def company_prefix(cls):
        return cls.random_element(cls.company_prefixes)
