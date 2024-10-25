
from langchain.agents import AgentType,initialize_agent,load_tools
from load_llm import *

# load tools(wikipedia) and get agent
def load_tools_and_get_agent():
  llm = get_LLM()
  tool = load_tools(["wikipedia","llm-math"],llm=llm)
  agent = initialize_agent(tool, llm, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose= True)
  return agent

agent = load_tools_and_get_agent()


# This is the old question means LLM easily give answer
print(agent.run("In which year First cricket played?"))

print("=================")
print()

# Latest question it means LLM Not train on latest data , so here LLM just refine answer of wikipedia
print(agent.run("Who won 2024  Cricket T-20 World cup?"))

print("=================")
print()