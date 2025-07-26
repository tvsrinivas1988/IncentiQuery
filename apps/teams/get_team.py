from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination,MaxMessageTermination


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from agents.prompts.selector_prompt import selector_prompt

from agents.planning_agent import getPlanningAgent
from agents.query_creator_agent import getQueryCreatorAgent
from agents.query_executor_agent import getQueryExecutorAgent

def getDataAnalyzerTeam(model_client):
    planning_agent = getPlanningAgent(model_client)
    query_creator_agent = getQueryCreatorAgent(model_client)
    query_executor_agent = getQueryExecutorAgent(model_client)

    text_mention_termination = TextMentionTermination('TERMINATE')
    max_message_termination = MaxMessageTermination(max_messages=20)
    combined_termination = text_mention_termination | max_message_termination

    selector_team = SelectorGroupChat(
    participants=[planning_agent, query_creator_agent, query_executor_agent],
    model_client=model_client,
    termination_condition=combined_termination,
    selector_prompt=selector_prompt,
    allow_repeated_speaker=True)

    return selector_team

