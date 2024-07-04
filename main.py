from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sql_app import crud , models
import schemas
from sql_app.database import SessionLocal, engine

#import sys
#from pathlib import Path 
#sys.path[0]=str(Path(sys.path[0]).parent)




models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#دانشجو ها
@app.post("/Creatstu/", response_model=schemas.Student)
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db,STid=student.STid)
    if db_student:
        raise HTTPException(status_code=400, detail="STid already exists")
    return crud.create_student(db=db, student=student)



@app.get("/GetStu/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student



@app.put("/updatestudent/{student_id}", response_model=schemas.Student)
def update_student(student_id: str,student:schemas.Student,db:Session = Depends(get_db)):
    db_student = crud.update_student(db,student_id, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student



@app.get("/delstudent/{student_id}",response_model=schemas.Student)
def delete_student(student_id:int,db:Session=Depends(get_db)):
    db_student = crud.get_student(db,Student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    crud.removestudent(db,Student_id=student_id)
    return db_student



#استاد ها
@app.post("/Creatostad/", response_model=schemas.Ostad)
def create_ostad(ostad: schemas.Ostad, db: Session = Depends(get_db)):
    db_ostad = crud.get_ostad(db,lid=ostad.lid)
    if db_ostad:
        raise HTTPException(status_code=400, detail="ostad already exists")
    return crud.create_ostad(db=db, ostad=ostad)



@app.get("/Getostad/{ostad_id}", response_model=schemas.Ostad)
def read_Ostad(ostad_id: int, db: Session = Depends(get_db)):
    db_ostad = crud.get_ostad(db,ostad_id)
    if db_ostad is None:
        raise HTTPException(status_code=404, detail="ostad not found")
    return db_ostad

@app.put("/updateostad/{ostad_id}", response_model=schemas.Ostad)
def update_ostad(ostad_id: str,ostad:schemas.Ostad,db:Session = Depends(get_db)):
    db_ostad = crud.update_ostad(db,ostad_id, ostad)
    if db_ostad is None:
        raise HTTPException(status_code=404, detail="ostad not found")
    return db_ostad



@app.delete("/delostad/{ostad_id}",response_model=schemas.Ostad)
def delete_ostad(ostad_id:int,db:Session=Depends(get_db)):
    db_ostad =crud.get_ostad(db,ostad_id)
    if db_ostad is None:
        raise HTTPException(status_code=404, detail="ostad notfound")
    crud.deleteostad(db,ostad_id)
    return db_ostad




#درس ها
@app.post("/CreatCou/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db,cid=course.cid)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_course(db,course)



@app.get("/GetCou/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db,course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@app.put("/updatecourse/{course_id}", response_model=schemas.Course)
def update_course(course_id: str,course:schemas.Course,db:Session = Depends(get_db)):
    db_course = crud.update_course(db,course_id, course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course



@app.delete("/delcourse/{course_id}",response_model=schemas.Course)
def delete_course(course_id:int,db:Session=Depends(get_db)):
    db_course = crud.get_course(db,course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course notfound")
    crud.deletecourse(db,course_id)
    return db_course