#!/usr/bin/env python3
"""
create an async function
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    """ collects values from async_generator """
    return [i async for i in async_generator()]
