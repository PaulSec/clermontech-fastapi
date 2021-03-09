from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class TalkBase(BaseModel):
    name: str
    duration: int
    created_at: datetime
    event_id: int
    speaker_id: int

    class Config:
        orm_mode = True


# class used when integrated in the DB (id = auto-increment)
class SpeakerInfoBase(BaseModel):
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        orm_mode = True


# class used when integrated in the DB (id = auto-increment)
class SpeakerTalk(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class Talk(BaseModel):
    name: str
    duration: int
    speaker_id: int

    class Config:
        orm_mode = True


class EventTalk(BaseModel):
    name: str
    duration: int
    # speaker_id: int
    speaker: SpeakerTalk

    class Config:
        orm_mode = True


# class used for the registration (through the API)
class SpeakerRegistration(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


# class used as a HTTP response through the API
class SpeakerOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    created_at: datetime
    presentations: Optional[List[Talk]] = []

    class Config:
        orm_mode = True


# class used when integrated in the DB (id = auto-increment)
class EventBase(BaseModel):
    name: str
    created_at: datetime

    class Config:
        orm_mode = True


# class used for the registration (through the API)
class EventRegistration(BaseModel):
    name: str

    class Config:
        orm_mode = True


# class used as a HTTP response through the API
class EventOut(BaseModel):
    id: int
    name: str
    created_at: datetime
    presentations: Optional[List[EventTalk]] = []

    class Config:
        orm_mode = True
