from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class UsernameValidator:
    def __init__(self, message:Optional[str]=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "Ensure this value contains only letters, numbers, and underscore."


    def __call__(self, value):
        if not re.fullmatch(r'\w+', value):
            raise ValidationError(self.message)

