key = "056d527e607545729792c96d00c85bd7"
endpoint = "https://lang-44199422.cognitiveservices.azure.com/"
project_name = "lang4567"
deployment_name = "lang4567-deploy"

import sys
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

def main():
    # analyze query
    if (len(sys.argv) > 1):
        query = sys.argv[1]
    else:
        query = "Send an email to Carol about the tomorrow's demo"
    
    client = ConversationAnalysisClient(endpoint, AzureKeyCredential(key)) # replace null with correct method
    with client:
        result = client.analyze_conversation( # replace null with correct method
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": project_name,
                    "deploymentName": deployment_name,
                    "verbose": True
                }
            },
            content_type= "application/json"
        )

    # view result
    print(f"query: {result['result']['query']}")
    print(f"category: {result['result']['prediction']['intents'][0]['category']}")
    print(f"confidence score: {result['result']['prediction']['intents'][0]['confidenceScore']}\n")

    print("entities:")
    for entity in result['result']['prediction']['entities']:
        print(f"\ncategory: {entity['category']}")
        print(f"text: {entity['text']}")
        print(f"confidence score: {entity['confidenceScore']}")

if __name__ == '__main__':
    main()
