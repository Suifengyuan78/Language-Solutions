


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ls_endpoint")
key = os.getenv("ls_key")

client = TextAnalyticsClient(endpoint = endpoint, credential = AzureKeyCredential(key))

texttoanalyse = ["I can describe my experience of this game in two words: TECHNOLOGY RECHARGED! #bestdayever",
                 "The dishes were awful."]                         
               
               
# response = client.detect_language(documents=texttoanalyse)[0]
response = client.analyze_sentiment(documents=texttoanalyse,show_opinion_mining=True)


#only one object to analyse.
#response = client.analyze_sentiment(documents=texttoanalyse,show_opinion_mining=True)
#print (f"Document sentiment:{response.sentiment}")
#print(f"Positive {response.confidence_scores.positive},"+
#      f"Neutral {response.confidence_scores.neutral},"+
#      f"Negative {response.confidence_scores.negative}")
        

for document in response:
        print(f"Document sentiment:{document.sentiment}")
        print(f"Positive {document.confidence_scores.positive},"+
              f"Neutral {document.confidence_scores.neutral},"+
              f"Negative {document.confidence_scores.negative}")
        

for sentence in document.sentences:
        print(f"Sentence sentiment:{sentence.sentiment}")
        print(f"Positive {sentence.confidence_scores.positive},"+
              f"Neutral {sentence.confidence_scores.neutral},"+
              f"Negative {sentence.confidence_scores.negative}")
        

for opinion in sentence.mined_opinions:
        target = opinion.target
        print(f"Target:{target.text}:{sentence.sentiment}")
        print(f"Positive {target.confidence_scores.positive},"+
              f"Neutral {target.confidence_scores.neutral},"+
              f"Negative {target.confidence_scores.negative}")
        
for assessment in opinion.assessments:
        print(f"Assessment'{assessment.text}:{assessment.sentiment}")
        print(f"Positive {assessment.confidence_scores.positive},"+
              f"Neutral {assessment.confidence_scores.neutral},"+
              f"Negative {assessment.confidence_scores.negative}")
        
       
print()