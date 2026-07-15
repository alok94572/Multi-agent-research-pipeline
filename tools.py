from langchain.tools import tool
from tavily import TavilyClient
from newspaper import Article
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
    Robust scraper with:
    - Wikipedia handling
    - Junk removal
    - Sentence-safe truncation
    - Crash protection
    """

    try:
        from newspaper import Article
        from bs4 import BeautifulSoup
        import requests
        import re

        MAX_CHARS = 8000

        # ✅ Wikipedia handling
        if "wikipedia.org" in url:
            response = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            soup = BeautifulSoup(response.text, "html.parser")

            content_div = soup.find("div", {"id": "mw-content-text"})

            if content_div:
                paragraphs = content_div.find_all("p")
            else:
                paragraphs = soup.find_all("p")

            raw_text = "\n".join(
                p.get_text(strip=True)
                for p in paragraphs
                if len(p.get_text(strip=True)) > 80
            )

        else:
            # ✅ Normal websites
            article = Article(url)
            article.download()
            article.parse()

            raw_text = article.text

            if not raw_text:
                return "No readable article content found."

        # ✅ Remove common junk phrases
        junk_phrases = [
            "Read More",
            "Continue reading",
            "Advertisement",
            "Subscribe",
            "Sign up",
            "Back to top"
        ]

        for phrase in junk_phrases:
            raw_text = raw_text.replace(phrase, "")

        # ✅ Remove breadcrumb-style patterns (Adventure / Arctic)
        raw_text = re.sub(r"\w+\s*/\s*\w+", "", raw_text)

        # ✅ Remove very short junk lines
        lines = raw_text.split("\n")
        cleaned_lines = [
            line.strip()
            for line in lines
            if len(line.strip()) > 40
        ]

        cleaned_text = "\n".join(cleaned_lines)

        # ✅ ✅ ✅ Sentence-safe truncation
        sentences = re.split(r'(?<=[.!?])\s+', cleaned_text)

        final_text = ""
        current_length = 0

        for sentence in sentences:
            sentence = sentence.strip()

            if not sentence:
                continue

            if current_length + len(sentence) > MAX_CHARS:
                break

            final_text += sentence + " "
            current_length += len(sentence)

        return final_text.strip()

    except Exception as e:
        return f"Scraping failed safely: {str(e)}"
