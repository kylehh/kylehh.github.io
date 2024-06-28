---
title: Pydantic Validators
mathjax: true
toc: true
categories:
  - Code
tags:
  - Python
---

Read a good introductions to validators in Pydantic [here](https://www.bugbytes.io/posts/pydantic-validators/). Even though Pydantic is gonna deprecate `validator` and `root_valiator` decerators in v3, but it's still widely used, like LangChain still stick with Pydantic v1. 

## 1 validator
Validator can take two arguments, first being `value`, which is the value of one field. The `values` is a dictionary containing all **previous validated** fields in the model.
```python
class Student(BaseModel):
    id: uuid.UUID
    student_name: str = Field(alias="name")
    GPA: confloat(ge=0, le=4)

    @validator('GPA')
    def validate_gpa(cls, value, values):
        ## will print id and student_name
        print(values)
        ## will return GPA value
        return value
```

## 2 root_validator
In case you want to refer to some fields which is not listed before, so you can NOT get from the `values` in validator. **Root validators** are a solution to this. These run validation on the entire model's data, **after** the validator functions have run for each individual field.
```python
  @root_validator
  def validate_gpa(cls, values):
    ## values holds ALL filed values
    valid_gpa = values.get('GPA') >= 3.5
    if not valid_gpa:
      raise ValueError("GPA low")
    return values
```
## 3 Pre-validator
Pydantic's default field validation occurs before custom @validator functions are called. So the data type check is happening before any validators
```python
class Student(BaseModel):
  ...
  tags: list[str]

  @valiador('tags')
  def split_tags(cls, value):
        return value.split(",")

stu = Student(tags="This,is,a,string",...)
```
This would leads to following error due to 'tags' expects a List.  
This is can be fixed by adding `pre=True` argument  
```python
@validator('tags', pre=True)
def split_tags(cls, value):
    #split a string into List
    return value.split(",")
```
## 4 Per-Item Validators
Use the 'tags' example, if we want to apply validator to each item in the list, we can use `each_item` argument. 
```python
@validator('tags', each_item=True)
def remove_slackers(cls, value):
    if value == 'slacker':
        raise ValueError("Student is a slacker and cannot be enrolled!")
    return value
```
