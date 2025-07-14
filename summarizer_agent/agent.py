from google.adk.agents import Agent

root_agent = Agent(
    name="summarizer_agent",
    description="An agent that takes a block of text and returns a concise summary.",
    model="gemini-2.0-flash",
    instruction="You are an expert text summarizer. Your sole purpose is to take the text provided by the user and generate a clear, concise, and accurate summary of its main points.",
    tools=[]
)