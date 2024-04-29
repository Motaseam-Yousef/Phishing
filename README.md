# Phishing Detection App

This application uses machine learning to determine if a website is a phishing site based on its URL features. It is built using Streamlit, which allows for a simple web interface, and uses a model trained with joblib.

## Installation

To run this application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/). After installing Python, you need to install the required packages:

```bash
pip install streamlit joblib
```

## Usage

The application loads a pre-trained model to predict whether a given set of URL features indicate a phishing site. To use the application:

1. Clone this repository to your local machine.
2. Place your trained model in the same directory as the application or update the path in the script to where your model is located (`phishing.pkl`).
3. Run the application using Streamlit:

```bash
streamlit run app.py
```

4. Open your browser and go to `http://localhost:8501`.
5. Enter the URL features into the input box and click the "Predict" button.

## How It Works

The application uses a function `predict_phishing` that takes URL features as input and uses a trained model to predict if the site is a phishing site. The predictions are displayed in the Streamlit interface.

## Contributing

Feel free to fork this repository and submit pull requests. You can also open an issue if you find any bugs or have suggestions for improvements.
