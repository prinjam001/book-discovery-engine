# 📚 Book Recommender System

A machine learning based **Book Recommendation System** built using Python and Streamlit. The application recommends books based on the user's selected book using a **content-based recommendation approach**.

## 🎯 Overview

Finding a good book can be difficult when there are thousands of books available. This project provides a simple and interactive solution that recommends similar books based on the selected title.

The application uses preprocessed book data and similarity scores to generate relevant recommendations.

## ✨ Key Features

- 📚 Search and select books
- 🤖 Content-based book recommendations
- 🔍 Find similar books
- ⚡ Fast recommendation generation
- 🎨 Interactive Streamlit interface
- 📊 Preprocessed recommendation model
- 🌐 Ready for web deployment
- 💻 Easy to run locally

## 🧠 How It Works

The recommendation system follows these steps:

1. User selects a book.
2. The application identifies the selected book.
3. Precomputed similarity scores are used to find similar books.
4. The system selects the most relevant books.
5. Recommended books are displayed to the user.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Pickle
- Machine Learning
- Content-Based Recommendation

## 📁 Project Structure

```text
book-recommender-system/
│
├── app.py
├── book-recommender-system.ipynb
├── requirements.txt
├── books.pkl
├── popular.pkl
├── pt.pkl
└── similarity_scores.pkl
## 🌐 Live Demo

🚀 **Live Demo:** [Book Recommender System](https://book-recommender-prinjam.streamlit.app/)

Try the live application and get book recommendations based on your selected book.
