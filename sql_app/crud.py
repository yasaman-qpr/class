from sqlalchemy.orm import Session
#import sys
#from pathlib import Path 
#sys.path[0]=str(Path(sys.path[0]).parent)
import schemas
from sql_app import models



#دانشجو ها
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.STid == student_id).first()



def create_student(db: Session, student: schemas.Student):
    db_student = models.student(STid=student.STid,Fname=student.Fname,Lname=student.Lname,fathername=student.fathername,birth=student.birth,
                    Ids=student.ids,borncity=student.borncity,address=student.address,zipcode=student.zipcode,cphone=student.cphone,
                    hphone=student.hphone,department=student.department,major=student.major,married=student.married,ID=student.ID,
                    Scourseids=student.Scourseids,lids=student.lids)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student



def update_student(db:Session, student_id: str, student : models.Student):
    db_student = db.query(models.Student).filter(models.student.STid == student_id).first()
    if db_student is None:
        return db_student
    else:
        for key , value in student.dict().items():
            setattr(db_student.key,value)
        db.commit()
        db.refresh(db_student)
        return db_student
    


def remove_student(db :Session,Student_id:int):
    db_student = db.query(models.Student).filter(models.Student.STid == Student_id).first()
    db.delete(db_student)
    db.commit()



#اساتید
def get_ostad(db: Session, ostad_id: int):
    return db.query(models.Ostad).filter(models.Ostad.id == ostad_id).first()



def create_ostad(db: Session, ostad: schemas.Ostad):
    db_ostad = models.ostad(lid=ostad.lid,Fname=ostad.Fname,Lname=ostad.Lname,ostadid=ostad.ostadid,department=ostad.department,
                    major=ostad.major,Birth=ostad.Birth,borncity=ostad.borncity,address=ostad.address,zipcode=ostad.zipcode,
                    cphone=ostad.cphone,hphone=ostad.hphone,lcourseids=ostad.lcourseids)
    db.add(db_ostad)
    db.commit()
    db.refresh(db_ostad)
    return db_ostad



def update_ostad(db:Session, ostad_id: str, ostad : models.Ostad):
    db_ostad = db.query(models.Ostad).filter(models.ostad.lid == ostad_id).first()
    if db_ostad is None:
        return db_ostad
    else:
        for key , value in ostad.dict().items():
            setattr(db_ostad,key,value)
        db.commit()
        db.refresh(db_ostad)
        return db_ostad
    


def remove_ostad(db :Session,ostad_id:int):
    db_ostad = db.query(models.Ostad).filter(models.Ostad.lid == ostad_id).first()
    db.delete(db_ostad)
    db.commit()








#درس ها
def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.cid == course_id).first()



def create_cousre(db: Session, course: schemas.Course):
    db_course = models.course(cid=course.cid,cname=course.cname,department=course.department,credit=course.credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



def update_course(db:Session, course_id: str, course : models.Course):
    db_course = db.query(models.Course).filter(models.course.cid == course_id).first()
    if db_course is None:
        return db_course
    else:
        for key , value in course.dict().items():
            setattr(db_course.key,value)
        db.commit()
        db.refresh(db_course)
        return db_course
    


def removecourse(db :Session,Course_id:int):
    db_course = db.query(models.Course).filter(models.Course.cid == Course_id).first()
    db.delete(db_course)
    db.commit()









