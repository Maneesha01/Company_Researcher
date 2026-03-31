from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from typing import List

class CompanyReport(BaseModel):
    '''Detailed Research on company'''
    Name: str = Field("Name of Company")
    Summary: str =Field("Summary of company in 1 line")
    Technical_Focus : str = Field("Technologies company is mainly focussed   on")
    Future_Aspirations: str = Field("Future aspirations of the company")

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
