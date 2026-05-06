from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from typing import List

class CompanyReport(BaseModel):
    '''Detailed Research on company'''
    name: str = Field ("Official name of the company")
    summary: str = Field ("Brief 1 or 2 lines overview describing what the company does")
    technical_focus: List[str] = Field("Core technologies, domains, or technical areas focus of company")
    key_products: List[str] = Field("Major products or services offered by the company")
    competitors: List[str] = Field("Main competing companies in the same market or domain")
    risks: List[str] = Field("Potential risks such regulations, or technical challenges")
    sources: List[str] = Field("List of URLs or references used to gather the information")

@CrewBase
class Researcher():
    """Researcher crew"""

    agents_config="config/agents.yaml"
    tasks_config="config/tasks.yaml"

    @agent
    def Researcher_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Researcher_Agent'], 
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def Analyst_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Analyst_Agent'], 
            verbose=True
        )

   
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], 
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'], 
            output_pydantic=CompanyReport,
            output_file="output/final_report.md"
            
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Researcher crew"""
        

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            
        )
