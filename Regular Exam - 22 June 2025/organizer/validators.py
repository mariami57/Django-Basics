import re
from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CompanyNameValidator:
    def __init__(self, message:Optional[str]=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or 'The company name is invalid!'

    def __call__(self, value):
        if not re.fullmatch(r'[A-Za-z0-9\- ]*', value):
            raise ValidationError(self.message)

@deconstructible
class SecretKeyValidator:
    def __init__(self, message:Optional[str]=None):
        self.message = message

    @property
    def message(self):
        return self.__message


    @message.setter
    def message(self, value):
        self.__message = value or 'Your secret key must have 4 unique digits!'

    def __call__(self, value):
        if len(value) != 4 or len(set(value)) != len(value):
            raise ValidationError(self.message)
        else:
            for char in value:
                if not char.isdigit():
                    raise ValidationError(self.message)



