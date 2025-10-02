from crewai import Task
 
from tools import serper_dev_tool
from agents import skill_trend_researcher, study_plan_architect, career_recommendation_agent

# Initialize Gemini tool
 

# Task 1: Research in-demand skills
skill_research_task = Task(
    description=(
        "Analyze the current job market and tech trends to identify the most in-demand "
        "skills and technologies in the user's domain of interest (e.g., Data Science, "
        "Cybersecurity, Web Development, UI/UX, Android development, Artificial Intelligence). Use Serper and web scraping to extract data "
        "from job boards and industry blogs."
    ),
    expected_output=(
        "A structured list of trending skills, tools, and job roles in the given domain, "
        "along with brief descriptions and popularity indicators."
    ),
    tools=[serper_dev_tool],
    agent=skill_trend_researcher
)

# Task 2: Build a personalized study plan
study_plan_task = Task(
    description=(
        "Based on the user's background, learning preferences, and the skills provided by "
        "the skill_trend_researcher, generate a personalized week-by-week learning plan. "
        "Include recommended courses, books, hands-on projects, and timelines."
    ),
    expected_output=(
        "A markdown-formatted study roadmap including weekly goals, resources, and suggested projects. "
        "The plan should be tailored to the user's skill level and time commitment."
    ),
    agent=study_plan_architect,
    async_execution=False,
    output_file='study_plan.md'
)

# Task 3: Career recommendations
career_recommendation_task = Task(
    description=(
        "Analyze the user's learning goals and the generated study plan to recommend relevant "
        "entry-level job roles, freelance opportunities, or certifications that align with the user's trajectory. "
        "Suggestions should be practical and achievable within a 3–6 month period."
    ),
    expected_output=(
        "A markdown-formatted list of recommended career paths, job titles, certifications, and platforms to apply "
        "or learn more (e.g., Coursera, CompTIA, Upwork, LinkedIn)."
    ),
    agent=career_recommendation_agent,
    async_execution=False,
    output_file='career_path.md'
)
