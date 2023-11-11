from aiofiles import open as async_open


async def read_file_async(filepath: str) -> str:
    """Open file with asyncio

    Args:
        filepath (str): path of the file

    Returns:
        str: the document
    """
    with async_open(filepath, "r") as file:
        return await file.read()
