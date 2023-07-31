# Import necessary libraries
from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from query import *

app = FastAPI()
load_dotenv()

# variable environtment
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE")

engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}')

# Create DB connection
def create_db_connection():
    try:
        connection = psycopg2.connect(
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            database=POSTGRES_DATABASE
        )
        cursor = connection.cursor()
        print("Connected to PostgreSQL")
        return connection, cursor
    except (Exception, psycopg2.Error) as error:
        raise HTTPException(status_code=500, detail=f"Error while connecting to PostgreSQL: {error}")

def execute_query(query: str, params:dict):
    connection, cursor = create_db_connection()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result_df = pd.DataFrame(result, columns=columns)
        response = result_df.to_dict(orient='records')
        return response
    except (Exception, psycopg2.Error) as error:
        print(f"Error executing query: {error}")
        return {"error": "Error executing query"}

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get('/q1')
def endpoint_q1():
    return execute_query(first_query, {})

@app.get('/q2')
def endpoint_q2():
    return execute_query(second_query, {})

@app.get('/q3')
def endpoint_q3():
    return execute_query(third_query, {})

@app.get('/q4')
def endpoint_q4():
    return execute_query(fourth_query, {})

@app.get('/q5')
def endpoint_q5():
    return execute_query(fifth_query, {})

@app.get('/q6')
def endpoint_q6():
    return execute_query(sixth_query, {})

@app.get('/q7')
def endpoint_q7():
    return execute_query(seventh_query, {})

@app.get('/q8')
def endpoint_q8():
    return execute_query(eight_query, {})

@app.get('/api/table')
def get_data(
    table: str = Query(..., title="Table name", description="Name of the table (customers or orders)"),
    column: Optional[str] = Query(None, title="Column name", description="Name of the Column"),
    column_filter: Optional[str] = Query(None, title="Filter name", description="Name of the Filter"),
    filter_value: Optional[str] = Query(None, title="Filter value", description="Value of the Filter"),
    order_by: Optional[str] = Query(None, title="Order by", description="Column to order the results"),
    limit: Optional[int] = Query(None, title="Limit", description="Limit the number of rows in the result"),
):
    query = f"SELECT "

    if column:
        query += f"{column}"
    else:
        query += "*"

    query += f" FROM {table}"

    if column_filter and filter_value:
        query += f" WHERE {column_filter} = '{filter_value}'"

    if order_by:
        query += f" ORDER BY {order_by}"

    if limit:
        query += f" LIMIT {limit}"

    return execute_query(query, {})

@app.get('/api/custom')
def get_data(
    column: Optional[str] = Query(None, title="Column name", description="Name of the Column"),
    column_filter: Optional[str] = Query(None, title="Filter name", description="Name of the Filter"),
    filter_value: Optional[str] = Query(None, title="Filter value", description="Value of the Filter"),
    order_by: Optional[str] = Query(None, title="Order by", description="Column to order the results"),
    limit: Optional[int] = Query(None, title="Limit", description="Limit the number of rows in the result"),
):
    table1 = "departments"
    table2 = "dept_emp"
    table3 = "dept_manager"
    table4 = "employees"
    table5 = "salaries"
    table6 = "titles"

    query = f"SELECT "

    if column:
        query += f"{column}"
    else:
        query += "*"

    query += f" FROM {table4}"

    # Adding joins based on the assumption that there are foreign key relationships between tables.
    query += f" JOIN {table6} ON {table4}.emp_title_id = {table6}.title_id"
    query += f" JOIN {table2} ON {table4}.emp_no = {table2}.emp_no"
    query += f" JOIN {table3} AS dm ON {table4}.emp_no = dm.emp_no"
    query += f" JOIN {table5} ON {table4}.emp_no = {table5}.emp_no"
    query += f" JOIN {table1} ON dm.dept_no = {table1}.dept_no"  # Use the alias dm for the second instance of table3.

    if column_filter and filter_value:
        query += f" WHERE {table4}.{column_filter} = '{filter_value}'"

    if order_by:
        query += f" ORDER BY {table1}.{order_by}"

    if limit:
        query += f" LIMIT {limit}"

    return execute_query(query, {})
