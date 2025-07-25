from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BadWordValidator(object):
    def __init__(self, bad_words: Optional[list]=None, message: Optional[str] = None) -> None:
        self.bad_words = bad_words
        self.message = message

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self,value) -> None:
        self.__message = value or "The text contains bad words."

    def __call__(self, value:str) -> None:
        for bad_word in value.split():
            if bad_word.lower() in self.bad_words:
                raise ValidationError(self.message)

