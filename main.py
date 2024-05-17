from fastapi import FastAPI, Depends, HTTPException
from models import Student
from database import get_db
from pydantic import BaseModel

app = FastAPI(title="This is SKV FastAPI App")


class StudentDetails(BaseModel):
    name : str
    clas : int




@app.get("/")
async def get():
    return {"msg":"Hello Radha ji"}


@app.get("/student/{student_id}")
async def get_data(student_id : int, db = Depends(get_db)):

    student_data = db.query(Student).filter(Student.id == student_id).first()

    if student_data is None:
        raise HTTPException(status_code=404, detail="Student Record Not Found")
    
    
    return {"Student":student_data}


#get all student records
@app.get("/student")
async def get_all_student(db = Depends(get_db)):

    student_data = db.query(Student).all()

    if student_data is None:
        raise HTTPException(status_code=404, detail="Student Record Not Found")

    return student_data


#post a student
@app.post("/student")
async def post_data(student_details : StudentDetails, db = Depends(get_db)):

    student_data = Student(name = student_details.name, clas = student_details.clas)

    db.add(student_data)
    db.commit()
    db.close()

    return student_details


#update a student
@app.put("/student/{student_id}")
async def update_data(student_id : int, student_details : StudentDetails, db = Depends(get_db)):

    student_data  = db.query(Student).filter(Student.id == student_id).first()

    if student_data is None:
        raise HTTPException(status_code=404, detail="Student record not found")
    
    student_data.name = student_details.name
    student_data.clas = student_details.clas

    db.commit()
    db.close()

    return student_details


#delete Student records
@app.delete("/studnet/{student_id}")
async def delete_data(student_id : int, db = Depends(get_db)):
    
    student_data = db.query(Student).filter(Student.id == student_id).first()

    if student_data is None:
        raise HTTPException(status_code=404, detail="Student record not found")
    
    db.delete(student_data)

    db.commit()

    db.close()

    return {"msg":"Record deleted successfully!"}