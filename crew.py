from crewai import Crew, Process
from agents import skill_trend_researcher,study_plan_architect,career_recommendation_agent
from tasks import skill_research_task, study_plan_task, career_recommendation_task


crew = Crew(
    agents = [skill_trend_researcher, study_plan_architect, career_recommendation_agent],
    tasks = [skill_research_task, study_plan_task, career_recommendation_task],
    process = Process.sequential,
    memory = False,
    cache = False,
    max_rpm = 5,
    share_crew=True,
    llm_provider = "gemini"
)


result = crew.kickoff(inputs={"domain":"Artificial Intelligence"})
print(result)