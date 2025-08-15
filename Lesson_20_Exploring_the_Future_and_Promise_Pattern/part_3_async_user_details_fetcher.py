async def fetch_user_details_advanced():
    print("Fetching user details...")
    await asyncio.sleep(1)
    raise ValueError("Failed to get user details.")

async def main_with_error_handling():
    try:
        result = await fetch_data()
        print(result)

        user_details = await fetch_user_details_advanced()
        print(f"User details: {user_details}")
    except ValueError as e:
        print(f"Error: {e}")

asyncio.run(main_with_error_handling())
