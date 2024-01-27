#!/usr/bin/env python3
# Author: Arash Zarif

class RoseDictionary:
    def __init__(self):
        self.items = []

    def __setitem__(self, key, value):
        for index, (existing_key, _) in enumerate(self.items):
            if existing_key == key:
                self.items[index] = (key, value)
                return
        self.items.append((key, value))

    def __getitem__(self, key):
        for item_key, item_value in self.items:
            if item_key == key:
                return item_value
        raise KeyError(key)

    def __delitem__(self, key):
        for index, (item_key, _) in enumerate(self.items):
            if item_key == key:
                del self.items[index]
                return
        raise KeyError(key)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(dict(self.items))

    def pop_item(self, raise_error=False, default=None, error_msg=''):
        if not self.items:
            if raise_error:
                raise KeyError(error_msg) if error_msg else KeyError('Dictionary is empty.')
            return default
        return self.items.pop()[1]

    def get_item(self, key, raise_error=False, default=None, error_msg=''):
        try:
            return self.__getitem__(key)
        except KeyError:
            if raise_error:
                raise KeyError(error_msg) if error_msg else KeyError('Key not found.')
            return default
