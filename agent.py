from browser_use.llm import ChatGoogle
from browser_use import Agent
from dotenv import load_dotenv
import asyncio

load_dotenv()
llm = ChatGoogle(model='gemini-2.0-flash-exp')

async def main():
    agent = Agent(
        task="search mrBeast youtube videos",
        llm=llm
    )
    result = await agent.run()
    print(f"Task completed: {result}")

if __name__ == "__main__":
    asyncio.run(main())