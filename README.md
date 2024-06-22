# Bird-Call-Identification-Using-Deep-Learning

![Screenshot 2024-06-22 235539](https://github.com/Rushdi-Rzx/Bird-Call-Identification-Using-Deep-Learning/assets/127214329/7162d787-6d2a-4032-8319-fc701b361a5b)

![Screenshot 2024-06-23 005358](https://github.com/Rushdi-Rzx/Bird-Call-Identification-Using-Deep-Learning/assets/127214329/484d9093-82b6-4e44-bdda-8c8702a67a53)

![Screenshot 2024-06-23 005412](https://github.com/Rushdi-Rzx/Bird-Call-Identification-Using-Deep-Learning/assets/127214329/e47baf0c-fc32-4335-8b8c-192ae9175b25)

![Screenshot 2024-06-23 005424](https://github.com/Rushdi-Rzx/Bird-Call-Identification-Using-Deep-Learning/assets/127214329/34ed66a7-4c44-49a9-aa14-1eb5c43c7c8b)


This project aims to classify bird species based on their audio calls. It uses a Convolutional Neural Network (CNN) to achieve this classification.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Web Interface](#web-interface)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Bird Sound Classifier is a machine learning project that identifies bird species from audio recordings. It uses deep learning techniques to process audio data and predict the species of the bird.

## Features
- Load and preprocess audio data
- Data augmentation for robust training
- CNN model for audio classification
- Model training and evaluation
- Web interface for user-friendly interaction

## Installation
To run this project locally, you'll need to install the required dependencies. Follow the steps below:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/bird-sound-classifier.git
    cd bird-sound-classifier
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install additional dependencies:
    ```sh
    pip install pydub librosa tensorflow scikit-learn matplotlib tqdm
    ```

## Usage
1. **Preprocess Data**: Ensure your dataset is organized with separate folders for each bird species containing their audio files.
2. **Run Model Training**: Use the provided script to train the model on your dataset.
3. **Evaluate the Model**: Check the model's performance using the test dataset.
4. **Run the Web Interface**: Launch the web interface to classify new bird calls.

## Data
The dataset should be organized as follows:

/content/drive/MyDrive/Bird/
├── BrownTinamou/
│ ├── audio1.mp3
│ ├── audio2.wav
│ └── ...
├── CinereousTinamou/
│ ├── audio1.mp3
│ ├── audio2.wav
│ └── ...
└── GreatTinamou/
├── audio1.mp3
├── audio2.wav
└── ...



