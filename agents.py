from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)

# Writer
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer."),
    ("human", """Write a detailed research report on:

Topic: {topic}

Research:
{research}

Structure:
- Introduction
- Key Findings (min 3)
- Conclusion
- Sources
""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict research critic."),
    ("human", """Review this report:

{report}

Format:
Score: X/10
Strengths:
- ...
Areas to Improve:
- ...
Verdict:
...""")
])

critic_chain = critic_prompt | llm | StrOutputParser()
