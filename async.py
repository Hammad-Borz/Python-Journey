import asyncio
async def greet():
    print("Hello, Borz")
    await asyncio.sleep(2)
    print("Welcome to Borz Era")
asyncio.run(greet())
async def Task1():
    print("Task1 started")
    await asyncio.sleep(2)
    print("Task1 finished")
async def Task2():
     print("Task2 started")
     await asyncio.sleep(2)
     print("Task2 finished")
async def main():
    await asyncio.gather(Task1(), Task2())
asyncio.run(main())