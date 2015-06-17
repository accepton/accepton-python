class Response(dict):
    def __init__(self, *args, **kwargs):
        super(Response, self).__init__(*args, **kwargs)

        for (key, value) in self.items():
            self[key] = self.convert_value(value)

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __getitem__(self, item):
        try:
            return super(Response, self).__getitem__(item)
        except KeyError as error:
            raise AttributeError(*error.args)

    def __setattr__(self, name, value):
        if isinstance(value, dict):
            return self.__setitem__(name, Response(value))
        else:
            return self.__setitem__(name, value)

    def convert_value(self, value, duping=False):
        if isinstance(value, Response):
            return value.copy()
        elif isinstance(value, dict):
            return Response(value)
        elif isinstance(value, list):
            return [self.convert_value(v) for v in value]
        else:
            return value
