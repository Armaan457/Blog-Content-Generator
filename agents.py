from crewai import Agent, LLM
from tools import yt_tool

import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model="groq/llama3-8b-8192", 
    base_url="https://api.groq.com/openai/v1", 
    api_key=os.getenv("GROQ_API_KEY")
)


blog_researcher = Agent(
    role = "Blog researcher from Youtube videos",
    goal = "Get relevant video content for topic {topic} from youtube channel",
    verbose = True,
    memory = True,
    backstory = "Expert in understanding videos about ML, DL and GenAI videos and providing suggestion",
    tools = [yt_tool],
    allow_delegation = True,
    llm=llm
)

blog_writer = Agent(
    role = "Blog writer",
    goal = "Write great tech content about video {topic} from youtube channel",
    verbose = True,
    memory = True,
    backstory = "A master of writing tech blogs and articles, helping people understand complex topics and learn better",
    tools = [yt_tool],
    allow_delegation = False,
    llm=llm
)