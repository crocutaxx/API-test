from pydantic import BaseModel, field_validator, conint, ValidationInfo
from datetime import datetime
from typing import Optional, Literal


class Dialog(BaseModel):
    id: str
    groupId: int
    userId: Optional[int] = None
    messageId: Optional[int] = None
    messageSettingsId: Optional[int] = None
    name: str
    surname: Optional[str] = None
    image: Optional[str] = None
    message: Optional[str] = None
    fileText: Optional[str] = None
    group: bool
    time: Optional[datetime] = None
    unread: str

    @field_validator('id', 'name', 'message')
    def check_non_empty_string(cls, v, field: ValidationInfo):
        if not v:
            raise ValueError(f'{field.field_name} cannot be empty')
        return v


class GetUserDialogs(BaseModel):
    root: list[Dialog]
