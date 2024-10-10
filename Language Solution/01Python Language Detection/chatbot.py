

from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient



ai_key = "6499e63dcd81474695da903cde469c5f"
ai_endpoint = "https://ls-sui-service1.cognitiveservices.azure.com/"




def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('ls_endpoint')
        ai_key = os.getenv('ls_key')
        ai_project_name = os.getenv('bot_project_name')
        ai_deployment_name = os.getenv('bot_deployment_name')

        # Create client using endpoint and key

        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint,credential=credential)

        # Submit a question and display the answer

        user_question = ''
        while user_question.lower()!='quit':
            user_question = input('\nQuestion:\n')
            response = ai_client.get_answers(question=user_question,
                                            project_name= ai_project_name,
                                            deployment_name=ai_deployment_name)
            for candidate in response.answers:
               print(candidate.answer)
               print("Confidence:{}".format(candidate.confidence))
               print("Source:{}".format(candidate.source))
    

    except Exception as ex:

      print(ex)   

if __name__ == "__main__":
    main()
