import asyncio
from teams.get_team import getDataAnalyzerTeam
from models.deepseek_model_client import get_deepseek_model_client
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.ui import Console

async def main():
    deepseek_model_client = get_deepseek_model_client()
    team = getDataAnalyzerTeam(deepseek_model_client)

    try:
        task = "How amny territories are there and can you list all of them?"
        ##async for message in team.run_stream(task=task):
        ##print(message)
        
        await Console(team.run_stream(task=task))


    except Exception as e:
        print(e)

    
if(__name__=='__main__'):
    asyncio.run(main())