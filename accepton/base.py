from datetime import datetime

DEFAULTS = {
    datetime: None,
    dict: {},
    int: None,
    str: None,
}


class Base(object):
    def __init__(self, attrs={}):
        self.attrs = attrs

    def __repr__(self):
        attrs = sorted(["%s=%s" % (k, v) for (k, v) in self.attrs.items()])
        return "%s(%s)" % (self.__class__.__name__, ", ".join(attrs))

    def initialize_attr(self, attr, data_type):
        if attr not in self.attrs or self.attrs[attr] is None:
            setattr(self, attr, DEFAULTS[data_type])
            return

        if isinstance(self.attrs[attr], data_type):
            setattr(self, attr, self.attrs[attr])
        else:
            try:
                value = data_type(self.attrs[attr])
            except ValueError:
                value = self.attrs[attr]
            setattr(self, attr, value)
