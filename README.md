# AI Art Advisor

## Environment setup

First, **clone this repository** to your local machine:

    git clone https://github.com/simoncwang/AIArtAdvisor.git

Then, **create a Python environment**

Conda:

    conda create -n advisor-env python=3.11

Python:

    python -m venv advisor-env

**activate the environment** with

Conda:

    conda activate advisor-env

Python:

    advisor-env\Scripts\activate (windows)
    source advisor-env/bin/activate (Unix or MacOS)

Next, **install the required packages** with:

        pip install -r requirements.txt

## Launching the app

To demonstrate the functionality of the art advisor, a **simple Gradio app** has been created. To launch it, simply run:

        python art_advisor.py

or

        python3 art_advisor.py

depending on how your environment is set up.

This will create an app running on a local server, which can be found by the url provided in the terminal or command line (e.g. http://127.0.0.1:XXXX). Open this in any browser to see the app!

## Usage

The Gradio app has several main sections:

### Image upload

Here, you can upload any image of your artwork (currently only supports .png format). You can also upload via webcam or your clipboard by selecting the icons at the bottom.

<img width="100%" alt="Screenshot 2024-06-06 at 6 39 15 PM" src="https://github.com/simoncwang/ArtAdvisor/assets/120291065/f1f53712-20db-44e2-9a25-85623abdff52">

### OpenAPI key

In order for the app to make api calls to the gpt-4o model, you must provide your own OpenAI API key. However, rest assured that no one (including me) will have access to your private key since this app is hosted locally on your computer!


<img width="100%" alt="Screenshot 2024-06-06 at 6 41 34 PM" src="https://github.com/simoncwang/ArtAdvisor/assets/120291065/5dd94dd6-cf51-4142-94a1-67005fb4fe45">

### Feedback window

After some time (typically 10-15 seconds depending on file size), the advisor will give you feedback/advice in the form of text here!

<img width="100%" alt="Screenshot 2024-06-06 at 6 42 25 PM" src="https://github.com/simoncwang/ArtAdvisor/assets/120291065/0566f999-7ed6-40a0-bbda-014f46da4bce">

## Example

As an example, I have uploaded an image of the famous Mona Lisa painting by Leonardo da Vinci to see what the art advisor has to say!

<img width="100%" alt="Screenshot 2024-06-06 at 6 43 37 PM" src="https://github.com/simoncwang/ArtAdvisor/assets/120291065/bc781c0b-3913-4f7e-919e-bb9a8dfc514f">

### Full feedback text

<blockquote>
This artwork is widely recognized as the "Mona Lisa," an iconic painting by Leonardo da Vinci. Here is some constructive feedback on this masterpiece:

### Positive Feedback:

1. **Use of Light and Shadow (Chiaroscuro):**
   - The subtle gradation of light and shadow creates a lifelike three-dimensionality and a tender, almost ethereal quality. This technique brings forward the subject with a delicate realism.

2. **Composition:**
   - The composition is perfectly balanced with the subject placed using the rule of thirds. The way the figure is framed against the background adds depth and guides the viewer's eye seamlessly through the painting.

3. **Expressive Face and Emotion:**
   - The enigmatic expression of the subject, often described as an ambiguous smile, invites a range of interpretations and emotions, making the artwork profoundly engaging and mysterious.

4. **Detail and Texture:**
   - The intricate detailing on the subject's hair, clothing, and the subtle textures of the skin showcase exceptional skill and attention to detail.

### Constructive Criticism:

1. **Varnish Yellowing:**
   - Over time, the varnish has yellowed, altering the original colors. Restorative work could potentially address this issue to bring back the painting's initial vibrancy.

2. **Background Detailing:**
   - While the background features beautifully misty landscapes, some critics might argue for a slightly more detailed rendering of elements to match the meticulous detail in the foreground subject.

3. **Posture and Hand Position:**
   - The posture and hand position of the subject are serene but could be viewed as somewhat stiff. Exploring slightly more relaxed or dynamic poses could add an additional layer of naturalism.

4. **Cohesion Between Foreground and Background:**
   - There is a slight stylistic difference between the hyper-realistic figure and the more abstract, sfumato background. A more cohesive blending of these elements could enhance the overall unity of the painting.

Overall, the "Mona Lisa" remains a timeless piece of art that continues to captivate viewers and artists alike. The feedback offered is in the context of taking an already renowned piece and discussing areas that provoke thought rather than suggesting fundamental changes to what many consider perfection.

</blockquote>
