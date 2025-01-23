from datetime import date

from pydantic import BaseModel


class ReadConfig(BaseModel):
    """
    ユーザ情報取得スキーマ

    Attributes:
        email (str): メールアドレス
        first_name (str | None): 名
        first_name_ruby (str | None): 名ルビ
        last_name (str | None): 姓
        last_name_ruby (str | None): 姓ルビ
        zip_code (str | None): 郵便番号
        state (str | None): 都道府県
        city (str | None): 市区町村
        address (str | None): 住所
        phone_number (str | None): 電話番号
        birthday (str | None): 誕生日
    """

    email: str
    first_name: str | None
    first_name_ruby: str | None
    last_name: str | None
    last_name_ruby: str | None
    zip_code: str | None
    state: str | None
    city: str | None
    address: str | None
    phone_number: str | None
    birthday: date | None


class OutReadConfig(BaseModel):
    """
    ユーザ情報取得レスポンススキーマ

    Attributes:
        contents (ReadConfig): ユーザ情報
    """

    contents: ReadConfig
