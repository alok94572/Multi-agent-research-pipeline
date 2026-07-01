📜 Research Pipeline
Multi‑Agent AI Research & Automated Report Generation System
A fully automated AI-powered research pipeline built using LangChain, Ollama (Llama 3.1), and Streamlit.

This system orchestrates four specialized AI agents that work sequentially to:

Search the web
Scrape deep content
Generate a structured research report
Critically evaluate the final output
The final result is a professional research document that can be downloaded as:

📄 PDF (Styled & Print-Ready)
📝 DOCX (Editable Word Document)
🗒️ TXT (Plain Text)
🚀 Live Workflow
text

User Input (Research Topic)
        │
        ▼
🔍 Search Agent
        │
        ▼
📖 Reader Agent
        │
        ▼
✍️ Writer Agent
        │
        ▼
🧐 Critic Agent
        │
        ▼
📄 Final Report + Feedback + Downloads
✨ Features
✅ Multi-Agent Architecture (Modular & Scalable)
✅ Real-time Web Search
✅ Intelligent URL Selection & Scraping
✅ Structured Research Report Generation
✅ AI-Powered Critical Review with Scoring
✅ Beautiful Streamlit UI with Live Agent Status
✅ Progress Tracking & Activity Logs
✅ Export Options (PDF, DOCX, TXT)
✅ Clean Session State Management

🧠 Agent Breakdown
🔍 Search Agent
Finds recent, reliable, and detailed information about the topic.
Uses a web search tool.
📖 Reader Agent
Selects the most relevant URL.
Scrapes deeper content from the page.
✍️ Writer Agent
Generates a structured report:

Introduction
Key Findings (Minimum 3 detailed points)
Conclusion
Sources
🧐 Critic Agent
Strictly evaluates the report and provides:

text

Score: X/10

Strengths:
- ...

Areas to Improve:
- ...

One line verdict:
...
🛠️ Tech Stack
Python
LangChain
Ollama (Llama 3.1)
Streamlit
FPDF2
python-docx
dotenv
📂 Suggested Project Structure
text

research-pipeline/
│
├── app.py                # Streamlit UI
├── pipeline.py           # Agent execution logic
├── agents.py             # Agent and chain definitions
├── tools.py              # Web search & scraping tools
├── .env                  # Environment variables
├── requirements.txt
└── README.md
⚙️ Installation Guide
1️⃣ Clone the Repository
Bash

git clone https://github.com/your-username/research-pipeline.git
cd research-pipeline
2️⃣ Create Virtual Environment (Recommended)
Mac / Linux
Bash

python -m venv venv
source venv/bin/activate
Windows
Bash

python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
If you have a requirements.txt:

Bash

pip install -r requirements.txt
Or install manually:

Bash

pip install streamlit langchain langchain-core langchain-ollama python-dotenv fpdf2 python-docx
4️⃣ Install & Run Ollama
Download Ollama from:

👉 https://ollama.com/download

Pull the required model:

Bash

ollama pull llama3.1
Make sure Ollama is running locally before starting the app.

▶️ Running the Application
Bash

streamlit run app.py
Then open:

text

http://localhost:8501
📥 Download Options
After pipeline completion, you can download:

Format	Description
📄 PDF	Styled, print-ready report
📝 DOCX	Editable Microsoft Word file
🗒️ TXT	Plain text version
🎨 UI Highlights
Modern dark premium theme
Animated hero section
Real-time agent status cards
Step progress bar
Activity logs
Clean tab-based result layout
Structured output formatting
🔐 Environment Variables
If your search tool requires API keys, create a .env file:

text

YOUR_API_KEY=your_key_here
Load it in Python:

Python

from dotenv import load_dotenv
load_dotenv()
📌 Example Use Cases
Academic research assistance
Technical deep-dives
AI-generated whitepapers
Market research summaries
Quick research validation
Learning & topic exploration
🔮 Future Improvements
Multi-source scraping (instead of single URL)
Citation formatting (APA / MLA / Chicago)
RAG with vector database
Agent memory support
Cloud deployment version
Parallel agent execution
Adjustable research depth (Basic / Advanced / Expert)
🤝 Contributing
Pull requests are welcome.

If you'd like to improve:

UI/UX
Agent reasoning
Prompt engineering
Search accuracy
Performance optimization
Fork the repo and submit a PR 🚀

📜 License
MIT License

👨‍💻 Author
Built with ❤️ using LangChain, Ollama, and Streamlit.