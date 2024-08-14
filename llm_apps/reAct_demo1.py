import os
from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.schema import HumanMessage
model = ChatOpenAI(
    model_name='gpt-3.5-turbo'
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

print(agent_executor('who are going to be the italian male athletes for climbing at the Paris 2024 Olympics?'))

