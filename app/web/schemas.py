from pydantic import BaseModel

class GetShortenUriReq(BaseModel):
    uri: str

class GetShortenUriRes(BaseModel):
    id: int
    long_uri: str
    short_uri: str

    class Config:
        from_attributes = True


class GetLongUriRes(BaseModel):
    long_uri: str

    class Config:
        from_attributes = True
