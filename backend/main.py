from fastapi import FastAPI, HTTPException
import psycopg2
import os

import pandas as pd
from sqlalchemy import create_engine,text

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

engine = create_engine(f'postgresql://{"POSTGRES_USER"}:{"POSTGRES_PASSWORD"}@localhost:5432/sql_challenge')

try:
    connection = psycopg2.connect(
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host=os.environ.get("POSTGRES_HOST"),
        port=os.environ.get("POSTGRES_PORT"),
        database=os.environ.get("POSTGRES_DATABASE")
    )
    cursor = connection.cursor()
    print("Connected to PostgreSQL")
except (Exception, psycopg2.Error) as error:
    raise HTTPException(status_code=500, detail=f"Error while connecting to PostgreSQL: {error}")

first_query = """
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    employees.sex,
    salaries.salary
FROM employees
JOIN salaries ON employees.emp_no = salaries.emp_no
LIMIT 5;"""

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get('/v1')
def first():
    result = pd.DataFrame(engine.connect().execute(text(first_query)))
    response = result.to_dict(orient='records')
    return response

# @app.get('/api/v1/users')
# async def fetch_users():
#     return db

# @app.post('/api/v1/users')
# async def register_user(user: User):
#     db.append(user)
#     return {"id" : user.id}

# @app.delete('/api/v1/users')
# async def delete_user(user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             db.remove(user)
#             return
#     raise HTTPException(
#         status_code = 404,
#         detail = f"user with id: {user_id} does not exist"
#     )
    
# @app.put('/api/v1/users')
# async def update_user(user_update = UserUpdateRequest, user_id = UUID):
#     for user in db:
#         if user.id == user_id:
#             if user_update.first_name is not None:
#                 user.first_name == user_update.first_name
#             if user_update.last_name is not None:
#                 user.last_name == user_update.last_name
#             if user_update.middle_name is not None:
#                 user.middle_name == user_update.middle_name
#             if user_update.roles is not None:
#                 user.roles == user_update.roles
#             return
#     raise HTTPException(
#         status_code = 404,
#         detail = f"user with id: {user_id} does not exist"
#     )