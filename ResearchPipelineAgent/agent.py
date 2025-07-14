from dotenv import load_dotenv
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

# Load environment variables from the .env file
load_dotenv()

# Define the model to be used by all agents for consistency
model_abstraction = "gemini-2.0-flash"

# --- Agent 1: Web Searcher ---
# This agent takes the user's initial query, searches the web, and passes the raw results.
web_search_agent = Agent(
    name="web_search_agent",
    description="Researches a given topic using Google Search.",
    model=model_abstraction,
    instruction="You are a web researcher. Use the google_search tool to find information on the provided topic.",
    tools=[google_search],
    output_key="search_results"  # The output will be stored in this variable
)

# --- Agent 2: Summarizer ---
# This agent takes the search results and creates a concise summary.
summarizer_agent = Agent(
    name="summarizer_agent",
    description="Summarizes the content provided to it.",
    model=model_abstraction,
    instruction="""
    You are an expert summarizer.
    Review the provided search results below and create a clear and concise summary of the main points.

    **Search Results to review**
    {search_results}
    """,
    output_key="summary"  # The output will be stored in this variable
)

# --- Agent 3: Fact-Checker and Report Writer ---
# This agent takes the summary, fact-checks it, and writes the final report.
fact_checker_agent = Agent(
    name="fact_checker_agent",
    description="Fact-checks a summary and writes a final report.",
    model=model_abstraction,
    instruction="""
    You are a meticulous fact-checker and report writer.
    Your final task is to review the summary provided below, use the google_search tool to verify its claims,
    and then write a final, polished report for the user. Clearly state whether claims are verified.

    **Summary to fact-check**
    {summary}
    """,
    tools=[google_search],
    # This is the final step, so its output will be the final response to the user.
    output_key="final_report"
)

# --- The Sequential Pipeline Agent ---
# This agent orchestrates the entire workflow by running the sub-agents in a specific order.
research_pipeline = SequentialAgent(
    name="ResearchPipelineAgent",
    description="Executes a sequence of search, summarization, and fact-checking.",
    sub_agents=[
        web_search_agent,
        summarizer_agent,
        fact_checker_agent
    ],
)

# --- The Root Agent ---
# The adk web command will discover and serve this root_agent.
root_agent = research_pipeline