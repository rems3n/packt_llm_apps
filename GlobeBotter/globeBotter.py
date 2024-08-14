from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chains import LLMChain, ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

chat = ChatOpenAI()
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=chat, verbose=True, memory=memory
)

response = conversation.run("Hi there!")

print ("AI:", response)