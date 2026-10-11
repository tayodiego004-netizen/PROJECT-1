# Final Project

## Emotion Detection Application

This project implements an emotion detection application using IBM Watson Natural Language Processing services. It analyzes text and returns scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Technologies Used

- Python
- Flask
- IBM Watson NLP Emotion Prediction API
- Requests
- Pylint for static code analysis
- Unit testing with unittest

## Application Features

- Detects emotions from text input.
- Identifies the dominant emotion.
- Handles blank input and unsuccessful API responses.
- Provides a Flask web endpoint for emotion detection.

## How to Run

Install the dependencies:

```bash
python -m pip install flask requests pylint
```

Run the application:

```bash
python server.py
```

## Static Code Analysis

Run Pylint on the server file:

```bash
python -m pylint server.py
```
