from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from apps.config.constants import MODEL_NAME,MODEL_BASE_URL,MODEL_FAMILY,MODEL_VISION,MODEL_FUNCTION_CALLING,MODEL_JSON_OUTPUT,MODEL_STRUCTURED_OUTPUT

from dotenv import load_dotenv

load_dotenv()
##api_key = os.getenv("OPENROUTER_API_KEY")
#api_key = os.getenv("OPENAI_API_KEY")
##api_key = os.getenv("GROQ_API_KEY")
api_key =st.secrets["GROQ_API_KEY"]


def get_deepseek_model_client():
    deepseekmodel_client =  OpenAIChatCompletionClient(model="meta-llama/llama-4-scout-17b-16e-instruct",
                                          base_url="https://api.groq.com/openai/v1",
                                          api_key=api_key,
                                          model_info={
        "family":'Groq',
        "vision" :True,
        "function_calling":True,
        "json_output": False,
        "structured_output": False
    }
)

    ##deepseekmodel_client = OpenAIChatCompletionClient(model="gpt-4o")

    return deepseekmodel_client
