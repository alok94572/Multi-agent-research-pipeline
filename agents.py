from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

# Writer
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert, professional research writer. Your task is to write a comprehensive, well-structured research report in Markdown format."),
    ("human", """Write a detailed, advanced research report on:

Topic: {topic}

Research Data:
{research}

Format Requirements:
Use Markdown format strictly.
# Introduction
Write a compelling introduction summarizing the topic.

## Key Findings
Provide at least 3-5 detailed key findings based strictly on the research provided. Use bullet points or numbered lists where appropriate.

## In-Depth Analysis
Analyze the implications, future outlook, or deeper technical context of the findings.

## Conclusion
Provide a strong concluding summary.

## Sources
List the URLs or sources used in the research data.
""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict, expert research critic and editor. You critically review research reports for accuracy, depth, and formatting."),
    ("human", """Review the following research report:

{report}

Provide your feedback strictly in the following Markdown format:

# Critic Review

**Score:** X/10

### 🟢 Strengths:
- (List 2-3 strong points of the report)

### 🔴 Areas to Improve:
- (List 2-3 specific improvements, missing details, or formatting issues)

### ⚖️ Verdict:
(One line overall verdict)""")
])

critic_chain = critic_prompt | llm | StrOutputParser()
