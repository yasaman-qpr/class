from sqlalchemy.orm import Session
from sqlalchemy import delete , update
from . import models, schemas


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()



def create_cousre(db: Session, course: schemas.Course):
    db_course = models.course(cid=course.cid,cname=course.cname,department=course.department,credit=course.credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



def delete_course (db,id):
    query= delete(models.course).where(models.course.course_id==id)
    db.execute(query)
    db.commit()



def update_course(db,id,date):
    query= update(models.course).where(models.course.course_id==id).values(**data.dict())
    db.execute(query)
    db.commit()








