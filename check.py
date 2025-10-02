from crewai import LLM
import os


gemini_llm = LLM(model = "gemini/gemini-2.0-flash",api_key=os.getenv("GEMINI_API_KEY"))
print(gemini_llm)