# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import BaseProvider


class Provider(BaseProvider):
    merchandise_brands = (
        'Apple', 'Bork', 'Carnaby', 'D&G', 'Enduro', 'Freeze', 'Good', 'Horse', 'Indiana', 'Joahn',
        'Kale', 'Lemon', 'Moon', 'NIИ', 'Orange', 'P&G', 'Racoon', 'Samsung', 'Tommy Hillfiger',
        'Unicorn', 'Verdana', 'Wow', 'Xerox', 'Yellow', 'Zero'
    )

    merchandise_types = ('Shoes', 'Coat', 'Computer', 'Example')

    merchandise_formats = ('{{merchandise_type}} {{merchandise_brand}}',)

    modifications_formats = ('# size', 'type #')

    def merchandise(self):
        """
        Get a merchandise name.
        """
        pattern = self.random_element(self.merchandise_formats)
        return self.generator.parse(pattern)

    @classmethod
    def merchandise_brand(cls):
        """
        Get a brand name.
        :example 'Apple'
        """
        return cls.random_element(cls.merchandise_brands)

    @classmethod
    def merchandise_type(cls):
        """
        Get a merchandise type.
        :example 'Shoes'
        """
        return cls.random_element(cls.merchandise_types)

    def merchandise_modifications(self, count=0):
        """
        Get a product with modifications list.
        :result (
            'Merchandise name',
            ('mod1', 'mod2', 'mod3')
        )
        """
        m_format = self.random_element(self.modifications_formats)
        modifications = []
        for i in range(0, count):
            modifications.append(self.bothify(m_format))

        return self.merchandise(), tuple(modifications)
