from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, Request

from . import models, schemas, crud
from .database import engine, SessionLocal
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # start_time = time.time()
    response = await call_next(request)
    # process_time = time.time() - start_time
    # response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Paul-Header"] = "Welcome back you all and stay safe!"
    return response


@app.post("/speakers", response_model=schemas.SpeakerOut)
def create_user(speaker: schemas.SpeakerRegistration, db: Session = Depends(get_db)):
    db_speaker = crud.get_speaker_by_first_name(
        db, first_name=speaker.first_name, last_name=speaker.last_name
    )
    if db_speaker:
        raise HTTPException(status_code=400, detail="Speaker already registered")
    speaker_db = schemas.SpeakerInfoBase(
        first_name=speaker.first_name,
        last_name=speaker.last_name,
        created_at=datetime.now(),
    )
    return crud.create_speaker(db=db, speaker=speaker_db)


@app.get("/speakers", response_model=List[schemas.SpeakerOut])
def get_speakers(db: Session = Depends(get_db)):
    return crud.get_speakers(db=db)


@app.get("/speakers/{speaker_id}", response_model=schemas.SpeakerOut)
def get_speaker(speaker_id: int, db: Session = Depends(get_db)):
    return crud.get_speaker(db=db, speaker_id=speaker_id)


@app.get("/events", response_model=List[schemas.EventOut])
def get_events(db: Session = Depends(get_db)):
    return crud.get_events(db=db)


@app.get("/events/{event_id}", response_model=schemas.EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = crud.get_event(db=db, event_id=event_id)
    print(event.presentations)
    return event


@app.post("/events", response_model=schemas.EventOut)
def create_event(event: schemas.EventRegistration, db: Session = Depends(get_db)):
    event_db = schemas.EventBase(**event.dict(), created_at=datetime.now())
    return crud.create_event(db=db, event=event_db)


@app.post("/events/{event_id}/talks", response_model=schemas.Talk)
def create_talk(event_id: int, talk: schemas.Talk, db: Session = Depends(get_db)):
    db_event = crud.get_event(db, event_id=event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found, omgwtfbbq?")

    db_speaker = crud.get_speaker(db, speaker_id=talk.speaker_id)
    if not db_speaker:
        raise HTTPException(status_code=404, detail="User not found, w00t?")

    talk_db = schemas.TalkBase(
        **talk.dict(), created_at=datetime.now(), event_id=event_id
    )
    return crud.create_talk(db=db, talk=talk_db)
