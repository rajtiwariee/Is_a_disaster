import streamlit as st
import tensorflow as tf

# Load the pre-trained model
model_6_pretrained = tf.keras.models.load_model('./model_6_saved_model_format/')

# Set the Streamlit app title and description
st.title("Disaster 🌪️ Prediction App")
st.markdown("Enter text to predict if it indicates a disaster or not.")

# Input text box for user input
input_text = st.text_area("Enter the input:")

# Define class names for predictions
class_names = ['Not a Disaster🕊️', 'Disaster🌪️']

# Make a prediction when the user clicks the "Predict" button
if st.button("Predict"):
    if input_text:
        # Preprocess the input text
        input_text = [input_text]  # The model expects a list of inputs

        # Make predictions
        pred_prob = tf.squeeze(model_6_pretrained.predict(input_text))
        pred = int(tf.round(pred_prob))

        # Calculate the prediction probability as a percentage and format it
        prediction_probability_percentage = f"{pred_prob * 100:.2f}"

        # Display the prediction results
        st.subheader("Prediction Results:")
        st.write("Input Text:")
        st.write(input_text[0])
        st.write(f"Predicted Class: {class_names[pred]}")
        st.write(f"Prediction Probability: {prediction_probability_percentage}%")


# Add custom CSS for background image
# Add a background image using st.image
# background_image = st.image("background.jpg", use_column_width=True)
# Add a background image using CSS
# background_image_path = "./background.jpg"  # Replace with the actual absolute path
# st.markdown(
#     f"""
#     <style>
#     body {{
#         background-image: url("{background_image_path}");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# Add any additional content or explanations
# st.markdown("This app uses a pre-trained model to predict whether the entered text indicates a disaster or not.")

# About section
st.markdown("## About This App")

st.write("Welcome to the Disaster Prediction App, a tool designed to predict whether a given text indicates a disaster or not. This app utilizes a pre-trained text classification model, enabling quick and accurate predictions.")
st.write("Whether you want to assess social media posts, news articles, or any text data for potential disaster-related content, this app is here to assist you.")

st.markdown("### How It Works")
st.write("1. Enter the text you'd like to analyze into the input box.")
st.write("2. Click the 'Predict' button.")
st.write("3. The app will evaluate the text and provide a prediction as well as the prediction probability.")

st.markdown("### Model Details")
st.write("The app employs a pre-trained deep learning model that has been fine-tuned to classify text as either indicating a disaster or not. It is based on a neural network architecture and was trained on a diverse dataset of text examples.")

st.markdown("### Technology Stack")
st.write("This app is powered by Streamlit for the user interface and TensorFlow for the machine learning model. Streamlit offers a simple yet powerful way to create web apps, while TensorFlow is used for the text classification task.")

st.markdown("### Disclaimer")
st.write("The predictions made by this app are based on the patterns and information available in the training data. While it can be a valuable tool, please note that it may not be infallible and should be used in conjunction with human judgment for critical decisions.")


st.markdown("### References")
st.write("The underlying model and techniques used in this app may be based on research and resources from the following:")
st.write("- [Hugging Face Transformers](https://huggingface.co/transformers/)")
st.write("- [TensorFlow](https://www.tensorflow.org/)")

st.markdown("Thank you for using the Disaster Prediction App. We hope it proves to be a useful tool for your text classification needs.")
