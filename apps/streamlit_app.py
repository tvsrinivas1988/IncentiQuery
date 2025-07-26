import os
import asyncio
import streamlit as st
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from teams.get_team import getDataAnalyzerTeam
from models.deepseek_model_client import get_deepseek_model_client
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from autogen_agentchat.ui import Console


st.title(" IncentiQuery - Your DataBase  ChatBot!!")

user_question = st.text_input("Enter your question:")

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None



async def run_incentiquery(task):
    deepseek_model_client = get_deepseek_model_client()
    team = getDataAnalyzerTeam(deepseek_model_client)
    
    if st.session_state.autogen_team_state is not None:
        await team.load_state(st.session_state.autogen_team_state)

    try:
        #task = user_question
        async for message in team.run_stream(task=task):
            #st.markdown(f"**{message.content}")
            if isinstance(message,TextMessage):
                if message.source.startswith('user'):
                    with st.chat_message('user',avatar='👤'):
                        st.markdown(message.content)
                elif message.source.startswith('Planning_agent'):
                    with st.chat_message('Planning_agent',avatar='🤖'):
                        st.markdown(message.content)
                elif message.source.startswith('QueryCreatorAgent'):
                    with st.chat_message('QueryCreatorAgent',avatar='👨‍💻'):
                        st.markdown(message.content)
                elif message.source.startswith('QueryExecutorAgent'):
                    with st.chat_message('QueryExecutorAgent',avatar='👨'):
                        st.markdown(message.content)
                st.session_state.messages.append(message.content)
            elif isinstance(message,TaskResult):
                st.markdown(f'Stop Reason :{message.stop_reason}')
                st.session_state.messages.append(message.stop_reason)
                st.session_state.autogen_team_state = await team.save_state()

        
        return None
        #await Console(team.run_stream(task=task))


    except Exception as e:
        st.error(f"Error Occured !! {e}")
        return e
    
response = asyncio.run(run_incentiquery(user_question))