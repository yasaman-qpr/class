from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


from .database import Base

#دانشجو ها 
class student(Base):
    __tablename__="student"

    STid = Column(String,primary_key=True)
    Fname= Column(String)
    Lname=Column(String)
    fathername=Column(String)
    Ids = Column(Integer) 
    borncity = Column(String)
    address = Column(String)
    zipcode = Column(Integer)
    cphone = Column(Integer)
    hphone = Column(Integer)
    department = Column(String)
    major = Column(String)
    married = Column(String)
    ID = Column(Integer)
    courseids = Column(Integer)
    lids = Column(Integer)



 #استاد 
class Ostad(Base):
    __tablename__ = "Ostad"

    lid = Column(String,primary_key=True)
    Fname = Column(String)
    Lname = Column(String)
    ostadid = Column(Integer)
    department = Column(String)
    major = Column(String)
    Birth = Column(String)
    borncity = Column(String)
    address = Column(String)
    zipcode = Column(Integer)
    cphone = Column(Integer)
    hphone = Column(Integer)
    lcourseids = Column(Integer)

                     
                     
 #درس ها
class Course(Base):
    __tablename__ = "course"

    cid = Column(String, primary_key=True)
    Cname = Column(String)
    department = Column(String)
    credit= Column(Integer)

