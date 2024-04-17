from datetime import datetime, timedelta
from collections import Counter

class Food:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def check_expiration(self):
        return True
