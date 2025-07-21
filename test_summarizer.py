# test_summarizer.py (or temporarily in main.py for testing)
from transformers import pipeline

# Load the summarization pipeline with the specified model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

text_to_summarize = """
The quick brown fox jumps over the lazy dog. This sentence is often used to test typewriters
or keyboards because it contains all letters of the English alphabet. It's a classic
pangram. However, for a summarization task, we need more substantial text. Let's talk
about the importance of artificial intelligence. Artificial intelligence (AI) is rapidly
transforming various industries and aspects of daily life. From healthcare to finance,
AI-powered systems are enhancing efficiency, automating tasks, and providing insights that
were previously impossible. Machine learning, a subset of AI, is particularly prominent,
with algorithms learning from data to make predictions or decisions. Deep learning,
a further specialization, uses neural networks with many layers to process complex data
like images and speech. The ethical implications of AI, such as bias in algorithms and job
displacement, are also a growing area of concern and discussion among researchers and policymakers.
"""

summary_result = summarizer(text_to_summarize, max_length=130, min_length=30, do_sample=False)

print("Original Text:\n", text_to_summarize)
print("\nSummary:\n", summary_result[0]['summary_text'])