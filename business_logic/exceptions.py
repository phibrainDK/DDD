from rest_framework import status


class IlegalStateException(Exception):
    status_code: int = status.HTTP_403_FORBIDDEN
    error_code: str
    error_message: str

    @property
    def detail(self):
        return {
            "error_code": self.error_code,
            "error_message": self.error_message,
            "status_code": self.status_code,
        }


class InvalidEditStatus(IlegalStateException):
    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "DDD001"
    error_message = "The given state is ilegal"
