from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class TravelerNicknameValidator:
    def __init__(self, message:Optional[str]=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "Your nickname is invalid!"

    def __call__(self, value):
        for char in value:
            if not char.isalnum():
                raise ValidationError(self.message)