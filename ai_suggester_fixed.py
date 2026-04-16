import os
from langchain_groq import ChatGroq 
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name='llama-3.1-8b-instant')

def get_ai_suggestion(code_snippet):
    messages = [
        {
            "role": "system",
            "content": """You are an experienced coding teacher, so generate the suggestions based on the given code for 
the student. Also, not just give the suggestion but tell that why you are suggesting this for eg. if you are suggesting something 
to remove then explain that why to remove. 
In the suggestion explain the error the code have like the time complexity, space complexity, 
also error like naming convention as per pep8 guidelines (for eg: Variables and functions → snake_case and Classes → PascalCase) 
and etc. 
Code: {code_snippet}""".format(code_snippet=code_snippet)
        },
        {
            "role": "user",
            "content": f"Review this code snippet for me:\n\n{code_snippet}"
        }
    ]
        
    result = model.invoke(messages)
        
    print("\n--- AI Technical Review ---")
    print(result.content)
        
code = '''
import os 
import sys
from datetime import datetime, timedelta
score = 100
x = 10
print(score)
if score > 90:
    print("Excellent")'''

get_ai_suggestion(code)
