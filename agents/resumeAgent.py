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
    Analyze the provided resume 
    {resume}
    Extract the following information in a structured JSON format. Ensure all fields are accurately captured:
    
    {{
        "name": "string",              // Full name of the candidate
        "skills": ["string", ...],     // List of technical/professional skills (e.g., Python, Django, etc.)
        "education": [                // List of educational qualifications
            {{
            "degree": "string",        // Degree name (e.g., "Bachelor of Science")
            "institution": "string",  // University/school name
            "year": "string"          // Graduation year (e.g., "2020")
            }},
            ...
        ],
        "work_experience": [          // List of work experiences
            {{
            "role": "string",         // Job title (e.g., "Software Engineer")
            "company": "string",      // Company name
            "duration": "string",     // Employment period (e.g., "Jan 2020 - Present")
            "description": "string"   // Key responsibilities/achievements (1-2 lines)
            }},
            ...
        ]
    }}
    
    Instructions:
    Name: Extract the full name from the header/contact section.
    Skills: Include hard skills (languages, tools, frameworks). Ignore vague terms like "teamwork."
    Education: Capture degrees, institutions, and years. Prioritize higher education.
    Work Experience: Focus on job titles, companies, durations, and concise descriptions.
    If a field is missing or unclear, return null or an empty array.\
        
    Example Output:
    {{
        "name": "John Doe",
        "skills": ["Python", "Django", "JavaScript", "SQL"],
        "education": [
            {{
            "degree": "Master of Computer Science",
            "institution": "XYZ University",
            "year": "2021"
            }}
        ],
        "work_experience": [
            {{
            "role": "Backend Developer",
            "company": "ABC Corp",
            "duration": "2021 - Present",
            "description": "Developed REST APIs using Django and optimized database queries."
            }}
        ]
    }}
    Notes:
    Prefer accuracy over completeness. Skip ambiguous details.
    Maintain consistent formatting (e.g., years as strings).
    """,
)

agent_prompt_template = ChatPromptTemplate([system_prompt_template])

agent = agent_prompt_template | chat_llm | JsonOutputParser()
