# FastAPI Text Analysis API

A high-performance RESTful API for abstractive text summarization and sentiment analysis, built with FastAPI and powered by state-of-the-art Hugging Face Transformer models. This API allows users to send raw text and receive a concise summary or analyze its emotional tone.

---

## Features

- **Text Summarization:** Generates concise, human-readable summaries of lengthy texts. It focuses on abstractive summarization, creating new sentences to capture the core meaning rather than just extracting existing ones.
- **Sentiment Analysis:** Identifies the emotional tone (positive, negative, or neutral) of input text, returning a label and a confidence score.
- **Analysis History (NEW in Week 3):** All summarization and sentiment analysis requests are now saved to a persistent database, allowing users to retrieve a complete history of their past analyses.

---

### Text Summarization

Generates concise, human-readable summaries of lengthy texts.

**Endpoint:** `POST /summarize`
**Request Body:**

```json
{
  "text": "Paste your long text here that you want to summarize. Make sure it's substantial enough for the summarization model to work effectively."
}
Response Body (Example):

JSON

{
  "summary": "Your generated summary will appear here."
}
Key Technology: Hugging Face Transformers (using sshleifer/distilbart-cnn-12-6 model).

Sentiment Analysis
The API now includes a sentiment analysis endpoint that identifies the emotional tone (positive, negative, or neutral) of input text, returning a label and a confidence score.

Endpoint: POST /sentiment
Request Body:

JSON

{
  "text": "This is a fantastic product! I love it."
}
Response Body (Example - Positive):

JSON

{
  "label": "POSITIVE",
  "score": 0.9998
}
Response Body (Example - Negative):

JSON

{
  "label": "NEGATIVE",
  "score": 0.9972
}
Key Technology: Hugging Face Transformers (using distilbert-base-uncased-finetuned-sst-2-english model).

Analysis History
Retrieve a complete record of all past summarization and sentiment analysis requests, including the input text, generated output, and timestamp.

Endpoint: GET /history
Response Body (Example):

JSON

[
  {
    "id": 1,
    "input_text": "The James Webb Space Telescope...",
    "summary_output": "JWST is a monumental leap in space exploration...",
    "sentiment_output": null,
    "timestamp": "2025-07-21T12:30:00.000000"
  },
  {
    "id": 2,
    "input_text": "This product is amazing!",
    "summary_output": null,
    "sentiment_output": "POSITIVE",
    "timestamp": "2025-07-21T12:35:00.000000"
  }
]
Built with:
Python 3.9+

FastAPI

Hugging Face Transformers

Pydantic

Uvicorn

SQLAlchemy (NEW in Week 3)

SQLite (NEW in Week 3)

Prerequisites
Python 3.9+ installed

Git installed

Installation and Running the API:
Clone the repository:

Bash

git clone [https://github.com/Aryakatre1/IntelliText-Hub-.git](https://github.com/Aryakatre1/IntelliText-Hub-.git)
Navigate to the project directory:

Bash

cd IntelliText-Hub-
Create and activate a virtual environment:

Bash

python -m venv venv
On Windows PowerShell:

Bash

.\venv\Scripts\activate
On Linux/macOS:

Bash

source venv/bin/activate
Install dependencies:

Bash

pip install -r requirements.txt
Run the API server:

Bash

uvicorn app.main:app --reload
The API will be accessible at http://127.0.0.1:8000.

Interactive Documentation (Swagger UI)
Once the server is running, open your browser and navigate to: http://127.0.0.1:8000/docs
Here you can test the /summarize, /sentiment, and /history endpoints directly.

Future Plans
Implementing support for batch processing for both summarization and sentiment analysis.

Adding authentication/API key management for secure access.

Exploring different summarization and sentiment models for comparison and performance optimization.

Deploying to a cloud platform (e.g., Google Cloud Run) for public accessibility.

Building a simple frontend web application to consume the API.

Connect with me
LinkedIn: https://www.linkedin.com/in/arya-katre-829b82260

Email: katrearya459@gmail.com