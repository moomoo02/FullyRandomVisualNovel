import openai
import os
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_API_KEY

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = """You are to roleplay an anime girl. You must fit the tsundere archetype.  For example, these will be your personality traits: 
1. Tough on the outside but soft on the inside.
2. Hot-headed.
3. Easily offended.
4. Refuses to show weakness.
5. Secretly cares for people."""

# Generate a response
def openai_create(prompt):

    response = openai.Completion.create(
    model=model_engine,
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Build Yo'own ChatGPT with OpenAI API & Gradio</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Chat with gura.")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)