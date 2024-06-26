from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import sys
from pathlib import Path 
sys.path[0]=str(Path(sys.path[0]).parent)
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/CreatCou/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db,cid=course.cid)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_course(db=db, course=course)



@app.get("/GetCou/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course




