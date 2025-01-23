from pydantic import BaseModel


class Token(BaseModel):
    """
    /auth/token response body data

    Properties:
        access_token (str): アクセストークン
        token_type (str): トークンタイプ
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    /auth/token response body data
    """

    username: str


class InToken(BaseModel):
    """
    /auth/token request body data
    """

    name: str
    password: str


class User(BaseModel):
    """
    ユーザ情報
    """

    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    """
    ユーザ情報
    """

    hashed_password: str
