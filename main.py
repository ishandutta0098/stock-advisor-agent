from datetime import datetime

from crewai import Crew, Process

from src.agents import analyst, data_explorer, fin_expert, news_info_explorer
from src.tasks import advise, analyse, get_company_financials, get_company_news
from src.utils import timestamp

# Define the crew with agents and tasks in sequential process
crew = Crew(
    agents=[data_explorer, news_info_explorer, analyst, fin_expert],
    tasks=[get_company_financials, get_company_news, analyse, advise],
    verbose=True,
    Process=Process.sequential,
    step_callback=timestamp,
)

# Run the crew with a specific stock
result = crew.kickoff(inputs={"stock": "RELIANCE"})

# Print the final result
print("Final Result:", result)
