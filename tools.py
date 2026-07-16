from langchain.tools import tool
from tavily import TavilyClient
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# ─────────────────────────────────────────────
# 🔍 WEB SEARCH TOOL
# ─────────────────────────────────────────────
@tool
def web_search(query: str) -> str:
    """
    Search the web for reliable information.
    Returns structured results (Title, URL, Snippet).
    """

    try:
        results = tavily.search(query=query, max_results=5)

        formatted_results = []

        for r in results.get("results", []):
            formatted_results.append(
                f"Title: {r.get('title')}\n"
                f"URL: {r.get('url')}\n"
                f"Snippet: {r.get('content', '')[:250]}\n"
            )

        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"Search error: {str(e)}"


# ─────────────────────────────────────────────
# 📖 SCRAPE URL TOOL (CLEANED VERSION)
# ─────────────────────────────────────────────
@tool
def scrape_url(url: str) -> str:
    """
    Robust, fast scraper that reads text from a URL using requests and BeautifulSoup.
    Truncates content safely to prevent LLM context overflow.
    """
    import requests
    from bs4 import BeautifulSoup
    import re
    
    MAX_CHARS = 10000
    
    try:
        response = requests.get(
            url,
            timeout=8,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            }
        )
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header", "aside"]):
            script.decompose()
            
        # Target the main article or fallback to body/all p tags
        main_content = soup.find("article") or soup.find("main") or soup.find("div", {"id": "content"}) or soup.body
        
        if not main_content:
            return "Could not extract readable content from this page."
            
        paragraphs = main_content.find_all("p")
        
        if not paragraphs:
            # Fallback to general text extraction
            text = main_content.get_text(separator="\n")
        else:
            text = "\n".join(
                p.get_text(strip=True)
                for p in paragraphs
                if len(p.get_text(strip=True)) > 40
            )
            
        # Clean up the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # Truncate to MAX_CHARS
        if len(text) > MAX_CHARS:
            text = text[:MAX_CHARS] + "... [Content truncated for length]"
            
        return text.strip()
        
    except requests.Timeout:
        return "Scraping failed: Request timed out."
    except requests.RequestException as e:
        return f"Scraping failed: Request error - {str(e)}"
    except Exception as e:
        return f"Scraping failed safely: {str(e)}"
