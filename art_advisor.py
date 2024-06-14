import base64
import requests
from openai import OpenAI
import gradio as gr
import numpy as np
import os
from PIL import Image as im 

# art critique function
def critique(your_image, openai_api_key, user_text):

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

    payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "You are a knowledgeable art critic, skilled in giving the artist feedback to help them improve their artwork. Please list out both positive and negative aspects of their work in a constructive way. Also, do your best to take into account any specific questions or comments they have and answer them!"},
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
            submit_btn = gr.Button("Submit")
        with gr.Column():
            gr.Markdown("## Feedback")
            result = gr.Markdown(label="Feedback")

    submit_btn.click(critique, inputs=[image,api_key,user_text], outputs=result)

# demo = gr.Interface(
#     critique,
#     inputs=[gr.Image(), "text"],
#     outputs=["text"],
#     title = "Art Advisor",
#     description = "Welcome to your personal art advisor! I can give you constructive feedback to help you learn and take your art to the next level!",
# )

# launching the demo
demo.launch()