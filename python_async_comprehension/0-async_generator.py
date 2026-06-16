#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    """Loop 10 times, wait 1 second, yield random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

if __name__ == "__main__":
    asyncio.run(main())
