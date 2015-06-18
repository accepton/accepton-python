from ..request import Request

__all__ = ["Utils"]


class Utils(object):
    def as_params(self, args):
        if 'self' in args:
            args.pop('self')

        return dict((k, v) for k, v in args.items() if v)

    def perform_post_with_object(self, path, params, klass):
        return self.perform_request_with_object('post', path, params, klass)

    def perform_request(self, request_method, path, params):
        request = Request(self, request_method, path,
                          self._with_environment(params))
        return request.perform()

    def perform_request_with_object(self, request_method, path, params, klass):
        response = self.perform_request(request_method, path, params)
        return klass(response)

    def _with_environment(self, params):
        copy = params.copy()
        copy.update({'environment': self.environment})
        return copy
