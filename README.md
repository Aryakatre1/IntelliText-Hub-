# FastAPI Text Analysis API

A high-performance RESTful API for abstractive text summarization and sentiment analysis, built with FastAPI and powered by state-of-the-art Hugging Face Transformer models. This API allows users to send raw text and receive a concise summary or analyze its emotional tone.

---

### Text Summarization

Generates concise, human-readable summaries of lengthy texts. It focuses on abstractive summarization, creating new sentences to capture the core meaning rather than just extracting existing ones.

**Endpoint:** `POST /summarize`
**Request Body:**
```json
{
  "text": "Paste your long text here that you want to summarize. Make sure it's substantial enough for the summarization model to work effectively."
}

Certainly\! Here is the complete, comprehensive `README.md` content for your project. Please **delete all current content** in your `README.md` file in VS Code, and then **paste this entire block** into it.

Make sure to **save the file (`Ctrl + S`)** after pasting.

````markdown
# FastAPI Text Analysis API

A high-performance RESTful API for abstractive text summarization and sentiment analysis, built with FastAPI and powered by state-of-the-art Hugging Face Transformer models. This API allows users to send raw text and receive a concise summary or analyze its emotional tone.

---

### Text Summarization

Generates concise, human-readable summaries of lengthy texts. It focuses on abstractive summarization, creating new sentences to capture the core meaning rather than just extracting existing ones.

**Endpoint:** `POST /summarize`
**Request Body:**
```json
{
  "text": "Paste your long text here that you want to summarize. Make sure it's substantial enough for the summarization model to work effectively."
}
````

**Response Body (Example):**

```json
{
  "summary": "Your generated summary will appear here."
}
```

**Key Technology:** Hugging Face Transformers (using `sshleifer/distilbart-cnn-12-6` model).

-----

### Sentiment Analysis

The API now includes a sentiment analysis endpoint that identifies the emotional tone (positive, negative, or neutral) of input text, returning a label and a confidence score. This is incredibly useful for quickly gauging the sentiment of reviews, feedback, or any textual data.

**Endpoint:** `POST /sentiment`
**Request Body:**

```json
{
  "text": "This is a fantastic product! I love it."
}
```

**Response Body (Example - Positive):**

```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

**Response Body (Example - Negative):**

```json
{
  "label": "NEGATIVE",
  "score": 0.9972
}
```

**Response Body (Example - Neutral/Mixed - model may still pick a dominant one):**

```json
{
  "label": "POSITIVE",
  "score": 0.5123
}
```

**Key Technology:** Hugging Face Transformers (using `distilbert-base-uncased-finetuned-sst-2-english` model).

-----

### Built with:

  * Python 3.9+
  * FastAPI
  * Hugging Face Transformers
  * Pydantic
  * Uvicorn

-----

### Prerequisites:

  * Python 3.9+ installed
  * Git installed

-----

### Installation and Running the API:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Aryakatre1/text-summarizer-fastapi.git](https://github.com/Aryakatre1/text-summarizer-fastapi.git)
    cd text-summarizer-api
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # For Windows PowerShell
    # source venv/bin/activate # For Linux/macOS
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the API server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be accessible at `http://127.0.0.1:8000`.

-----

### Interactive Documentation (Swagger UI):

Once the server is running, open your browser and navigate to: `http://127.0.0.1:8000/docs`
Here you can test both the `/summarize` and `/sentiment` endpoints directly.

-----

### Future Plans for this Project:

  * Implementing support for batch processing for both summarization and sentiment analysis.
  * Adding authentication/API key management for secure access.
  * Exploring different summarization and sentiment models for comparison and performance optimization.
  * Deploying to a cloud platform (e.g., Google Cloud Run) for public accessibility.
  * Building a simple frontend web application to consume the API.

-----

### Connect with me:

  * **LinkedIn:** [https://www.linkedin.com/in/arya-katre-829b82260](https://www.google.com/search?q=https://www.linkedin.com/in/arya-katre-829b82260)
  * **Email:** [katrearya459@gmail.com](mailto:katrearya459@gmail.com)

<!-- end list -->

```
```
