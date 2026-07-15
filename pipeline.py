from tools import web_search, scrape_url
from agents import writer_chain, critic_chain
import re

def run_research_pipeline(topic: str):

    state = {}

    print("Step 1 — Searching...")
    search_results = web_search.invoke({"query": topic})
    state["search_results"] = search_results

    print("Step 2 — Extracting URL...")
    urls = re.findall(r'https?://\S+', search_results)

    if urls:
        best_url = urls[0]
        scraped_content = scrape_url.invoke({"url": best_url})
    else:
        scraped_content = "No valid URL found."

    state["scraped_content"] = scraped_content

    print("Step 3 — Writing report...")
    research_combined = f"""
SEARCH RESULTS:
{search_results}

SCRAPED CONTENT:
{scraped_content}
"""

    report = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    state["report"] = report

    print("Step 4 — Critic reviewing...")
    feedback = critic_chain.invoke({
        "report": report
    })

    state["feedback"] = feedback

    return state
