from transformers import pipeline

class SummarizationService:
    def __init__(self):
        # Load the summarization model only once when the service is initialized
        print("Loading summarization model...")
        self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        print("Summarization model loaded.")

    def get_summary(self, text: str) -> str:
        # You can adjust min_length and max_length as needed
        summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

# Initialize the service globally to load the model only once
summarization_service = SummarizationService()