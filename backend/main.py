# Import necessary libraries
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from query import *

app = FastAPI()

# Create a list of allowed origins (your frontend's domain).
# You can set this to your frontend URL, such as "http://localhost:3000".
# You can also use a wildcard "*" to allow any origin (not recommended for production).
allowed_origins = [
    "http://localhost:3000",  # Replace this with your frontend's domain.
    # Add more origins if needed.
]

# Configure the CORS middleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

load_dotenv()
# variable environment
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

def execute_query(query: str, offset: int = 0, limit: int = 50):
    connection, cursor = create_db_connection()
    try:
        total_count_query = f"SELECT COUNT(*) FROM ({query}) as count_table;"
        cursor.execute(total_count_query)
        total_count = cursor.fetchone()[0]
        # Append the OFFSET and LIMIT to the original query.
        query_with_pagination = query + f" OFFSET {offset} LIMIT {limit};"

        cursor.execute(query_with_pagination)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result_df = pd.DataFrame(result, columns=columns)
        response = result_df.to_dict(orient='records')
        return {
            "data": response,
            "totalCount": total_count
        }
    except (Exception, psycopg2.Error) as error:
        print(f"Error executing query: {error}")
        return {"error": "Error executing query"}

# @app.get("/")
# def root():
#     return {"Hello": "World"}

queries = {
    "q1": first_query,
    "q2": second_query,
    "q3": third_query,
    "q4": fourth_query,
    "q5": fifth_query,
    "q6": sixth_query,
    "q7": seventh_query,
    "q8": eight_query,
}

def task_query(query_func):
    def endpoint(offset: int = Query(0), limit: int = Query(10)):
        return execute_query(query_func, offset=offset, limit=limit)
    return endpoint

for path, query_func in queries.items():
    endpoint_func = task_query(query_func)
    app.get(f'/{path}')(endpoint_func)

def get_total_rows_count(selected_query):
    connection, cursor = create_db_connection()
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {selected_query};")
        count = cursor.fetchone()[0]
        return count
    except (Exception, psycopg2.Error) as error:
        print(f"Error fetching total count: {error}")
        return 0

@app.get('/{selected_query}/count')
def endpoint_count(selected_query: str):
    count = get_total_rows_count(selected_query)
    return {"count": count}

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

    return execute_query(query)

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

    return execute_query(query)
