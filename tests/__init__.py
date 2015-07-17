import os


def fixture_response(path):
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures',
                           path)) as fixture:
        return fixture.read()
