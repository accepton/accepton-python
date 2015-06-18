import os


def fixture_response(path):
    return open(os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        path)).read()
