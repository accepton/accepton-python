class Headers(object):
    def __init__(self, client):
        self.client = client

    def request_headers(self):
        headers = {}
        headers["accept"] = "application/json"
        headers["authorization"] = self.__bearer_auth_header()
        headers["user-agent"] = self.client.user_agent

        return headers

    def __bearer_auth_header(self):
        return "Bearer {0}".format(self.client.api_key)
