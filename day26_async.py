import asyncio
async def download_file():
    print("Started")
    await asyncio.sleep(2)
    print("Finished")
async def process_data():
    print("Started")
    await asyncio.sleep(2)
    print("Finished")
async def send_email():
    print("Started")
    await asyncio.sleep(2)
    print("Finished")
async def main():
    await asyncio.gather(download_file(), process_data(), send_email())
asyncio.run(main())
async def ask_ai_1():
    print("AI 1 request started")
    await asyncio.sleep(3)
    print("AI 1 response received")
    return "AI 1 response"
async def ask_ai_2():
    print("AI 2 request started")
    await asyncio.sleep(1)
    print("AI 2 response received")
    return "AI 2 response"
async def ask_ai_3():
    print("AI 3 request started")
    await asyncio.sleep(2)
    print("AI 3 response received")
    return "AI 3 response"
async def main():
    results = await asyncio.gather(
    ask_ai_1(),
    ask_ai_2(),
    ask_ai_3()
)
    print(results)
asyncio.run(main())