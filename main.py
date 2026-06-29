from fastapi import FastAPI, Depends, HTTPException
import schemas
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Grade Tracker", 
              description="Track student grades with FastAPI",
              version="1.0.0")


#Create
@app.post("/students", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

#READ ALL
@app.get("/students/", response_model=List[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

#Read one
@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

#Update
@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return db_student

#Delete
@app.delete("/students/{student_id}", response_model=schemas.StudentResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return db_student