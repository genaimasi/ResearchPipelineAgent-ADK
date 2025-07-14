from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm

# Load environment variables (.env must contain: GOOGLE_API_KEY)
load_dotenv()

# Use Gemini model instead of OpenAI
model = "gemini-2.5-flash"   # Gemini Pro model name for ADK
model_abstraction = model

# Research Agent
research_agent = LlmAgent(
    name="research_agent",
    instruction="You will research on a provided topic and share the output of research",
    model=model_abstraction,
    output_key="research_content"
)

# Reviewer Agent
reviewer_agent = LlmAgent(
    name="reviewer_agent",
    instruction="""
    You are an expert reviewer.
    You will review the below provided content and make changes to make 
    the content more engaging and impactful.

    **Content to review**
    {research_content}
    """,
    model=model_abstraction,
    output_key="reviewed_content"
)

# LinkedIn Poster Agent
linkedin_poster = LlmAgent(
    name="linkedin_agent",
    instruction="""
    You are an expert writer of articles on LinkedIn.
    You will be provided with research content. You will need to create 
    an impactful title for the content. You will also format the content 
    aligning it to LinkedIn article format. The final title and content output 
    must be ready to be posted on LinkedIn.

    **Content to review**
    {reviewed_content}
    """,
    model=model_abstraction,
    output_key="linkedin_content"
)

# Sequential Pipeline
research_pipeline_agent = SequentialAgent(
    name="LinkedInPostPipelineAgent",
    sub_agents=[research_agent, reviewer_agent, linkedin_poster],
    description="Executes a sequence of research and research review activities.",
)

# Root Agent
root_agent = research_pipeline_agent