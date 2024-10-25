# Agent-Gen-AI

# Agents :

**LangChain Agent with OpenAI and Tool Integration**
This project demonstrates the use of LangChain agents integrated with OpenAI's GPT-3.5-turbo model to handle both pre-2021 knowledge and real-time queries using external tools like SerpAPI and Wikipedia. The agent is initialized to fetch live data when the LLM lacks up-to-date information, ensuring accurate responses to recent events or complex queries. Tools such as LLM Math allow the model to perform calculations. GPT-3.5-turbo’s knowledge cutoff is September 2021, so external APIs are used for real-time data. The project showcases dynamic agent responses with LangChain's Zero-Shot React Description agent.

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