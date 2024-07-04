from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sql_app.database import Base

#دانشجو ها 
class Student(Base):
    __tablename__="student"

    STid = Column(String,primary_key=True)
    Fname= Column(String)
    Lname=Column(String)
    fathername=Column(String)
    birth=Column(String)
    Ids = Column(String) 
    borncity = Column(String)
    address = Column(String)
    zipcode = Column(Integer)
    cphone = Column(String)
    hphone = Column(String)
    department = Column(String)
    major = Column(String)
    married = Column(String)
    id = Column(String)
    Scourseids = Column(String)
    lids = Column(String)



 #استاد 
class Ostad(Base):
    __tablename__ = "Ostad"

    lid = Column(Integer,primary_key=True)
    Fname = Column(String)
    Lname = Column(String)
    id = Column(String)
    department = Column(String)
    major = Column(String)
    Birth = Column(String)
    borncity = Column(String)
    address = Column(String)
    zipcode = Column(Integer)
    cphone = Column(String)
    hphone = Column(String)
    lcourseids = Column(String)

                     
                     
 #درس ها
class Course(Base):
    __tablename__ = "course"

    cid = Column(String, primary_key=True)
    Cname = Column(String)
    department = Column(String)
    credit= Column(Integer)

