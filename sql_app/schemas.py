from typing import Union

from pydantic import BaseModel
class student(BaseModel):
    STid: str
    Fname: str 
    Lname: str
    fathername: str
    Ids: int
    borncity: str
    address: str
    zipcode: int
    cphone: int
    hphone: int
    department: str
    major: str
    married: str
    Ids: int
    courseids: int
    lids: int



class Ostad(BaseModel):
    lid: str
    Fname: str
    Lname: str 
    ostadid : int 
    department: str 
    major: str 
    Birth: str 
    borncity: str
    address: str
    zipcode: int
    cphone: int
    hphone:int
    lcourseids:int



class Course(BaseModel):
    cid: str
    Cname: str
    department : str
    credit : int
    