from sqlalchemy.orm import Session

from . import models, schemas


def get_speaker_by_first_name(db: Session, first_name: str = "", last_name: str = ""):
    return (
        db.query(models.SpeakerInfo)
        .filter(models.SpeakerInfo.first_name == first_name)
        .filter(models.SpeakerInfo.last_name == last_name)
        .first()
    )


def get_speakers(db: Session):
    return db.query(models.SpeakerInfo).all()


def get_speaker(db: Session, speaker_id=-1):
    return (
        db.query(models.SpeakerInfo).filter(models.SpeakerInfo.id == speaker_id).first()
    )


def get_events(db: Session):
    return db.query(models.EventInfo).all()


def get_event(db: Session, event_id=-1):
    return db.query(models.EventInfo).filter(models.EventInfo.id == event_id).first()


def create_speaker(db: Session, speaker: schemas.SpeakerInfoBase):
    db_speaker = models.SpeakerInfo(**speaker.dict())
    db.add(db_speaker)
    db.commit()
    db.refresh(db_speaker)
    return db_speaker


def create_talk(db: Session, talk: schemas.TalkBase):
    print(talk.dict())
    db_talk = models.TalkInfo(**talk.dict())
    db.add(db_talk)
    db.commit()
    db.refresh(db_talk)
    return db_talk


def create_event(db: Session, event: schemas.EventBase):
    db_event = models.EventInfo(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event