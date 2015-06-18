import unittest
from accepton.base import Base


class Example(Base):
    def __init__(self, attrs):
        super(Example, self).__init__(attrs)
        self.initialize_attr("foo", str)
        self.initialize_attr("foobar", str)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.model = Example({"foo": "bar", "integer": "a"})

    def test_known_property(self):
        self.assertEqual(self.model.foo, "bar")

    def test_unknown_property(self):
        self.assertRaises(AttributeError, lambda: self.model.missing)

    def test_missing_attr(self):
        self.assertEqual(self.model.foobar, None)

    def test_repr(self):
        self.assertEqual(repr(self.model), "Example(foo=bar, integer=a)")

    def test_initialize_attr_for_correct_type(self):
        self.model.initialize_attr("integer", int)
        self.assertEqual(self.model.integer, "a")
