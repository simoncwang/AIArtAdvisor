import base64
import requests
from openai import OpenAI
import gradio as gr
import numpy as np 
from PIL import Image as im 

def critic(np_image):

    # converting input image from numpy array to png and saving it
    image = im.fromarray(np_image)
    image.save('test_images/image.png')

    # OpenAI API Key
    api_key = "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"

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # # Path to your image
    image_path = "test_images/image.png"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "You are a knowledgeable art critic, skilled in giving the artist both positive and negative feedback to help them improve their artwork"},
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Please give me constructive feedback on this artwork."
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # print(response.json()['choices'][0]['message']['content'])

    return response.json()['choices'][0]['message']['content']



demo = gr.Interface(
    critic,
    gr.Image(),
    outputs=["text"],
    title = "Art Advisor",
    description = "Welcome to your personal art advisor! I can help give you constructive feedback so you can take your art to the next level!",
)

demo.launch()