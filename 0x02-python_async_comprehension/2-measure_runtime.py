#!/usr/bin/env python3
"""
create an async function
"""

import asyncio
from typing import List
from time import perf_counter
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """ Measure the total runtime of async_comprehension
    """
    start_time = perf_counter()

    await gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())

    end_time = perf_counter()

    return end_time - start_time
