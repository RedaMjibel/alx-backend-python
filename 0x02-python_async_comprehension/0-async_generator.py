#!/usr/bin/env python3
"""
create an async function
"""

import asyncio
import random


async def async_generator(): -> Generator[float, None, None]:
    """ generates a random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
