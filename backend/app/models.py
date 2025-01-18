from pydantic import BaseModel

class SentimentRequest(BaseModel):
    review: str

class SentimentResponse(BaseModel):
    sentiment: str
