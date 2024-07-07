from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sql_app import crud , models
import schemas
from sql_app.database import SessionLocal, engine
import datavalidation
import re

router = APIRouter()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/Creatstu/", response_model = schemas.Student)
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student.STID)
    if db_student:
        raise HTTPException(status_code= 400, detail= "دانشجویی با این آیدی قبلا ثبت شده است")
    datavalidation.stu_valid(student)
    error = {}
    lids = student.LIDs.split(",")
    scourseids = student.Scourseids.split(",")
    for course in scourseids:
        db_students_course = crud.get_course(db,course)
        if db_students_course is None:
            error[course] = f"این ترم {course} ارایه نمیشود"
    for ostad in lids:
        db_student_ostad = crud.get_ostad(db,ostad)
        if db_student_ostad is None:
            error[ostad] = f" استاد {ostad} ارایه نمی دهد"
    if error:
        raise HTTPException(detail=error , status_code= 404)
    return crud.create_student(db, student)



@router.get("/GetStu/{student_id}", response_model= schemas.Student_out)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    stid= r"^(401|402|403)114150([01-99]{2})$"
    if db_student is None or re.match(pattern=stid , string=str(student_id))== None:
        raise HTTPException(status_code=404, detail="دانشجویی با این آیدی موجود نیست یا کد دانشجویی اشتباه می باشد")
    return db_student



@router.put("/updatestudent/{student_id}", response_model= schemas.Student)
def update_student(student_id: str, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    stid= r"^(401|402|403)114150([01-99]{2})$"
    if db_student is None or re.match(pattern=stid , string=str(student_id))== None:
        raise HTTPException(status_code= 404, detail= "دانشجویی با این آیدی موجود نیست یا کد دانشجویی اشتباه می باشد")
    datavalidation.stu_valid
    error = {}
    lids = student.LIDs.split(",")
    scourseids = student.Scourseids.split(",")
    for course in scourseids:
        db_students_course = crud.get_course(db,course)
        if db_students_course is None:
            error[course] = f"این ترم {course} ارایه نمیشود"
    for ostad in lids:
        db_student_ostad = crud.get_ostad(db,ostad)
        if db_student_ostad is None:
            error[ostad] =f" استاد {ostad} ارایه نمی دهد"
    if error:
        raise HTTPException(detail=error , status_code= 404)
    return db_student



@router.delete("/delstudent/{student_id}", response_model= schemas.Student_out)
def delete_student(student_id: int, db: Session= Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    stid= r"^(401|402|403)114150([01-99]{2})$"
    if db_student is None or re.match(pattern=stid , string=str(student_id))== None:
        raise HTTPException(status_code= 404, detail="دانشجویی با این آیدی موجود نیست یا کد دانشجویی اشتباه می باشد")
    crud.delete_student(db, student_id)
    return db_student