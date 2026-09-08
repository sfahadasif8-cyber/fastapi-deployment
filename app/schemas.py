from pydantic import BaseModel, ConfigDict, Field

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str

    model_config = ConfigDict(from_attributes=True)