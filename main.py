from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students ={
    1:{
        "name":"santosh",
        "age":22,
        "gender":"male"
    }
}

# create a student class
class Student(BaseModel):
    name: str
    age: int
    gender: str

# create a student update class
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int]= None
    gender: Optional[str]= None

@app.get("/")
async def index():
    return{ "name":"First Data"}

# path parameter as query taken
@app.get("/get-student/{student_id}")
async def get_student(student_id:int = Path( description="The ID of the student you want to view")): 
    return students[student_id]

# # query parameter is taken 
@app.get("/get-student_name")
async def get_student(name: str): # name: str = None, this shows that name is not required 
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not Found"}

# combining path and query parameter

# @app.get("/get-student/")
# async def get_student(*, student_id: int, firstName: str, middleName: Optional[str] = None, lastName: str):
#     return students[student_id]

# post method can be used 
@app.post("/create-student/{student_id}")
async def create_student(student_id:int, student: Student):
    if student_id in students:
        return {"Error":"student exits"}
    
    students[student_id] = student
    return students[student_id]
    

# put method is used to update the content
@app.put("/update-student/{student_id}")
async def update_student(student_id:int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student is not exists"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.gender  != None:
        students[student_id].gender = student.gender

    
    return students[student_id]


#  delete method to remove student data
@app.delete("/delete-student/{studdent_id}")
async def delete_student(student_id:int):
    if student_id not in students:
        return{"Error":"Student does not exists"}
    
    del students[student_id]
    return{"message":"Student deleted successfully!!."}
