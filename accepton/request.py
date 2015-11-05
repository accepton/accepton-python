try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
import dateutil.parser
import requests
from .error import error_from_response
from .headers import Headers
from .response import Response

__all__ = ["Request"]

URLS = {
    "development": "http://checkout.accepton.dev",
    "staging": "https://staging-checkout.accepton.com",
    "production": "https://checkout.accepton.com"
}


class Request(object):

    def __init__(self, client, request_method, path, options={}):
        options = self.__options_with_defaults(options)
        url = URLS[options.pop("environment")]
        self.client = client
        self.request_method = request_method
        self.uri = urlparse(path if path.startswith("http") else url + path)
        self.options = options
        self.headers = Headers(client).request_headers()

    def perform(self):
        args = self.__build_request_args()
        response = requests.request(self.request_method,
                                    self.uri.geturl(),
                                    **args)
        response_body = Response(response.json(object_hook=self.__deserialize))
        return self.__fail_or_return_response_body(response_body,
                                                   response.status_code)

    def __build_request_args(self):
        options_key = 'params' if self.request_method == 'get' else 'json'

        args = {}
        args["headers"] = self.headers
        args[options_key] = self.options

        return args

    def __default_options(self):
        return {"environment": "production"}

    def __deserialize(self, response):
        for attr, value in response.items():
            if attr == "created" or attr.endswith("_at"):
                response[attr] = dateutil.parser.parse(response[attr])

        return response

    def __fail_or_return_response_body(self, body, status_code):
        error = error_from_response(body, status_code)
        if error is not None:
            raise error
        else:
            return body

    def __options_with_defaults(self, options):
        defaults = self.__default_options()
        defaults.update(options)
        return defaults
