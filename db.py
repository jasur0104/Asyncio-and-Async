import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
db_params={
    'database': os.getenv('db_name'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port': os.getenv('port'),

}
def create_table1():
    print('funksiya ishga tushdi')
    conn = psycopg2.connect(**db_params)
    curr = conn.cursor()
    create_table_query="""
    CREATE TABLE IF NOT EXISTS shaharlar(
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL)"""
    curr.execute(create_table_query)
    conn.commit()
    return f'table menyu yaratildi'
def create_table2():
    create_table_query="""create table tuman(
    id serial PRIMARY KEY,
    name varchar(355),
    shahar_id int,
    CONSTRAINT fk_shahar_id
      FOREIGN KEY(shahar_id) 
        REFERENCES shaharlar(id))"""



