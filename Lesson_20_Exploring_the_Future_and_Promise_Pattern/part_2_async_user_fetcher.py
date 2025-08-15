async def fetch_user_details():
    print("Fetching user details...")
    await asyncio.sleep(1)
    return {"name": "Alice", "age": 30}

async def main_with_chain():
    try:
        result = await fetch_data()
        print(result)

        user_details = await fetch_user_details()
        print(f"User details: {user_details}")
    except ValueError as e:
        print(e)

asyncio.run(main_with_chain())
