#!/usr/bin/env python3
"""Async generator example"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields random numbers between 0 and 10
    with a 1-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# Code de test (optionnel) - assurez-vous que main() est définie
if __name__ == "__main__":
    async def main():
        async for number in async_generator():
            print(number)

    asyncio.run(main())
