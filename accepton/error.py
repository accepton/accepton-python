__all__ = ["error_from_response", "parse_error", "Error", "ClientError",
           "ServerError", "BadRequest", "Unauthorized", "InternalServerError",
           "BadGateway", "ServiceUnavailable", "GatewayTimeout"]


def error_from_response(response_body, status_code):
    if status_code not in ERRORS:
        return None

    error_class = ERRORS[status_code]
    message = parse_error(response_body)
    return error_class(message, status_code)


def parse_error(body):
    if body is None or not any(body):
        return ""

    return body.error.message


class Error(Exception):
    def __init__(self, message='', code=None):
        super(Error, self).__init__(message)
        self.status_code = code


class ClientError(Error):
    """Raised when AcceptOn returns a 4xx HTTP status code"""


class BadRequest(ClientError):
    """Raised when AcceptOn returns a 400 HTTP status code"""


class Unauthorized(ClientError):
    """Raised when AcceptOn returns a 401 HTTP status code"""


class NotFound(ClientError):
    """Raised when AcceptOn returns a 404 HTTP status code"""


class ServerError(Error):
    """Raised when AcceptOn returns a 5xx HTTP status code"""


class InternalServerError(ServerError):
    """Raised when AcceptOn returns a 500 HTTP status code"""


class BadGateway(ServerError):
    """Raised when AcceptOn returns a 502 HTTP status code"""


class ServiceUnavailable(ServerError):
    """Raised when AcceptOn returns a 503 HTTP status code"""


class GatewayTimeout(ServerError):
    """Raised when AcceptOn returns a 504 HTTP status code"""


ERRORS = {
    400: BadRequest,
    401: Unauthorized,
    404: NotFound,
    500: InternalServerError,
    502: BadGateway,
    503: ServiceUnavailable,
    504: GatewayTimeout
}
