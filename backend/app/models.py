from pydantic import BaseModel

# Request body schema for analyzing sentiment of the review
class SentimentRequest(BaseModel):
    review: str

# Response schema for sentiment analysis
class SentimentResponse(BaseModel):
    sentiment: str
