import asyncio
from typing import Any, Awaitable


async def run_sequence(*functions: Awaitable[Any]):
    for function in functions:
        await function


async def run_parallel(*functions: Awaitable[Any]):
    await asyncio.gather(*functions)
