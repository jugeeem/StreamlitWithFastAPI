from pydantic import BaseModel

class OutUpdateConfig(BaseModel):
    """
    ユーザ情報更新レスポンススキーマ

    Attributes:
        result (bool): 更新結果
    """

    status: int
    message: str
