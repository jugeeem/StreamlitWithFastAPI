from fastapi import Depends

from src.app.auth.util import get_current_active_user
from src.app.schema.auth import User

user_depends: User = Depends(get_current_active_user)
