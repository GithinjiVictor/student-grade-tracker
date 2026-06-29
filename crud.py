from sqlalchemy.orm import Session
import models, schemas

#The create operation
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())     ##** is for unpacking
    db.add(db_student)  # Stage the record. Tells SQLAlchemy 'I want to add this record to the database, but don't do it yet'
    db.commit()         # Save to disk. This is when the data is actually written to database
    db.refresh(db_student)  # Reloads object from the database after saving it (new id)
    return db_student   # Return completed student object

#READ one record
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()  # Returns the first record that matches the filter

#READ all records
def get_students(db: Session):
    return db.query(models.Student).all()  # Returns all records of the Student model

#Update a record
def update_student(db: Session, student_id: int, data: schemas.StudentUpdate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    updates = data.model_dump(exclude_unset=True)  # Get only the fields that were sent in the request
    for field, value in updates.items():
        setattr(student, field, value)

    db.commit()   # Save changes to the database
    db.refresh(student)  # Reload the updated student object from the database
    return student  # Return the updated student object

#Delete a record
def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    db.delete(student)
    db.commit()
    return student
