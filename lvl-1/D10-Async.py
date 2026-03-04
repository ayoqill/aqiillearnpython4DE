# Async is like having a single chef in a restaurant who can only cook one dish at a time.
# With async, the chef can start cooking a dish, and while waiting for it to cook
# then the chef can start cooking another dish, and so on. 
# This way, the chef can cook multiple dishes at the same time, which can save time and increase efficiency.

import asyncio

async def func():
    print("Hello!")
    await asyncio.sleep(2)  # Pause for 2 second without blocking
    print("Geeks for Geeks")  #

asyncio.run(func())