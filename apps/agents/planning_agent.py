from autogen_agentchat.agents import AssistantAgent
from agents.prompts.planning_agent_prompt import planning_agent_system_message


def getPlanningAgent(model_client):
    planning_agent = AssistantAgent(
        name='Planning_agent',
        model_client=model_client,
        description = 'An Agent that solves creates a detailed plan on how the input question can be broken down and tackled',
        system_message=planning_agent_system_message
    )
    return planning_agent