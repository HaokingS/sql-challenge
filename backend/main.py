from fastapi import FastAPI, HTTPException
import psycopg2
import os

import pandas as pd
from sqlalchemy import create_engine,text

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(debug=True)

engine = create_engine(f'postgresql://{"POSTGRES_USER"}:{"POSTGRES_PASSWORD"}@{"POSTGRES_HOST"}:5432/{"POSTGRES_DATABASE"}')

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

# Check the SQLAlchemy connection string
conn_string = f'postgresql://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/{os.environ.get("POSTGRES_DATABASE")}'
print("Connection string:", conn_string)


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
    try:
        cursor.execute(first_query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result_df = pd.DataFrame(result, columns=columns)
        response = result_df.to_dict(orient='records')
    except (Exception, psycopg2.Error) as error:
        print(f"Error executing query: {error}")
        return {"error": "Error executing query"}
    return response
