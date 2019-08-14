import requests

from .exceptions import *


class WrappedSession(requests.Session):
    def __init__(self):
        super(WrappedSession, self).__init__()

    def get(self, url):
        res = super(WrappedSession, self).get(url)
        if res.status_code >= 200 and res.status_code < 400:
            return res
        elif res.status_code == 400:
            raise BadRequestError(res.text)
        elif res.status_code == 403:
            raise AuthError(res.text)
        elif res.status_code == 404:
            text = res.text
            if not text:
                text = "404"
            raise NotFoundError(text)
        elif res.status_code == 504:
            raise GatewayTimeoutError()
        else:
            raise ServerError(res.text)
