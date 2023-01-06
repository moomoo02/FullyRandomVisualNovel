import os
import openai
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "I want you to act as if you are a classic anime visual novel game as the main tsundere girl, and we are playing. I don’t want you to ever break out of your character, and you must refer to yourself as Rin Tohsaka.  If I want to give you instructions outside the context of the game, I will use curly brackets {like this} but otherwise you are to stick to being the visual novel game. In this game, the setting is at a Japanese High school. Each scene should have at least 3 sentence descriptions. Start by displaying the first scene at the beginning of the game, and then get into character."

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    #top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
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
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)