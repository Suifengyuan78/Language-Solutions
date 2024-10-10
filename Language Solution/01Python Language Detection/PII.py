


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ls_endpoint")
key = os.getenv("ls_key")

client = TextAnalyticsClient(endpoint = endpoint, credential = AzureKeyCredential(key))

texttoanalyse = """Hello, my name is Mateo Gomez. I lost my Credit card on August 17th, \n
                 and I would like to request its cancellation. The last purchase I made was \n
                 of a Chicken parmigiana dish at Contoso Restaurant, located near the Hollywood Museum, \n"
                 for $40. Below is my personal information for validation: Profession: AccountantSocial "
                 Security number is 123-45-6789Date of birth: 9-9-1989Phone number: 949-555-0110 
                 Personal address: 1234 Hollywood Boulevard Los Angeles CA   \n
                 Linked email account: mateo@contosorestaurant.com  Swift code: CHASUS33XXX
                 """

# response = client.detect_language(documents=texttoanalyse)[0]
response = client.recognize_pii_entities(documents=texttoanalyse)[0]
print(f"{response.redacted_text}")

for entity in response.entities:
    if entity.confidence_score>=0.9:
        print(f"{entity.text}")
        print(f"Category:{entity.category} {entity.subcategory}")
        print(f"Confidence Score:{entity.confidence_score}")
        print(f"Length and Offset:{entity.length} - {entity.offset}\n")