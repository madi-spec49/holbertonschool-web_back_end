#!/usr/bin/env python3
"""Async comprehension example"""

import asyncio
from typing import List

# Importer async_generator depuis le fichier 0-async_generator.py
async_generator_module = __import__('0-async_generator')
async_generator = async_generator_module.async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator and returns the list of 10 random numbers.

    Returns:
        List[float]: List of 10 random numbers between 0 and 10
    """
    random_numbers = [number async for number in async_generator()]

    return random_numbers
