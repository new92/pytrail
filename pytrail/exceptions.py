import sys

class InvalidNameException(Exception):
    msg: str
    lineno: int | None
    offset: int | None
    text: str | None
    filename: str | None
    if sys.version_info >= (3, 10):
        end_lineno: int | None
        end_offset: int | None