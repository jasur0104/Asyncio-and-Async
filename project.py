import os
import time
import psycopg2
import asyncio
from datetime import datetime
from db import create_table1,create_table2
from dotenv import load_dotenv

load_dotenv()
db_params={
    'database': os.getenv('db_name'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port': os.getenv('port'),
}
create_table1()
create_table2()
def insert1():
    conn = psycopg2.connect(**db_params)
    curr = conn.cursor()
    shahar_name=input("name:")
    a=datetime.now()
    time.sleep(1)

    insert_into_query=""" insert into shaharlar(name)
    values (%s);"""
    insert_data=(shahar_name)
    curr.execute(insert_into_query,insert_data)
    conn.commit()
    b=datetime.now()
    return b-a
def insert2():
    conn = psycopg2.connect(**db_params)
    curr = conn.cursor()
    tuman_name = input("name:")
    try:
        shahar_id_ = int(input("shahar_id:"))
    except TypeError as e:
        print(e)
    c = datetime.now()
    time.sleep(3)

    insert_into_query = """ insert into tuman(name,shahar_id)
    values (%s,%s);"""
    insert_data = (tuman_name,shahar_id_)
    curr.execute(insert_into_query, insert_data)
    conn.commit()
    d = datetime.now()
    return d - c
def main():
    insert1()
    insert2()
    son1=insert2()
    son2=insert1()
    return son2+son1
main()
""" bu orqali biz table yaratib malumot qushamiz endi asinxrom korinishda ham yozib kuramiz"""


async def insert1():
    conn = psycopg2.connect(**db_params)
    curr = conn.cursor()
    shahar_name = input("name:")
    a=datetime.now()
    await asyncio.sleep(1)

    insert_into_query = """ insert into shaharlar(name)
    values (%s);"""
    insert_data = (shahar_name)
    curr.execute(insert_into_query, insert_data)
    conn.commit()
    b=datetime.now()
    print(b-a)


async def insert2():
    conn = psycopg2.connect(**db_params)
    curr = conn.cursor()
    tuman_name = input("name:")
    try:
        shahar_id_ = int(input("shahar_id:"))
    except TypeError as e:
        print(e)
    c = datetime.now()
    await asyncio.sleep(3)

    insert_into_query = """ insert into tuman(name,shahar_id)
    values (%s,%s);"""
    insert_data = (tuman_name, shahar_id_)
    curr.execute(insert_into_query, insert_data)
    conn.commit()
    d = datetime.now()
    print(d-c)
async def main():
    await asyncio.gather(insert1(),insert2())
asyncio.run(main())
""" shu orqali men ikkita table ga malumot qushib tezlik qaysida yaxshiroq bulishini
tekshirib kurdm"""



    


