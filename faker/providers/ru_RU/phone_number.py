from ..phone_number import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+7 (###) ###-##-##',
        '+7 (###) ##-##-##',
        '8 ### #######',
        '###-##-##',
    )

    mobile_formats = (
        '+7 (916) ###-##-##',
        '+7 (926) ###-##-##',
        '+7 (962) ###-##-##',
        '+7 (903) ###-##-##',
        '+7 (905) ###-##-##',
    )

    @classmethod
    def mobile_phone_number(cls):
        return cls.numerify(cls.random_element(cls.mobile_formats))
