from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

research_task = Task(
    description=
        "Identify the video {topic}"
        "Get detailed information about the video from the channel",
    expected_output = "A detailed summary of the video {topic} based on the video content",    
    tools = [yt_tool],
    agent = blog_researcher
)

writing_task = Task(
    description=
        "Get info from youtube channel on video {topic}",
    expected_output = "Summarise the info from youtube channel on topic {topic} and create content for blog",    
    tools = [yt_tool],
    agent = blog_writer,
    aysnc_execution = False,
    output_file="blog_content.md"
)