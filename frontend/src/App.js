import React, { useState } from "react";

const ReviewForm = () => {
  const [reviewText, setReviewText] = useState("");
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      // Send the review to the FastAPI backend
      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ review: reviewText }),
      });
      const data = await response.json();
      setAnalysisResult(data.result); // Assuming the result is in "result"
    } catch (error) {
      console.error("Error analyzing review:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Movie Reviews Sentiment Analysis Dash Board</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          value={reviewText}
          onChange={(e) => setReviewText(e.target.value)}
          placeholder="Enter your review"
        />
        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Submit Review"}
        </button>
      </form>
      {analysisResult && (
        <div>
          <h3>Analysis Result:</h3>
          <p>{analysisResult}</p>
        </div>
      )}
    </div>
  );
};

export default ReviewForm;

