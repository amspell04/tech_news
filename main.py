import fetch_news 
import create_briefing
import invoke_news_analysis
from datetime import datetime
import subprocess

def generate_todays_briefing():
    todays_date = datetime.date
    briefing_name = "morning_digest" + todays_date

    todays_news = fetch_news()
    summarized_news = invoke_news_analysis(todays_news)
    briefing_path = create_briefing(summarized_news, briefing_name)

    subprocess.run(["lp", briefing_path])



if __name__ == "__main__":
    generate_todays_briefing()