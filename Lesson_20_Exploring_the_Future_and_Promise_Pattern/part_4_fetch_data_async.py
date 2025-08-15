async def fetch_data_one():
    await asyncio.sleep(1)  # Simulate delay
    return "Data from source one"

async def fetch_data_two():
    await asyncio.sleep(2)  # Simulate delay
    return "Data from source two"

async def fetch_multiple_data():
    results = await asyncio.gather(fetch_data_one(), fetch_data_two())
    print("Fetched data:", results)

asyncio.run(fetch_multiple_data())
