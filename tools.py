from crewai_tools import YoutubeChannelSearchTool
import os

os.environ["OPENAI_API_KEY"] = "dummy_key" # To bypass the missing API key error, not used

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle="@krishnaik06")