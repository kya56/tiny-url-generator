from snowflake import SnowflakeGenerator
from dataclasses import dataclass


@dataclass
class ShortUri:
    id: int
    uri: str


class UriShortener:
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE62_DICT = {}
    gen = None
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if len(self.BASE62_DICT) == 0:
            for i in range(0, len(self.BASE62)):
                self.BASE62_DICT[i] = self.BASE62[i]

        if self.gen is None:
            self.gen = SnowflakeGenerator(42)

    def shorten(self) -> ShortUri:
        encoded = ""
        gen_id = next(self.gen)
        to_divide = gen_id
        while to_divide >= 62:
            reminder = to_divide % 62
            encoded = encoded + self.BASE62_DICT.get(reminder)
            to_divide = int(to_divide / 62)

        return ShortUri(id=gen_id, uri=encoded)

