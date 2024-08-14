import os
from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.schema import HumanMessage
model = ChatOpenAI(
    model_name='gpt-4o-mini'
)
load_dotenv(dotenv_path='/Users/christophergusty/code/packt/.env', override=True)
key = os.environ["SERPAPI_API_KEY"]
search = SerpAPIWrapper(serpapi_api_key=key)
tools = [
    Tool.from_function(
        func=search.run,
        name="Search",
        description="useful for when you need to answer questions about current events"
    )
    ]
agent_executor = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent_executor('how many gold, silver, and bronze medals did the USA win in the 2024 Paris Olympics?'))

