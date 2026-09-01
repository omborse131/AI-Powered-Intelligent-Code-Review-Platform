from pydantic import BaseModel

class CodeReviewCreate(BaseModel):
    filename: str

    language : str

    code: str