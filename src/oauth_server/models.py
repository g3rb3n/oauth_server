from pydantic import BaseModel


class ApiError(BaseModel):
    """
    """
    exception: str
    message: str

class Code(BaseModel):
    """
    """
    code: str

class Configuration(BaseModel):
    """
    """
    client_id: str
    client_secret: str
    scope: str
