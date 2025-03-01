import gradio as gr
import joblib

vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
model = joblib.load("models/logistic_regression_model.pkl")

def predict_sentiment(review):
    review_tfidf = vectorizer.transform([review])
    prediction = model.predict(review_tfidf)[0]
    return "Positive" if prediction == 1 else "Negative"

interface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(label="Enter your movie review"),
    outputs=gr.Textbox(label="Sentiment"),
    title="Movie Review Sentiment Checker"
)

interface.launch(share=True)