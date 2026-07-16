from tools import web_search, scrape_url
from agents import writer_chain, critic_chain
import re

def run_research_pipeline(topic: str):
    """
    Executes the research pipeline and yields progress updates to allow streaming UI.
    """
    state = {}

    yield {"step": 0, "status": "Searching the web...", "state": state}
    try:
        search_results = web_search.invoke({"query": topic})
        state["search"] = search_results
    except Exception as e:
        state["search"] = f"Search failed: {e}"

    yield {"step": 1, "status": "Reading and scraping content...", "state": state}
    urls = re.findall(r'https?://[^\s)\]]+', state.get("search", ""))
    
    if urls:
        best_url = urls[0]
        try:
            scraped_content = scrape_url.invoke({"url": best_url})
        except Exception as e:
            scraped_content = f"Scraping failed: {e}"
    else:
        scraped_content = "No valid URL found in search results."

    state["reader"] = scraped_content

    yield {"step": 2, "status": "Writing research report...", "state": state}
    research_combined = f"SEARCH RESULTS:\n{state.get('search', '')}\n\nSCRAPED CONTENT:\n{state.get('reader', '')}"
    
    try:
        report = writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })
    except Exception as e:
        report = f"Writing failed: {e}"

    state["report"] = report

    yield {"step": 3, "status": "Critic reviewing report...", "state": state}
    try:
        feedback = critic_chain.invoke({
            "report": report
        })
    except Exception as e:
        feedback = f"Review failed: {e}"

    state["feedback"] = feedback
    
    yield {"step": 4, "status": "Pipeline complete!", "state": state}
