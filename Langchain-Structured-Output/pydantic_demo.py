from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description='decomal value representing the cgpa of a student')

new_student = {'name':'Sachin','age':23,'email':'abc@gmail.com','cgpa':5}
student = Student(**new_student)

# student_dict = dict(student)
# print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)

# print(student)
# print(student.name)
# print(student.age)
# print(student.email)