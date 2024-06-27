import streamlit as st
import numpy as np
import tensorflow as tf
import librosa
import soundfile as sf
import io
import os

# Function to load and return model
@st.cache(allow_output_mutation=True)
def load_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        raise e
    return model

# Function to preprocess the input data
def preprocess_input(audio_data, num_mfcc=13, n_fft=2048, hop_length=512, expected_time_steps=120):
    # Save audio data to a temporary file
    with io.BytesIO(audio_data) as f:
        audio, sr = sf.read(f)
    
    # Extract MFCCs
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
    
    # Normalize MFCCs
    mfccs_normalized = mfccs.T  # Transpose to have shape (time_steps, num_mfcc)
    
    # Adjust number of time steps to match expected shape
    if mfccs_normalized.shape[0] < expected_time_steps:
        # Pad MFCCs if fewer time steps
        mfccs_normalized = np.pad(mfccs_normalized, ((0, expected_time_steps - mfccs_normalized.shape[0]), (0, 0)))
    elif mfccs_normalized.shape[0] > expected_time_steps:
        # Truncate MFCCs if more time steps
        mfccs_normalized = mfccs_normalized[:expected_time_steps, :]
    
    # Add an additional dimension for compatibility with Conv2D input shape
    mfccs_reshaped = mfccs_normalized[np.newaxis, ..., np.newaxis]  # Shape (1, expected_time_steps, num_mfcc, 1)
    
    return mfccs_reshaped

# Main function to run the Streamlit app
def main():
    st.title('Audio Classification App')
    st.write('Upload an audio file and get predictions!')

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        audio_data = uploaded_file.read()
        st.audio(audio_data, format='audio/wav')  # Display the audio file

        # Preprocess the audio data
        processed_data = preprocess_input(audio_data)

        # Print the current working directory for debugging
        st.write("Current working directory:", os.getcwd())
        
        # Load the model
        model_path = 'MODELS_exported/MODEL_CNN01/model_CNN_1.keras'  # Replace with your model path
        try:
            model = load_model(model_path)
            # Make prediction
            if processed_data is not None:
                prediction = model.predict(processed_data)
                st.write('Prediction:')
                st.write(prediction)  # Display the prediction results
        except Exception as e:
            st.error(f"Failed to load or predict using the model: {str(e)}")

if __name__ == '__main__':
    main()
