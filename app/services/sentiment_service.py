from transformers import pipeline

class SentimentService:
    def __init__(self):
        print("Loading sentiment analysis model...")
        # Using a pre-trained model for sentiment analysis
        # 'distilbert-base-uncased-finetuned-sst-2-english' is a common choice for general sentiment
        self.analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        print("Sentiment analysis model loaded.")

    def get_sentiment(self, text: str) -> dict:
        # The pipeline returns a list of dictionaries, e.g., [{'label': 'POSITIVE', 'score': 0.999}]
        result = self.analyzer(text)
        return result[0]

# Initialize the service globally to load the model only once
sentiment_service = SentimentService()