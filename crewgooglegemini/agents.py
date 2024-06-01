from crewai import Agent
from dotenv import load_dotenv
from tools import tool
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

news_researcher=Agent(
    role="Senior Researcher",
    goal='Uncover actual technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by Authenticity, you're at the forefront of"
        "innovation, and provide authentic information to explore and share knowledge that could change"
        "the current world filled with unrealistic information."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

news_writer = Agent(
  role='Writer',
  goal='Narrate Authetic information about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "at providing authentic narrative bringing"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

