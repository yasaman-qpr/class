from sqlalchemy import Column, String, Integer
from sql_app.database import Base


#دانشجو ها 
class Student(Base):
    __tablename__="Student"

    STID = Column(String, primary_key = True)
    Fname= Column(String)
    Lname=Column(String)
    fathername=Column(String)
    birth=Column(String)
    IDS = Column(String) 
    borncity = Column(String)
    address = Column(String)
    zipcode = Column(Integer)
    cphone = Column(String)
    hphone = Column(String)
    department = Column(String)
    major = Column(String)
    married = Column(String)
    ID = Column(String)
    Scourseids = Column(String)
    LIDs = Column(String)



 #استاد 
class Ostad(Base):
    __tablename__ = "Ostad"

    LID = Column(Integer, primary_key = True)
    Fname = Column(String)
    Lname = Column(String)
    ID = Column(String)
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
    __tablename__ = "Course"

    CID = Column(String, primary_key = True)
    Cname = Column(String)
    department = Column(String)
    credit= Column(Integer)