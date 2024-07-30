from pydantic import BaseModel, field_validator, ValidationInfo
from datetime import datetime
from typing import Optional


class Creator(BaseModel):
    id: int
    email: str
    password: str
    surname: str
    name: str
    patronymic: Optional[str] = None
    image: Optional[str] = None
    blocked: bool
    deleted: bool
    createdAt: datetime
    updatedAt: datetime

    @field_validator('surname', 'name', 'email', 'patronymic')
    def check_names_not_empty(cls, v, field: ValidationInfo):
        if field.field_name in ['surname', 'name'] and not v:
            raise ValueError(f'{field.field_name} cannot be empty')
        return v


class CreatorLow(BaseModel):
    id: int
    surname: str
    name: str

    @field_validator('id', 'name', 'surname')
    def check_names_not_empty(cls, v, field: ValidationInfo):
        if not v:
            raise ValueError(f'{field.field_name} cannot be empty')
        return v


class MeetBase(BaseModel):
    id: int
    roomId: str
    topic: str
    date: str
    time: str
    description: Optional[str] = None
    speakerVideo: bool
    speakerAudio: bool
    membersVideo: bool
    membersAudio: bool
    waitingHall: bool
    recordVideo: Optional[str] = None
    recordAudio: Optional[str] = None
    createdAt: str
    updatedAt: str

    @field_validator('id', 'roomId', 'topic', 'time', 'description', 'recordVideo', 'recordAudio',
                     mode='before')
    def check_non_empty_string(cls, value, field):
        if isinstance(value, str) and not value.strip():
            raise ValueError(f"{field.name} cannot be empty")
        return value

    @field_validator('createdAt', 'updatedAt', 'date', mode='before')
    def check_datetime(cls, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} is not a valid datetime")
        return value


class CreateNewMeeting(BaseModel):
    roomId: str
    topic: str
    date: datetime
    time: str
    durationHour: int
    durationMinute: str
    description: Optional[str] = None
    password: Optional[str] = None
    speakerVideo: bool
    speakerAudio: bool
    membersVideo: bool
    membersAudio: bool
    waitingHall: bool
    calendar: str
    template: str
    creator: Creator
    recordVideo: Optional[str] = None
    recordAudio: Optional[str] = None
    id: int
    status: str
    createdAt: datetime
    updatedAt: datetime

    @field_validator('roomId', 'topic', 'time', 'durationMinute', 'calendar', 'template', 'status')
    def check_non_empty_string(cls, v, field: ValidationInfo):
        if not v:
            raise ValueError(f'{field.field_name} cannot be empty')
        return v


class GetMeetingByMeetId(MeetBase):
    password: Optional[str] = None
    durationHour: int
    durationMinute: int
    calendar: int
    template: int
    scheduleMeetingDocuments: list
    creator: CreatorLow
    status: str

    @field_validator('password', 'creator', 'scheduleMeetingDocuments', 'status', mode='before')
    def check_non_empty_string(cls, value, field):
        if isinstance(value, str) and not value.strip():
            raise ValueError(f"{field.name} cannot be empty")
        return value

    @field_validator('durationMinute', 'calendar', 'template', mode='before')
    def check_positive_integer(cls, value, field):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{field.name} must be a positive integer")
        return value

