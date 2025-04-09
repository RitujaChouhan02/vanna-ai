import os
from dotenv import load_dotenv
from vanna.openai import OpenAI_Chat
from vanna.vannadb import VannaDB_VectorStore


# Load the .env file
load_dotenv()

class MyVanna(VannaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        MY_VANNA_MODEL = 'metaverse'
        VANNA_API_KEY = os.getenv('VANNA_API_KEY')
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL,  vanna_api_key=VANNA_API_KEY, config=config)
        OpenAI_Chat.__init__(self, config=config)

vn = MyVanna(config={
    'api_key': os.getenv('OPENAI_API_KEY'),
    'model': 'gpt-4o-mini'
})