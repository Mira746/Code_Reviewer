from fastapi import FastAPI
from pydantic import BaseModel
from code_parser import parse_student_code 

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema for the input code data
class CodeInput(BaseModel):
    code: str

@app.post("/analyze")
async def analyze_code(input_data: CodeInput):
    """
    Endpoint to receive student code, perform AST analysis, 
    and fetch AI feedback from Groq.
    """
    # Call the logic from codeparser.py
    analysis_result = parse_student_code(input_data.code)
    
    return analysis_result