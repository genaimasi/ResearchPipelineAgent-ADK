from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types

root_agent = Agent(
    name="fact_checker_agent",
    description="An agent that verifies claims using Google Search.",
    model="gemini-2.0-flash",
    instruction="""
    You are a meticulous fact-checker. Your sole purpose is to verify a claim provided by the user.

    You MUST follow this process:
    1.  Use the `Google Search` tool to find current information about the claim from reliable sources.
    2.  Compare the information from the search results to the user's original claim.
    3.  Based on your comparison, state whether the claim is "VERIFIED" or "UNVERIFIED".
    4.  Provide a brief justification for your conclusion, citing the source you found.
    """,
    tools=[google_search]
)