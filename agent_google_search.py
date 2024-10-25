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


# load tools and get agent
def load_tools_and_get_agent():
  llm = get_LLM()
  tool = load_tools(["serpapi","llm-math"],llm=llm)
  agent = initialize_agent(tool, llm, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose= True)
  return agent


agent = load_tools_and_get_agent()

print(agent.run("How much is US GDP in 2024 plus 5?"))

"""
Note :
1. Here we asking queston GDP OF us in 2024 --> It means we are fetching a data from google search and passing to LLM for Refine and then added 5
It means GPT have trained on data up until September 2021. So agent come in picture.

2. GPT-3.5-turbo, like previous GPT models, is trained on data up until September 2021. This means that any knowledge or events occurring after that date are not included in the model's training data.
If you're working with GPT-3.5-turbo, keep in mind that the model will not have knowledge of events, developments, or information after September 2021 unless provided explicitly during a conversation.
"""