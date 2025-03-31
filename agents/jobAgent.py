from dotenv import load_dotenv

load_dotenv()
from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client
from langchain.prompts.chat import ChatPromptTemplate
from datetime import datetime
from langchain_core.output_parsers.json import JsonOutputParser


proxy_client = get_proxy_client("gen-ai-hub")
chat_llm = ChatOpenAI(
    proxy_model_name="gpt-4o-mini", proxy_client=proxy_client, temperature=0.0
)

system_prompt_template = (
    "system",
    """ 
    Extract the following details from the given job description and return them in a structured JSON format:
    {jobDescription}
    
    Job Title (e.g., "Software Engineer")
    Company Name (e.g., "Tech Corp")
    Required Skills (list of hard/technical skills like "Docker", "Kubernetes", etc.)
    Preferred Skills (optional, if mentioned)
    Job Location (e.g., "Remote", "New York, NY")
    Job Type (e.g., "Full-time", "Contract")
    Experience Level (e.g., "Mid-level", "Senior")
    Salary Range (if mentioned)
    Job Responsibilities (bullet-point list)
    Qualifications (e.g., education, certifications)
    
    Output Format (JSON):
    {{
        "title": "",
        "company": "",
        "required_skills": [],
        "preferred_skills": [],
        "location": "",
        "job_type": "",
        "experience_level": "",
        "salary_range": "",
        "responsibilities": [],
        "qualifications": []
    }}
    
    Instructions:
    Omit fields if data is unavailable.
    Normalize skill names (e.g., "K8s" → "Kubernetes").
    Extract only explicit requirements (avoid inferred skills).
    """,
)

agent_prompt_template = ChatPromptTemplate([system_prompt_template])

agent = agent_prompt_template | chat_llm | JsonOutputParser()
