# Rural Build Guard Classifier

Enhancing Rural Infrastructure with AI Precision

This project implements a classifier that determines whether an image belongs to Indian rural areas or urban areas using machine learning models from Fastai and Gradio. The classifier is trained on the Techies dataset and deployed using Gradio for easy interaction.

## Live project

The project is live at https://huggingface.co/spaces/beckk123/ruralbuildguard

## Model

The model is available at https://drive.google.com/file/d/16RoJmW_k-IO2eja_LwUgqTCS5xaP-V-N/view
## Technologies Used

Python, FastAI, Convolutional Neural Networks (CNN), Transfer Learning, Image Classification, Data Preprocessing, Data Augmentation

## Installation

To install the required packages, use the following commands:

**pip install gradio torch fastai folium==0.12.1 flask**

## Usage

1. Make sure you have all the required dependencies installed.
2. Run the provided Python script `app.py`.
3. Upload an image to the interface.
4. The classifier will predict whether the image belongs to Indian rural areas or urban areas.

## File Description

- `app.py`: Contains the Python script for loading the model, defining the classification function, and launching the Gradio interface.
- `techiesmodel.pkl`: Pre-trained Fastai model for classifying images.
- `README.md`: This file, providing information about the project.
- `requirements.txt` : Lists all the dependencies required by the project.

## Requirements

- Python 3.6 or higher
- Gradio 4.8.0
- PyTorch
- Fastai
- Folium 0.12.1
- Flask

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
