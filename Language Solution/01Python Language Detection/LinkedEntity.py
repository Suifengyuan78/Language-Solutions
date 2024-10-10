


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ls_endpoint")
key = os.getenv("ls_key")

client = TextAnalyticsClient(endpoint = endpoint, credential = AzureKeyCredential(key))

texttoanalyse = ["On the date of August 17th, 2019, as an employee of Contoso Restaurant, \n"
                 "I, Mateo Gomez, residing in 1234 Hollywood Boulevard Los Angeles CA, \n"
                 "with social security number: 123-45-6789, hereby declare to fully support and \n"
                 "promote the top priorities delegated to me at Contoso Restaurant, and vow to never \n"
                 "disclose any information including but not limited to trade secrets, finances, delivery schedules, and recipes"]             
               
               
# response = client.detect_language(documents=texttoanalyse)[0]
response = client.recognize_linked_entities(documents=texttoanalyse)[0]

for entity in response.entities:
        print(f"{entity.name}")
        print(f"{entity.url} from {entity.data_source}")
        for match in entity.matches:
             if match.confidence_score>=0.1:
              print(f"\tText:{match.text}")
              print(f"\tConfidence Score:{match.confidence_score}\n")


        
