from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NamesValidator:
    def __init__(self, message:Optional[str]=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = "Your name must contain letters only!"

    def __call__(self,value):
        for char in value:
            if not char.isalpha():
                raise ValidationError(self.message)

@deconstructible
class PasscodeLengthValidator:
    def __init__(self, message:Optional[str]=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = "Your passcode must be exactly 6 digits!"

    def __call__(self,value):
        if len(value) != 6:
            raise ValidationError(self.message)
        for char in value:
            if not char.isdigit():
                raise ValidationError(self.message)
