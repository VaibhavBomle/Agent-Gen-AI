from langchain.agents import AgentType,initialize_agent,load_tools
from langchain_openai import ChatOpenAI
import os

from load_llm import *


# load tools(serpapi) and get agent
def load_tools_and_get_agent():
  llm = get_LLM()
  tool = load_tools(["serpapi","llm-math"],llm=llm)
  agent = initialize_agent(tool, llm, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose= True)
  return agent


agent = load_tools_and_get_agent()

print(agent.run("How much is US GDP in 2024 plus 5?"))

print("============",end="")
print(agent.run("in which year indian team won its second world cup?"))

print("============",end="")
print(agent.run("How much seat Won by indian Policitcs party in 2014?"))

"""
Note :
1. Here we asking queston GDP OF us in 2024 --> It means we are fetching a data from google search and passing to LLM for Refine and then added 5
It means GPT have trained on data up until September 2021. So agent come in picture.

2. GPT-3.5-turbo, like previous GPT models, is trained on data up until September 2021. This means that any knowledge or events occurring after that date are not included in the model's training data.
If you're working with GPT-3.5-turbo, keep in mind that the model will not have knowledge of events, developments, or information after September 2021 unless provided explicitly during a conversation.
"""