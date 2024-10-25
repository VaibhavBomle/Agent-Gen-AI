from langchain.agents import AgentType,initialize_agent,load_tools
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize LLM
def get_LLM():
  openai_api_key = os.getenv("OPENAI_API_KEY")
  serp_api_key = os.getenv("SERP_API_KEY")
  os.environ["SERPAPI_API_KEY"] = serp_api_key  
  llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key= openai_api_key
   )
  return llm
