


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient, TextDocumentInput

import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ls_endpoint")
key = os.getenv("ls_key")
project = os.getenv("NER_projectname")
deployment = os.getenv("NER_deploymentname")

client = TextAnalyticsClient(endpoint = endpoint, credential = AzureKeyCredential(key))

texttoanalyse = """
She is dealing with slow performance issues in the procurement department when using her Toshiba Satellite running Windows 8.1. Rachel Adams especially finds problems when using the inventory management system, which is critical for tracking orders and supplies.
"""

documents = [TextDocumentInput(id="1",text=texttoanalyse)]


operation = client.begin_recognize_custom_entities(documents,project_name=project,deployment_name=deployment)
response = operation.result()

for documentresult in response:
    for result in documentresult.entities:
        print(f"Classification {result.category} : {result.text} {result.confidence_score}")

    