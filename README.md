# Movie Review Sentiment Checker

This project predicts whether movie reviews are positive or negative using machine learning on the IMDB Dataset of 50k Movie Reviews.

## Description
- **Dataset**: IMDB Dataset of 50k Movie Reviews from Kaggle ([link](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)).
- **Preprocessing**: Text preprocessing with SpaCy (lemmatization, stop words removal) and TF-IDF vectorization.
- **Models**: Logistic Regression (best model with ~88% accuracy), trained and saved using scikit-learn and joblib.
- **Interface**: Interactive Gradio interface for testing reviews.

## How to Use (Locally)
1. Clone the repository:
   ```bash
   git clone https://github.com/Bekmaitnation/movie-reviews-sentiment-analysis.git
   cd movie-reviews-sentiment-analysis

2.Install dependencies:
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

3.Run the Gradio interface:
   python src/interface.py

##Files
models/ - Saved models and vectorizer (tfidf_vectorizer.pkl, logistic_regression_model.pkl).
src/train_models.py - Code to train the models on the IMDB dataset.
src/interface.py - Gradio interface to test the model with new reviews.
README.md - Project documentation.
requirements.txt - List of Python dependencies.

##Results
Best Model: Logistic Regression with an accuracy of ~88%.

##Example:
 Input: "This movie is amazing!"
 Output: "Positive"
 Input: "Terrible film, waste of time."
 Output: "Negative"

Author
Name: BekmamatItnation
GitHub: https://github.com/BekmamatItnation

## Screenshots
![screenshot_gradio](https://github.com/user-attachments/assets/0be04bb5-b6b6-4e09-9780-b3723c2d7027)

##try it live
Test the model here: [Hugging Face Space](https://huggingface.co/spaces/Blackmamat/Movie-review-sentiment)

Date: March 2025

License
MIT License

