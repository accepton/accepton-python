import unittest
from accepton.error import error_from_response, Error, ERRORS
from accepton.response import Response


class ErrorFromResponseTest(unittest.TestCase):
    def setUp(self):
        self.response = Response({'error': {'message': 'error message'}})

    def test_status_code_mapping(self):
        for (status, error) in ERRORS.items():
            instance = error_from_response(self.response, status)
            self.assertEqual(isinstance(instance, error), True)


class ErrorTest(unittest.TestCase):
    def setUp(self):
        self.error = Error('this is the error message', 400)

    def test_message(self):
        self.assertEqual(str(self.error), 'this is the error message')

    def test_status_code(self):
        self.assertEqual(self.error.status_code, 400)
