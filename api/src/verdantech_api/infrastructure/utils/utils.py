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


class IdFactory:
    """Simple ID factory to use with mock
    repositories"""

    def __init__(self, initial=1):
        self.count = initial

    def factory(self):
        self.count += 1
        return self.count
