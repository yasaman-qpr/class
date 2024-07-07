from fastapi import Depends, APIRouter , HTTPException
from sqlalchemy.orm import Session
from sql_app import crud 
import schemas
from sql_app.database import SessionLocal
import datavalidation


router = APIRouter()
#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/CreatCou/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course.CID)
    if db_course:
        raise HTTPException(status_code= 400, detail= "قبلا درسی با این آیدی ثبت شده است")
    datavalidation.cou_valida(course)
    return crud.create_course(db, course)



@router.get("/GetCou/{course_id}", response_model= schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if db_course is None or len(str(course_id)) !=5:
        raise HTTPException(status_code= 404, detail= "درسی با این آیدی موجود نیست یا آیدی اشتباه می باشد")
    return db_course


@router.put("/updatecourse/{course_id}", response_model= schemas.Course)
def update_course(course_id: int, course:schemas.Course, db:Session = Depends(get_db)):
    db_course = crud.update_course(db, course_id, course)
    if db_course is None or len(str(course_id)) !=5:
        raise HTTPException(status_code= 404, detail= "درسی با این آیدی موجود نیست یا آیدی اشتباه می باشد")
    datavalidation.cou_valida(course)
    return db_course



@router.delete("/delcourse/{course_id}",response_model= schemas.Course)
def delete_course(course_id: int, db: Session= Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if db_course is None or len(str(course_id)) !=5:
        raise HTTPException(status_code= 404, detail= "درسی با این آیدی موجود نیست یا آیدی اشتباه می باشد")
    crud.delete_course(db, course_id)
    return db_course