from pydantic import BaseModel



class Student(BaseModel):
    STid: str
    Fname: str 
    Lname: str
    fathername: str
    birth: str
    Ids: str
    borncity: str
    address: str
    zipcode: int
    cphone: str
    hphone: str
    department: str
    major: str
    married: str
    Id: str
    Scourseids: str
    lids: str



class Ostad(BaseModel):
    lid: int
    Fname: str
    Lname: str 
    id : str 
    department: str 
    major: str 
    Birth: str 
    borncity: str
    address: str
    zipcode: int
    cphone: str
    hphone: str
    lcourseids: str



class Course(BaseModel):
    cid: str
    Cname: str
    department : str
    credit : int
    