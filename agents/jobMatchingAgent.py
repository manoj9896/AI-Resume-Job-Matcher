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
    Analyze the given resume and job description, then provide a JSON output with the following details:
    
    Match Score (0-100): A numerical score representing how well the resume matches the job description based on skills, experience, and qualifications.
    Missing Skills: A list of key skills/technologies mentioned in the job description but missing from the resume.
    Summary: A brief explanation (2-3 sentences) of the candidate’s overall fit, highlighting strengths and gaps.
    
    Format the output as:
    {{
    "match_score": 85,
    "missing_skills": ["Docker", "Kubernetes"],
    "summary": "Candidate is a strong match overall..."
    }}
    
    Input:
    Resume: {resume}
    Job Description: {jobDescription}

    Instructions:
    Prioritize hard skills (e.g., tools, languages) and explicit requirements from the job description.
    Ignore minor formatting issues in the input texts.
    """,
)

agent_prompt_template = ChatPromptTemplate([system_prompt_template])

agent = agent_prompt_template | chat_llm | JsonOutputParser()
