from fastapi import FastAPI
from sql_app import models
from sql_app.database import engine
from router import course , ostad , student



app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(course.router, tags= ['course'])
app.include_router(ostad.router, tags= ['ostad'])
app.include_router(student.router, tags= ['student'])