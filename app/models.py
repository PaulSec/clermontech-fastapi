from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.types import DateTime
from .database import Base
from sqlalchemy.orm import relationship

Base = declarative_base()


class SpeakerInfo(Base):
    __tablename__ = "speakers"

    id = Column(Integer, primary_key=True)  # Auto-increment should be default
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    created_at = Column(DateTime)

    presentations = relationship("TalkInfo", back_populates="speaker_talks")
    speaker = relationship("TalkInfo", back_populates="speaker")


class TalkInfo(Base):
    __tablename__ = "talks"
    id = Column(Integer, primary_key=True)  # Auto-increment should be default
    event_id = Column(Integer, ForeignKey("events.id"))
    speaker_id = Column(Integer, ForeignKey("speakers.id"))
    name = Column(String(255), index=True)
    duration = Column(Integer, index=True)
    created_at = Column(DateTime)

    speaker = relationship("SpeakerInfo", back_populates="speaker")
    speaker_talks = relationship("SpeakerInfo", back_populates="presentations")
    event_talks = relationship("EventInfo", back_populates="presentations")


class EventInfo(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)  # Auto-increment should be default
    name = Column(String(255), index=True)
    created_at = Column(DateTime)
    presentations = relationship("TalkInfo", back_populates="event_talks")
