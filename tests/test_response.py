import unittest
from accepton.response import Response


class ResponseTest(unittest.TestCase):
    def setUp(self):
        self.response = Response({'foo': 'bar', 'nested': {'one': 'two'}})

    def test_getting_known_attr(self):
        self.assertEqual(self.response.foo, 'bar')

    def test_getting_nested_attr(self):
        self.assertEqual(self.response.nested.one, 'two')

    def test_getting_unknown_attr(self):
        self.assertRaises(AttributeError, lambda: self.response.foobar)

    def test_setting_known_attr(self):
        self.response.foo = 'BAR'
        self.assertEqual(self.response.foo, 'BAR')

    def test_setting_unknown_attr(self):
        self.response.hi = 'there'
        self.assertEqual(self.response.hi, 'there')

    def test_conversion_to_dict(self):
        dictionary = dict(self.response)
        self.assertEqual(dictionary, {'foo': 'bar', 'nested': {'one': 'two'}})

    def test_setting_a_dict_transforms_it(self):
        self.response.foobar = {'hi': 'there'}
        self.assertEqual(isinstance(self.response.foobar, Response), True)
