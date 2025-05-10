#!/usr/bin/env python3
import re


class MyString:
    def __init__(self, value = ""):
        self._value = value
    

    @property
    def value(self):
      return self._value
    

    @value.setter
    def value(self, val):

      if isinstance(val, str):
        self._value = val
        print(val,self._value)

      else:
        print("The value must be a string.")


    def is_sentence(self):
       return self._value.endswith(".")
    

    def is_question(self):
       return self._value.endswith("?")
    

    def is_exclamation(self):
       return self._value.endswith("!")
    

    def count_sentences(self):
      if not self._value.strip():
        return 0

        # Split by '.', '!', or '?' (one or more times), then strip empty strings
      parts = re.split(r'[.!?]+', self._value)
      sentences = [s.strip() for s in parts if s.strip()]
      return len(sentences)

          

MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...").count_sentences()