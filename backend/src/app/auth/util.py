from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from src.app.core import settings
from src.app.db.connection import pool
from src.app.db.sql import auth_query
from src.app.db.util import execute_read_query
from src.app.schema.auth import ExistsUser, TokenData, User, UserInDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def verify_password(plain_password, hashed_password) -> bool:
    """
    パスワードの検証

    Args:
        plain_password (str): 平文パスワード
        hashed_password (str): ハッシュ化されたパスワード

    Returns:
        bool: パスワードが一致するかどうか
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    """
    パスワードのハッシュ化

    Args:
        password (str): 平文パスワード

    Returns:
        str: ハッシュ化されたパスワード
    """
    return pwd_context.hash(password)


async def get_user(username: str) -> UserInDB | None:
    """
    ユーザ情報の取得

    Args:
        username (str): ユーザ名

    Returns:
        list[UserInDB]: ユーザ情報
    """
    param = [username]
    response = await execute_read_query(auth_query.GET_USER, param, UserInDB)
    if not response:
        return None
    result = response[0]

    return result


async def authenticate_user(username: str, password: str) -> UserInDB | bool:
    """
    ユーザ認証

    Args:
        username (str): ユーザ名
        password (str): パスワード

    Returns:
        UserInDB | bool: ユーザ情報 or False
    """
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user


def create_access_token(form_data: dict, expires_delta: timedelta | None = None) -> str:
    """
    アクセストークンの生成

    Args:
        form_data (dict): ユーザ情報
        expires_delta (timedelta | None, optional): 有効期限. Defaults to None.

    Returns:
        str: アクセストークン
    """
    to_encode = form_data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.BACKEND_SECRET_KEY, algorithm=settings.ALGORITHM
    )

    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    """
    現在のユーザ情報を取得

    Args:
        token (str): トークン

    Returns:
        User: ユーザ情報
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.BACKEND_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    """
    現在のアクティブなユーザ情報を取得

    Args:
        current_user (User): ユーザ情報

    Returns:
        User: ユーザ情報
    """
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )

    return current_user


async def exists_user(name: str) -> bool:
    """
    ユーザの存在確認

    Args:
        name (str): ユーザ名

    Returns:
        bool: ユーザが存在するかどうか
    """
    result = False
    param = [name]
    response = await execute_read_query(auth_query.EXISTS_USER, param, ExistsUser)
    if response:
        result = True

    return result


async def register_user(param_user: list, param_user_info: list) -> None:
    """
    新規ユーザ登録

    Args:
        param_user (list): ユーザ情報
        param_user_info (list): ユーザ詳細情報

    Returns:
        None
    """
    async with pool.connection() as conn:
        await conn.execute(auth_query.INSERT_USR_USER, param_user)
        await conn.execute(auth_query.INSERT_USR_USER_INFO, param_user_info)
