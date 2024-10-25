# Agent-Gen-AI

# Agents :

**LangChain Agent with OpenAI and Tool Integration**
Demonstrates the use of LangChain agents, specifically the Zero-Shot React Description agent, in conjunction with OpenAI's GPT-3.5-turbo model and various tools (e.g., SerpAPI, Wikipedia, LLM Math). The code showcases how an agent is initialized and can respond to both pre-2021 knowledge queries as well as those requiring real-time data fetching from external APIs.

**Key Features:**
Integration with LangChain: The agent leverages LangChain for managing tool integrations and query resolution.
External Tools:
SerpAPI: Fetches live data, like US GDP in 2024.
Wikipedia: Fetches historical information or recent knowledge (e.g., World Cup winners).
LLM Math: Performs mathematical operations using LLM.


1.**Create Virtual Environment**

2.**Install Dependencies:**
   Install the necessary Python libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
   
   Note : facing some issue to get Output so we have install library "numexpr"