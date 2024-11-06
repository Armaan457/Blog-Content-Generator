# Blog Content Generator

A blog content generator project that utilises AI agents to research and write blog posts based on YouTube videos from a specific channel.

# Technologies used
**Framework**: CrewAI <br>
**LLM**: llama3-8b-8192 (via Groq) <br>
**Database**: SQLite & Chroma (Chroma using SQLite as its storage backend) <br>
**Tools**: YoutubeChannelSearchTool <br>

# Setup

Clone the repository:

```sh
> git clone https://github.com/Armaan457/Blog-Content-Generator.git
```

Create and activate a virtual environment:

```sh
> python -m venv venv
> venv\scripts\activate
```

Install dependencies:

```sh
> pip install -r requirements.txt
```

Run the main script:

```sh
> python crew.py
```

# Example

Provided in the `blog_content.md` file is the blog content for the video **How To Learn Data Science Smartly  by Krish Naik**