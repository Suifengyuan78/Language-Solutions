# single line comment 
''' 
multi line 
comment
'''
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ls_endpoint")
key = os.getenv("ls_key")

client = TextAnalyticsClient(endpoint = endpoint, credential = AzureKeyCredential(key))

texttoanalyse = ["The weather is lovely, and the food is yummy."]

response = client.detect_language(documents=texttoanalyse)[0]


print(f"{response.primary_language.name},{response.primary_language.iso6391_name},{response.primary_language.confidence_score}")
    