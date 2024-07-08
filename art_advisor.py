import base64
import requests
from openai import OpenAI
import gradio as gr
import numpy as np
import os
from PIL import Image as im 

# art critique function
def critique(language, system_role, your_image, openai_api_key, user_text):

    print(system_role)

    # converting input image from numpy array to png and saving it
    image = im.fromarray(your_image)
    image.save('images/image.png')

    # checking if the image size is less than 20MB (requirement for gpt vision)
    print(os.path.getsize('images/image.png'))
    if os.path.getsize('images/image.png') > 20000000:
        raise gr.Error('File size is > 20MB, please choose a different file')

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # # Path to your image
    image_path = "images/image.png"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
    }

    # the defualt input text prompt
    default_text = "Please give me constructive feedback on this artwork, and things I could work on to improve it."

    # "You are a knowledgeable art critic, skilled in giving the artist feedback to help them improve their artwork. Please list out both positive and negative aspects of their work in a constructive way. Also, do your best to take into account any specific questions or comments they have and answer them!"

    payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": system_role + language},
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": default_text
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            },
            {
            "type": "text",
            "text": user_text   
            }
        ]
        }
    ],
    "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # print(response.json()['choices'][0]['message']['content'])

    return response.json()['choices'][0]['message']['content']


# Gradio demo!

# the role of the system
system_prompt = "test"

# system role prompt strings
genz_prompt = "Give constructive feedback for this painting including negative and positive aspects as well as how to improve, but use gen-z slang and references in your response."

beginner_prompt = "You are an art teacher focused on inspiring young or beginner artists. Please list out both positive and negative aspects of their work in a constructive way. Answer their questions and give advice using very simple terms that are easy to understand for a beginner artist or young child, but still accurate enough to teach them good art principles! Think children's book or cartoon tone!"

intermediate_prompt = "You are an art critic that focuses on intermediate level artists. Think a high school student or artist that has a few years of experience! Give them constructive feedback by listing out both positive and negative aspects of their work as well as how to improve it!"

advanced_prompt = "You are an expert art critic that specializes in helping professional artists improve. You are skilled and extremely knowledgeable about advanced art techniques. Please list out both positive and negative aspects of their work in a constructive way. Answer any questions the artist might have and provide feedback using a tone that an extremely experienced artist would benefit from. Think art textbook or professional artist in terms of the tone of your response!"

# language prompts
english_prompt = "Please write your response in English."

chinese_prompt = "Please write your response in Chinese."
    
with gr.Blocks() as demo:
    gr.Markdown(
        """

        # AI Art Advisor

        Welcome to your personal AI art advisor! I can give you constructive feedback to help you learn and take your art to the next level!
        """
    )

    with gr.Accordion("Click for instructions:", open=False):
        gr.Markdown(
            """

            - Upload any artwork as a .png or .jpg image into the image upload section. Note, due to gpt-4o restrictions, please keep file sizes <20MB!

            - Paste your own OpenAI API key into the API key textbox.

            - (Optional) Type any specific questions or comments into the additional textbox. For example, "I am having trouble making this painting more interesting, what could I do to create a better focal point?"
                - By default, the advisor will give you the postives and negatives of your work, as well as some advice on how to improve it
            
            """
        )

    with gr.Row():
        with gr.Column():
            gr.Markdown("## Your art")
            image = gr.Image()
            api_key = gr.Textbox(label="OpenAI API Key", placeholder="your API key here")
            user_text = gr.Textbox(label="Specific questions", placeholder="your questions or comments here")

            skill_select = gr.Dropdown(
                choices=[("Gen-Z", genz_prompt), ("Beginner", beginner_prompt), ("Intermediate", intermediate_prompt), ("Advanced", advanced_prompt)], 
                label="Level", 
                info="Select your desired skill level to cater your feedback!",
                value=intermediate_prompt,
                interactive=True
            )

            language_select = gr.Dropdown(
                choices=[("English", english_prompt), ("Chinese", chinese_prompt)], 
                label="Language", 
                value=english_prompt,
                interactive=True
            )

            submit_btn = gr.Button("Submit")


        with gr.Column():
            gr.Markdown("## Feedback")
            result = gr.Markdown(label="Feedback")

    submit_btn.click(critique, inputs=[language_select,skill_select,image,api_key,user_text], outputs=result)

# demo = gr.Interface(
#     critique,
#     inputs=[gr.Image(), "text"],
#     outputs=["text"],
#     title = "Art Advisor",
#     description = "Welcome to your personal art advisor! I can give you constructive feedback to help you learn and take your art to the next level!",
# )

# launching the demo
demo.launch()