from pydantic import BaseModel


class InSignup(BaseModel):
    """
    /auth/signup request body data
    """

    username: str
    password: str
    email: str


class ExistsUser(BaseModel):
    """
    ユーザ存在チェック

    Properties:
        username (str): ユーザ名
    """

    username: str


class OutSignup(BaseModel):
    """
    /auth/signup response body data
    """

    message: str
