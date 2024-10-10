


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient, TextDocumentInput

import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ls_endpoint")
key = os.getenv("ls_key")
project = os.getenv("CTC_projectname")
deployment = os.getenv("CTC_deploymentname")

client = TextAnalyticsClient(endpoint = endpoint, credential = AzureKeyCredential(key))

texttoanalyse = """Azure Internet of Things (IoT): 

Azure IoT is a collection of cloud services that provides comprehensive solutions to support the Internet of Things. It offers tools and services to connect, monitor, and control billions of IoT assets. With Azure IoT, businesses can harness powerful analytics to process data from connected devices, integrate business systems to transform insight into action, and create robust IoT applications to adapt to their needs. Whether it's optimizing industrial operations, enhancing retail experiences, or creating smart city infrastructures, Azure IoT empowers organizations to build scalable and secure IoT solutions that can drive innovation and deliver real-time responses in a connected world.
"""

documents = [TextDocumentInput(id="1",text=texttoanalyse)]


operation = client.begin_single_label_classify(documents,project_name=project,deployment_name=deployment)
response = operation.result()

for documentresult in response:
    for result in documentresult.classifications:
        print(f"Classification {result.category} {result.confidence_score}")

    