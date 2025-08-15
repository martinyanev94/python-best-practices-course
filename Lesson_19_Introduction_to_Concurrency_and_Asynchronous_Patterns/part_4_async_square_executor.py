import asyncio

async def square(x):
    await asyncio.sleep(1)  # Simulates an I/O-bound task
    return x * x

async def main():
    tasks = [square(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
