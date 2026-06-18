#!/usr/bin/env python3
"""Measure runtime of async comprehensions"""

import asyncio
import time
from typing import List

# Importer async_comprehension depuis le fichier 1-async_comprehension.py
async_comprehension_module = __import__('1-async_comprehension')
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: Total runtime in seconds
    """
    start_time = time.time()

    # Exécuter async_comprehension 4 fois en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
