class RoseDictionary:
    def __init__(self):
        self.items = []

    def __setitem__(self, key, value):
        for index, item in enumerate(self.items):
            if item[0] == key:
                self.items[index] = (key, value)
                return
        self.items.append((key, value))

    def __getitem__(self, key):
        for item in self.items:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def __delitem__(self, key):
        for index, item in enumerate(self.items):
            if item[0] == key:
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
                if error_msg:
                    raise KeyError(error_msg)
                else:
                    raise KeyError('error_msg')
            else:
                if default:
                    return default
                else:
                    print('Dictionary was empty and no default value/message was specified.')
        else:
            return self.items.pop()[1]

    def get_item(self, key, raise_error=False, default=None, error_msg=''):
        try:
            return self.__getitem__(key)
        except KeyError:
            if raise_error:
                if error_msg:
                    raise KeyError(error_msg)
                else:
                    raise KeyError('error_msg')
            else:
                if default:
                    return default
                else:
                    print('Dictionary was empty and no default value/message was specified.')

