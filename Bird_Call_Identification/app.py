from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow import keras
import numpy as np
import librosa
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
label_encoder = LabelEncoder()
# Fit the LabelEncoder with the bird species classes
label_encoder.fit(['Brown Tinamou', 'Cinereous Tinamou', 'Great Tinamou'])
model = tf.keras.models.load_model('bird_species_classifier.h5')

  # Load your trained model here
max_len = 500  # Adjust this value based on your feature extraction and padding

def extract_features(y, sr, n_mfcc=13):
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def pad_features(features, max_len):
    if features.shape[1] < max_len:
        pad_width = max_len - features.shape[1]
        features = np.pad(features, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        features = features[:, :max_len]
    return features

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    y, sr = librosa.load(file, sr=None)
    features = extract_features(y, sr)
    features = pad_features(features, max_len)
    features = np.expand_dims(features, axis=0)
    features = features[..., np.newaxis]
    prediction = model.predict(features)
    predicted_class = label_encoder.inverse_transform(np.argmax(prediction, axis=1))

    return jsonify({'prediction': predicted_class[0]})

if __name__ == '__main__':
    app.run(debug=True)
