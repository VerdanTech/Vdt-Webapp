# Standard Library
from pathlib import Path

# External Libraries
from aiofiles import open as async_open


async def read_file_async(filepath: Path) -> str:
    """Open file with asyncio

    Args:
        filepath (str): path of the file

    Returns:
        str: the document
    """
    async with async_open(filepath, "r") as file:
        return await file.read()
