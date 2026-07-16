# 📜 Research Pipeline

**Multi‑Agent AI Research & Automated Report Generation System**

A fully automated, ultra-fast AI-powered research pipeline built using **LangChain**, **Google Gemini API**, and **Streamlit**.

This system orchestrates four specialized AI agents that work sequentially to:
1. **Search the web** for the latest, most relevant information.
2. **Scrape deep content** from the top sources.
3. **Generate a structured research report** synthesizing the findings.
4. **Critically evaluate** the final output for accuracy and depth.

The final result is a professional research document that can be instantly downloaded as:
- 📄 **PDF** (Styled & Print-Ready)
- 📝 **DOCX** (Editable Word Document)
- 🗒️ **TXT** (Plain Text)

---

## 🚀 Live Workflow

```text
User Input (Research Topic)
        │
        ▼
🔍 Search Agent (Tavily/DuckDuckGo)
        │
        ▼
📖 Reader Agent (BeautifulSoup Web Scraper)
        │
        ▼
✍️ Writer Agent (Gemini 3.5 Flash)
        │
        ▼
🧐 Critic Agent (Gemini 3.5 Flash)
        │
        ▼
📄 Final Report + Feedback + Downloads
```

---

## ✨ Features
- **Multi-Agent Architecture**: Modular & scalable design.
- **Lightning Fast**: Powered by Google's `gemini-3.5-flash` for instant report generation.
- **Dynamic UI**: Beautiful Streamlit interface with live skeleton loaders and real-time agent status cards.
- **Robust Web Scraping**: Custom BeautifulSoup integration with strict timeouts to prevent hanging.
- **AI-Powered Critical Review**: Objective scoring and actionable feedback on every report.
- **Export Options**: Natively generate PDF, DOCX, and TXT files.

---

## ⚙️ Installation & Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/research-pipeline.git
cd research-pipeline
```

### 2️⃣ Create Virtual Environment (Highly Recommended)
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Mac / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Install all required packages via pip:
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up Environment Variables
This project requires API keys for Google Gemini and Tavily Search. Create a file named `.env` in the root directory and add the following:
```env
Tavily_Api_key=your_tavily_key_here
GOOGLE_API_KEY=your_gemini_key_here
```

### 5️⃣ Run the Application
```bash
streamlit run app.py
```
Then open your browser to `http://localhost:8501`.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **LangChain & LangChain Google GenAI**
- **Google Gemini (gemini-3.5-flash)**
- **Streamlit** (Frontend UI)
- **BeautifulSoup & Requests** (Web Scraping)
- **FPDF2 & python-docx** (Document Export)
- **python-dotenv**

---

## 🔮 Future Improvements
- Multi-source scraping (instead of single URL)
- Citation formatting (APA / MLA / Chicago)
- RAG with vector database integration
- Adjustable research depth (Basic / Advanced / Expert)

---
*Built with ❤️ using LangChain, Google Gemini, and Streamlit.*
