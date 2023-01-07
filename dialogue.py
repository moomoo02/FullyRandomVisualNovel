import os
import openai
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

from pychatgpt import Chat, Options

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

options = Options()

# [New] Pass Moderation. https://github.com/rawandahmad698/PyChatGPT/discussions/103
# options.pass_moderation = False

# [New] Enable, Disable logs
options.log = True

# Track conversation
options.track = True 

# Use a proxy
options.proxies = 'http://localhost:8080'

# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist

# options.chat_log = "chat_log.txt"
# options.id_log = "id_log.txt"

# Create a Chat object
chat = Chat(email=EMAIL, password=PASSWORD, options=options)
answer = chat.ask("How are you?")
print(answer)