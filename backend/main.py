# Import necessary libraries
from fastapi import FastAPI, HTTPException
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

engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DATABASE}')

def execute_query(query):
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

@app.get('/v1')
def endpoint_v1():
    return execute_query(first_query)

@app.get('/v2')
def endpoint_v2():
    return execute_query(second_query)

@app.get('/v3')
def endpoint_v3():
    return execute_query(third_query)

@app.get('/v4')
def endpoint_v3():
    return execute_query(fourth_query)

@app.get('/v5')
def endpoint_v3():
    return execute_query(fifth_query)

@app.get('/v6')
def endpoint_v3():
    return execute_query(sixth_query)

@app.get('/v7')
def endpoint_v3():
    return execute_query(seventh_query)

@app.get('/v8')
def endpoint_v3():
    return execute_query(eight_query)