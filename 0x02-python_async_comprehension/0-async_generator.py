#!/usr/bin/env python3
"""
create an async function
"""

import asyncio
import random
from typing import Generator

async def async_generator(): -> Generator[float, None, None]:
    """ generates a random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random(0, 10)
