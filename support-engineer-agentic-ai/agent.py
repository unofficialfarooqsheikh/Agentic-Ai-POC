from agents import Agent, Runner, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv(override=True)

# PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"
# PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
# print(PERPLEXITY_API_KEY)
# perplexity_client = AsyncOpenAI(base_url=PERPLEXITY_URL, api_key=PERPLEXITY_API_KEY)
# perplexity_model = OpenAIChatCompletionsModel(model="pplx-70b-online", openai_client=perplexity_client)

GOOGLE_API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
google_api_client = AsyncOpenAI(base_url=GOOGLE_API_URL, api_key=GOOGLE_API_KEY)
google_api_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=google_api_client)

# groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
# deepseek_model = OpenAIChatCompletionsModel(model="deepseek-chat", openai_client=deepseek_client)


agent = Agent(name="Assistant", instructions="You are a helpful assistant", model=google_api_model)

result = Runner.run_sync(agent, "write python code to substract all the numbers from list 1 from list 2")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.