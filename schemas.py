from pydantic import BaseModel



class Student(BaseModel):
    STID: str
    Fname: str 
    Lname: str
    fathername: str
    birth: str
    IDS: str
    borncity: str
    address: str
    zipcode: int
    cphone: str
    hphone: str
    department: str
    major: str
    married: str
    ID: str
    Scourseids: str
    LIDs: str
    
class Student_out(BaseModel):
    STID: str
    Fname: str
    Lname: str
    fathername: str


class Ostad(BaseModel):
    LID: int
    Fname: str
    Lname: str 
    ID : str 
    department: str 
    major: str 
    Birth: str 
    borncity: str
    address: str
    zipcode: int
    cphone: str
    hphone: str
    lcourseids: str

class Ostad_out(BaseModel):
    LID: int
    Fname: str
    Lname: str
    ID: str


class Course(BaseModel):
    CID: str
    Cname: str
    department : str
    credit : int
    