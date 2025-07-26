from autogen_agentchat.agents import AssistantAgent
from agents.prompts.query_creator_agent_prompt import query_creator_agent_prompt
import os
import sys

def getQueryCreatorAgent(model_client):
    query_creator_agent = AssistantAgent(
        name='QueryCreatorAgent',
        model_client=model_client,
        description = 'An Agent that creates Postgres SQL Query for the input question',
        system_message=query_creator_agent_prompt
    )
    return query_creator_agent