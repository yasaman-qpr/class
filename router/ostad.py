from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sql_app import crud
import schemas
from sql_app.database import SessionLocal, engine
import datavalidation


router = APIRouter()

#dependecy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/Creatostad/", response_model=schemas.Ostad)
def create_ostad(ostad: schemas.Ostad, db: Session = Depends(get_db)):
    db_ostad = crud.get_ostad(db, ostad.LID)
    if db_ostad:
        raise HTTPException(status_code= 400, detail= "استادی قبلا با این کد ثبت شده است")
    datavalidation.ostad_valid(ostad)
    error = {}
    lcourseid = ostad.lcourseids.split(",")
    for course in lcourseid:
        db_ostad_course = crud.get_course(db,course)
        if db_ostad_course is None:
            error["lcourseid"] = f"این ترم {course} برای تدریس موجود نیست"
    if error:
        raise HTTPException(status_code= 404 , detail=error)
    return crud.create_ostad(db, ostad)


@router.get("/Getostad/{ostad_id}", response_model=schemas.Ostad_out)
def read_Ostad(ostad_id: int, db: Session = Depends(get_db)):
    db_ostad = crud.get_ostad(db, ostad_id)
    if db_ostad is None or len(str(ostad_id)) !=6 :
        raise HTTPException(status_code= 404, detail= "استادی با این ایدی یافت نشد یا کد استاد اشتباه می باشد")
    return db_ostad


@router.put("/updateostad/{ostad_id}", response_model= schemas.Ostad)
def update_ostad(ostad_id: str, ostad:schemas.Ostad, db: Session = Depends(get_db)):
    db_ostad = crud.update_ostad(db, ostad_id, ostad)
    if db_ostad is None or len(str(ostad_id)) !=6 :
        raise HTTPException(status_code= 404, detail= "استادی با این کد یافت نشد یا کد استاد اشتباه می باشد")
    datavalidation.ostad_valid(ostad)
    error = {}
    lcourseid = ostad.lcourseids.split(",")
    for course in lcourseid:
        db_ostad_course = crud.get_course(db,course)
        if db_ostad_course is None:
            error["lcourseid"] = f"این ترم {course} برای تدریس موجود نیست"
    if error:
        raise HTTPException(status_code= 404 , detail=error)
    return db_ostad



@router.delete("/delostad/{ostad_id}",response_model=schemas.Ostad_out)
def delete_ostad(ostad_id:int,db:Session=Depends(get_db)):
    db_ostad =crud.get_ostad(db, ostad_id)
    if db_ostad is None or len(str(ostad_id)) !=6:
        raise HTTPException(status_code= 404, detail= "استادی با این کد یافت نشد یا کد استاد اشتباه می باشد")
    crud.delete_ostad(db,ostad_id)
    return db_ostad
