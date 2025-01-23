from pydantic import BaseModel


class InConfig(BaseModel):
    """
    ユーザ情報リクエストペイロードスキーマ

    Attributes:
        email (str): メールアドレス
        first_name (str): 名
        last_name (str): 姓

        zip_code (str): 郵便番号
        state (str): 都道府県
        city (str): 市区町村
        address (str): 住所
        phone_number (str): 電話番号
        birthday (str): 誕生日
    """

    email: str
    first_name: str
    first_name_ruby: str
    last_name: str
    last_name_ruby: str
    zip_code: str
    state: str
    city: str
    address: str
    phone_number: str
    birthday: str
