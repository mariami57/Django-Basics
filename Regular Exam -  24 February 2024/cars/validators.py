from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class YearValidator:
    def __init__(self, message:Optional[str]=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "Year must be between 1999 and 2030!"

    def __call__(self, value):
        if value < 1999 or value > 2030:
            raise ValidationError(self.message)
