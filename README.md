# Environment setup

First, clone this repository to your local machine:

    git clone https://github.com/simoncwang/ArtAdvisor.git

Then, create a Python environment

Conda:

    conda create -n advisor-env python=3.11

Python:

    python -m venv advisor-env

activate it with

Conda:

    conda activate advisor env

Python:

    advisor-env\Scripts\activate (windows)
    source advisor-env/bin/activate (Unix or MacOS)

# Launching the app

To demonstrate the functionality of the art advisor, a simple app has been created using Gradio. To launch it, simply run:

        python art_advisor.py

or

        python3 art_advisor.py

depending on how your environment is set up.

This will create an app running on a local server, which can be found by the url provided in the terminal or command line (e.g. http://127.0.0.1:XXXX).

# Usage

The Gradio app has several main sections:

## Image upload

Here, you can upload any image of your artwork (currently only supports .png format). You can also upload via webcam or your clipboard by selecting the icons at the bottom.

<img width="100%" alt="Screenshot 2024-06-06 at 6 39 15 PM" src="https://github.com/simoncwang/ArtAdvisor/assets/120291065/f1f53712-20db-44e2-9a25-85623abdff52">

## OpenAPI key

In order for the app to make api calls to the gpt-4o model, you must provide your own OpenAI API key. However, rest assured that no one (including me) will have access to your private key since this app is hosted locally on your computer!


<img width="100%" alt="Screenshot 2024-06-06 at 6 41 34 PM" src="https://github.com/simoncwang/ArtAdvisor/assets/120291065/5dd94dd6-cf51-4142-94a1-67005fb4fe45">

## Feedback window

After some time (typically 10-15 seconds depending on file size), the advisor will give you feedback/advice in the form of text here!

<img width="100%" alt="Screenshot 2024-06-06 at 6 42 25 PM" src="https://github.com/simoncwang/ArtAdvisor/assets/120291065/0566f999-7ed6-40a0-bbda-014f46da4bce">

