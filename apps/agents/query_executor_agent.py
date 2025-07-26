import os
import sys
from autogen_agentchat.agents import AssistantAgent
from agents.prompts.query_executor_agent_prompt import query_executor_agent_prompt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from apps.utils.get_db_data import run_sql_query

def sql_executor_fn(sql_query:str) -> str:
    try:
            result = run_sql_query(sql_query)
            return f"Query executed successfully. Results:\n{result}"
    except Exception as e:
        return f"Execution error: {e}"
    
def getQueryExecutorAgent(model_client):
    query_executor_agent = AssistantAgent(
        name='QueryExecutorAgent',
        model_client=model_client,
        tools=[sql_executor_fn],
        description = 'An Agent that runs the Postgres SQL Query prepared by the Query Creator Agent using the tools provided',
        system_message=query_executor_agent_prompt
    )
    return query_executor_agent

