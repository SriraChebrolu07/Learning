import os
from dotenv import load_dotenv
from crewai import Agent, Crew
from langchain_groq import ChatGroq
from langchain.agents import Tool
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, ReadOnlySharedMemory
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

# Initialize the language model
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

# Define the search tool
search = DuckDuckGoSearchRun()

# Define the tools for the agent
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    ),
]

# Define the agent
agent = Agent(
    role="Analysis Agent",
    goal="Answer user's requests accurately",
    tools=tools,
    llm=llm,
    memory=ConversationBufferMemory(memory_key="chat_history"),
)

# Define the crew
crew = Crew(agents=[agent])

# Define the task
task = "Answer the question: What is the capital of France?"

# Run the task
crew.run(task)
