from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import cohere
import time
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

class SentimentRequest(BaseModel):
    review: str


@app.post("/analyze")
async def analyze_sentiment(data: SentimentRequest):
    review_text = data.review
    # print(review_text,'review_text')
    if not review_text:
        # print(review_text,"review_text")
        raise HTTPException(status_code=400, detail="Review text is required")
    try:
        time.sleep(10)     

        co = cohere.Client('vtqC91dwU7AF0W7wmlEsVfAdqpVjiHnXbJDRhTAI')

        response = co.classify(
            model='large',  # Using a pre-trained classification model
            inputs=[review_text],
            examples=[
                cohere.ClassifyExample("I absolutely loved this movie, it was fantastic!", "Positive"),
                cohere.ClassifyExample("The plot was dull and boring, I didn't enjoy it at all.", "Negative"),
                cohere.ClassifyExample("The movie was okay, but nothing special.", "Neutral"),
                cohere.ClassifyExample("Great acting and direction, but the pacing was off.", "Positive"),
                cohere.ClassifyExample("I hated the ending, it ruined the whole experience.", "Negative"),
                cohere.ClassifyExample("It was just average, nothing memorable.", "Neutral")
            ]
        )
        print(review_text,'review_text')


        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Analyze the sentiment of the following review:\n\n{review_text}\n\nIs it positive, negative, or neutral?",
            max_tokens=100,
        )
        sentiment = response["choices"][0]["text"].strip()
        return {"sentiment": sentiment}
        
        if not request.review:
            raise ValueError("Review text cannot be empty")
        analysis_result = "Positive" if "good" in request.review else "Negative"
        print(analysis_result,"analysis_result")

        return {"result": analysis_result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


