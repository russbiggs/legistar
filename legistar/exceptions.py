class ClientError(Exception):
    pass


class ServerError(Exception):
    status = 500


class AuthError(ClientError):
    status = 401


class BadRequestError(ClientError):
    status = 400


class NotFoundError(ClientError):
    status = 404


class GatewayTimeoutError(ServerError):
    status = 504
