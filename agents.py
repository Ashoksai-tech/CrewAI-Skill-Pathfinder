from crewai import Agent
from tools import serper_dev_tool
import os  
from crewai import LLM

from dotenv import load_dotenv

load_dotenv()


gemini_llm = LLM(model="gemini/gemini-2.0-flash",api_key=os.getenv("GEMINI_API_KEY"))
 


skill_trend_researcher = Agent(
    role = "Skill Trend Researcher",
    llm=gemini_llm,
    goal = "Identify the most in-demand and emerging skills in a given domain by analyzing job boards, tech blogs, and news articles.",
    verbose = True,
    memory = True,
    backstory = "You are an expert in labor market research and tech trends. You analyze current job postings and industry updates to extract relevant skills, tools, and trends that are highly sought after.",
    tools = [serper_dev_tool],  # example tools
    allow_delegation = True
)


study_plan_architect = Agent(
    role = "Study Plan Architect",
    llm = gemini_llm,
    goal = "Create a personalized, week-by-week learning roadmap using the skills identified by the Skill Trend Researcher and the user's preferences.",
    verbose = True,
    memory = True,
    backstory = "You are a skilled educational consultant and curriculum designer. You craft personalized learning paths that are aligned with market trends and tailored to the user’s time, level, and preferred learning style.",
    tools = [],  # example tools for generating structured plans
    allow_delegation = True
)


career_recommendation_agent = Agent(
    role = "Career Recommendation Advisor",
    llm = gemini_llm,
    goal = "Suggest potential job roles, certifications, and next steps based on the user's learning path and goals.",
    verbose = True,
    memory = True,
    backstory = "You are a career counselor with a deep understanding of job markets and career paths. You help learners understand how to turn their new skills into real opportunities, such as entry-level roles or freelance gigs.",
    tools = [],  # could use basic LLM or search if needed
    allow_delegation = False  # Should work independently
)

