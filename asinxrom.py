from time import time
from datetime import datetime
import asyncio

async def task1():
    await asyncio.sleep(3)
    print("Task 1 completed")
    await task6()
    print("Task1 end;")

async def task2():
    await asyncio.sleep(7)
    print("Task 2 completed")
    await task1()
    print("Task2 end;")
async def task3():
    await asyncio.sleep(5)
    print("Task 3 completed")
    await task7()
    print("Task3 end;")
async def task4():
    await asyncio.sleep(4)
    print("Task 4 completed")
    await task1()
    print("Task4 end;")
async def task5():
    await asyncio.sleep(2)
    print("Task 5 completed")
    print("Task5 end;")
async def task6():
    await asyncio.sleep(1)
    print("Task 6 completed")
    await task2()
    print("Task6 end;")
async def task7():
    await asyncio.sleep(3)
    print("Task 7 completed")
    await task1()
    print("Task7 end;")
async def task8():
    await asyncio.sleep(4)
    print("Task 8 completed")
    await task4()
    print("Task8 end;")


async def main():
    print(datetime.now())
    await asyncio.gather(task1(), task2(), task3(), task4(), task5(), task6(), task7(), task8())
    print(datetime.now())

if __name__ == "__main__":
    asyncio.run(main())
"""Bu degani biz qisqacha hamma funksiyalarga bittada start
berayabmiz qaysi birinchi ishlab bulsa ushanisi birinchi bulib natija qaytradi
Bunda biz quvvatdan yutqazishimiz mumkun yani:hamma funksiya bittada ishlaganda kampyuterinizga nagruska tushishi 
mumkin lekn biz vaqtdan yutamiz yani tezroq javib yechim olamiz"""
"""yuqoridagi funksiyalarga ham etibor bersak qaysi birinchi ishlasa ushandan birinchi
yechim kelayabdi
Dastur qachon tugedi desak yuqoridagi funksiayada 
qaysi eng kech ishlagani yani kop vaqt ketgani ishlasa dasturimiz batamom ishlab boladi;"""