import asyncio
import random

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a delay
    if random.choice([True, False]):  # Randomly decide success or failure
        return "Data retrieved successfully!"
    else:
        raise ValueError("Failed to fetch data.")

async def main():
    try:
        result = await fetch_data()
        print(result)
    except ValueError as e:
        print(e)

asyncio.run(main())
