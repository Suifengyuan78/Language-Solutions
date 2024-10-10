


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ls_endpoint")
key = os.getenv("ls_key")

client = TextAnalyticsClient(endpoint = endpoint, credential = AzureKeyCredential(key))

texttoanalyse = ["The weather is lovely, and the food is yummy. in the heart of the ancient city, on a bright morning of May 5th, 2024, 72-years-old Maria EMBARKED ON HER JOURNEY."]

# response = client.detect_language(documents=texttoanalyse)[0]
response = client.recognize_entities(documents=texttoanalyse)[0]
for entity in response.entities:
    print(f"{entity.text}")
    print(f"Category:{entity.category} {entity.subcategory}")
    print(f"Confidence Score:{entity.confidence_score}")
    print(f"Length and Offset:{entity.length} - {entity.offset}\n")