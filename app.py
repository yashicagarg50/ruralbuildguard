from fastai.vision.all import *
import gradio as gr
from PIL import Image
def style(x): return x[0].isupper()


learn = load_learner('techiesmodel.pkl')

categories = ('Indian rural areas','Indian urban areas')

def classify_image(img):
    pred, idx, probs = learn.predict(img)
    img = img.resize((192, 192))
    # Your classification logic here
    return dict(zip(categories,map (float,probs)))



# image = gr.inputs.Image(shape=(192, 192))
# label = gr.outputs.Label()

# intf = gr. Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)

intf = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(),
    title="Rural Build Guard",
    description="Upload an image and classify whether it belongs to Indian rural areas or urban areas."
    # examples=['']
)

intf.launch(inline=False)
